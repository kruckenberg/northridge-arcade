import turtle


def play_pong():
    # globals
    screen_padding = 20 * 2
    screen_width = 1200
    right_edge = screen_width / 2
    left_edge = -right_edge

    screen_height = 900
    top_edge = screen_height / 2
    bottom_edge = -top_edge

    midpoint = 0

    ball_x_speed = 0.15
    ball_x_direction = 1
    ball_y_speed = 0.15
    ball_y_direction = 1

    # screen
    screen = turtle.Screen()
    screen.title("Knight's Pong")
    screen.bgcolor("black")
    screen.setup(
        width=screen_width + screen_padding, height=screen_height + screen_padding
    )
    screen.tracer(0)  # manually control screen updates with main game loop

    # left paddle
    l_paddle = turtle.Turtle()
    l_paddle.penup()  # don't draw paddle's path
    l_paddle.speed(0)  # manually control paddle movement
    l_paddle.shape("square")
    l_paddle.shapesize(5, 1)  # stretch square into a rectangle
    l_paddle.color("white")
    l_paddle.goto(left_edge, midpoint)  # set paddle's starting position

    # right paddle
    r_paddle = turtle.Turtle()
    r_paddle.penup()  # don't draw paddle's path
    r_paddle.speed(0)  # manually control paddle movement
    r_paddle.shape("square")
    r_paddle.shapesize(5, 1)  # stretch square into a rectangle
    r_paddle.color("white")
    r_paddle.goto(right_edge, midpoint)  # set paddle's starting position

    # ball
    ball = turtle.Turtle()
    ball.penup()  # don't draw ball's path
    ball.speed(0)  # manually control ball's movement
    ball.shape("circle")
    ball.color("white")

    def move_ball():
        ball.setx(ball.xcor() + (ball_x_speed * ball_x_direction))
        ball.sety(ball.ycor() + (ball_y_speed * ball_y_direction))

    # main game loop
    while True:
        screen.update()

        move_ball()


if __name__ == "__main__":
    play_pong()
