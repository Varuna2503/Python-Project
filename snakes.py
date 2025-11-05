import turtle
import random

# Screen and game setup
w, h = 500, 500
food_size = 10
delay = 100  

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

game_running = True  # Controls game state

def reset():
    global snake, snake_dir, food_position, game_running

    # Start from the bottom
    start_y = -h // 2 + 60  # 60 px above bottom edge
    snake = [[0, start_y], [0, start_y + 20], [0, start_y + 40], [0, start_y + 60], [0, start_y + 80]]
    snake_dir = "up"

    food_position = get_random_food_position()
    food.goto(food_position)

    game_running = True
    move_snake()

def move_snake():
    global snake_dir, game_running

    if not game_running:
        return

    # Create new head
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_dir][0]
    new_head[1] += offsets[snake_dir][1]

    # wall collisions
    if (
        new_head[0] > w / 2 - 10 or new_head[0] < -w / 2 + 10 or
        new_head[1] > h / 2 - 10 or new_head[1] < -h / 2 + 10
    ):
        game_over("You hit the wall!")
        return

    # --- Collision with itself ---
    if new_head in snake:
        game_over("You hit yourself!")
        return

    # Move forward
    snake.append(new_head)

    # Check for food collision
    if not food_collision():
        snake.pop(0)

    # Draw snake
    pen.clearstamps()
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

    # Update screen and schedule next move
    screen.update()
    turtle.ontimer(move_snake, delay)

def food_collision():
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

def get_random_food_position():
    x = random.randint(-w // 2 + 20, w // 2 - 20)
    y = random.randint(-h // 2 + 20, h // 2 - 20)
    x -= x % 20
    y -= y % 20
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

#direction controls
def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"

def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"

def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"

def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"

# Game Over
def game_over(reason):
    global game_running
    game_running = False
    pen.clearstamps()
    pen.hideturtle()
    pen.goto(0,0)
    pen.write(
        f"GAME OVER!\n{reason}",
        align="center",
        font=("Arial", 24, "bold")
    )
    screen.update()

# main screen
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake Game ")
screen.bgcolor("black")
screen.tracer(0)

#snake
pen = turtle.Turtle("square")
pen.penup()
pen.color("lime")

#food
food = turtle.Turtle("circle")
food.color("light blue")
food.shapesize(food_size / 20)
food.penup()

#key respondents
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")


reset()
turtle.done()
