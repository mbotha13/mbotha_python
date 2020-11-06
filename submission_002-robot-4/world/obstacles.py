import traceback
import random
obstacle_list = []
def get_obstacles():
    # print(f'From {__name__}: I was called. (line 5)')
    r_range = random.randint(1,10)
    for i in range(r_range):
        obstacle = (random.randint(-100,100), random.randint(-200,200))
        obstacle_list.append(obstacle)
    return obstacle_list
 
def is_position_blocked(x,y):
    for i in obstacle_list:
        x_check = i[0]
        y_check = i[1]
        if x_check <= x <= (x_check + 4) and y_check <= y <= (y_check + 4): #and x_check == x and y_check == y :
            return True
    return False

def is_path_blocked(x1,y1, x2, y2):
    if x1 == x2:
        if y2 < y1:
            for i in range(y1,y2,-1):
                if is_position_blocked(x1, i):
                    return True
        else:
            for i in range(y1,y2 + 1):
                if is_position_blocked(x1, i):
                    return True
    else:
        if y1 == y2:
            if x2 < x1:
                for i in range(x1,x2,-1):
                    if is_position_blocked(i, y1):
                        return True
            else:
                for i in range(x1,x2 + 1):
                    if is_position_blocked(i, y1):
                        return True
    return False
