import cv2
import os
from flask import Flask, jsonify, send_file
from ultralytics import YOLO
from utils import detect_anomalies

app = Flask(__name__)
ALERTS = []

@app.route("/alerts", methods=["GET"])
def get_alerts():
    return jsonify(ALERTS)

@app.route("/frame", methods=["GET"])
def get_frame():
    frame_path = "static/frames/alert.jpg"
    if os.path.exists(frame_path):
        return send_file(frame_path, mimetype='image/jpeg')
    return "No frame available", 404

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture("sample_data/test_video.mp4")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        alert, output_frame = detect_anomalies(model, frame)

        if alert:
            ALERTS.append({"type": alert, "frame": "alert.jpg"})
            cv2.imwrite("backend/static/frames/alert.jpg", output_frame)
            print("Anomaly Detected:", alert)

        resized_display = cv2.resize(output_frame, (600, 800))  # width x height
        cv2.imshow("VisionGuard - Press Q to Quit", resized_display)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
