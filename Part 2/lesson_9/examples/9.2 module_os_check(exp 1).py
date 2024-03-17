import os

path = os.path.abspath(os.path.join("..","examples"))
if os.path.exists(path):
    for i_elem in os.listdir(path):

        if os.path.isfile(i_elem):
            print("Размер файла",i_elem," = ",os.path.getsize(i_elem),"байт")
        elif os.path.isdir(i_elem):
            print("Это папка")
else:
    print("Такого пути не существует!")