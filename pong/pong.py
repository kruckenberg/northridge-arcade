import turtle


def play_pong():
    # screen globals
    screen_padding = 20 * 2
    screen_width = 1200
    right_edge = screen_width / 2
    left_edge = -right_edge

    screen_height = 900
    top_edge = screen_height / 2
    bottom_edge = -top_edge

    midpoint = 0

    # ball globals
    ball_x_speed = 0.1
    ball_x_direction = 1
    ball_y_speed = 0.1
    ball_y_direction = 1

    # score
    score_left = 0
    score_right = 0

    # screen
    screen = turtle.Screen()
    screen.title("Knight's Pong")
    screen.bgcolor("black")
    screen.setup(
        width=screen_width + screen_padding, height=screen_height + screen_padding
    )
    screen.tracer(0)  # manually control screen updates with main game loop

    # scoreboard
    scoreboard = turtle.Turtle()
    scoreboard.speed(0)
    scoreboard.color("white")
    scoreboard.penup()
    scoreboard.goto(0, top_edge - 50)

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

    def change_ball_y_direction():
        nonlocal ball_y_direction
        ball_y_direction *= -1

    def change_ball_x_direction():
        nonlocal ball_x_direction
        ball_x_direction *= -1

    # paddle movement
    def move_l_paddle_up():
        l_paddle.sety(l_paddle.ycor() + 20)

    def move_l_paddle_down():
        l_paddle.sety(l_paddle.ycor() - 20)

    def move_r_paddle_up():
        r_paddle.sety(r_paddle.ycor() + 20)

    def move_r_paddle_down():
        r_paddle.sety(r_paddle.ycor() - 20)

    def update_scoreboard():
        scoreboard.clear()
        scoreboard.write(
            f"{score_left} - {score_right}",
            align="center",
            font=("Courier", 24, "bold"),
        )

    screen.listen()
    screen.onkeypress(move_l_paddle_up, "w")
    screen.onkeypress(move_l_paddle_down, "s")
    screen.onkeypress(move_r_paddle_up, "Up")
    screen.onkeypress(move_r_paddle_down, "Down")

    # check for wall collisions
    def check_for_wall_collision():
        ball_y_position = ball.ycor()

        if ball_y_position > top_edge or ball_y_position < bottom_edge:
            change_ball_y_direction()

    def check_for_l_paddle_collision():
        ball_x_position, ball_y_position = ball.position()
        l_paddle_x_position, l_paddle_y_position = l_paddle.position()

        # determine if ball is within paddle's y range
        if (
            ball_y_position >= l_paddle_y_position - 50
            and ball_y_position <= l_paddle_y_position + 50
        ):
            # determine if ball is within paddle's x range
            if (
                ball_x_position <= l_paddle_x_position + 20
                and ball_x_position >= l_paddle_x_position - 20
            ):
                change_ball_x_direction()

    def check_for_r_paddle_collision():
        ball_x_position, ball_y_position = ball.position()
        r_paddle_x_position, r_paddle_y_position = r_paddle.position()

        # determine if ball is within paddle's y range
        if (
            ball_y_position >= r_paddle_y_position - 50
            and ball_y_position <= r_paddle_y_position + 50
        ):
            # determine if ball is within paddle's x range
            if (
                ball_x_position <= r_paddle_x_position + 20
                and ball_x_position >= r_paddle_x_position - 20
            ):
                change_ball_x_direction()

    def check_for_point():
        ball_x_position, ball_y_position = ball.position()

        if ball_x_position < left_edge:
            nonlocal score_right
            score_right += 1
            change_ball_x_direction()
            update_scoreboard()
            ball.goto(midpoint, midpoint)

        if ball_x_position > right_edge:
            nonlocal score_left
            score_left += 1
            update_scoreboard()
            change_ball_x_direction()
            ball.goto(midpoint, midpoint)

    # initialize scoreboard
    update_scoreboard()

    # main game loop
    while True:
        screen.update()

        move_ball()
        check_for_point()
        check_for_wall_collision()
        check_for_l_paddle_collision()
        check_for_r_paddle_collision()


if __name__ == "__main__":
    play_pong()
