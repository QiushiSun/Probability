import cv2
import numpy as np
# Read image
IMG = cv2.imread("kitten.png")
Height, Width, Center = IMG.shape
# Median Filter
Kernal_size = 3
## Zero padding
padding = Kernal_size // 2
out_put = np.zeros((Height + padding * 2, Width + padding * 2, Center), dtype=np.float)
out_put[padding:padding + Height, padding:padding + Width] = IMG.copy().astype(np.float)
tmp = out_put.copy()

#smoothing
for pixel_y in range(Height):
    for pixel_x in range(Width):
        for center in range(Center):
            out_put[padding + pixel_y, padding + pixel_x, center] = np.median(tmp[pixel_y:pixel_y + Kernal_size, pixel_x:pixel_x + Kernal_size, center])
# end of smoothing

out_put = out_put[padding:padding + Height, padding:padding + Width].astype(np.uint8)

cv2.imwrite("after_smooth.jpg", out_put)


