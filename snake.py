from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
screen.listen()


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()

    def create_snake(self):
        starting_positions = [(0, 0), (-10, 0), [-20, 0]]
        for position in starting_positions:
            new_segment = Turtle("square")
            # new_segment.shapesize(0.5,0.5)
            new_segment.color(0,255,127)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        new_segment = Turtle("square")
        # new_segment.shapesize(0.5,0.5)
        new_segment.color(0,255,127)
        new_segment.penup()
        new_segment.goto(self.segments[len(self.segments) - 1].pos())
        self.segments.append(new_segment)

    def reset(self):
        self.segments.clear()
        self.create_snake()

    def move_upwards(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def move_downwards(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[x - 1].xcor()
            new_y = self.segments[x - 1].ycor()
            self.segments[x].goto(new_x, new_y)
        self.segments[0].fd(20)
