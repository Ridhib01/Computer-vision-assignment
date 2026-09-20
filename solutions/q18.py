import cv2
import numpy as np
from pathlib import Path
gray=cv2.imread(str(Path(__file__).resolve().parents[1]/"sample.jpg"),cv2.IMREAD_GRAYSCALE)
print("Mean:",float(np.mean(gray))); print("Standard deviation:",float(np.std(gray)))
