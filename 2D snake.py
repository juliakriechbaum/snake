import os
import keyboard
import time
import random

rows, cols = 10, 10    # field (grid) size. i is row, j is column
speed = 10
timer = 0
direction = "l"
snake = [[5,4],[5,5],[5,6]]
garden = []
a = 5
b = 4
head = [a,b]

field_inxs_tup = [(i,j) for i in range(rows) for j in range(cols)]   # field indices as list of tuples
field_inxs_lst = [list(tup) for tup in field_inxs_tup]    # field indices as list of lists

def snake_set(snake):  # snake as set, allows to create field without snake (field minus snake)
    snake_set = set(map(tuple, snake)) 
    return snake_set

def create_garden(garden,snake_set,field_inxs_tup):
    snake_set = snake_set(snake)
    garden = [_ for _ in field_inxs_tup if _ not in snake_set]   #garden as a list of tuples
    garden_inxs = [list(_) for _ in garden]   # list of lists of indices in garden
    return garden_inxs

garden_inxs = create_garden(garden,snake_set,field_inxs_tup)

def create_apple(garden_inxs):
    apple = random.choice(garden_inxs)
    return apple

apple = create_apple(garden_inxs)

def show_field(rows,cols,snake,apple):
    os.system("cls" if os.name == "nt" else "clear")  # be nice and make this user friendly for all systems. clears screen for Windows/Linux
    field = [["." for _ in range(cols)] for _ in range(rows)]
    for _ in snake:
        i, j = _
        field[i][j] = "x"
    i,j = head
    field[i][j] = "X" 
    i, j = apple
    field[i][j] = "o"
    for row in field:
       print(" ".join(row))

show_field(rows,cols,snake,apple)

input("Press 'Enter' to start the game")

# it works until here

while True:
    #timer += 1

    #if keyboard.is_pressed("l") and direction != "r":
    #    direction = "l"  
    #if keyboard.is_pressed("r") and direction != "l":
    #    direction = "r"
    #if keyboard.is_pressed("u") and direction != "d":
    #    direction = "u"
    #if keyboard.is_pressed("d") and direction != "u":
    #    direction = "d"

    #if timer == speed:   # how to slow down a snake. else: feed it.
    #    timer = 0

        direction = input("choose l, r, u, d ")
        if direction == "l":
            b -= 1
        if direction == "r":
            b += 1
        if direction == "u":
            a -= 1
        if direction == "d":
            a += 1

        head = [a,b]
        if head in snake:
            print("ouch")
            break
        else: snake.insert(0,head)

        if snake == field_inxs_lst:
            print("I own this game!")
            break

        if head == apple:
            garden_inxs = create_garden(garden,snake_set,field_inxs_tup)
            apple = create_apple(garden_inxs)
        else:
            snake.pop(-1)
            
        if head not in field_inxs_lst:
            print("ouch")
            break

        show_field(rows,cols,snake,apple)

        #time.sleep(0.1)