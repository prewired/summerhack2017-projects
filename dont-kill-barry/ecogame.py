from tkinter import *
from PIL import Image, ImageTk
import numpy as np
tk=Tk()
tk.title("Don't Kill Barry!!")
canvas=Canvas(tk,width=1500,height=700)
canvas.pack()
image = Image.open("House_1.png")
image3 = Image.open("penguinbar.png")
image4 = Image.open("humanbar.png")
photo = ImageTk.PhotoImage(image)
photo3 = ImageTk.PhotoImage(image3)
photo4 = ImageTk.PhotoImage(image4)
measure=canvas.create_image(700+50,350,image=photo3)
measure2=canvas.create_image(670+50,350,image=photo4)
border1 = canvas.create_line(685+50,700,685+50,0)
border2 = canvas.create_line(715+50,700,715+50,0)
border3 = canvas.create_line(655+50,700,655+50,0)
pengscore=50
humanscore=20
adder=0
icebar=canvas.create_rectangle(655+50,700-pengscore+2,685+50,700-pengscore,fill="black")
energybar=canvas.create_rectangle(685+50,700-humanscore+2,715+50,700-humanscore,fill="black")
house=canvas.create_image(350,450,image=photo)
movedone=True
class statobj(object):
      def __init__(self,x,y,file):
          canvas.create_image(x,y,image=file)
ocea=ImageTk.PhotoImage(Image.open("ocean.png"))
ocean=statobj(1141,355,ocea)          
penguin1 = PhotoImage(file="penguin_image/penguin_1.png")
penguin2 = PhotoImage(file="penguin_image/penguin_2.png")
penguin3 = PhotoImage(file="penguin_image/penguin_3.png")
penguin4 = PhotoImage(file="penguin_image/penguin_4.png")
penguin5 = PhotoImage(file="penguin_image/penguin_5.png")
penguin6 = PhotoImage(file="penguin_image/penguin_6.png")
penguin7 = PhotoImage(file="penguin_image/penguin_7.png")
penguin8 = PhotoImage(file="penguin_image/penguin_8.png")
penguin9 = PhotoImage(file="penguin_image/penguin_9.png")
penguin10 = PhotoImage(file="penguin_image/penguin_10.png")
penguin11 = PhotoImage(file="penguin_image/penguin_11.png")
penguin12 = PhotoImage(file="penguin_image/penguin_12.png")
iceberg1 = PhotoImage(file="iceberg_image/iceberg1.png")
iceberg2 = PhotoImage(file="iceberg_image/iceberg2.png")
iceberg3 = PhotoImage(file="iceberg_image/iceberg3.png")
iceberg4 = PhotoImage(file="iceberg_image/iceberg4.png")
iceberg5 = PhotoImage(file="iceberg_image/iceberg5.png")
iceberg6 = PhotoImage(file="iceberg_image/iceberg6.png")
iceberg7 = PhotoImage(file="iceberg_image/iceberg7.png")
iceberg8 = PhotoImage(file="iceberg_image/iceberg8.png")
iceberg9 = PhotoImage(file="iceberg_image/iceberg9.png")
iceberg10 = PhotoImage(file="iceberg_image/iceberg10.png")
dead1 = PhotoImage(file="penguin_image/dying_penguin/penguin_1.png")
dead2 = PhotoImage(file="penguin_image/dying_penguin/penguin_2.png")
dead3 = PhotoImage(file="penguin_image/dying_penguin/penguin_3.png")
dead4 = PhotoImage(file="penguin_image/dying_penguin/penguin_4.png")
dead5 = PhotoImage(file="penguin_image/dying_penguin/penguin_5.png")
blankimage = PhotoImage(file="blank_image.png")
penguins = [penguin1, penguin2, penguin3, penguin4, penguin5, penguin6, penguin7, penguin8, penguin9, penguin10, penguin11, penguin12]
icebergs = [iceberg1, iceberg2, iceberg3, iceberg4, iceberg5, iceberg6, iceberg7, iceberg8, iceberg9, iceberg10]
dead = [dead1, dead2, dead3, dead4, dead5, blankimage]
currentpenguin = 0
currenticeberg = 0
direction = -2
energy_used = 0
energy_using = 0
totenergy=0
satis=350
alive = True
dying = 0
def die():
    global dying
    canvas.itemconfigure(penguin, image=dead[dying])
    dying += 1
    print("dead")
    if dying <= 5:
        canvas.after(200, die)
        canvas.move(penguin, 0, 10)
        scree=ImageTk.PhotoImage(Image.open("gameover.png"))
        screen=statobj(700,350,scree)
def penguin_movement():
    global currentpenguin, direction, alive
    if (currentpenguin+1) % 6 == 0:
        direction *= -1
    if currentpenguin >= 11:
        currentpenguin = 0
    else:
        currentpenguin += 1
    canvas.move(penguin, direction, 0)
    canvas.itemconfigure(penguin, image=penguins[currentpenguin])
    if alive == True:
        canvas.after(100, penguin_movement)
