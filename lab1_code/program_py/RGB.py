from PIL import Image
import numpy as np
import os

def save_rgb_components(image_path, output_folder):
    # Создаем папку для сохранения, если её нет
    os.makedirs(output_folder, exist_ok=True)
    
    # Открываем изображение и приводим его к формату RGB
    img = Image.open(image_path).convert("RGB")  # 👈 Добавлено приведение к RGB
    
    # Преобразуем изображение в массив numpy
    img_array = np.array(img)

    # Извлекаем компоненты R, G, B
    red = img_array.copy()
    red[:, :, 1] = 0  # Обнуляем зеленый канал
    red[:, :, 2] = 0  # Обнуляем синий канал

    green = img_array.copy()
    green[:, :, 0] = 0  # Обнуляем красный канал
    green[:, :, 2] = 0  # Обнуляем синий канал

    blue = img_array.copy()
    blue[:, :, 0] = 0  # Обнуляем красный канал
    blue[:, :, 1] = 0  # Обнуляем зеленый канал

    # Сохраняем изображения
    Image.fromarray(red).save(os.path.join(output_folder, "red_component.png"))
    Image.fromarray(green).save(os.path.join(output_folder, "green_component.png"))
    Image.fromarray(blue).save(os.path.join(output_folder, "blue_component.png"))

# Вызов функции
save_rgb_components("comand7.png", "output_folder")
