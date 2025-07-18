import random
all_numbers=[]
while len(all_numbers)<12:
    one_number=random.randint(1,100)
    if one_number not in all_numbers:
        all_numbers.append(one_number)
player1_list=all_numbers[:6]
player2_list=all_numbers[6:]
drow_box=all_numbers.copy()
print("all numbers:",all_numbers)
print("game start")
print("player 1:",player1_list)
print("player 2:",player2_list)
while drow_box:
    current_draw=random.choice(drow_box)
    drow_box.remove(current_draw)
    print("picked number:",current_draw)
    if current_draw in player1_list:
        player1_list.remove(current_draw)
        print("player 1 had it!")
    if current_draw in player2_list:
        player2_list.remove(current_draw)
        print("player 2 had it!")
    if len(player1_list)==0:
        print("player 1 win")
        break
    elif len(player2_list)==0:
        print("player 2 win")
        break