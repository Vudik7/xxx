import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

def sauvola_threshold(image, window_size=5, k=0.2, r=128):
    """
    Адаптивная бинаризация Сауволы.
    
    :param image: Полутоновое изображение (grayscale)
    :param window_size: Размер окна (нечетное число, по умолчанию 5)
    :param k: Коэффициент регулировки (обычно от 0.2 до 0.5)
    :param r: Динамический диапазон стандартного отклонения (по умолчанию 128)
    :return: Бинаризированное изображение
    """
    img = image.astype(np.float32)

    # Среднее значение в окне 5x5
    mean = cv2.boxFilter(img, ddepth=-1, ksize=(window_size, window_size))
    
    # Средний квадрат (для вычисления стандартного отклонения)
    mean_sq = cv2.boxFilter(img**2, ddepth=-1, ksize=(window_size, window_size))
    
    # Стандартное отклонение
    std_dev = np.sqrt(mean_sq - mean**2)
    
    # Вычисляем локальный порог
    threshold = mean * (1 + k * ((std_dev / r) - 1))
    
    # Применяем бинаризацию
    binary_image = (img > threshold).astype(np.uint8) * 255
    
    return binary_image

# 📌 Загрузка нескольких изображений для теста
image_paths = glob.glob("binarization/*.png")  # Папка с изображениями
images = [cv2.imread(img, cv2.IMREAD_GRAYSCALE) for img in image_paths]

# 📌 Создаем папку для сохранения обработанных изображений
output_dir = "binarization/processed"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 📌 Обрабатываем каждое изображение и выводим результат
plt.figure(figsize=(12, 6))

for i, img in enumerate(images):
    binary_img = sauvola_threshold(img, window_size=5)

    # Сохраняем обработанное изображение
    output_path = os.path.join(output_dir, f"processed_{i+1}.png")
    cv2.imwrite(output_path, binary_img)

    # Отображаем оригинал и обработанное изображение
    plt.subplot(len(images), 2, 2*i + 1)
    plt.imshow(img, cmap='gray')
    plt.title(f"Оригинал {i+1}")
    plt.axis("off")

    plt.subplot(len(images), 2, 2*i + 2)
    plt.imshow(binary_img, cmap='gray')
    plt.title(f"Бинаризация Сауволы {i+1}")
    plt.axis("off")

plt.tight_layout()
plt.show()