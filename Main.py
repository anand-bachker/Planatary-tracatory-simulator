import cv2
import os as o
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
root=Tk()
root.state('zoomed')
root.title('Welcome to Space')
root.configure(background='lightblue')

#First frame Initialization---------------------------------------------------
image1 = PhotoImage(file='buttonwallpaper.png')
f2=Frame(root,height=1080,width=1920)
f2.pack()
def p():
    print('working')
    Second()
buttonmain=Button(f2,image=image1,comman=p)
buttonmain.pack()
#Second page---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
f2img1=PhotoImage(file='first.png')
f2img2=PhotoImage(file='second.png')
f2img3=PhotoImage(file='third.png')
f2img4=PhotoImage(file='fourth.png')
def Second():
    global f2
    f2.destroy()
    f2=Frame(root,width=1600,height=1080)
    f2.config(background='lightblue')
    f2.pack()
    butorb=Button(f2,image=f2img1 ,comman=sol)
    butorb.place(x=0,y=0)
    butproj=Button(f2,image=f2img2 ,comman=impproj)
    butproj.place(x=680,y=0)
    butkyp=Button(f2,image=f2img3 ,comman=knowyourplanets)
    butkyp.place(x=0,y=350)
    butgra=Button(f2,image=f2img4,comman=stats)
    butgra.place(x=680,y=350)



#graph--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def impproj():
    o.system('start graph.py')



#solar system---------------------------------------------------
def sol():
    o.system('start solar.py')





#know your planet-------------------------------------------------------------------
kypimg1 = PhotoImage(file='b.png')
def knowyourplanets():
    global root,f2
    f2.destroy()
    f2=Frame(root,width=1600,height=1080)
    f2.config(background='lightblue')
    f2.pack()
    #head text
    f2head=Label(f2,width=14,bg='lightblue',height=1,font=('Times',41,'bold','underline'),text='SOLAR SYSTEM')
    f2head.place(x=80,y=50)

    #body text
    f2body=Label(f2,width=33,height=6,font=('Times',23),bg='lightblue',justify=LEFT,text='The Solar System is the Sun and all the\n objects that orbit around it. The Sun is\n orbited by planets, asteroids, comets and\n other things. The Solar System is about 4.6\n billion years old. It formed by gravity in a\n large molecular cloud.')
    f2body.place(x=80,y=120)

    #ender
    f2ender=Label(f2,width=24,bg='yellow',height=1,font=('Times',32,'bold','underline'),text='CHOOSE YOUR NEXT STOP')
    f2ender.place(x=230,y=360)

    #Image
    f2img1 = PhotoImage(file='b.png')
    f2leb=Label(f2,image=kypimg1)
    f2leb.place(x=1050,y=0)

    #buttons
    Button(f2,text='SUN',height=5,width=20,command=third1).place(x=100,y=450)
    Button(f2,text='Mercury',height=5,width=20,command=third2).place(x=300,y=450)
    Button(f2,text='Venus',height=5,width=20,command=third3).place(x=500,y=450)
    Button(f2,text='Earth',height=5,width=20,command=third4).place(x=700,y=450)
    Button(f2,text='Mars',height=5,width=20,command=third5).place(x=100,y=550)
    Button(f2,text='Jupiter',height=5,width=20,command=third6).place(x=300,y=550)
    Button(f2,text='Saturn',height=5,width=20,command=third7).place(x=500,y=550)
    Button(f2,text='Uranus',height=5,width=20,command=third8).place(x=700,y=550)
    Button(f2,text='Pluto',height=5,width=20,command=third9).place(x=100,y=650)
    Button(f2,text='Goback',height=5,width=20,command=Second,bg='red').place(x=1300,y=650)



