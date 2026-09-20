import cv2
from pathlib import Path
image=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"))
h,w=image.shape[:2]
print("Total pixels:",h*w)
