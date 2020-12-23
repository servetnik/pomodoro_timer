from tkinter import *
import pyglet
import tkinter.messagebox as mb

times = 0
cl = 0
chek = 1
song = pyglet.media.load('kolokol.mp3')
song2 = pyglet.media.load('kolokol2.mp3')

root = Tk()
root.geometry('500x300')
root.title('Timer')

message = StringVar()
message.set("25")
message1 = StringVar()
message1.set("5")
txt = Entry(root, width=10, textvariable=message)
per = Entry(root, width=10, textvariable=message1)
sec = 60
perer = 5
mint = 25

def tick():
       global sec, times, mint, start, chek, perer
       if cl != 0:
           start.pack_forget()
       if times == 0:
           mint = int(txt.get()) - 1
           perer = int(per.get()) - 1
       sec -= 1
       times += 1
       if sec == -1:
           mint -= 1
           sec = 59
       if mint == -1:
           chek += 1
           if chek % 2 == 0:
               mint = perer
               song.play()
           else:
               mint = int(txt.get()) - 1
               song2.play()
           
       if sec < 10:
           time['text'] = str(mint) + ':' + '0' + str(sec)
       else:
           time['text'] = str(mint) + ':' + str(sec)
           
       time.after(1000, tick)

def inf():
    mb.showinfo("О методе Pomodoro", "Метод «Помидора» (Pomodoro) — техника управления временем, предложенная Франческо Чирилло в конце 1980-х.\
 Методика предполагает увеличение эффективности работы при меньших временных затратах за счет глубокой концентрации и коротких перерывов. \
 В классической технике отрезки \
времени – «помидоры» длятся полчаса: 25 минут работы и 5 минут отдыха.")
time = Label(root, font='Times 30', fg='#0F0')
time.pack()
txt.pack()
per.pack()
question = Button(root,text='?', command= inf)
question.place(x=50, y=25)
label1 = Label(root, text = 'работа')
label1.place(x=20, y=130)
label2 = Label(root, text = 'отдых')
label2.place(x=20, y=190)
if cl == 0:
    start =Button(root, fg='blue', text='Start', command=tick)
    start.pack()
    cl += 1
    print(cl)

root.mainloop()
