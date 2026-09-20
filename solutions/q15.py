import cv2
from pathlib import Path
image=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"))
b,g,r=cv2.split(image)
merged=cv2.merge([b,g,r])
cv2.imshow("Merged",merged); cv2.waitKey(0); cv2.destroyAllWindows()
