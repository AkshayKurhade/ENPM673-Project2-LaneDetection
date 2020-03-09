import numpy as np
import cv2
import imutils
import time
import yaml
# def processconfig(image):
#     # K Matrix
#     K = [[1.15422732e+03   0.00000000e+00   6.71627794e+02]
#         [0.00000000e+00   1.14818221e+03   3.86046312e+02]
#         [0.00000000e+00    0.00000000e+00  1.00000000e+00]]
#     # Distance coeff
#     dist = [[-2.42565104e-01, - 4.77893070e-02, - 1.31388084e-03, - 8.79107779e-05, 2.20573263e-02]]
#     image2= cv2.undistort(image,K,dist)
#     cv2.imshow(image2)
#     cv2.waitKey(0)

def crop_image(img):
    length_rect = 300
    breadth_rect = 50
    cv2.rectangle(img, (0, img.shape[0] - breadth_rect), (img.shape[1], img.shape[0] - length_rect), (0, 0, 255))
    cropped_image = img[(img.shape[0] - length_rect):(img.shape[0] - breadth_rect), (0):(img.shape[1])]
    return cropped_image
def mask_image(img):
    mask = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")
    pts = np.array(
        [[90, img.shape[0] - 25], [90, img.shape[0] - 35], [img.shape[1] / 2 - 30, 100], [img.shape[1] / 2 + 30, 100],
         [img.shape[1] - 90, img.shape[0] - 35], [img.shape[1] - 90, img.shape[0] - 25]], dtype=np.int32)
    cv2.fillConvexPoly(mask, pts, 255)
    masked = cv2.bitwise_and(img, img, mask=mask)
    return masked
def main():
    frame = cv2.imread('data/test.png')
    # processconfig(frame)
    cv2.imshow("Original Frame", frame)
    # cv2.undistort()
    cv2.waitKey(200)
    cropped_frame=crop_image(frame)
    cv2.imshow("snipped",cropped_frame)
    cv2.waitKey(200)
    masked_frame=mask_image(cropped_frame)
    cv2.imshow("masked",masked_frame)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()