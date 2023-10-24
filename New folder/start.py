from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import winsound
#show-window2--------------------------

def main():
    global window
    window.destroy()
    window = Tk()
    window.title('window2')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/tree2.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    canvas.create_text(650, 170, text="Super A Five", fill="blue", font=('DRAGON HUNTER', 50))

    button_back = Button(canvas, text="Play",font=90, command=window3, bg='blue',border=25)
    button_back.pack()
    button_back.place(x=550, y=250, width=250)
    
    button_back2 = Button(canvas, text="Display",font=90 ,command=Display, bg='blue',border=25)
    button_back2.pack()
    button_back2.place(x=550, y=370, width=250)

    button_back3 = Button(canvas, text="Story",font=90, command=show_story, bg='blue',border=25)
    button_back3.pack()
    button_back3.place(x=550, y=490, width=250)


    window.mainloop()

#show-window3--------------------------------------

def window3():
    global window
    window.destroy() 
    window = Tk()
    window.title('av')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/tree.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=main, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)

    button_back = Button(canvas, text="Hard",font=90, command=Hard, bg='blue',border=25)
    button_back.pack()
    button_back.place(x=550, y=220, width=250)
    
    button_back2 = Button(canvas, text="Normal",font=90, command=Normal, bg='blue',border=25)
    button_back2.pack()
    button_back2.place(x=550, y=340, width=250)

    button_back3 = Button(canvas, text="Easy",font=90, command=Easy, bg='blue',border=25)
    button_back3.pack()
    button_back3.place(x=550, y=460, width=250)
    # window.after(1000, window4)
    window.mainloop()


#show-window4-----------------------------------------

def window4():
    global window
    window.destroy() 
    windows4 = Tk()
    windows4.title('v')
    app_width = windows4.winfo_screenwidth()
    app_height = windows4.winfo_screenheight()
    windows4.geometry(f'{app_width}x{app_height}')
    frame = Frame(windows4, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/window4.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    windows4.mainloop()

# show window for button story------------

def show_story():
    global window
    window.destroy() 
    window = Tk()
    window.title('show story')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/story.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=main, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)    
    cteat_img = Image.open("image/Player.png")
    cteat_img = cteat_img.resize((300, 300))
    background1 = ImageTk.PhotoImage(cteat_img)
    canvas.create_image(180, 350, image=background1, anchor=NW)

    window.mainloop()


#--show window for display-----------

def Display():
    global window
    window.destroy() 
    window = Tk()
    window.title('show story')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/display.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=main, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)    

    window.mainloop()

#Easy Game--------------------------------

