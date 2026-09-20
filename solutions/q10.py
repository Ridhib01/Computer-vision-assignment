import cv2
from pathlib import Path
image=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"))
h,w=image.shape[:2]
resized=cv2.resize(image,(w//2,h//2))
print("New size:",resized.shape[1],"x",resized.shape[0])
cv2.imshow("Q10 - Resized",resized); cv2.waitKey(0); cv2.destroyAllWindows()
