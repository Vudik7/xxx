# Лабораторные работа по курсу OABИ
|**Студент:**|*Вудвуд Андрей*|
|------------|--------------|
|**Группа:** |*Б22-564*     |
|**Вариант:**|*19*           |
```sh
### Лабораторная работа №1. Цветовые модели и передискретизация изображений
### Лабораторная работа №2. Обесцвечивание и бинаризация растровых изображений
### Лабораторная работа №3. Фильтрация изображений и морфологические операции
### Лабораторная работа №4. Выделение контуров на изображении
```
### 1.  **Цветовые модели**
#### 1.1  Выделение компоненты R, G, B и сохранение как отдельные изображения. 
| images   | naruto |
|----------|------------|
|![!](/naruto_RGB/naruto.png) |![!](/naruto_RGB/blue.png)|
|![!](/naruto_RGB/green.png)  |![!](/naruto_RGB/red.png)|

| images   |     shifu |
|----------|------------|
|![!](/shifu_RGB/shifu.png) |![!](/shifu_RGB/blue.png)|
|![!](/shifu_RGB/green.png)  |![!](/shifu_RGB/red.png)|

| images   |     mcqueen |
|----------|------------|
|![!](/mcqueen_RGB/mcqueen.png) |![!](/mcqueen_RGB/blue.png)|
|![!](/mcqueen_RGB/green.png)  |![!](/mcqueen_RGB/red.png)|

| images   |     comand7 |
|----------|------------|
|![!](/comand7_RGB/comand7.png) |![!](/comand7_RGB/blue.png)|
|![!](/comand7_RGB/green.png)  |![!](/comand7_RGB/red.png)|



#### 1.2 Приводим изображение к цветовой модели HSI, сохраняем яркостную компоненту как отдельное изображение. 

| images исходные   |     @all |
|----------|------------|
|![!](/naruto_RGB/naruto_HSI/naruto.png) |![!](/mcqueen_RGB/mcqueen_HSI/mcqueen.png)|
|![!](/shifu_RGB/shifu_HSI/shifu.png)  |![!](/comand7_RGB/comand7_HSI/comand7.png)|


#### 1.3 Инвертируем яркостную компоненту в исходном изображении, сохраняем производное изображение.
| images исходные   |     @all |
|----------|------------|
|![!](/naruto_RGB/naruto_HSI/naruto_I/naruto_inverted.png) |![!](/mcqueen_RGB/mcqueen_HSI/mcqueen_I/mcqueen_inverted.png)|
|![!](/shifu_RGB/shifu_HSI/shifu_I/shifu_inverted.png)  |![!](/comand7_RGB/comand7_HSI/comand7_I/comand7_inverted.png)|


### 2. Передискретизация

Исходное изображение размером `720x458` :

![Original](/original/text1.png)

Исходное изображение размером `720x720` :

![Original](/original/spiral1.png)

#### 2.1 Растяжение (интерполяция) изображения в M раз

Интерполяция в 2 раза. Исходный размер `720x458` результирующий размер `1440x916`:

![UpsamplingX2](res/upsampling2_text1.jpg)

Интерполяция в 3 раза. Исходный размер `720x458` результирующий размер `2160x1374`:

![UpsamplingX3](res/upsampling_text1.jpg)

---

Интерполяция в 2 раза. Исходный размер `720x720` результирующий размер `1440x1440`:

![UpsamplingX2](res/upsampling2_spiral1.png)

Интерполяция в 3 раза. Исходный размер `720x720` результирующий размер `2160x2160`:

![UpsamplingX3](res/upsampling3_spiral1.png)

#### 2.2 Сжатие (децимация) изображения в N раз

Децимация в 2 раза. Исходный размер `720x458` результирующий размер `360x229`:

![DownsamplingX2](res/downsampling2_text1.png)

Децимация в 3 раза. Исходный размер `720x458` результирующий размер `240x153`:

