file_size = float((input("Введите рамер файла в МБ: ")))
percent_download = float(round(0, 1))
buffer_file_size = float(0.0)
internet_speed = float(input("Введите скорость интернета Мб/с: "))
time_left = int(0)

while buffer_file_size < file_size:
    buffer_file_size = buffer_file_size + internet_speed
    if buffer_file_size > file_size:
        buffer_file_size = file_size
    percent_download = (buffer_file_size/file_size) * 100
    if percent_download > 100:
        percent_download = 100
    time_left = int(file_size - buffer_file_size)/ internet_speed
    if time_left < 0:
        time_left = 0
    print("Скачано:",round(buffer_file_size,2),"Mb\t ","   ",round(percent_download,2),"%\t"," ","Осталось",int(time_left),"sec")


