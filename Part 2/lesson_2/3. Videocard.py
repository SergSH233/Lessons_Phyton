# Цель:
# Внести имеющийся по условию список видеокарт
# Создать переменную с наименованием модели которую в этот день разобрали
#   -По условию эта страшая в своей ленейке модель
# Вывести список оставшихся моделей

def delisting(model, list):
    new_list = []
    for x in list:
        if x != model:
            new_list.append(x)
    return new_list


model = "3090"
shop_list = ["3070", "2060", "3090", "3070", "3090"]
print("Старый список: ",shop_list,"\nНовый список: ",delisting(model,shop_list))