def Easy():
    global window,x,position_enemy2,y,position_enemy3,a,position_enemy4,b
    window.destroy() 
    window = Tk()
    window.title('Easy')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/bg.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=window3, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)    
    # ---------add Wall of window4------   
    canvas.create_rectangle(0, 630, 400, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 20, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 1400, 20, fill="black", tags="wall")
    canvas.create_rectangle(1250, 0, 1300, 1200, fill="black", tags="wall")
    canvas.create_rectangle(500, 630, 1536, 810, fill="black", tags="wall")
    canvas.create_rectangle(500, 530, 550, 810, fill="black", tags="wall")
    canvas.create_rectangle(600, 570, 550, 810, fill="black", tags="wall")
    canvas.create_rectangle(650, 595, 550, 810, fill="black", tags="wall")
    canvas.create_rectangle(400, 530, 350, 810, fill="black", tags="wall")
    canvas.create_rectangle(400, 570, 300, 810, fill="black", tags="wall")
    canvas.create_rectangle(400, 600, 250, 810, fill="black", tags="wall")

    # -----add wall 2-------
    canvas.create_rectangle(400, 350, 200, 380, fill="black", tags="wall")
    canvas.create_rectangle(900, 350, 800, 380, fill="black", tags="wall")
    canvas.create_rectangle(1000, 470, 750, 440, fill="black", tags="wall")
    canvas.create_rectangle(1100, 550, 700, 520, fill="black", tags="wall")

    # -------add wall the end--------

    canvas.create_rectangle(1400, 120, 1000, 90, fill="black", tags="wall")
    canvas.create_rectangle(980, 190, 850, 160, fill="black", tags="wall")


    canvas.create_rectangle(400, 350, 200, 380, fill="black", tags="wall")
    canvas.create_rectangle(600, 320, 450, 290, fill="black", tags="wall")
    canvas.create_rectangle(730, 260, 640, 230, fill="black", tags="wall")
    canvas.create_rectangle(780, 320, 750, 290, fill="black", tags="wall")
    canvas.create_rectangle(810, 210, 780, 180, fill="black", tags="wall")
    canvas.create_rectangle(200, 310, 100, 280, fill="black", tags="wall")
    #-----------enemy-----------
    enemy1 = Image.open("image/enemy.png")
    enemy1 = enemy1.resize((70, 70))
    background1 = ImageTk.PhotoImage(enemy1)
    position_enemy1=canvas.create_image(180, 300, image=background1, anchor=NW)

    x = 3
    def movebird1():
        global x

        canvas.move(position_enemy1, x, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy1)
        if leftPos <= 180 or rightPos >= 410:
            x = -x
        print(x)
        canvas.after(30, movebird1)
    canvas.after(30, movebird1)


    enemy2 = Image.open("image/enemy.png")
    enemy2 = enemy2.resize((70, 70))
    background2 = ImageTk.PhotoImage(enemy2)
    position_enemy2=canvas.create_image(630, 580, image=background2, anchor=NW)
    y=3
    def movebird2():
        global y

        canvas.move(position_enemy2, y, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy2)
        if leftPos <= 630 or rightPos >= 1250:
            y = -y
        print(y)
        canvas.after(30, movebird2)
    canvas.after(30, movebird2)


    enemy2 = Image.open("image/enemy.png")
    enemy2 = enemy2.resize((70, 70))
    background3 = ImageTk.PhotoImage(enemy2)
    position_enemy3=canvas.create_image(730, 390, image=background3, anchor=NW)
    a=3
    def movebird3():
        global a

        canvas.move(position_enemy3, a, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy3)
        if leftPos <= 730 or rightPos >= 1020:
            a = -a
        print(a)
        canvas.after(30, movebird3)
    canvas.after(30, movebird3)



    enemy3 = Image.open("image/enemy.png")
    enemy3 = enemy3.resize((70, 70))
    background4 = ImageTk.PhotoImage(enemy3)
    position_enemy4=canvas.create_image(830, 110, image=background4, anchor=NW)
    b=3
    def movebird4():
        global b

        canvas.move(position_enemy4, b, 0)

        (leftPos, topPos, rightPos, bottomPos) = canvas.bbox(position_enemy4)
        if leftPos <= 830 or rightPos >= 1000:
            b = -b
        print(b)
        canvas.after(40, movebird4)
    canvas.after(30, movebird4)

    
    # --------add door--------

    image = Image.open('./image/door.png')
    imageTk = ImageTk.PhotoImage(image)
    canvas.create_image(1220, 59,image=imageTk)

    # ----------add coint -------

    
    image2 = Image.open('./image/coint.png')
    imageTk2 = ImageTk.PhotoImage(image2)
    canvas.create_image(1050, 69,image=imageTk2)
    canvas.create_image(169, 259,image=imageTk2)
    canvas.create_image(129, 259,image=imageTk2)
    canvas.create_image(529, 268,image=imageTk2)
    canvas.create_image(759, 500,image=imageTk2)
    canvas.create_image(859, 500,image=imageTk2)
    canvas.create_image(959, 500,image=imageTk2)
    canvas.create_image(1059, 500,image=imageTk2)
   



    window.mainloop()

    

#Normal Game--------------------------------

