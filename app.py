from flask import Flask, Response, render_template
import cv2
import argparse
import threading, os
from dataclasses import dataclass
from imutils.video import WebcamVideoStream

@dataclass
class VideoLimited:
    f: cv2.VideoWriter = cv2.VideoWriter()
    t: cv2.TickMeter = cv2.TickMeter()

app = Flask(__name__)

wvs = WebcamVideoStream(src=0).start()

@app.route("/")
def index():
    return render_template("index.html")

def generate():

    while True:
        frame = wvs.read()
        if frame is None:
            print("no frame")
            continue
        
        frame = cv2.flip(frame, 1)
        ok, image = cv2.imencode(".jpg", frame)
        if not ok:
            continue

        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
            bytearray(image) + b'\r\n')

@app.route("/video_feed")
def video_feed():
    return Response(generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host",)
    ap.add_argument("--port",)
    ap.add_argument("--frame",)
    ap.add_argument("-P", "--preview", action='store_true')
    args = vars(ap.parse_args())

    app.run(host="0.0.0.0", port="5000", debug=True,
            threaded=False, use_reloader=False)

    wvs.stop()

if __name__ == "__main__":
    main()

