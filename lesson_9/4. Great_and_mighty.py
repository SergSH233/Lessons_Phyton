enter_phrase = input("Введите предложение для определения самого длинного слова в нем: ")
phrase = enter_phrase + " "
long_word = ""
word_length = 0
buffuer_word = ""
caunter = 0
for letter in phrase:
    if letter == " ":
        if caunter > word_length:
            word_length = caunter
            long_word = buffuer_word
            caunter = 0
            buffuer_word = ""
    else:
        buffuer_word = buffuer_word + letter
        caunter += 1
print("Самое длинное слово -",long_word,"\nЕго длинна =", word_length)