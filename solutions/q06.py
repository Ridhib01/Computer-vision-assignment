import cv2
from pathlib import Path
root=Path(__file__).resolve().parents[1]
image=cv2.imread(str(root/"sample.jpg"))
out=root/"q06_saved_copy.jpg"
cv2.imwrite(str(out),image)
print("Saved:",out)
