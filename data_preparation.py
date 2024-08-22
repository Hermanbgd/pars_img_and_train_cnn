import shutil
import os

# Пример подготовки данных для обучения нейронной сети на Keras. Данные разбиваются на три каталога:
#
# train (данные для обучения)
# val (данные для проверки)
# test (данные для тестирования)
# В каждом каталоге создаются по два подкаталога, в соответсвии с названиями классов.
#
# Изображения переписваются из исходного каталога в новую структуру. По-умолчанию для обучения используется
# 80% изображений, для проверки - 10%, для тестрования также 10%.


# Каталог с набором данных
data_dir = 'fruits_images'
# Каталог с данными для обучения
train_dir = 'train'
# Каталог с данными для проверки
val_dir = 'val'
# Каталог с данными для тестирования
test_dir = 'test'
# Часть набора данных для тестирования
test_data_portion = 0.1
# Часть набора данных для проверки
val_data_portion = 0.1
# Количество элементов данных в одном классе
nb_images = 5000

# Функция создания каталога с десятью подкаталогами по названию классов.
def create_directory(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    os.makedirs(os.path.join(dir_name, "apple"))
    os.makedirs(os.path.join(dir_name, "banana"))
    os.makedirs(os.path.join(dir_name, "blueberry"))
    os.makedirs(os.path.join(dir_name, "cherry"))
    os.makedirs(os.path.join(dir_name, "kiwi"))
    os.makedirs(os.path.join(dir_name, "lime"))
    os.makedirs(os.path.join(dir_name, "orange"))
    os.makedirs(os.path.join(dir_name, "raspberry"))
    os.makedirs(os.path.join(dir_name, "strawberry"))
    os.makedirs(os.path.join(dir_name, "watermelon"))

# Создание структуры каталогов для обучающего, проверочного и тестового набора данных

create_directory(train_dir)
create_directory(val_dir)
create_directory(test_dir)

# Функция копирования изображений в заданный каталог. Изображения фруктов копируются в отдельные подкаталоги

def copy_images(start_index, end_index, source_dir, dest_dir):
    for i in range(start_index, end_index+1):
        shutil.copy2(os.path.join(f'{source_dir}/apple_images', "apple." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "apple"))
        shutil.copy2(os.path.join(f'{source_dir}/banana_images', "banana." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "banana"))
        shutil.copy2(os.path.join(f'{source_dir}/blueberry_images', "blueberry." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "blueberry"))
        shutil.copy2(os.path.join(f'{source_dir}/cherry_images', "cherry." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "cherry"))
        shutil.copy2(os.path.join(f'{source_dir}/kiwi_images', "kiwi." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "kiwi"))
        shutil.copy2(os.path.join(f'{source_dir}/lime_images', "lime." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "lime"))
        shutil.copy2(os.path.join(f'{source_dir}/orange_images', "orange." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "orange"))
        shutil.copy2(os.path.join(f'{source_dir}/raspberry_images', "raspberry." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "raspberry"))
        shutil.copy2(os.path.join(f'{source_dir}/strawberry_images', "strawberry." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "strawberry"))
        shutil.copy2(os.path.join(f'{source_dir}/watermelon_images', "watermelon." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "watermelon"))

# Расчет индексов наборов данных для обучения, проверки и тестирования

start_val_data_idx = int(nb_images * (1 - val_data_portion - test_data_portion))
start_test_data_idx = int(nb_images * (1 - test_data_portion))
print(start_val_data_idx)
print(start_test_data_idx)

# Копирование изображений
copy_images(1, start_val_data_idx, data_dir, train_dir)
copy_images(start_val_data_idx, start_test_data_idx, data_dir, val_dir)
copy_images(start_test_data_idx, nb_images, data_dir, test_dir)

