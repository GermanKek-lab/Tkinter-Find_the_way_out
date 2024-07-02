import tkinter
import random


def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])

def do_nothing(x):
    pass

def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")

def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
        
    if event.keysym == 'Down':
        move_wrap(player, (0, step))
    
    if event.keysym == 'Right':
        move_wrap(player, (step, 0))
    
    if event.keysym == 'Left':
        move_wrap(player, (-step, 0))
    check_move()


master = tkinter.Tk()

step = 60
N_X = 10
N_Y = 10
canvas = tkinter.Canvas(master, bg='blue',
                        width=step * N_X, height=step * N_Y)

player_pos = (random.randint(0, N_X - 1) * step,
              random.randint(0, N_Y - 1) * step)
exit_pos = (random.randint(0, N_X - 1) * step,
            random.randint(0, N_Y - 1) * step)

player = canvas.create_oval((player_pos[0], player_pos[1]),
                            (player_pos[0] + step, player_pos[1] + step), 
                            fill='green')
exit = canvas.create_oval((exit_pos[0], exit_pos[1]),
                          (exit_pos[0] + step, exit_pos[1] + step), 
                          fill='yellow')

label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()

def prepare_and_start():
    global player, exit
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    exit_pos = (random.randint(1, N_X - 1) * step,
                random.randint(1, N_Y - 1) * step)
    player = canvas.create_oval(
        (player_pos[0], player_pos[1]), 
        (player_pos[0] + step, player_pos[1] + step), 
        fill='green')
    exit = canvas.create_oval(
        (exit_pos[0], exit_pos[1]), 
        (exit_pos[0] + step, exit_pos[1] + step), 
        fill='yellow')
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)

restart = tkinter.Button(master, text="Начать заново", command=prepare_and_start())
restart.pack()

step = 60  # Размер клетки
N_X = 10
N_Y = 10   # Размер сетки
master = tkinter.Tk()
label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas = tkinter.Canvas(master, bg='blue', 
                        height=N_X * step, width=N_Y * step)
canvas.pack()
restart = tkinter.Button(master, text="Начать заново",
                         command=prepare_and_start)
restart.pack()
prepare_and_start()
master.mainloop()

def prepare_and_start():
    global player, exit, fires
    canvas.delete("all")    
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    exit_pos = (random.randint(1, N_X - 1) * step,
                random.randint(1, N_Y) * step)
    player = canvas.create_oval(
        (player_pos[0], player_pos[1]), 
        (player_pos[0] + step, player_pos[1] + step), 
        fill='green')
    exit = canvas.create_oval(
        (exit_pos[0], exit_pos[1]), 
        (exit_pos[0] + step, exit_pos[1] + step), 
        fill='yellow')
    N_FIRES = 6  # Число клеток, заполненных огнем
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(1, N_X - 1) * step,
                    random.randint(1, N_Y - 1) * step)
        fire = canvas.create_oval(
            (fire_pos[0], fire_pos[1]), 
            (fire_pos[0] + step, fire_pos[1] + step), 
            fill='red')
        fires.append(fire)
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)

player_pic = tkinter.PhotoImage(file="doctor.gif")
player = canvas.create_image((player_pos[0], player_pos[1]), image=player_pic, anchor='nw')


player_pic = tkinter.PhotoImage(file="doctor.gif")
exit_pic = tkinter.PhotoImage(file="tardis.gif")
fire_pic = tkinter.PhotoImage(file="fire.gif")
enemy_pic = tkinter.PhotoImage(file="dalek.gif")

def prepare_and_start():
    global player, exit, fires
    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    player = canvas.create_image(
        (player_pos[0], player_pos[1]), image=player_pic, anchor='nw')
    exit_pos = (random.randint(1, N_X - 1) * step,
                random.randint(1, N_Y - 1) * step)
    exit = canvas.create_image(
        (exit_pos[0], exit_pos[1]), image=exit_pic, anchor='nw')
    N_FIRES = 6  # Число клеток, заполненных огнем
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(1, N_X - 1) * step,
                    random.randint(1, N_Y - 1) * step)
        # fire = canvas.create_oval((fire_pos[0],fire_pos[1]), 
        # (fire_pos[0] + step, fire_pos[1] + step), fill='red')
        fire = canvas.create_image(
            (fire_pos[0], fire_pos[1]), image=fire_pic, anchor='nw')
        fires.append(fire)
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)

def prepare_and_start():
    global player, exit, fires, enemies
    canvas.delete("all")
    player_pos = (random.randint(0, N_X - 1) * step,
                  random.randint(0, N_Y - 1) * step)
    player = canvas.create_image(player_pos, image=player_pic, anchor='nw')
    exit_pos = (random.randint(0, N_X - 1) * step, 
                random.randint(0, N_Y - 1) * step)
    exit = canvas.create_rectangle(exit_pos, exit_pos[0] + 10, exit_pos[1] + 10, fill="black")
    N_FIRES = 6 #Число клеток, заполненных огнем
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(0, N_X - 1) * step, 
                    random.randint(0, N_Y - 1) * step)
        fire = canvas.create_rectangle(fire_pos, fire_pos[0] + 10, fire_pos[1] + 10, fill="black")
        fires.append(fire)
    N_ENEMIES = 4 #Число врагов
    enemies = []
    for i in range(N_ENEMIES):
        enemy_pos = (random.randint(0, N_X - 1) * step, 
                     random.randint(0, N_Y - 1) * step)
        enemy = canvas.create_image(enemy_pos, image=enemy_pic, anchor='nw')
        enemies.append((enemy, random.choice([always_right, random_move])))
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)

def always_right():
    return (step, 0)


def random_move():
    return random.choice([(step, 0), (-step, 0), (0, step), (0, -step)])

for enemy in enemies:
    direction = enemy[1]() # вызвать функцию перемещения у "врага"
    move_wrap(enemy[0], direction)


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")
        master.bind("<KeyPress>", do_nothing)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)
    for e in enemies:
        if canvas.coords(player) == canvas.coords(e[0]):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)