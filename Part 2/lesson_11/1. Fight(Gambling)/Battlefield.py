import random
import time
import Player
# Цель: Создать мини игру о дерущихся войнах

# Кол-во игроков(Позже доделать)
# На какого грока сделаем ставку (Доделать)
# Сделать систему подсчета баллов и расчет коэффициентов (Доделать)
# Сделать цикл инициализации игроков (Доделать)

# Прописать рандомность атаки
# Проверку кол-ва жизней у апонента
# Итоговый результат

player_name1 = input("Please enter name player 1: ")
player_name2 = input("Please enter name player 2: ")
player1 = Player.Player(player_name1)
player2 = Player.Player(player_name2)
while True:
    cube = random.randint(1, 2)
    if cube == 1:
        attack = random.randint(5, 50)
        player2.health -= attack
        print("{player1} attack!\nAttack - {attack}\nHealth {player2}: {health}\n".
              format(player1=player1.name,
                     player2=player2.name,
                     attack=attack,
                     health=player2.health)
              )
        time.sleep(5)
        if player2.health <= 0:
            print("{player1} Winner!".format(player1=player1.name))
            break
    if cube == 2:
        attack = random.randint(5, 50)
        player1.health -= attack
        print("{player2} attack!\nAttack - {attack}\nHealth {player1}: {health}\n".
              format(player1=player1.name,
                     player2=player2.name,
                     attack=attack,
                     health=player1.health
                     ))
        time.sleep(5)
        if player1.health <= 0:
            print("{player2} Winner!".format(player2=player2.name))
            break