def iceberg_shrink():
    global energy_used, energy_using, alive,satis
    c=canvas.coords(icebar)
    canvas.coords(icebar,c[0],satis,c[2],satis+3)
    c=canvas.coords(energybar)
    energynew=750-energy_used
    energy_used=energy_used-0.8
    canvas.coords(energybar,c[0],energynew,c[2],energynew+3)
    if energy_used <= 1000:
        currenticeberg = int(energy_used/60)-1
        if currenticeberg <= 0:
            currenticeberg = 0
        canvas.itemconfigure(iceberg, image=icebergs[currenticeberg])
    else:
        canvas.itemconfigure(iceberg, image=blankimage)
        alive = False
        die()
    if alive == True:
        canvas.after(500, iceberg_shrink)
iceberg = canvas.create_image(1100, 440, image=icebergs[currenticeberg])
penguin = canvas.create_image(1100, 400, image=penguins[currentpenguin])
penguin_movement()
iceberg_shrink()
def kill():
    global box
    canvas.delete(box)
def click(event):
    global movedone
    #if movedone == True:
     #person.moveroom(event)
    global box
    #person.moveroom(event)
    mx,my=event.x,event.y
    box=canvas.create_rectangle(mx,my,mx+1,my+1,fill="#0ff00f")
    tk.after(10,kill)
def isclicked(x1,y1,x2,y2):
    vari=False
    coll=canvas.find_overlapping(x1,y1,x2,y2)
    if len(coll) > 2:
      for x in coll:
        try:
         if canvas.itemcget(x,"fill") == "#0ff00f":
            vari=True
        except TclError:
         pass
    return vari
class human(object):
    def __init__(self,x,y,name,maxi):   
        self.delay=10
        self.max=maxi
        self.name=name
        self.me=canvas.create_image(x,y,tags="imreal",image=ImageTk.PhotoImage(Image.open(name % 1)))
        self.count=1
        self.step=1
        self.rnum=3
        self.counter=1
        self.floor="down"
        self.room="right"
        self.floor,self.room=self.roomcheck()
        self.animate()
        self.loop1("if movedone == False:self.animate()",0,65)
    def roomcheck(self):
        x,y=canvas.coords(self.me)
        if y > 500:
            floor="down"
        elif x < 500 and x > 50:
            floor="up"
        if x > 380:
            room="right"
        elif x < 480 and x > 50:
            room="left"
        return floor,room    
    def moveroom(self,event):
        global movedone
        movedone=False
        x,y=event.x,event.y
        if y > 500:
            if x > 380:
             self.roomfour()
            else:
             self.roomthree()
        elif y < 500 and y > 100:
            if x > 400:
             self.roomtwo()
            elif x < 400 and x > 50:
             self.roomone()
        else:
             movedone = True
    def roomone(self):
        self.rnum=1
        if self.step == 1:
         self.movetostairs()
        elif self.step == 2:
         if self.floor == "down":
           self.updown()
         else:
           self.step=self.step+1
           self.roomone()
        elif self.step == 3: 
         self.left()
        elif self.step == 4: 
         self.floor,self.room=self.roomcheck()
         #self.movetostairs()
         self.step=1
         global movedone
         movedone=True
    def roomtwo(self):
        self.rnum=2
        if self.step == 1:
         self.movetostairs()
        elif self.step == 2:
         if self.floor == "down":
           self.updown()
         else:
           self.step=self.step+1
           self.roomtwo()
        elif self.step == 3:
            self.right()
        elif self.step == 4: 
         self.floor,self.room=self.roomcheck()
         #self.movetostairs()
         self.step=1
         global movedone
         movedone=True
    def roomthree(self):
        self.rnum=3
        if self.step == 1:
         self.movetostairs()
        elif self.step == 2: 
         if self.floor == "up":
           self.updown()
         else:
           self.step=self.step+1
           self.roomthree()
        elif self.step == 3:   
         self.left()
        elif self.step == 4: 
         self.floor,self.room=self.roomcheck()
         #self.movetostairs()
         self.step=1
         global movedone
         movedone=True
    def roomfour(self):
        self.rnum=4
        if self.step == 1:
         self.movetostairs()
        elif self.step == 2:
         if self.floor == "up":
           self.updown()
         else:
           self.step=self.step+1
           self.roomfour()
        elif self.step == 3:
            self.right()
        elif self.step == 4: 
         self.floor,self.room=self.roomcheck()
         #self.movetostairs()
         self.step=1
         global movedone
         movedone=True
    def left(self):
        if self.floor == "down":
         self.loop1("canvas.move(self.me,-2,0)",200,10)
         self.name="revh (%i).png"
        elif self.floor == "up":
         self.loop1("canvas.move(self.me,-2,0)",150,10)
         self.name="revh (%i).png"
    def right(self):
        if self.floor == "down":
         self.loop1("canvas.move(self.me,2,0)",50,10)
         self.name="hm (%i).png"
        elif self.floor == "up":
         self.loop1("canvas.move(self.me,2,0)",50,10)
         self.name="hm (%i).png"
    def movetostairs(self):
         myx=canvas.coords(self.me)[0]
         if self.floor == "down":
          if self.room == "left":  
           self.loop1("canvas.move(self.me,2,0)",abs(550-myx)/2,10)
           self.name="hm (%i).png"
          elif self.room == "right":
           self.loop1("canvas.move(self.me,-2,0)",abs(550-myx)/2,10)
           self.name="revh (%i).png"
         elif self.floor == "up":
           if self.room == "left":
            self.loop1("canvas.move(self.me,2,0)",abs(358-myx)/2,10)
            self.name="hm (%i).png"
           elif self.room == "right":
            self.loop1("canvas.move(self.me,-2,0)",abs(358-myx)/2,10)
            self.name="revh (%i).png"
    def updown(self):
        if self.floor == "up":
           self.loop1("canvas.move(self.me,1,1)",165,10)
           self.name="hm (%i).png"
        elif self.floor == "down":
           self.loop1("canvas.move(self.me,-1,-1)",165,10)
           self.name="revh (%i).png"
    def loop1(self,command,count,delay):
        exec(command)
        count=count-1
        self.loop2(command,count,delay)
    def loop2(self,command,count,delay):
        if count != 1:
         tk.after(delay,lambda:self.loop1(command,count,delay))
        else:
         self.step=self.step+1
         if self.rnum == 1:
           self.roomone()
         elif self.rnum == 2:
           self.roomtwo()
         elif self.rnum == 3:
           self.roomthree()
         elif self.rnum == 4:
           self.roomfour()
    def animate(self):
        file=(self.name % self.count)
        self.photo=ImageTk.PhotoImage(Image.open(file))
        canvas.itemconfig(self.me,image=self.photo)
        c=canvas.coords(self.me)
        self.count=self.count+self.counter
        if self.count >= self.max:
            self.count=1
