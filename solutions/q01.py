import cv2
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"sample.jpg"
image=cv2.imread(str(p))
if image is None: raise FileNotFoundError("Could not load sample.jpg")
cv2.imshow("Q1 - Image",image); cv2.waitKey(0); cv2.destroyAllWindows()
