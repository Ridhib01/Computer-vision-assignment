import cv2
from pathlib import Path
image_path=Path(__file__).resolve().parents[1]/"sample.jpg"
image=cv2.imread(str(image_path))
print("Image loaded successfully." if image is not None else "Image failed to load.")
