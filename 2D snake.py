import os
import keyboard
import time
import numpy as np


# snake, size: one block. field, 10x10 blocks. position of snake is in the center [5][4]

rows, cols = 10, 10    # field (grid) size. i is row, j is column
#speed = 10
#timer = 0
#direction = "l"
i = 5
j = 4
field_inx = [[(i,j) for j in range(cols)] for i in range(rows)]   # use numpy ???
np_field_inx = np.array(field_inx)
snake = np_field_inx[5:6, 4:7]
print(snake)

#def create_field(rows,cols,snake):
#    os.system("cls")
#    field = [["." for y in range(cols)] for x in range(rows)]    # nested list comprehension
#    field[snake[0]:snake[-1]] = "x"
#
#    for row in field:
#        print(" ".join(row))
#
#create_field(rows,cols,snake)

# uncomment 20-28: sends error:
#  File "c:\Users\julie\Desktop\data\01 programming\snake\2D snake.py", line 25, in create_field
#    field[snake[0]:snake[-1]] = "x"
#    ~~~~~^^^^^^^^^^^^^^^^^^^^
# TypeError: only integer scalar arrays can be converted to a scalar index

# find out how to convert each item's inx into integer scalar arrays (ähnlich zu Skalaren in der Vektorrechnung)


