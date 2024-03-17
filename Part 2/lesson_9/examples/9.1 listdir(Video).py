# examples(Video)
import os

# Имя файла
folder_name = "project"  # Имя папки
file_name = "my_file.txt"  # Имя файла

# Генерация относительного пути
rel_path = os.path.join('docs', folder_name, file_name)
print(rel_path)

# Генерация абсолютного пути
abs_path = os.path.abspath(file_name)
print(abs_path)


# Поиск проекта из спика названий

def print_dirs(project):
    print("\nСодержимое дериктории", project)
    # Проход по каждой папке проекта
    for i_elem in os.listdir(project):
        # Каждый i_elem это элемент вложенный в корневую папку
        print("I_ELEM:",i_elem)
        path = os.path.join(project, i_elem)
        # Вывод в консоль получившегося пути
        print(" ", path)


project_list = ["Part 1", "Part 2"]
for i_project in project_list:
    print("I_project: ", i_project) # Проход по списку проектов
    path_to_project = os.path.abspath(os.path.join('..', '..','..', i_project))
    # Берется значение i_project и подставляется в абсолютный путь
    # ".." - показывает на сколько нужно поднятся по древу вверх
    print_dirs(path_to_project)
