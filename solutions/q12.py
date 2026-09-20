import cv2
from pathlib import Path
root=Path(__file__).resolve().parents[1]
image=cv2.imread(str(root/"sample.jpg"))
x=int(input("Enter x: ")); y=int(input("Enter y: "))
image[y,x]=[255,255,255]
cv2.imwrite(str(root/"q12_modified_pixel.jpg"),image)
print("Modified pixel saved.")
