import math
import turtle

# Configuración inicial
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)

# Dibujar el girasol
turtle.goto(0, -40)
turtle.pendown()
h = 0
phi = 137.508 * (math.pi / 180.0)
for i in range(16):
    for j in range(18):
        turtle.color("yellow")
        h += 0.005
        turtle.rt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.lt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.rt(180)
    turtle.circle(40, 24)

turtle.penup()
turtle.goto(0, 0)
turtle.color("black")
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()

# Mostrar centro del girasol
phi = 137.508 * (math.pi / 180.0)
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()
    
# Escribe "Te Quiero" en la parte superior del girasol
turtle.penup()
turtle.goto(0, 300)  # Ajusta la posición vertical según sea necesario
turtle.color("White")  # Color del texto
turtle.write("Te Quiero", align="center", font=("Arial", 24, "bold"))

# Oculta el cursor de la tortuga antes de salir
turtle.hideturtle()

# Cierra la ventana al hacer clic
turtle.exitonclick()
