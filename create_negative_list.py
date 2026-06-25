import os

negative_dir = "dataset/negative"
output_file = "annotations/negatives.txt"

os.makedirs("annotations", exist_ok=True)

with open(output_file, "w", encoding="utf-8") as f:
    for filename in os.listdir(negative_dir):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            path = os.path.join(negative_dir, filename)
            f.write(path + "\n")

print("Negative list saved to", output_file)
