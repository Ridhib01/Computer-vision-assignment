import cv2
from pathlib import Path
gray=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"),cv2.IMREAD_GRAYSCALE)
print("Mean intensity:",float(gray.mean()))
