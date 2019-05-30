#!/c/Users/christian/AppData/Local/Programs/Python/Python36/python
import time
import random
import os
import numpy as np

width  = 20
height = 10
snake_chr = 'o'

direction = {
        'N':[1,0],
        'S':[-1,0],
        'E':[0,1],
        'W':[0, -1]
        }
dir_str = 'NSEW'
cur_dir = 'E'

field = [[' ' for j in range (width)] for i in range (height)]

def disp_update ():
    global field
    print ('#' * (width+2))
    for line in field:
        print ('%c%s%c' % ('#', ''.join (line), '#'))
    print ('#' * (width+2))

def add_head (head):
    global field
    y = head[0]
    x = head[1]
    if (y < 0 or y >= height or x < 0 or x >= width):
        return False
    field[y][x] = snake_chr
    return True

def rand_dir ():
    global cur_dir
    if cur_dir == 'N':
        new_dirs = 'NEW'
    elif cur_dir == 'S':
        new_dirs = 'SEW'
    elif cur_dir == 'E':
        new_dirs = 'NSE'
    elif cur_dir == 'W':
        new_dirs = 'NSW'
    
    cur_dir = new_dirs[random.randint (0, len (new_dirs)-1)]
    return direction.get (cur_dir)

def main ():
    global field
    snake_pos = []
    Head = [5, 10]
    Dir = direction.get(cur_dir)
    timestamp = 0
    field[Head[0]][Head[1]] = 'o'
    
    while True:
        os.system ('cls')
        timestamp += 1
        Dir = rand_dir ()
        print (timestamp, Head, Dir)
        Head = np.add (Head, Dir)
        if (not add_head (Head)):
            print ('you lose')
            break
        disp_update ()
        time.sleep (1)


if __name__ == "__main__":
    main ()


