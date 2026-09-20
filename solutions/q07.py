import cv2
from pathlib import Path
image=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"),cv2.IMREAD_GRAYSCALE)
cv2.imshow("Q7 - Grayscale",image); cv2.waitKey(0); cv2.destroyAllWindows()