#Third Page------------------------------------------------------------------------------------------------------------
def third1():
    img=cv2.imread('Sun.png',1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()
#-------------------------------------------------------------------------------------------------------------------------------------
def third2():
    img=cv2.imread('Mercury.png',1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()
#------------------------------------------------------------------------------------------------------------------------------------------
def third3():
    img=cv2.imread('Venus.png',1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()
#--------------------------------------------------------------------------------------------------------------------------------------------
def third4():
    img=cv2.imread('Earth.png',1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.title("Earth")
    plt.show()
#----------------------------------------------------------------------------------------------------------------------------------------------------
def third5():
    img=cv2.imread('Mars.png',1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def third6():
    img=cv2.imread('Jupiter.png',1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def third7():
    img=cv2.imread('Saturn.png',1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def third8():
    img=cv2.imread('Uranus.png',1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def third9():
    img=cv2.imread('Neptune.png',1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()


#stats------------------------------------------------------------------------------------------------------------------------------------------------------------
def stats():
    global root,f2
    f2.destroy()
    f2=Frame(root,width=1600,height=1080)
    f2.config(background='palegreen1')
    f2.pack()
    Label(f2,width=33,height=6,font=('Times',50),bg='palegreen1',justify=LEFT,text='STATISTICS').place(x=230,y=-180)
    #body text1
    f2body=Label(f2,width=33,height=6,font=('Times',24),bg='palegreen1',justify=LEFT,text=' Here are are some statistics of the planets \n in our solar system:-')
    f2body.place(x=70,y=65)

    #body text2
    f2body=Label(f2,width=33,height=6,font=('Times',24),bg='palegreen1',justify=LEFT,text="Click the button below to see if  your \n rockets  velocity is enough to \nescape the gravity of a planet:-")
    f2body.place(x=70,y=260)

    #Button
    Button(f2,text='Radius',height=3,width=20,bg="grey",command=radius).place(x=100,y=210)
    Button(f2,text='Distance from sun',height=3,width=20,bg="White",command=dissun).place(x=300,y=210)
    Button(f2,text='Gravity',height=3,width=20,bg="grey",command=grav).place(x=500,y=210)
    Button(f2,text='Esacpe velocity',height=3,width=20,bg="white",command=esc).place(x=700,y=210)
    Button(f2,text='Goback',height=5,width=20,command=Second,bg='red').place(x=1300,y=650)
    Button(f2,text='Click me',height=5,width=20,command=escvel,bg='Yellow').place(x=450,y=500)
    Button(f2,text='Take off',height=5,width=20,command=vel,bg='grey').place(x=450,y=630)
    Button(f2,text='Exit',height=5,width=20,command=exit,bg='red').place(x=1300,y=450)






#Radius-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def radius():
    x=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
    y=[24397,60318,63710,33895,699110,582320,253620,246220]
    plt.bar(x,y,color='orange')
    plt.title('Radius Of Different Planets Of Solar System')
    plt.ylabel('RADIUS(in hundreds in metre)')
    plt.xlabel('PLANETS')
    plt.show()
#Distance from the sun--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def dissun():
    x=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
    y=[58,108,150,228,778,1427,2870,4497]
    plt.bar(x,y,color='yellow')
    plt.title('Distance from Sun Of Different Planets Of Solar System')
    plt.xlabel('PLANETS')
    plt.ylabel('DISTANCE(in millions in metre)')
    plt.show()
#gravity---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def grav():
    x=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
    y=[3.7,8.87,9.8,3.711,24.79,10.44,8.87,11.15]
    plt.bar(x,y,color='blue')
    plt.title('Gravity Of Different Planets Of Solar System')
    plt.ylabel('GRAVITY(in m/s**2)')
    plt.show()
#escape velocity----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def esc():
    x=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
    y=[4.25,10.36,11.17,5.02,59.54,35.46,21.28,23.44]
    plt.bar(x,y,color='red')
    plt.title('Escape Velocity Of Different Planets Of Solar System')
    plt.xlabel('PLANETS')
    plt.ylabel('ESCAPE VELOCITY(in Km/s)')
    plt.show()




#escape velocity calculator----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def escvel():
        import escvel


#rocket-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def vel():
    o.system('start Rocket.py')
        
        
root.mainloop()
