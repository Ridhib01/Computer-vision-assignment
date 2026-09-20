import cv2
from pathlib import Path
root=Path(__file__).resolve().parents[1]
image=cv2.imread(str(root/"sample.jpg"))
rotated=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite(str(root/"q25_rotated_90.jpg"),rotated)
cv2.imshow("Q25 - Rotated 90",rotated); cv2.waitKey(0); cv2.destroyAllWindows()
