from tkinter import *
root3 = Tk()
root3.geometry("260x450+30+30")
rig=PhotoImage(file='Rig.png')
wro=PhotoImage(file='Wro.png')

#PLANETS---------------------------------------------------------------------------------------------------------------------------------------
def mercury():
    global a,ff
    b=float(a.get())
    g=3.7
    R=2439700
    print('Gravity of Mercury is',g,'m/s**2')
    print('Radius of Mercury is',R,'m')
    EV=((2*g*R)**0.5)
    print('The Escape Velocity of Mercury is',EV,'m/s')
    print('Therefore,The minimum velocity required to Escape from Mercury is',EV,'m/s')
    if b>=EV:
        print('Your Space Shuttle/Rocket is Efficient to Escape from Gravity of Mercury')
        dec=Label(root3,image=wro)
        dec.place(x=30,y=240)
    else:
        print('Your Space Shuttle/Rocket is NOT Efficient to Escape from Gravity of Mercury')
        dec=Label(root3,image=rig)
        dec.place(x=30,y=240)

def venus():
    global a
    b=float(a.get())
    g=8.87
    R=6031800
    print('Gravity of Venus is',g,'m/s**2')
    print('Radius of Venus is',R,'m')
    EV=((2*g*R)**0.5)
    print('The Escape Velocity of Venus is',EV,'m/s')
    print('Therefore,The minimum velocity required to Escape from Venus is',EV,'m/s')
    if b>=EV:
        print('Your Space Shuttle/Rocket is Efficient to Escape from Gravity of Venus.')
        dec=Label(root3,image=wro)
        dec.place(x=30,y=240)
    else:
        print('Your Space Shuttle/Rocket is NOT Efficient to Escape from Gravity of Venus.')
        dec=Label(root3,image=rig)
        dec.place(x=30,y=240)

def earth():
    global a
    b=float(a.get())
    g=9.8
    R=6371000
    print('Gravity of Earth is',g,'m/s**2')
    print('Radius of Earth is',R,'m')
    EV=((2*g*R)**0.5)
    print('The Escape Velocity of Earth is',EV,'m/s')
    print('Therefore,The minimum velocity required to Escape from Earth is',EV,'m/s')
    if b>=EV:
        print('Your Space Shuttle/Rocket is Efficient to Escape from Gravity of Earth.')
        dec=Label(root3,image=wro)
        dec.place(x=30,y=240)
    else:
        print('Your Space Shuttle/Rocket is NOT Efficient to Escape from Gravity of Earth.')
        dec=Label(root3,image=rig)
        dec.place(x=30,y=240)

def mars():
    global a
    b=float(a.get())
    g=3.711
    R=3389500
    print('Gravity of Mars is',g,'m/s**2')
    print('Radius of Mars is',R,'m')
    EV=((2*g*R)**0.5)
    print('The Escape Velocity of Mars is',EV,'m/s')
    print('Therefore,The minimum velocity required to Escape from Mars is',EV,'m/s')
    if b>=EV:
        print('Your Space Shuttle/Rocket is Efficient to Escape from Gravity of Mars')
        dec=Label(root3,image=wro)
        dec.place(x=30,y=240)
    else:
        print('Your Space Shuttle/Rocket is NOT Efficient to Escape from Gravity of Mars')
        dec=Label(root3,image=rig)
        dec.place(x=30,y=240)

def jupiter():
    global a
    b=float(a.get())
    g=24.79
    R=69911000
    print('Gravity of Jupiter is',g,'m/s**2')
    print('Radius of Jupiter is',R,'m')
    EV=((2*g*R)**0.5)
    print('The Escape Velocity of Jupiter is',EV,'m/s')
    print('Therefore,The minimum velocity required to Escape from Jupiter is',EV,'m/s')
    if b>=EV:
        print('Your Space Shuttle/Rocket is Efficient to Escape from Gravity of Jupiter')
        dec=Label(root3,image=wro)
        dec.place(x=30,y=240)
    else:
        print('Your Space Shuttle/Rocket is NOT Efficient to Escape from Gravity of Jupiter.')
        dec=Label(root3,image=rig)
        dec.place(x=30,y=240)

def saturn():
    global a
    b=float(a.get())
    g=10.44
    R=58232000
    print('Gravity of Saturn is',g,'m/s**2')
    print('Radius of Saturn is',R,'m')
    EV=((2*g*R)**0.5)
    print('The Escape Velocity of Saturn is',EV,'m/s')
    print('Therefore,The minimum velocity required to Escape from Saturn is',EV,'m/s')
    if b>=EV:
        print('Your Space Shuttle/Rocket is Efficient to Escape from Gravity of Saturn.')
        dec=Label(root3,image=wro)
        dec.place(x=30,y=240)
    else:
        print('Your Space Shuttle/Rocket is NOT Efficient to Escape from Gravity of Saturn.')
        dec=Label(root3,image=rig)
        dec.place(x=30,y=240)
    
