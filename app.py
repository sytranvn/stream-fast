#!/usr/bin/env python3

from flask import Flask, Response, render_template, send_from_directory
import cv2
import argparse

app = Flask(__name__)

@app.route("/")
def hls():
    return render_template("hls.html")

@app.route("/favicon.ico")
def fav():
    return send_from_directory('static', 'favicon.ico')

@app.route("/stream/<path:path>")
def stream(path):
    cache = None if ".m3u8" not in path else 0
    return send_from_directory('out', path, cache_timeout=cache)

@app.route("/js/<path:path>")
def public(path):
    return send_from_directory('js', path)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host",default="0.0.0.0")
    ap.add_argument("--device", type=int, default=-1)
    ap.add_argument("--port",default="5000")
    ap.add_argument("--frame",)
    args = vars(ap.parse_args())

    app.run(host=args["host"], port=args["port"], debug=True)


if __name__ == "__main__":
    main()