def Normal():
    global window
    window.destroy() 
    window = Tk()
    window.title('Normal')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/normal.png")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=window3, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)    


     # ---------add Wall of window4------   
    canvas.create_rectangle(150, 630, 0, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 20, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 1400, 20, fill="black", tags="wall")
    canvas.create_rectangle(1250, 0, 1300, 1200, fill="black", tags="wall")
    canvas.create_rectangle(800, 630, 400, 810, fill="black", tags="wall")

    canvas.create_rectangle(450, 530, 400, 810, fill="black", tags="wall")
    canvas.create_rectangle(500, 570, 450, 810, fill="black", tags="wall")
    canvas.create_rectangle(550, 595, 500, 810, fill="black", tags="wall")

    canvas.create_rectangle(300, 530, 250, 810, fill="black", tags="wall")
    canvas.create_rectangle(300, 570, 200, 810, fill="black", tags="wall")
    canvas.create_rectangle(300, 600, 150, 810, fill="black", tags="wall")

    canvas.create_rectangle(900, 530, 850, 810, fill="black", tags="wall")
    canvas.create_rectangle(900, 570, 800, 810, fill="black", tags="wall")
    canvas.create_rectangle(800, 600, 750, 810, fill="black", tags="wall")


    canvas.create_rectangle(1050, 530, 1000, 810, fill="black", tags="wall")
    canvas.create_rectangle(1100, 570, 1050, 810, fill="black", tags="wall")
    canvas.create_rectangle(1150, 600, 1100, 810, fill="black", tags="wall")

    canvas.create_rectangle(1400, 630, 1150, 810, fill="black", tags="wall")

    # --------add wall 2---------

    canvas.create_rectangle(710, 120, 580, 90, fill="black", tags="wall")
    # canvas.create_rectangle(330, 0, 300, 90, fill="black", tags="wall")

    canvas.create_rectangle(700, 470, 600, 440, fill="black", tags="wall")
    canvas.create_rectangle(700, 500, 560, 470, fill="black", tags="wall")
    canvas.create_rectangle(740, 500, 600, 470, fill="black", tags="wall")

    # -----wall right-----
    canvas.create_rectangle(860, 410, 800, 380, fill="black", tags="wall")
    canvas.create_rectangle(960, 350, 900, 320, fill="black", tags="wall")
    canvas.create_rectangle(1280, 290, 1000, 260, fill="black", tags="wall")

    canvas.create_rectangle(930, 210, 900, 180, fill="black", tags="wall")
    canvas.create_rectangle(820, 170, 790, 140, fill="black", tags="wall")

    # ------wall left-------
    canvas.create_rectangle(480, 410, 420, 380, fill="black", tags="wall")
    canvas.create_rectangle(380, 350, 320, 320, fill="black", tags="wall")
    canvas.create_rectangle(280, 290, 0, 260, fill="black", tags="wall")

    canvas.create_rectangle(370, 210, 340, 180, fill="black", tags="wall")
    canvas.create_rectangle(490, 170, 460, 140, fill="black", tags="wall")
   
    # -----------door 2-------------

    image = Image.open('./image/door.png')
    imageTk = ImageTk.PhotoImage(image)
    canvas.create_image(645, 59,image=imageTk)

    # ------------coins 2--------------
    image2 = Image.open('./image/coint.png')
    imageTk2 = ImageTk.PhotoImage(image2)

    # -------------coins right------------
    canvas.create_image(1100, 240,image=imageTk2)
    canvas.create_image(1140, 240,image=imageTk2)
    canvas.create_image(1180, 240,image=imageTk2)
    canvas.create_image(1220, 240,image=imageTk2)

    canvas.create_image(915, 160,image=imageTk2)
    canvas.create_image(805, 120,image=imageTk2)

    canvas.create_image(1220, 450,image=imageTk2)
    canvas.create_image(1180, 450,image=imageTk2)
    canvas.create_image(1140, 450,image=imageTk2)
    canvas.create_image(1140, 490,image=imageTk2)
    canvas.create_image(1180, 490,image=imageTk2)
    canvas.create_image(1220, 490,image=imageTk2)

    # ---------------coins left-------------
    canvas.create_image(55, 240,image=imageTk2)
    canvas.create_image(95, 240,image=imageTk2)
    canvas.create_image(135, 240,image=imageTk2)
    canvas.create_image(175, 240,image=imageTk2)

    canvas.create_image(355, 160,image=imageTk2)
    canvas.create_image(475, 120,image=imageTk2)

    canvas.create_image(135, 480,image=imageTk2)
    canvas.create_image(95, 480,image=imageTk2)
    canvas.create_image(55, 480,image=imageTk2)
    canvas.create_image(55, 440,image=imageTk2)
    canvas.create_image(95, 440,image=imageTk2)
    canvas.create_image(135, 440,image=imageTk2)

    # ----------------coins center-----------------
    canvas.create_image(612, 330,image=imageTk2)
    canvas.create_image(652, 330,image=imageTk2)
    canvas.create_image(692, 330,image=imageTk2)
    canvas.create_image(612, 290,image=imageTk2)
    canvas.create_image(652, 290,image=imageTk2)
    canvas.create_image(692, 290,image=imageTk2)


   



    window.mainloop()

