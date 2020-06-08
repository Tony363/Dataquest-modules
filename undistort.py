import cv2
import numpy as np
import imutils


# DIM = (960, 540)
# K = np.array([[263.1021173128426, 0.0, 477.98780306608234], [0.0, 261.30612719984185, 300.714230825097], [0.0, 0.0, 1.0]])
# D = np.array([[-0.0007727739728155351], [-0.10019345132548932], [0.10790597488851726], [-0.040655761660861996]])

# def undistort(img):
#     h,w = img.shape[:2]
#     map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
#     return cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
# fixed = undistort(cv2.imread('tennis.jpg'))

# cv2.imshow("Image", fixed)
# cv2.imwrite('calibresult.jpg',fixed)


cammatrix = np.array(
[
    [2.37151261e+03, 0.00000000e+00, 2.06733086e+03],
    [0.00000000e+00, 6.79322889e+03, 1.02869100e+03],
    [0.00000000e+00, 0.00000000e+00, 1.00000000e+00],
])
distcoeffs = np.array([ 1.0452322802395216e-02, 7.6881756006305271e-02,
       -1.4692261279709901e-02, -1.5069476197619362e-02,
       -6.4572078715397163e-02 ])
image = cv2.imread("tennis.jpg")
h,w = image.shape[:2]
newcam,roi = cv2.getOptimalNewCameraMatrix(cammatrix, distcoeffs, (w,h), 1) 
newimage = cv2.undistort(image, cammatrix, distcoeffs, None, newcam)
image = imutils.resize(image, width=1080,height=1920)
newimage = imutils.resize(newimage, width=1080,height=1920)

cv2.imshow("Orig Image", image)
cv2.imshow("Image", newimage)
cv2.imwrite('calibresult.jpg',newimage)
cv2.waitKey(0)