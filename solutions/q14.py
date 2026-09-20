import cv2
from pathlib import Path
image=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"))
b,g,r=cv2.split(image)
cv2.imshow("Blue",b); cv2.imshow("Green",g); cv2.imshow("Red",r)
cv2.waitKey(0); cv2.destroyAllWindows()