![DownsamplingX3](res/downsampling3_text1.png)

---

Децимация в 2 раза. Исходный размер `720x720` результирующий размер `360x360`:

![DownsamplingX2](res/downsampling2_spiral1.png)

Децимация в 3 раза. Исходный размер `720x720` результирующий размер `240x240`:

![DownsamplingX3](res/downsampling3_spiral1.png)

#### 2.3 Передискретизация изображения в K=M/N раз путём растяжения и последующего сжатия (в два прохода)

Передискретизация изображения в K=3/2 раз за два прохода. Исходный размер `720x458` результирующий размер `1080x687`:

![Resampling2loop](res/downsampling3x2_text1.png)

---

Передискретизация изображения в K=3/2 раз за два прохода. Исходный размер `720x720` результирующий размер `1080x1080`:

![Resampling2loop](res/downsampling3x2_spiral1.png)

#### 2.4 Передискретизация изображения в K раз за один проход

Передискретизация изображения в K=3/2 раз за один проход. Исходный размер `720x458` результирующий размер `1080x687`:

![Resampling1loop](res/resampling_text1.png)

---

Передискретизация изображения в K=3/2 раз за один проход. Исходный размер `720x720` результирующий размер `1080x1080`:

![Resampling1loop](res/resampling_spiral1.png)

### 2. Приведение полноцветного изображения к полутоновому

Исходное изображение:

![Original](../original/test10.png)

Результирующее изображение с обычными коэффицентами:


![SemitoneNormal](res/halftone_test10.png)

Результирующее изображение с коэффицентами photoshop:

![SemitoneNormal](res/halftonePS_test10.png)

---

Исходное изображение:

![Original](../original/test11.jpg)

Результирующее изображение с обычными коэффицентами:

![SemitoneNormal](res/halftone_test11.jpg)

Результирующее изображение с коэффицентами photoshop:

![SemitoneNormal](res/halftonePS_test11.jpg)

### 3. Приведение полутонового изображения к монохромному методом пороговой обработки

> Алгоритм адаптивной бинаризации Кристиана

Исходное изображение:

![Original](res/downsampling_cat2.jpg)

|**B \ K**		|					0.2								   |					0.6				    			  |					0.8                                  |
|---------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|**20** 		|![kristian_threshold](res/threshold_b20_k0.2_cat2.jpg)|![kristian_threshold](res/threshold_b20_k0.6_cat2.jpg)|![kristian_threshold](res/threshold_b20_k0.8_cat2.jpg)|
|**40**			|![kristian_threshold](res/threshold_b40_k0.2_cat2.jpg)|![kristian_threshold](res/threshold_b40_k0.6_cat2.jpg)|![kristian_threshold](res/threshold_b40_k0.8_cat2.jpg)|
|**80**			|![kristian_threshold](res/threshold_b80_k0.2_cat2.jpg)|![kristian_threshold](res/threshold_b80_k0.6_cat2.jpg)|![kristian_threshold](res/threshold_b80_k0.8_cat2.jpg)|


---

Исходное изображение:

![Original](../original/text1.jpg)

Результирующее изображение c `k = 0.2`, `b = 15`:

![kristian_threshold](res/threshold_text1.jpg)


![Original](res/downsampling2_text1.jpg)


|**B \ K**		|					0.2									|					0.6									|					0.8                                 |
|---------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
|**20** 		|![kristian_threshold](res/threshold_b20_k0.2_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b20_k0.6_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b20_k0.6_downsampling2_text1.jpg)|
|**40**			|![kristian_threshold](res/threshold_b40_k0.2_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b20_k0.6_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b20_k0.6_downsampling2_text1.jpg)|
|**80**			|![kristian_threshold](res/threshold_b80_k0.2_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b40_k0.6_downsampling2_text1.jpg)|![kristian_threshold](res/threshold_b40_k0.6_downsampling2_text1.jpg)|