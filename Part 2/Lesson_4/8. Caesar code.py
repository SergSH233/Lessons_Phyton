# Цель: Написать программу шифрования подобную что была у Цезаря, где буквы изменяются на иные в зависимости от их
# расположения в алфавите. Сдвиг указывается пользователем.
# 1. Создать метод который при вызове запрашивает у пользователя слово(фразу) и сдвиг.
# 2. В методе создать массив "алфавит" для получения индексов букв.
# 3. Создать проверку на наличие в слове(фразе) знаков припинания и пробелов. Они не должны изменяться.
# 4. Сделать метод для поиска букв и их замене.
# 5. Собрать слово(фразу) и получившееся вернуть в консоль.
def CaesarCipher(words,offset):
    words = words.lower()
    alphabet = [chr(x) for x in range(ord("а"),ord("я") + 1)]
    print("DeBAG",alphabet,"\n",len(alphabet))
    new_words = ""
    for x in words:
        if x == " " or x == "." or x == "," or x == "!"  or x == "?" or x == "@" or x == "-":
            letter = x
            new_words = new_words + letter
        else:
            num = alphabet.index(x)
            num = (num + offset)% 32
            letter = alphabet[num]
            new_words = new_words + letter
    return new_words

# Метод расшифровки
def CaesarDeCipher():
    words = input("Введите зашифрованную фразу: ").lower()
    offset = int(input("Введите цифровой ключ: "))
    alphabet = [chr(x) for x in range(ord("а"),ord("я") + 1)]
    new_words = ""
    for x in words:
        if x == " " or x == "." or x == "," or x == "!"  or x == "?" or x == "@" or x == "-":
            letter = x
            new_words = new_words + letter
        else:
            num = alphabet.index(x)
            num = (num - offset)% 32
            letter = alphabet[num]
            new_words = new_words + letter
    print("Ваше сообщение: \n",new_words)

words = input("Введите фразу на русском: ")
offset = int(input("Задайте ключ смещения. Введите цифру: "))
print(CaesarCipher(words,offset))
CaesarDeCipher()


