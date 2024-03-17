import os

path = os.path.abspath(os.path.join(os.path.join("..","..")))
for i_elem in os.listdir(path):
    path_n = os.path.join(path,i_elem)
    print(" ",path_n)