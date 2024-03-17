import os

file_name = "admin.bat"
folder_name = "access"

rel_path = os.path.join("..",folder_name,file_name)
print("Относителный путь:",rel_path)

abs_path = os.path.abspath(os.path.join(folder_name,file_name))
print("Абсолютный путь:", abs_path)