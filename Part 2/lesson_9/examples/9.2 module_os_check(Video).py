import os


# Проверка на наличие имеющегося католога:
def print_dirs(project):
    print("\nСодержимое дериктории", project)
    if os.path.exists(project):
        for i_elem in os.listdir(project):
            path = os.path.join(project, i_elem)
            print(" ", path)
    else:
        print("Такого проекта данной директории нет")


# Validator не находится в данной структуре
project_list = ["Validator", "Part 1", "Part 2"]
for i_project in project_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', '..', i_project))
    print_dirs(path_to_project)


# Метод проверки файла в каталоге:

def find_file(cur_path, file_name):
    print("переходим в ", cur_path)
    x = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print("   смотрим путь:", path)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print("Это директория")
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None
    return result


file_path = find_file(os.path.abspath(os.path.join("..","..","..","..", "pythonProject2")), "main.py")
if file_path:
    print("Абсолютный путь к файлу:",file_path)
else:
    print("Файл не найден!")