def uranus():
    global a
    b=float(a.get())
    g=8.87
    R=25362000
    print('Gravity of Uranus is',g,'m/s**2')
    print('Radius of Uranus is',R,'m')
    EV=((2*g*R)**0.5)
    print('The Escape Velocity of Uranus is',EV,'m/s')
    print('Therefore,The minimum velocity required to Escape from Uranus is',EV,'m/s')
    if b>=EV:
        print('Your Space Shuttle/Rocket is Efficient to Escape from Gravity of Uranus.')
        dec=Label(root3,image=wro)
        dec.place(x=30,y=240)
    else:
        print('Your Space Shuttle/Rocket is NOT Efficient to Escape from Gravity of Uranus.')
        dec=Label(root3,image=rig)
        dec.place(x=30,y=240)
    

def neptune():
    global a
    b=float(a.get())
    g=11.15
    R=24622000
    print('Gravity of Neptune is',g,'m/s**2')
    print('Radius of Neptune is',R,'m')
    EV=((2*g*R)**0.5)
    print('The Escape Velocity of Neptune is',EV,'m/s')
    print('Therefore,The minimum velocity required to Escape from Neptune is',EV,'m/s')
    if b>=EV:
        print('Your Space Shuttle/Rocket is Efficient to Escape from Gravity of Neptune.')
        dec=Label(root3,image=wro)
        dec.place(x=30,y=240)
    else:
        print('Your Space Shuttle/Rocket is NOT Efficient to Escape from Gravity of Neptune.')
        dec=Label(root3,image=rig)
        dec.place(x=30,y=240)

def pluto():
    global a
    b=float(a.get())
    g=0.62
    R=1188300
    print('Gravity of Pluto is',g,'m/s**2')
    print('Radius of Pluto is',R,'m')
    EV=((2*g*R)**0.5)
    print('The Escape Velocity of Pluto is',EV,'m/s')
    print('Therefore,The minimum velocity required to Escape from Pluto is',EV,'m/s')
    if b>=EV:
        print('Your Space Shuttle/Rocket is Efficient to Escape from Gravity of Pluto.')
        dec=Label(root3,image=wro)
        dec.place(x=30,y=240)
    else:
        print('Your Space Shuttle/Rocket is NOT Efficient to Escape from Gravity of Pluto')
        dec=Label(root3,image=rig)
        dec.place(x=30,y=240)

def moon():
    global a
    b=float(a.get())
    g=1.62
    R=1737100
    print('Gravity of Moon is',g,'m/s**2')
    print('Radius of Moon is',R,'m')
    EV=((2*g*R)**0.5)
    print('The Escape Velocity of Moon is',EV,'m/s')
    print('Therefore,The minimum velocity required to Escape from Moon is',EV,'m/s')
    if b>=EV:
        print('Your Space Shuttle/Rocket is Efficient to Escape from Gravity of Moon.')
        dec=Label(root3,image=wro)
        dec.place(x=30,y=240)
    else:
        print('Your Space Shuttle/Rocket is NOT Efficient to Escape from Gravity of Moon.')
        dec=Label(root3,image=rig)
        dec.place(x=30,y=240)



#entries------------------------------------------------------------------------------------------------------------------------------------
Label(root3, text="Enter the \n maximum \nVelocity(in m/s)").place(x=30,y=21)

global a
a=Entry(root3)
a.place(x=115,y=21)

#BUTTONS-------------------------------------------------------------------------------------------------------------------
Button(root3, text = "Mercury", command = mercury).place(x = 20, y = 80, width=60, height=25)
Button(root3, text = "Venus", command = venus).place(x = 100, y = 80, width=60, height=25)
Button(root3, text = "Earth", command = earth).place(x = 180, y = 80, width=60, height=25)
Button(root3, text = "Moon", command = moon).place(x = 20, y = 110, width=60, height=25)
Button(root3, text = "Mars", command = mars).place(x = 100, y = 110, width=60, height=25)
Button(root3, text = "Jupiter", command = jupiter).place(x = 180, y = 110, width=60, height=25)
Button(root3, text = "Saturn", command = saturn).place(x = 20, y = 140, width=60, height=25)
Button(root3, text = "Uranus", command = uranus).place(x = 100, y = 140, width=60, height=25)
Button(root3, text = "Neptune", command = neptune).place(x = 180, y = 140, width=60, height=25)
Button(root3, text = "Pluto", command = pluto).place(x = 100, y = 170, width=60, height=25)
Button(root3, text = 'Reset',).place(x= 180, y=200, width=60, height =25)
root3.mainloop()
