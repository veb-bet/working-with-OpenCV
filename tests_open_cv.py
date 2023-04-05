import cv2
image = cv2.imread("images/pf3.png")

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#cropped = image[10:500, 500:2000]
#viewImage(cropped, "Image")

#(h, w, d) = image.shape
#center = (w // 2, h // 2)
#M = cv2.getRotationMatrix2D(center, 180, 1.0)
#rotated = cv2.warpAffine(image, M, (w, h))
#viewImage(rotated, "Поворот на 180 градусов")

#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#ret, threshold_image = cv2.threshold(image, 127, 255, 0)
#viewImage(gray_image, "Градация серого")
#viewImage(threshold_image, "Чёрно-белое")

#blurred = cv2.GaussianBlur(image, (51, 51), 0)
#viewImage(blurred, "Размытие")

output = image.copy()
cv2.rectangle(output, (200, 200), (1500, 1000), (0, 250, 250), 10)
viewImage(output, "Прямоугольник")