class statobj(object):
      def __init__(self,x,y,file):
          canvas.create_image(x,y,image=file)          
class houseobj(object):
    def __init__(self,x,y,name,imx,imy,maxi,mytype):
        self.type=mytype
        if self.type == "fire":
              self.energy=0.12
        elif self.type == "tv":
              self.energy=0.06
        elif self.type == "computer":
              self.energy=0.06
        elif self.type == "light":
              self.energy=0.05        
        self.delay=17
        self.max=maxi
        self.imx,self.imy=imx,imy
        self.name=name
        file=image=ImageTk.PhotoImage(Image.open(name % 1))
        self.me=canvas.create_image(x,y,image=file)
        self.count=1
        self.counter=1
        self.clicked=False
        self.anim=True
        self.darkpic=ImageTk.PhotoImage(Image.open("mask.png"))
        self.loop1()
    def loop1(self):
        self.dark=False
        #if self.type == "light" and new.isday == False and self.anim == False and self.dark == False:
           #self.dark=True
           #self.pic=canvas.create_rectangle(0, 0, 750, 700, fill="black", stipple="gray75")
        #else:
           #try: 
            #canvas.delete(self.pic)
           #except AttributeError:
               #pass
        self.file=(self.name % self.count)
        self.photo=ImageTk.PhotoImage(Image.open(self.file))
        canvas.itemconfig(self.me,image=self.photo)
        c=canvas.coords(self.me)
        if self.clicked == False:
         self.clicked=isclicked(c[0]-self.imx/4,c[1]-self.imy/4,c[0]+self.imx/4,c[1]+self.imy/4)
        #for x in coll:
         #if x != self.me and x != house and canvas.itemcget(x,"tags") == "imreal":   
        if self.clicked == True:
            self.anim=not self.anim
            self.clicked = False
            if self.anim == False:
                self.count=0
            else:
                self.count=1
        global energy_used,satis
        if self.anim == True:
           energy_used += self.energy
           satis -= self.energy/2
           self.count=self.count+self.counter
           if self.type == "fire":
            adder=0.1
           if self.count >= self.max:
              self.count=1
        elif self.anim == False:
            satis += self.energy/2
        self.loop2()
    def loop2(self):
        tk.after(self.delay,self.loop1)
