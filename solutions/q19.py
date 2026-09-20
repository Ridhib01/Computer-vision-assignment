import numpy as np
import cv2
image=np.full((256,256),128,dtype=np.uint8)
cv2.imshow("256x256 intensity 128",image); cv2.waitKey(0); cv2.destroyAllWindows()
