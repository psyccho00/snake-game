from turtle import Turtle

STARTING_POS= [(0,0),(-20,0),(-40,0)]
MOVE_DIS = 20
UP= 90
RIGHT= 0
LEFT= 180
DOWN= 270


class Snake:

    def __init__(self):
        self.segment_family = []
        self.create_snake()
        self.head = self.segment_family[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self,pos):
        segment = Turtle("square")
        segment.color("White")
        segment.penup()
        segment.goto(pos)
        self.segment_family.append(segment)

    def extend(self):
        self.add_segment(self.segment_family[-1].position())

    def move_snake(self):
        for parts in range(len(self.segment_family) - 1, 0, -1):
            x = self.segment_family[parts - 1].xcor()
            y = self.segment_family[parts - 1].ycor()
            self.segment_family[parts].goto(x, y)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