class window(object):
    def __init__(self,x,y,name,imx,imy,maxi):
        self.delay=10
        self.max=maxi
        self.imx,self.imy=imx,imy
        self.name=name
        self.me=canvas.create_image(x,y,image=ImageTk.PhotoImage(Image.open(name % 1)))
        self.count=1
        self.counter=1
        self.clicked=False
        self.var=False
        self.loop1()
    def loop1(self):
        file=(self.name % self.count)
        self.photo=ImageTk.PhotoImage(Image.open(file))
        canvas.itemconfig(self.me,image=self.photo)
        c=canvas.coords(self.me)
        if self.clicked == False:
         self.clicked=isclicked(c[0]-self.imx/4,c[1]-self.imy/4,c[0]+self.imx/4,c[1]+self.imy/4)  
        #for x in coll:
         #if x != self.me and x != house and canvas.itemcget(x,"tags") == "imreal":   
        if self.clicked == True:
           self.count=self.count+self.counter
           if self.count >= self.max:   
                self.counter=-1
                self.clicked=False
           if  self.count <= 1:   
              self.counter=1
              self.clicked=False
        self.loop2()
    def loop2(self):
        tk.after(self.delay,self.loop1)
class button(object):
    def __init__(self,x,y,text,color,actcolor,size,command):
        self.color=color
        self.actfill=actcolor
        self.command=command
        self.mx,self.my=0,0
        canvas.bind_all("<Motion>",self.mousemove)
        self.me=canvas.create_rectangle(x,y,x+size,y+size/2,fill=self.color,outline="white")
        read = canvas.create_text(x+size/2, y+size/4, text=text,fill="white")
        self.loop1()
    def kill(self):
        canvas.delete(self.me)
    def check(self):
        c=canvas.coords(self.me)
        if isclicked(c[0],c[1],c[2],c[3]):
          exec(self.command)
    def mousemove(self,event):
        self.mx,self.my=event.x,event.y
        self.checkmotion()
    def checkmotion(self):
        self.checker=canvas.create_rectangle(self.mx,self.my,self.mx+1,self.my+1,fill="#0f0f0f")
        c=canvas.coords(self.me)
        coll=canvas.find_overlapping(c[0],c[1],c[2],c[3])
        for x in coll:
            try:
             if canvas.itemcget(x,"fill") == "#0f0f0f":
                canvas.itemconfig(self.me,fill=self.actfill)
            except TclError:
                pass
        canvas.delete(self.checker)
    def loop1(self):
        canvas.itemconfig(self.me,fill=new.color,outline="white")
        self.checkmotion()
        self.check()
        self.loop2()
    def loop2(self):
        tk.after(30,self.loop1)
class game(object):
    def __init__(self):
        self.color="#0000ff"
        self.daylength=500
        self.count=200
        self.counter=1
        self.isday=True
        self.daynight()
    def daynight(self):
        if self.count > 254 or self.count <= 1:
           self.counter=self.counter-(self.counter*2)
        if self.count == 128:
            self.isday=not self.isday
        if self.isday == False:   
         global energy_used    
         print("You used",str(energy_used)+"kW today, good job!")
        self.color=('#%02X%02X%02X' % (self.count/1.5,self.count/1.5,self.count))
        canvas.config(bg=self.color)
        self.count=self.count+self.counter
        global humanscore,adder
        humanscore=humanscore-adder
        self.daynight2()
    def daynight2(self):
        tk.after(self.daylength,self.daynight)
new=game()
canvas.bind_all("<Button-1>",click)
awindow=window(175,440,"c (%i).png",320,320,10)
anwindow=window(520,440,"c (%i).png",320,320,10)
fireplace=houseobj(640,600,"fp (%i).png",320,320,1,"fire")
light1=houseobj(200,535,"lh (%i).png",50,250,1,"light")
television=houseobj(420,660,"tv (%i).png",150,150,1,"tv")
sofa=ImageTk.PhotoImage(Image.open("sofa.png"))
asofa=statobj(500,647,sofa)
fridge=ImageTk.PhotoImage(Image.open("fridge.png"))
ffffridgeo=statobj(65,633,fridge)
machine=ImageTk.PhotoImage(Image.open("washing.png"))
washingmachin=statobj(136,656,machine)
cooker=ImageTk.PhotoImage(Image.open("oven.png"))
washingmachin=statobj(180,647,cooker)
toil=ImageTk.PhotoImage(Image.open("toilet.png"))
toilette=statobj(410,483,toil)
tabl=ImageTk.PhotoImage(Image.open("table.png"))
table=statobj(260,658,tabl)
sin=ImageTk.PhotoImage(Image.open("sink.png"))
sink=statobj(650,464,sin)
bat=ImageTk.PhotoImage(Image.open("bathtub.png"))
bath=statobj(560,467,bat)
tabl2=ImageTk.PhotoImage(Image.open("table.png"))
table2=statobj(64,493,tabl2)
be=ImageTk.PhotoImage(Image.open("bed.png"))
bed=statobj(300,479,be)
computer=houseobj(64,456,"cp (%i).png",150,150,1,"computer")
tk.mainloop()
