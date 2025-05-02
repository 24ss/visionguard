import cv2
import numpy as np

previous_boxes = []

def detect_anomalies(model, frame):
    global previous_boxes
    results = model(frame, verbose=False)[0]
    alert_triggered = False
    alert_type = ""
    classes_of_interest = [0]  # person class

    crowd_threshold = 5
    lying_threshold_ratio = 0.3
    people_boxes = [r[:4] for r in results.boxes.data if int(r[-1]) in classes_of_interest]
    people_boxes = [list(map(int, box)) for box in people_boxes]

    # Crowd detection
    if len(people_boxes) > crowd_threshold:
        alert_type = "Crowding"
        alert_triggered = True

    # Lying down detection
    for box in people_boxes:
        x1, y1, x2, y2 = box
        w, h = x2 - x1, y2 - y1
        aspect_ratio = h / w
        if aspect_ratio < lying_threshold_ratio:
            alert_type = "Person lying down"
            alert_triggered = True

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

    # Lightweight fight detection — fast movement + proximity
    if previous_boxes:
        for (x1, y1, x2, y2) in people_boxes:
            for (px1, py1, px2, py2) in previous_boxes:
                dx = abs((x1 + x2)//2 - (px1 + px2)//2)
                dy = abs((y1 + y2)//2 - (py1 + py2)//2)
                dist = np.sqrt(dx**2 + dy**2)
                if dist < 100:  # close
                    # check movement
                    move_x = abs(x1 - px1)
                    move_y = abs(y1 - py1)
                    if move_x > 20 and move_y > 20:
                        alert_type = "Fight-like movement"
                        alert_triggered = True

    previous_boxes = people_boxes

    if alert_triggered:
        return alert_type, frame
    return None, frame
