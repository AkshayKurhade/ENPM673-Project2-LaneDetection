import numpy as np
import cv2
import imutils
import time

def main():
    frame = cv2.imread('data/test.png')
    cv2.imshow("Original Frame", frame)
    # cv2.undistort()
    cv2.waitKey(0)

if __name__ == '__main__':
    main()