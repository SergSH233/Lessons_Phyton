#Шифрование слова

word = input("Введите слова для шифрования: ")
print(len(word))
new_word = ""
min = 0
max = (len(word) - 1)
calc = len(word)
while calc > 0:
    new_word = new_word + word[min]
    min = min + 1
    calc = calc - 1
    # print("Test word A:", new_word)
    # print("calc:",calc)
    if max != (min -1):
        new_word = new_word + word[max]
        max = max - 1
        calc = calc - 1
        # print("Test word B:", new_word)
        # print("calc:",calc)
new_word = new_word.lower()
print(new_word)

#Расшифровка слова
word = input("Введите слова для расшифровки")
word = word.lower()
new_word = ""
word_1 = ""
word_2 = ""
calc = 1
for x in word:
    if calc%2 == 0:
        word_2 = x + word_2
        calc += 1
    else:
        word_1 = word_1 + x
        calc += 1

new_word = word_1 + word_2
print("Расшифрованное слово: ", new_word)