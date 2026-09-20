import cv2
from pathlib import Path
image=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"))
h,w=image.shape[:2]
downsampled=cv2.resize(image,(w//2,h//2),interpolation=cv2.INTER_AREA)
print("New resolution:",downsampled.shape[1],"x",downsampled.shape[0])
cv2.imshow("Q23 - Downsampled",downsampled); cv2.waitKey(0); cv2.destroyAllWindows()