#Hard Game--------------------------------

def Hard():
    global window
    window.destroy() 
    window = Tk()
    window.title('Hard')
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()
    window.geometry(f'{app_width}x{app_height}')
    frame = Frame(window, width=app_width, height=app_height)
    frame.pack()
    canvas = Canvas(frame, width=app_width, height=app_height)
    canvas.pack()
    bg_image = Image.open("image/bg3.jpg")
    bg_image = bg_image.resize((app_width, app_height))
    background = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=background, anchor=NW)
    button_back = Button(canvas, text="Back",font=40, command=window3, bg='red',border=10)
    button_back.pack()
    button_back.place(x=50, y=50, width=90)  

    # ----------Wall Of Hard----------
    canvas.create_rectangle(150, 630, 0, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 20, 810, fill="black", tags="wall")
    canvas.create_rectangle(0, 0, 1400, 20, fill="black", tags="wall")
    canvas.create_rectangle(1250, 0, 1300, 1200, fill="black", tags="wall")

    # -------------wall center--------------
    canvas.create_rectangle(750, 500, 550, 470, fill="black", tags="wall")

    # ---------------wall left-------------------
    canvas.create_rectangle(390, 550, 360, 520, fill="red", tags="wall")
    canvas.create_rectangle(490, 550, 460, 520, fill="red", tags="wall")

    # ----------------wall right-------------------
    canvas.create_rectangle(940, 550, 910, 520, fill="red", tags="wall")
    canvas.create_rectangle(840, 550, 810, 520, fill="red", tags="wall")
    

    canvas.create_rectangle(300, 530, 250, 810, fill="black", tags="wall")
    canvas.create_rectangle(300, 570, 200, 810, fill="black", tags="wall")
    canvas.create_rectangle(300, 600, 150, 810, fill="black", tags="wall")


    canvas.create_rectangle(1050, 530, 1000, 810, fill="black", tags="wall")
    canvas.create_rectangle(1100, 570, 1050, 810, fill="black", tags="wall")
    canvas.create_rectangle(1150, 600, 1100, 810, fill="black", tags="wall")

    canvas.create_rectangle(1400, 630, 1150, 810, fill="black", tags="wall")



    window.mainloop()
    
#show-of start window--------------

window = Tk()
app_width = window.winfo_screenwidth()
app_height = window.winfo_screenheight()
window.geometry(f'{app_width}x{app_height}')
bg_image = Image.open("./image/bg2.jpg")
bg_image = bg_image.resize((app_width, app_height))
background = ImageTk.PhotoImage(bg_image)

frame = Frame(window, width=app_width, height=app_height)
frame.pack()

canvas = Canvas(frame, width=app_width, height=app_height)
canvas.pack()
canvas.create_image(0, 0, image=background, anchor=NW)

splash_label = Label(window, text="Power A-five", font=("Robus", 60, "bold"))
splash_label.pack()
splash_label.place(relx=0.5, rely=0.3, anchor='center')
window.title("Progress Bar in Tk")
progressbar = ttk.Progressbar(mode="indeterminate")
progressbar.place(x=550, y=390, width=240)
progressbar.start()
window.after(2000, main) 
def play():
    winsound.PlaySound('./sound/086354_8-bit-arcade-video-game-start-sound-effect-gun-reload-and-jump-81124-_1_.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
play()

window.mainloop()


