"""Monta portada y conclusión corregidas conservando el audio del montaje final."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'output/videos/Videofinal.mp4'
RENDER = ROOT / 'media/videos/escenas/1080p60'
OUTPUT = ROOT / 'output/videos/Videofinal_corregido.mp4'
WORK = ROOT / 'output/videos/edicion_6min/correcciones_integral'

def ffmpeg(args):
    subprocess.run(['ffmpeg', '-hide_banner', '-v', 'error', '-nostdin', '-y', *args], check=True)

def probe(path):
    return json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-show_format', '-show_streams', '-show_chapters', '-of', 'json', str(path)]))

def stream_hash(path, stream):
    return subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(path), '-map', stream, '-c', 'copy', '-f', 'hash', '-hash', 'sha256', '-']).decode().strip()

if __name__ == '__main__':
    WORK.mkdir(parents=True, exist_ok=True)
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    for name, duration in [('Portada', 24), ('Conclusion', 46)]:
        assert float(probe(RENDER / f'{name}.mp4')['format']['duration']) == duration
    filters = ('[1:v]setpts=PTS-STARTPTS[p];'
               '[0:v]trim=start_frame=1440:end_frame=17040,setpts=PTS-STARTPTS[m];'
               '[2:v]setpts=PTS-STARTPTS[c];'
               '[0:v]trim=start_frame=19800:end_frame=21600,setpts=PTS-STARTPTS[f];'
               '[p][m][c][f]concat=n=4:v=1:a=0[v]')
    print('Exportando portada y conclusión corregidas...', flush=True)
    ffmpeg(['-i', str(SOURCE), '-i', str(RENDER / 'Portada.mp4'), '-i', str(RENDER / 'Conclusion.mp4'),
            '-filter_complex', filters, '-map', '[v]', '-map', '0:a:0', '-map_metadata', '0', '-map_chapters', '0',
            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-threads', '6', '-pix_fmt', 'yuv420p',
            '-c:a', 'copy', '-frames:v', '21600', '-t', '360', '-movflags', '+faststart', str(OUTPUT)])
    info = probe(OUTPUT)
    video = next(s for s in info['streams'] if s['codec_type'] == 'video')
    assert float(info['format']['duration']) == 360
    assert (video['width'], video['height'], video['r_frame_rate'], int(video['nb_frames'])) == (1920, 1080, '60/1', 21600)
    assert stream_hash(SOURCE, '0:a:0') == stream_hash(OUTPUT, '0:a:0')
    assert len(info['chapters']) == 7
    print('Verificando decodificación completa y capturas...', flush=True)
    ffmpeg(['-xerror', '-i', str(OUTPUT), '-map', '0:v:0', '-map', '0:a:0', '-f', 'null', '-'])
    for name, second in [('portada', 20), ('respuesta', 301), ('integral', 323), ('creditos', 350)]:
        ffmpeg(['-ss', str(second), '-i', str(OUTPUT), '-frames:v', '1', str(WORK / f'{name}.png')])
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == source_hash
    (WORK / 'verificacion.json').write_text(json.dumps(dict(
        video=str(OUTPUT), fuente=str(SOURCE), sha256_fuente=source_hash, duracion=360,
        resolucion='1920x1080', fps=60, audio_original_identico=True, capitulos=7,
        cambios=['00:00–00:24: pregunta en notación matemática y extremos explícitos',
                 '04:44–05:30: respuesta con intervalo cerrado y conexión con la integral',
                 '05:16–05:30: límite, integral y evaluación 185/12 visibles'],
        integral='185/12 = 15.4166666667', decodificacion_completa=True,
        nota='La conexión con la integral es un apoyo visual; se conserva la narración grabada.'
    ), ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'LISTO: {OUTPUT}', flush=True)
