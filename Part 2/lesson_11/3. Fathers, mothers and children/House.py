import random
import time

import Family
name_parent = input("Enter the name parent: ")
age_parent = int(input("Enter age parent: "))

name_children = input("Enter the name children: ")
age_children = int(input("Enter age children: "))

parent = Family.Parent(name_parent, age_parent)
children = Family.Children(name_children, age_children)

while True:
    if (parent.age - children.age) < 16:
        print("I'm calling the police! You gave birth to a child under the age of 16! You're under arrest!")
        break
    elif parent.age < children.age:
        print("Check your passport information! You clearly have some kind of age weirdness!")
        break
    children.status = random.randint(0, 3)
    children.print_children_state()
    if children.status == 0:
        parent.status = random.choice((0, 2, 3, 4))
        parent.print_parent_state()
        if parent.status == 0:
            parent.health += 10
            parent.scoring -= 10
            children.scoring += 5
            children.health += 10
            print("{parentName} не отреогировал(а) на реакцию ребенка, и {childrenName} продолжил(а) играть\n".format(
                parentName=parent.name,
                childrenName=children.name
            ))
            time.sleep(4)
        elif parent.status == 2:
            parent.health -= 5
            parent.scoring -= 20
            children.scoring -= 10
            print(
                "{parentName} решил(а) успокоить ребенка. Но {childrenName} продолжил(а) играть не реагируя на родителя\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)

        elif parent.status == 3:
            parent.health -= 15
            parent.scoring -= 30
            children.health -= 20
            children.scoring -= 30
            print(
                "{parentName} решил(а) отругать {childrenName}. {childrenName} обиженный(ая) он(а) ушла в комнату громко хлопнув дверью!\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)
        elif parent.status == 4:
            parent.health -= 10
            parent.scoring += 20
            children.health += 10
            children.scoring += 30
            print(
                "{parentName} решил(а) поиграть с {childrenName}. {parentName} и {childrenName} отлично провели вечер играя вместе!\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)
    elif children.status == 1:
        parent.status = random.randint(0, 4)
        parent.print_parent_state()
        if parent.status == 0:
            parent.health += 10
            parent.scoring -= 30
            children.scoring -= 30
            children.health -= 20
            print(
                "{parentName} не отреогировал(а) на реакцию ребенка, {childrenName} лег(ла) в этот вечер голодным(ой)\n"
                "Этот опыт ребенок запомнит на всю жизнь\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)
        elif parent.status == 1:
            parent.health -= 5
            parent.scoring += 30
            children.scoring += 30
            children.health += 20
            print(
                "{parentName} приготовил(а) ужин для ребенка.{childrenName} покушал(а), и отлично провел(а) вечер\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)

        elif parent.status == 2:
            parent.health -= 10
            parent.scoring -= 10
            children.health -= 20
            children.scoring -= 10
            print(
                "{parentName} решил(а) успакоить {childrenName}. {childrenName} голодный(ая) но с чуством что он(а) не один(а) ушел(а) спать. "
                "В голове у ребенка останется на долго что бывает такое что нет средств\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)

        elif parent.status == 3:
            parent.health -= 20
            parent.scoring -= 30
            children.health -= 50
            children.scoring -= 20
            print(
                "{parentName} решил(а) отругать {childrenName}. {childrenName} обиженный(ая) и голодный(ая) он(а) "
                "ушла в комнату громко хлопнув дверью, осознав что есть ущимления в еде\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)
        elif parent.status == 4:
            parent.health -= 20
            parent.scoring -= 15
            children.health -= 20
            children.scoring += 5
            print(
                "{parentName} решил(а) поиграть с {childrenName}. {parentName} отвлек(ла) {childrenName} и ненадолго "
                "ребенок позабыл о голоде\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)
    elif children.status == 2:
        parent.status = random.randint(0, 4)
        parent.print_parent_state()
        if parent.status == 0:
            parent.health += 10
            parent.scoring -= 15
            children.scoring -= 15
            children.health -= 15
            print(
                "{parentName} не отреогировал(а) на реакцию ребенка, {childrenName} ходил(ла) в этот вечер постоянно озираясь по сторонам\n"
                    .format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)
        elif parent.status == 1:
            parent.health -= 20
            parent.scoring -= 10
            children.scoring += 5
            children.health -= 10
            print(
                "{parentName} приготовил(а) ужин для ребенка не правильно поняв настроение\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)

        elif parent.status == 2:
            parent.health += 15
            parent.scoring += 30
            children.health += 25
            children.scoring += 25
            print(
                "{parentName} решил(а) успакоить {childrenName}. {childrenName} поговорив с родителем поняла "
                "что в сложных ситуациях всегда есть человек который сможет понять и выслушать!\n"
                    .format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)

        elif parent.status == 3:
            parent.health -= 20
            parent.scoring -= 30
            children.health -= 20
            children.scoring -= 15
            print(
                "{parentName} решил(а) отругать {childrenName}. Не разобравшись в ситуации {parentName} накричал(а). "
                "С тех пор {childrenName} держит все негодования в себе\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)
        elif parent.status == 4:
            parent.health -= 10
            parent.scoring += 5
            children.health += 5
            children.scoring += 5
            print(
                "{parentName} решил(а) поиграть с {childrenName}. {parentName} отвлек(ла) {childrenName} и ребенок позабыл о страхе\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)
    elif children.status == 3:
        parent.status = random.randint(0, 4)
        parent.print_parent_state()
        if parent.status == 0:
            parent.health += 10
            parent.scoring -= 10
            children.scoring -= 5
            children.health -= 0
            print(
                "{parentName} не отреогировал(а) на реакцию ребенка, {childrenName} продолжил(ла) в этот вечер "
                "проказничать и ходить на голове\n"
                    .format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)
        elif parent.status == 1:
            parent.health -= 10
            parent.scoring -= 5
            children.scoring -= 5
            children.health -= 5
            print(
                "{parentName} приготовил(а) ужин для ребенка. {childrenName} не стал кушать а продолжил(а) дурачится "
                "и ходить на голове\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)

        elif parent.status == 2:
            parent.health -= 15
            parent.scoring += 5
            children.health += 5
            children.scoring -= 15
            print(
                "{parentName} решил(а) успакоить {childrenName}. {childrenName} слушать не стал и продолжил(а) "
                "куралесить\n"
                    .format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)

        elif parent.status == 3:
            parent.health += 5
            parent.scoring += 30
            children.health += 10
            children.scoring += 25
            print(
                "{parentName} решил(а) отругать {childrenName}. {parentName} врозумил(а) {childrenName} и ребенок "
                "понял что так делать больше не стоит.\n"
                .format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)
        elif parent.status == 4:
            parent.health -= 10
            parent.scoring -= 5
            children.health -= 5
            children.scoring -= 10
            print(
                "{parentName} решил(а) поиграть с {childrenName}. Потакая ребенку они разнесли половину дома, "
                "но опыт ребенок преобрел негативный\n".format(
                    parentName=parent.name,
                    childrenName=children.name
                ))
            time.sleep(4)

    if children.scoring <= 25:
        print("Ребенок стал разбалованный. Родитель не смог правильно его воспитать!")
        break
    elif children.health <= 10:
        print("Ребенок присмерти! Родитель был лешен родительских прав!")
        break
    elif children.scoring >= 125:
        print("Ребенок достиг высоких показателей по жизни, благодоря его воспитанию!")
        break
    elif parent.health <= 0:
        print("Не выдержав натиска проблем родитель умирает, оставив ребенка одного.")
        break
    elif children.health >= 140:
        print("Ребенок вырос здоровым!")
        break
    elif parent.scoring >= 140:
        print("Родитель проявил себя как отличный человек став для своего ребенка настоящим другом!")
        break

