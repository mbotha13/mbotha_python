from world import obstacles
obstacle_list = obstacles.get_obstacles()
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100
def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False

def print_obstacles():
    '''
    Prints the list of where the obstacles are.
    '''
    # if len(obstacle_list) > 0:
    if len(obstacles.obstacle_list) > 0:
        print('There are some obstacles:')
        #obstacle_list = obstacles.get_obstacles()
        for i in obstacles.obstacle_list:
            x,y = i
            print('- At position',str(x)+','+str(y),'(to',str(x+4)+','+str(y+4)+')')

def reset_variables():
    '''
    Resets all variables.
    '''
    global position_x, position_y, current_direction_index
    position_x = 0
    position_y = 0
    current_direction_index = 0
    obstacles.obstacles = []
