import cv2
import numpy as np

def compute_integral_images(image):
   
    integral_image = cv2.integral(image)
    integral_sq_image = cv2.integral(image.astype(np.float32) ** 2)
    return integral_image, integral_sq_image

def get_window_sum(integral_image, x, y, w):
    
    half_w = w // 2
    x1, y1 = max(x - half_w, 0), max(y - half_w, 0)
    x2, y2 = min(x + half_w + 1, integral_image.shape[0] - 1), min(y + half_w + 1, integral_image.shape[1] - 1)
    return integral_image[x2, y2] - integral_image[x1, y2] - integral_image[x2, y1] + integral_image[x1, y1]

def sauvola_binarization(image, window_size=15, k=0.2, R=128):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    integral_image, integral_sq_image = compute_integral_images(image)
    
    binary_image = np.zeros_like(image, dtype=np.uint8)
    
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            sum_window = get_window_sum(integral_image, x, y, window_size)
            sum_sq_window = get_window_sum(integral_sq_image, x, y, window_size)
            mean = sum_window / (window_size ** 2)
            std_dev = np.sqrt((sum_sq_window / (window_size ** 2)) - (mean ** 2))
            threshold = mean * (1 + k * ((std_dev / R) - 1))
            if image[x, y] > threshold:
                binary_image[x, y] = 255
            else:
                binary_image[x, y] = 0
    
    return binary_image


if __name__ == "__main__":
    image = cv2.imread("example.png", cv2.IMREAD_GRAYSCALE)
    binary_image = sauvola_binarization(image, window_size=15, k=0.2, R=128)
    cv2.imwrite("binary_image.png", binary_image)
    cv2.imshow("Binary Image", binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()