from PIL import Image
import numpy as np

def semitone(old_image):
    
    return (0.3 * old_image[:, :, 0] + 0.59 * old_image[:, :, 1] + 0.11 * old_image[:, :, 2]).astype(np.uint8)

if __name__ == '__main__':
    image_name = 'capitan.png'
    pictures_folder = '22' 

    img_src = Image.open(f'{pictures_folder}/{image_name}').convert('RGB')
    img_src_arr = np.array(img_src)
    img_semitone_array = semitone(img_src_arr)
    img_semitone = Image.fromarray(img_semitone_array, 'L')
    img_semitone.show()
    output_image_name = f'semitone_{image_name.split(".")[0]}.bmp'
    img_semitone.save(output_image_name)
    print(f"Полутоновое изображение сохранено: {output_image_name}")
        