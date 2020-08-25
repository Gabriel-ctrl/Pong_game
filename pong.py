import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
# Score
score_a = 0
score_b = 0


##Paddle A 
paddle_a = turtle.Turtle()
#velocidade da animação
#no 0 é o maximo de vel. de animação
paddle_a.speed(0)    
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
#a podição inicial do paddle_a
paddle_a.goto(-350, 0)

##Padle B
paddle_b = turtle.Turtle()
#velocidade da animação
#no 0 é o maximo de vel. de animação
paddle_b.speed(0)    
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
#a podição inicial do paddle_b
paddle_b.goto(350, 0)

##Ball
ball = turtle.Turtle()
#velocidade da animação
#no 0 é o maximo de vel. de animação
ball.speed(0)    
ball.shape("circle")
ball.color("white")
ball.penup()
#a podição inicial do ball
ball.goto(0, 0)
#pra bola de mover
#variação de pixel q a bola se move, quando ela se move
ball.dx = 0.5
ball.dy = 0.5


#função para mover o paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
#função para mover para baixo

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#função para mover o paddle_b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
#função para mover para baixo

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#moving the ball
###########fazendo um placar
# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : {}  Player B : {}".format(score_a,score_b), align="center", font=("Courier",25,"normal"))

# main game loop - onde vai todas as paradas do jogo
while True:
    #toda hora q o while roda ele da um update na tela
    wn.update()
    #mover a bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #fazendo as bordas
    if ball.ycor() > 290:
        ball.sety(290 )
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1 
        score_a += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a,score_b), align="center", font=("Courier",25,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1     
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a,score_b), align="center", font=("Courier",25,"normal"))

    #colisão da bola com o paddle
      
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

