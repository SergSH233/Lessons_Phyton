# Цель: Обработать данные из словаря данного в задании. (Научится методам работы со словарями)
# 1. Вывести списки ключей и значений словаря
# 2. В ETH добавить ключ total_diff со значением 100.
# 3. Внутри fst_token_info значение ключа name поменять с fdf на doge.
# 4. Удалить total_out из словарей внутри списка tokens и присвоить сумму этих значений в total_out внутри ETH.
# 5. Внутри sec_token_info изменить название ключа price на total_price.

# Словарь из задания:
data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 2
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 8
        }
    ]
}

# Вывод всех значений по ключам.
for x in data.keys():
    print("Data - ключ:", x)
# Вывод всех значений по значениям.
for x in data.values():
    print("Data - значение:", x)
print()

# В ETH добавить ключ total_diff со значением 100.
print("ETH до:", data["ETH"])
data["ETH"]["total_diff"] = 100
print("ETH после:", data["ETH"])
print()

# Внутри fst_token_info значение ключа name поменять с fdf на doge.
print("Имя до:", data["tokens"][0]["fst_token_info"]["name"])
data["tokens"][0]["fst_token_info"]["name"] = "doge"
print("Имя после:", data["tokens"][0]["fst_token_info"]["name"])

# Удалить total_out из словарей внутри списка tokens и присвоить сумму этих значений в total_out внутри ETH.
print("Словарь tokens до удаления\n", data["tokens"][0])
print("ETH Totalout =", data["ETH"]["totalOut"])
sum = data["tokens"][0]["total_out"]
del (data["tokens"][0]["total_out"])
data["ETH"]["totalOut"] = data["ETH"]["totalOut"] + sum
print("Словарь tokens после удаления\n", data["tokens"][0])
print("ETH Totalout =", data["ETH"]["totalOut"])

# Внутри sec_token_info изменить название ключа price на total_price.

print("Старое название ключа:\n", data["tokens"][1])
data["tokens"][1]["total_price"] = data["tokens"][1].pop("sec_token_info")
print("Новое название ключа:\n", data["tokens"][1])
