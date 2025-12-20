import turtle

# --- Configuration ---
SHELL_RADIUS = 120
BODY_COLOR = "#7FB069"      # turtle skin (head/limbs)
SHELL_COLOR = "#4C8C2B"     # main shell
SHELL_PATTERN = "#7FC47F"   # pattern on shell
EYE_COLOR = "white"
PUPIL_COLOR = "black"
HIGHLIGHT = "#CFF7D0"
OUTLINE = "black"

# Setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Cartoon Turtle")
screen.bgcolor("#E8F6EF")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

def draw_circle(x, y, radius, color, outline=OUTLINE):
    t.penup()
    t.goto(x, y - radius)
    t.setheading(0)
    t.pendown()
    t.color(outline, color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()

def draw_oval(x, y, width, height, color, outline=OUTLINE):
    # Draw an oval by stretching a circle using circle with varying step angle
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(outline, color)
    t.begin_fill()
    # approximate oval by drawing multiple semicircles scaled
    for i in range(2):
        t.circle(width, 90)
        t.circle(height, 90)
    t.end_fill()
    t.penup()

def draw_shell():
    # Main shell (big circle)
    draw_circle(0, 20, SHELL_RADIUS, SHELL_COLOR)

    # Shell inner pattern: concentric rings & hex-like segments
    # Draw a lighter ring
    t.pensize(1)
    draw_circle(0, 40, int(SHELL_RADIUS * 0.75), SHELL_PATTERN, outline=SHELL_COLOR)
    # Decorative arcs (simple radial segments)
    t.color(OUTLINE)
    t.pensize(2)
    for angle in range(0, 360, 45):
        t.penup()
        t.goto(0, 40)
        t.setheading(angle)
        t.forward(SHELL_RADIUS * 0.75)
        t.pendown()
        t.forward(SHELL_RADIUS * 0.25)
        t.penup()

    # Shell ridge highlight
    t.color(HIGHLIGHT)
    t.pensize(2)
    t.penup()
    t.goto(-SHELL_RADIUS * 0.6, 95)
    t.setheading(-30)
    t.pendown()
    t.width(6)
    t.forward(SHELL_RADIUS * 1.2)
    t.width(2)
    t.penup()

def draw_head():
    # Neck / head
    t.color(OUTLINE, BODY_COLOR)
    t.pensize(2)
    t.penup()
    t.goto(-40, 40)
    t.setheading(180)
    t.pendown()
    t.begin_fill()
    t.circle(40, 180)   # upper arc/head top
    t.right(90)
    t.forward(60)       # bottom of neck
    t.right(90)
    t.circle(40, 180)
    t.end_fill()
    t.penup()

    # Face circle (head)
    draw_circle(80, 25, 40, BODY_COLOR)

    # Eyes
    # left eye
    draw_circle(60, 55, 12, EYE_COLOR, outline=OUTLINE)
    draw_circle(60, 60, 5, PUPIL_COLOR, outline=PUPIL_COLOR)
    # right eye
    draw_circle(100, 55, 12, EYE_COLOR, outline=OUTLINE)
    draw_circle(100, 60, 5, PUPIL_COLOR, outline=PUPIL_COLOR)

    # Smile (arc)
    t.penup()
    t.goto(70, 40)
    t.setheading(-60)
    t.pendown()
    t.pensize(3)
    t.color(OUTLINE)
    t.circle(20, 120)
    t.penup()

    # cheek highlight
    t.color(HIGHLIGHT)
    draw_circle(92, 40, 6, HIGHLIGHT, outline=HIGHLIGHT)

def draw_legs_and_tail():
    # front left leg
    t.pensize(2)
    t.color(OUTLINE, BODY_COLOR)
    t.penup()
    t.goto(-70, -10)
    t.setheading(-110)
    t.pendown()
    t.begin_fill()
    t.circle(40, 160)
    t.end_fill()
    t.penup()

    # front right leg
    t.penup()
    t.goto(90, -10)
    t.setheading(-70)
    t.pendown()
    t.begin_fill()
    t.circle(40, -160)
    t.end_fill()
    t.penup()

    # back left leg
    t.penup()
    t.goto(-90, -40)
    t.setheading(-160)
    t.pendown()
    t.begin_fill()
    t.circle(30, 150)
    t.end_fill()
    t.penup()

    # back right leg
    t.penup()
    t.goto(110, -40)
    t.setheading(-20)
    t.pendown()
    t.begin_fill()
    t.circle(30, -150)
    t.end_fill()
    t.penup()

    # tail - small triangle
    t.color(OUTLINE, BODY_COLOR)
    t.penup()
    t.goto(-SHELL_RADIUS - 10, -10)
    t.pendown()
    t.begin_fill()
    t.setheading(-160)
    t.forward(25)
    t.right(120)
    t.forward(18)
    t.right(120)
    t.forward(30)
    t.end_fill()
    t.penup()

def draw_decoration():
    # small spots on legs
    t.color(OUTLINE)
    for pos in [(-80, -5), (-60, 5), (95, -5), (115, 5), (-95, -35), (125, -35)]:
        t.penup()
        t.goto(pos)
        t.pendown()
        t.begin_fill()
        t.circle(4)
        t.end_fill()
        t.penup()
    # a stripe on shell
    t.color(OUTLINE, "#2E6B14")
    t.penup()
    t.goto(-SHELL_RADIUS, 70)
    t.setheading(20)
    t.pendown()
    t.begin_fill()
    t.circle(SHELL_RADIUS * 0.3, 120)
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.penup()

def write_name():
    t.color("#2B5D2C")
    t.penup()
    t.goto(0, -SHELL_RADIUS - 60)
    t.write("Toby the Turtle", align="center", font=("Comic Sans MS", 20, "bold"))

def main():
    # Draw order: legs under shell, shell, head and details so layering looks nice.
    # Draw back legs first (so they appear behind shell)
    draw_legs_and_tail()
    draw_shell()
    draw_head()
    draw_decoration()
    write_name()

    t.penup()
    t.goto(0, -SHELL_RADIUS - 90)
    t.pendown()

main()

# finish
t.hideturtle()
screen.update()
screen.exitonclick()



if choice == 1:
    player_attack += 25
    player_def += 15
    player_hp += 15
    print('player stats',
'atk:',player_attack,'',
'def:',player_def,'',
'hp:',player_hp)
elif choice == 2:
    player_attack += 10
    player_hp += 20
    player_def += 25
    print('player stats',
'atk:',player_attack,'',
'def:',player_def,'',
'hp:',player_hp)
elif choice == 3:
    player_attack += 10
    player_hp += 25
    player_def += 20
    print('player stats',
'atk:',player_attack,'',
'def:',player_def,'',
'hp:',player_hp)