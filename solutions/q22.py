import cv2
from pathlib import Path
gray=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"),cv2.IMREAD_GRAYSCALE)
quantized=((gray//64)*85).astype("uint8")
cv2.imshow("2-bit Quantized",quantized); cv2.waitKey(0); cv2.destroyAllWindows()
