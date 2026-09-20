import cv2
from pathlib import Path
image=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"))
x=int(input("Enter x: ")); y=int(input("Enter y: "))
b,g,r=image[y,x]
print("B:",int(b)); print("G:",int(g)); print("R:",int(r))
