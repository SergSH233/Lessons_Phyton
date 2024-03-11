# Цель: Переформатировать данный взятые из задания в кортеж для хранения и экономии данных.

# Полученные данные:
players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
# Преобразование их в картеж:
players_list = []
for i_player in players:
    player_info = tuple(i_player + players[i_player])
    players_list.append(player_info)
print(players_list)
