palindrom = input("Введите слово или предложение для проверки является ли оно палиндромом:\n")
palindrom = palindrom.lower()
word_1 = ""
word_2 = ""
for letter in palindrom:
    if letter != " " and letter != "–" and letter != "." and letter != "," and letter != "!"and letter != "?":
        word_1 = word_1 + letter
        word_2 = letter + word_2
#print(word_1, word_2)
if word_1 == word_2:
    print("Это слово или фраза - Палиндром")
else:
    print("Палиндрома нет")

