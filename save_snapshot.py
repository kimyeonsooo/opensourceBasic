import cv2
import csv
import time


def save_snapshot(result_img, data):
    timestamp = time.strftime("%d-%m-%Y-%H-%M-%S")
    image_path = f"frame-{timestamp}.jpg"
    csv_path = f"output-{timestamp}.csv"

    cv2.imwrite(image_path, cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR))

    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Gender", "Age"])
        writer.writerows(data)

    print("Snapshot saved:", image_path)
    print("CSV file saved:", csv_path)
    print("Timestamp:", timestamp)
