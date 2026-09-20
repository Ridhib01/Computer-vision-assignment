import cv2
from pathlib import Path
image=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"))
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Q8 - Grayscale",gray); cv2.waitKey(0); cv2.destroyAllWindows()
