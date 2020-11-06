import turtle

from .. import obstacles
# from robot import robot_start
obstacle_list = obstacles.get_obstacles()
position_x = 0
position_y = 0

directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100
def show_position(robot_name):
    #turtle = turtle.Turtle()
    #turtle.pensize(1)
    turtle.pencolor('black')
    # if obstacles.is_position_blocked(position_x,position_y) == True:
    #     print("Sorry, there is an obstacle in the way.")
    # elif obstacles.is_position_blocked(position_x,position_y) == False:
    turtle.goto(position_x,position_y)
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')

def draw_obstacles():
    '''
    Functions that draws the turtles obstacles.
    '''
    for i in obstacle_list:
        x,y = i
        turtle.speed(0)
        turtle.penup()
        turtle.color("blue")
        turtle.begin_fill()
        turtle.setposition(x,y)
        turtle.pendown()
        turtle.goto(x+4, y)
        turtle.goto(x+4, y-4)
        turtle.goto(x, y-4)
        turtle.goto(x,y)
        turtle.penup()
        turtle.end_fill()


def border():
    '''
    Draws the border and the safe zone of the turtle.
    '''
    #turtle = turtle.Turtle()
    turtle.speed(3)
    turtle.penup()
    turtle.goto(-100,-200)
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor('red')
    #border.hideturtle()
    for side in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
    turtle.penup()
    turtle.goto(0,0)
    turtle.left(90)
    

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    print(f'your path is blocked: {obstacles.is_path_blocked(position_x,position_y,new_x,new_y)}')
    if obstacles.is_path_blocked(position_x,position_y,new_x,new_y) == True:
        print("Sorry, there is an obstacle in the way.")
    elif obstacles.is_path_blocked(position_x,position_y,new_x,new_y) == False:
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
    #border()
    

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        # turtle.right(90)
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        # turtle.left(90)
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False

def print_obstacles():
    '''
    Prints the list of obstacles where the turtle can't go.
    '''
    if len(obstacles.obstacle_list) > 0:
        print('There are some obstacles:')
        for i in obstacle_list:
            x,y = i
            print('- At position',str(x)+','+str(y),'(to',str(x+4)+','+str(y+4)+')')

def reset_variables():
    '''
    Function that resets the the postions and obstacle list.
    '''
    global position_x, position_y, current_direction_index
    position_x = 0
    position_y = 0
    current_direction_index = 0
    obstacles.obstacles = []

draw_obstacles()
border()
