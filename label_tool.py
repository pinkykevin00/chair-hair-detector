import cv2
import os

positive_dir = "dataset/positive"
output_file = "annotations/positives.txt"

os.makedirs("annotations", exist_ok=True)

annotations = []

def select_object(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Cannot read:", image_path)
        return None

    bbox = cv2.selectROI("Select Object", image, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select Object")

    x, y, w, h = bbox

    if w == 0 or h == 0:
        return None

    return x, y, w, h

for filename in os.listdir(positive_dir):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        image_path = os.path.join(positive_dir, filename)
        print("Labeling:", image_path)

        bbox = select_object(image_path)

        if bbox is not None:
            x, y, w, h = bbox
            line = f"{image_path} 1 {x} {y} {w} {h}"
            annotations.append(line)
            print(line)
        else:
            print("Skipped:", image_path)

with open(output_file, "w", encoding="utf-8") as f:
    for line in annotations:
        f.write(line + "\n")

print("Done. Saved to", output_file)