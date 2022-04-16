import turtle as t
import math as m
from tkinter import*
global z,p,br
root2 = Tk()
root2.geometry("260x240+30+30")
t.setup(width=1.0, height=1.0, startx=None, starty=None)
p=t.Turtle()
w=t.Turtle()
z=t.Turtle()
w.up()
w.ht()
w.goto(600,300)
z.speed(0)
p.speed(0)
w.speed(0)
g=9.81
p.shape('turtle')

#reset
def reset():
    global x
    x=1
    z.clear()
    p.clear()
    z.up()
    p.up()
    z.goto(-600,300)
    z.down()
    z.goto(-600,-300)
    z.goto(600,-300)
    p.goto(-600,-300)
    p.down()
    z.ht()
reset()
br=False

#planets

def mercury():
    global g,e1,e2,e11,e22,br,planet
    planet='Mercury'
    e11=(float(e1.get()))*m.pi/180
    e22=(float(e2.get()))
    g=3.59
    br=True
    p.color('grey')
    main()

def venus():
    global g,e1,e2,e11,e22,br,planet
    planet='Venus'
    e11=(float(e1.get()))*m.pi/180
    e22=(float(e2.get()))
    g=8.87
    br=True
    p.color('Pale Goldenrod')
    main()

def earth():
    global g,e1,e2,e11,e22,br,planet
    planet='Earth'
    e11=(float(e1.get()))*m.pi/180
    e22=(float(e2.get()))
    g=9.81
    br=True
    p.color('Deep Sky Blue')

    
    main()

def moon():
    global g,e1,e2,e11,e22,br,planet
    planet='Moon'
    e11=(float(e1.get()))*m.pi/180
    e22=(float(e2.get()))
    g=1.62
    br=True
    p.color('Indian Red')
    main()

    
def mars():
    global g,e1,e2,e11,e22,br,planet
    planet='Mars'
    e11=(float(e1.get()))*m.pi/180
    e22=(float(e2.get()))
    g=3.77
    br=True
    p.color('Firebrick')
    main()

    
def jupiter():
    global g,e1,e2,e11,e22,br,planet
    planet='Jupiter'
    e11=(float(e1.get()))*m.pi/180
    e22=(float(e2.get()))
    g=25.96
    br=True
    p.color('Salmon')
    main()
    

def saturn():
    global g,e1,e2,e11,e22,br,planet
    planet='Saturn'
    e11=(float(e1.get()))*m.pi/180
    e22=(float(e2.get()))
    g=11.8
    br=True
    p.color('Gold')
    main()

def uranus():
    global g,e1,e2,e11,e22,br,planet
    planet='Uranus'
    e11=(float(e1.get()))*m.pi/180
    e22=(float(e2.get()))
    g=10.67
    br=True
    p.color('Powder Blue')
    main()

def neptune():
    global g,e1,e2,e11,e22,br,planet
    planet='Neptune'
    e11=(float(e1.get()))*m.pi/180
    e22=(float(e2.get()))
    g=14.7
    br=True
    p.color('Cyan')
    main()

def pluto():
    global g,e1,e2,e11,e22,br,planet
    planet='Pluto'
    e11=(float(e1.get()))*m.pi/180
    e22=(float(e2.get()))
    g=0.42
    br=True
    p.color('Wheat')
    main()

#main
def main():
    global br
    while br:
        global x,e11,e22
        y=(x*m.tan(e11)-g/2/e22/e22/((m.cos(e11))**2)*x*x)
        x+=2
        p.goto(x-600,y-300)
        if y<=0:
            br=False
            p.up()
            p.goto(-600,-300)
            p.down()
            x=2
            p.color('black')
            dataout()




#buttons



Button(root2, text = "Mercury", command = mercury).place(x = 20, y = 80, width=60, height=25)
Button(root2, text = "Venus", command = venus).place(x = 100, y = 80, width=60, height=25)
Button(root2, text = "Earth", command = earth).place(x = 180, y = 80, width=60, height=25)
Button(root2, text = "Moon", command = moon).place(x = 20, y = 110, width=60, height=25)
Button(root2, text = "Mars", command = mars).place(x = 100, y = 110, width=60, height=25)
Button(root2, text = "Jupiter", command = jupiter).place(x = 180, y = 110, width=60, height=25)
Button(root2, text = "Saturn", command = saturn).place(x = 20, y = 140, width=60, height=25)
Button(root2, text = "Uranus", command = uranus).place(x = 100, y = 140, width=60, height=25)
Button(root2, text = "Neptune", command = neptune).place(x = 180, y = 140, width=60, height=25)
Button(root2, text = "Pluto", command = pluto).place(x = 100, y = 170, width=60, height=25)
Button(root2, text = 'Reset', command = reset).place(x= 180, y=200, width=60, height =25)


    #entries
Label(root2, text="Launch Angle").place(x=30,y=21)
Label(root2, text="Initial Speed").place(x=30, y=47)
global e1,e2
e1=Entry(root2)
e2=Entry(root2)
e1.place(x=115,y=21)
e2.place(x=115,y=47)

#dataout
def dataout():
    global z
    w.clear()
    w.up()
    w.goto(600,300)
    w.down()
    w.write('R ='+str(round((e22**2)*(m.sin(e11*2))/g,2))+'m')
    w.up()
    w.goto(600,290)
    w.down()
    w.write('H max ='+str(round((e22**2)*(m.sin(e11)*m.sin(e11))/(2*g),2))+'m')
    w.up()
    w.goto(600,280)
    w.down()
    w.write('T ='+str(round((2*(e22)*(m.sin(e11))/g)))+'sec')
    w.up()
    w.goto(600,300)
    w.down()
    print('#######')
    print()
    print('Planet =',planet)
    print('g =',g)
    print('Initial Speed =',e22)
    print('Launch angle =',e1.get())
    print('Distance Covered ',round((e22**2)*(m.sin(e11*2))/g,2),'m')
    print('Max height attained =',round((e22**2)*(m.sin(e11)*m.sin(e11))/(2*g),2),'m')
    print('Time to reach heightest point',round((e22)*(m.sin(e11))/g,2),'sec')
    print('Total flight duration',round((2*(e22)*(m.sin(e11))/g)),'sec')
    print()
    print('#######')
root2.mainloop()
