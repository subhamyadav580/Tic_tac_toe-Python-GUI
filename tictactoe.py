from tkinter import *
import numpy as np

master = Tk(className="TIC TAC TOE")

#making canvas
c_width = 500
c_height = 500
C = Canvas(master,width = c_width, height = c_height)
C.pack()

def create_board():
    return (np.array([[2,2,2],
                     [2,2,2],
                     [2,2,2]]))

board = create_board()

def next_player(current_p):
    if current_p == 1:
        p = 0
        print("player changed to ",p)
    elif current_p == 0:
        p = 1
        print("player changed to ", p)
    return (p)

def draw():
    #drawing lines
    w = c_width/3
    h = c_height/3
    C.create_line(w, 0, w, c_height)
    C.create_line(w*2, 0, w*2, c_height)
    C.create_line(0, h, c_width, h)
    C.create_line(0, h*2, c_width, h*2)
#draw the shape
    #w=c_width/3
    #h=c_height/3
    #
#change the board
#evaluate the board
    #if matched then unbind
    #if draw then unbind

def draw_shape(x1,x2,y1,y2,pad,player):
    if player == 1:
        C.create_line(x1 + pad, y1 + pad, x2 - pad, y2 - pad)
        C.create_line(x2 - pad, y1 + pad, x1 + pad, y2 - pad)
    elif player == 0:
        C.create_oval(x1 + pad, y1 + pad, x2 - pad, y2 - pad)

def fill_quadrant(quad,pl):
    gw=c_width/3
    gh=c_height/3
    pad= gw/4 #padding

    #I quadrant
    if quad == 'I':
        draw_shape(0,gw,0,gh,pad,pl)
        board[0][0] = pl

    #II quadrant
    elif quad == 'II':
        draw_shape(gw,(gw*2),0,gh,pad,pl)
        board[0][1] = pl

    #III quadrant
    elif quad == 'III':
        draw_shape((gw*2),(gw*3),0,gh,pad,pl)
        board[0][2] = pl

    #IV quadrant
    elif quad == 'IV':
        draw_shape(0,gw,gh,(gh*2),pad,pl)
        board[1][0] = pl

    #V quadrant
    elif quad == 'V':
        draw_shape(gw,(gw*2),gh,(gh*2),pad,pl)
        board[1][1] = pl

    #VI quadrant
    elif quad == 'VI':
        draw_shape((gw*2),(gw*3),gh,(gh*2),pad,pl)
        board[1][2] = pl

    #VII quadrant
    elif quad == 'VII':
        draw_shape(0,gw,(gh*2),(gh*3),pad,pl)
        board[2][0] = pl

    #VIII quadrant
    elif quad == 'VIII':
        draw_shape(gw,(gw*2),(gh*2),(gh*3),pad,pl)
        board[2][1] = pl

    #IX quadrant
    elif quad == 'IX':
        draw_shape((gw*2),(gw*3),(gh*2),(gh*3),pad,pl)
        board[2][2] = pl

    return board

turnlist =[1]

def decide_quadrant(x,y):
    gw = c_width / 3
    gh = c_height / 3
    if y>0 and y<gh:
        if x>0 and x<gw:
            quadrant = 'I'
        elif x>gw and x<(gw*2):
            quadrant = 'II'
        elif x>(gw*2) and x<(gw*3):
            quadrant = 'III'

    elif y>gh and y<(gh*2):
        if x > 0 and x < gw:
            quadrant = 'IV'
        elif x > gw and x < (gw * 2):
            quadrant = 'V'
        elif x > (gw * 2) and x < (gw * 3):
            quadrant = 'VI'

    elif y>(gh*2) and y<(gh*3):
        if x > 0 and x < gw:
            quadrant = 'VII'
        elif x > gw and x < (gw * 2):
            quadrant = 'VIII'
        elif x > (gw * 2) and x < (gw * 3):
            quadrant = 'IX'

    return quadrant

def button_clicked(event):

    player = next_player(turnlist[-1])
    turnlist.append(player)

    quad = decide_quadrant(event.x,event.y)

    curr_board = fill_quadrant(quad,player)
    evaluate(curr_board)

def horizontal_check(b):
    for i in range(len(b)):
        if b[i,0] == b[i,1] and b[i,1] == b[i,2] and b[i,0]!=2:
            win = True
            player = b[i,0]
            break
        else:
            win = False
            player = 2

    win_dictionary = {
        "status": win,
        "player": player
    }
    return win_dictionary

def vertical_check(b):
    for i in range(len(b)):
        if b[0,i] == b[1,i] and b[1,i] == b[2,i] and b[0,i]!=2:
            win = True
            player = b[0,i]
            break
        else:
            win = False
            player = 2

    win_dictionary = {
        "status": win,
        "player": player
    }
    return win_dictionary

def diag_check(b):
    if b[0,0] == b[1,1] and b[1,1] == b[2,2] and b[0,0]!=2:
        win = True
        player = b[0,0]
    elif b[0,2] == b[1,1] and b[1,1] == b[2,0] and b[0,2]!=2:
        win = True
        player = b[0,2]
    else:
        win = False
        player = 2

    win_dictionary = {
        "status": win,
        "player": player
    }
    return win_dictionary


def evaluate(b):
    print ('evaluating...')
    h_d = horizontal_check(b)
    v_d = vertical_check(b)
    diag_d = diag_check(b)

    if h_d["status"]== True:
        print("Winner is " + str(h_d["player"]))
        C.unbind('<Button-1>')
    elif v_d["status"]== True:
        print("Winner is Player " + str(v_d["player"]))
        C.unbind('<Button-1>')
    elif diag_d["status"] == True:
        print("Winner is " + str(diag_d["player"]))
        C.unbind('<Button-1>')
    elif len(turnlist) == 10:
        print("DRAW MATCH")
        C.unbind('<Button-1>')

def play_game():
    draw()
    C.bind('<Button-1>', button_clicked)


play_game()

mainloop()

