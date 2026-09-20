import cv2
import matplotlib.pyplot as plt
from pathlib import Path
image=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"))
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB)); plt.axis("off"); plt.show()
