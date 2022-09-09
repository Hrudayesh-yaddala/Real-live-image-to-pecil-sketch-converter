import numpy as np
import cv2
import pyttsx3

a=input('enter the legend name :')

res=pyttsx3.init()

voices = res.getProperty('voices')
res.setProperty('voice', voices[1].id)
res.setProperty('rate',150)

res.say(f'mr.{a} smile please !!!!!!!!!!!!!!!!!!')


res.runAndWait()

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "promo.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

# load the image
img = cv2.imread('promo.png.')

cv2.imshow('original', img)
cv2.waitKey()
cv2.destroyAllWindows()


def pencil_sketch(img, ksize, gamma):
    # step-1 convert image into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # step-2: apply gaussian blur to the image
    blur = cv2.GaussianBlur(gray, (ksize, ksize), 0)
    # step-3: division image
    division_img = cv2.divide(gray, blur, scale=256)
    # step-4: adjusting gamma factor
    if gamma == 0:
        gamma = 0.01

    elif gamma < 0:
        raise Exception('Cannot Be Negative', 'Gamma value cannot be negative number (range = 0-1)')

    elif gamma > 1:
        raise Exception('Cannot be greater than 1', 'Gamma value cannot greater than 1 (range = 0-1)')

    invgamma = 1 / gamma
    lut = np.array([((i / 255) ** invgamma) * 255 for i in range(0, 256)])
    pencil_sketch_img = cv2.LUT(division_img.astype('uint8'),
                                lut.astype('uint8'))

    return pencil_sketch_img


pencil_img = pencil_sketch(img, 7, 0.3)

cv2.imshow('orignial', img)
cv2.imshow('Pencil Sketch', pencil_img)

cv2.waitKey()
cv2.destroyAllWindows()

image = cv2.imread('promo.png')
# create control pannel

cv2.namedWindow('Control Pannel')
cv2.createTrackbar('ksize', 'Control Pannel', 1, 100, (lambda x: None))
cv2.createTrackbar('gamma', 'Control Pannel', 1, 100, (lambda x: None))

while True:

    # take k-size
    k = cv2.getTrackbarPos('ksize', 'Control Pannel')
    # k size should be an odd number
    k = 2 * k + 1
    # calibrate gamma to 0 - 1 scale
    g = cv2.getTrackbarPos('gamma', 'Control Pannel')
    g = g / 100
    pencil_img = pencil_sketch(image, k, g)

    cv2.imshow('original', image)
    cv2.imshow('Pencil Sketch', pencil_img)
    cv2.imwrite('final.png',pencil_img)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()