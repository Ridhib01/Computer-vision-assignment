import cv2
from pathlib import Path
image=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"))
h,w,c=image.shape
print("Height:",h); print("Width:",w); print("Channels:",c)
