#Стоимость товара в местной валюте
coast = float(input("Введите стоимость товара в местной валюте: "))
#Конвертация местной валюты к доллару
dollar = float(input("Введите актуальный курс местной валюты к доллару|\nПример: 1 BYN /1-$|\nВвод:"))
yor_currency_in_dollar = float(input("Введите курс вашей валюты к доллару"))
coast_in_dollar = float((coast * dollar))
coast_in_BYN = float((coast_in_dollar * yor_currency_in_dollar))
print("С вашей карты списано",round(coast_in_BYN,2),"BYN")

