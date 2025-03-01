from PIL import Image
import numpy as np

def semitone(old_image):
    """
    Преобразует полноцветное изображение в полутоновое, используя взвешенное усреднение каналов RGB.

    Аргументы:
        old_image: Полноцветное изображение в формате numpy array (например, из PIL Image.Image).

    Возвращает:
        Полутоновое изображение в формате numpy array (тип np.uint8).
    """
    return (0.3 * old_image[:, :, 0] + 0.59 * old_image[:, :, 1] + 0.11 * old_image[:, :, 2]).astype(np.uint8)

if __name__ == '__main__':
    image_name = 'xray.png'  # Имя файла изображения (измените, если нужно)
    pictures_folder = 'pictures_src' # Папка, где лежит изображение

    try:
        img_src = Image.open(f'{pictures_folder}/{image_name}').convert('RGB')
        img_src_arr = np.array(img_src)

        img_semitone_array = semitone(img_src_arr)

        # Создание PIL Image из numpy array и отображение
        img_semitone = Image.fromarray(img_semitone_array, 'L')
        img_semitone.show()

        # Дополнительно: Сохранение полутонового изображения в файл (BMP формат)
        output_image_name = f'semitone_{image_name.split(".")[0]}.bmp' # Имя файла для сохранения
        img_semitone.save(output_image_name)
        print(f"Полутоновое изображение сохранено как: {output_image_name}")


    except FileNotFoundError:
        print(f"Ошибка: Файл '{image_name}' не найден в папке '{pictures_folder}'.")
        print(f"Пожалуйста, убедитесь, что файл '{image_name}' находится в папке '{pictures_folder}'")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        print("Убедитесь, что у вас установлены библиотеки Pillow (PIL) и NumPy.")