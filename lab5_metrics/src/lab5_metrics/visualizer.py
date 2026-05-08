import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread("data/test.jpg", 0)

plt.hist(imagen.flatten(), bins=50)

plt.title("Histograma")

plt.show()