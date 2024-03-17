import os


def find_file(cur_path, file_name):
    print("переходим в ", cur_path)
    keys_path = {}
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print("   смотрим путь:", path)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print("Это директория")
            result = find_file(path, file_name)
            if result:
                keys_path[file_name] = result
                break
        elif os.path.isfile(path):
            keys_path[file_name] = path
            break
    else:
        result = None
    return keys_path


find_file_name = input("Введите название файла который хотите найти: ")
file_path = find_file(os.path.abspath(os.path.join(os.path.sep, "task")), find_file_name)
print(file_path)