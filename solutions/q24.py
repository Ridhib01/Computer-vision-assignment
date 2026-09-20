import cv2
from pathlib import Path
image=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"))
x1,y1,x2,y2=map(int,input("Enter x1 y1 x2 y2: ").split())
roi=image[y1:y2,x1:x2]
cv2.imshow("Q24 - ROI",roi); cv2.waitKey(0); cv2.destroyAllWindows()
