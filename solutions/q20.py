import numpy as np
import cv2
image=np.tile(np.arange(256,dtype=np.uint8),(256,1))
cv2.imshow("Intensity Ramp",image); cv2.waitKey(0); cv2.destroyAllWindows()
