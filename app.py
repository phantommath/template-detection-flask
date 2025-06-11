from flask import Flask, render_template, request
from flask_socketio import SocketIO
import cv2
import os
import threading
import uuid

app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def detect_template(video_path, template_path, threshold=0.8):
    cap = cv2.VideoCapture(video_path)
    template = cv2.imread(template_path, 0)
    if template is None:
        socketio.emit('template_not_found')
        return
    t_h, t_w = template.shape[:2]
    frame_id = 0
    found = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        f_h, f_w = gray.shape[:2]
        # Pula frames menores que o template
        if f_h < t_h or f_w < t_w:
            frame_id += 1
            continue
        try:
            res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        except cv2.error:
            # Caso ocorra erro de dimensão ou outro, segue para o próximo frame
            frame_id += 1
            continue
        if (res >= threshold).any():
            socketio.emit('template_found', {'frame': frame_id})
            found = True
            break
        frame_id += 1

    cap.release()
    if not found:
        socketio.emit('template_not_found')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    vid = request.files.get('video')
    tpl = request.files.get('template')
    threshold = float(request.form.get('threshold', 0.8))

    if not vid or not tpl:
        return 'Arquivo de vídeo ou template não fornecido', 400

    video_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.mp4")
    template_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.jpg")
    vid.save(video_path)
    tpl.save(template_path)

    thread = threading.Thread(
        target=detect_template,
        args=(video_path, template_path, threshold)
    )
    thread.daemon = True
    thread.start()

    return 'Processando...'


if __name__ == '__main__':
    socketio.run(
    app,
    host='0.0.0.0',
    port=5000,
    allow_unsafe_werkzeug=True
)