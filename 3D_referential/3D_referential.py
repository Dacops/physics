import turtle, time, math
from tkinter import*

#window
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.title('physics')
screen.bgcolor('white')


def application():
    try:
        root.destroy()
    except:
        pass

    def end():
        root.destroy()
        turtle.bye()

    def error_message():
        global root
        root=Tk()
        error=Label(root, text='ERROR!\nChoose a value (0 < x ≤ 90)').pack()
        restart=Button(root, text='Restart', command=application).pack()
        leave=Button(root, text='Leave', command=end).pack()
        root.mainloop()

    def program():
        global ang
        ang = screen.textinput("Settings", "Choose your viewing angle (0 < x ≤ 90):\nRecommended values: (30 ≤ x ≤ 60)")
        if ang is None:
            end()
        try:
            ang = float(ang)
        except:
            error_message()


        turtle.color('white')
        turtle.speed(0)
        turtle.penup()
        turtle.goto(-600.00, -300.00)
        turtle.pendown()
        turtle.color('white')
        turtle.fillcolor('orange')
        turtle.begin_fill()


        if ang<0 or ang>90:
            error_message()
        else:
            turtle.fillcolor('orange')
            turtle.begin_fill()
            turtle.fd(600)
            turtle.lt(ang)
            turtle.fd(600)
            turtle.lt(180-ang)
            turtle.fd(600)
            turtle.lt(ang)
            turtle.fd(600)
            turtle.end_fill()


        for i in range(10):
            turtle.lt(180-ang)
            turtle.fd(600)
            turtle.lt(ang)
            turtle.fd(30)
            turtle.lt(180-ang)
            turtle.fd(600)
            turtle.lt(180+ang)
            turtle.fd(30)
            turtle.lt(180)


        for i in range(10):
            turtle.fd(600)
            turtle.lt(180-ang)
            turtle.fd(30)
            turtle.lt(ang)
            turtle.fd(600)
            turtle.lt(-ang)
            turtle.fd(30)
            turtle.rt(180-ang)
        turtle.lt(180-ang)


        turtle.penup()
        turtle.goto(-600.00, -300.00)
        turtle.fd(300)
        turtle.lt(ang)
        turtle.fd(300)
        turtle.lt(-ang)
        turtle.pendown()
        turtle.color('black')
        turtle.fd(400)
        turtle.lt(135)
        turtle.fd(20)
        turtle.lt(180)
        turtle.fd(20)
        turtle.lt(270)
        turtle.fd(20)
        turtle.lt(180)
        turtle.fd(20)
        turtle.write('X', font=('20'))
        turtle.lt(315)


        turtle.penup()
        turtle.goto(-600.00, -300.00)
        turtle.fd(300)
        turtle.lt(ang)
        turtle.fd(300)
        turtle.lt(-ang)
        turtle.pendown()
        turtle.lt(ang)
        turtle.fd(400)
        turtle.lt(135)
        turtle.fd(20)
        turtle.lt(180)
        turtle.fd(20)
        turtle.lt(270)
        turtle.fd(20)
        turtle.lt(180)
        turtle.fd(20)
        turtle.write('Y', font=('20'))
        turtle.lt(315-ang)

        if ang == 90:
            turtle.penup()
            turtle.goto(-600.00, -300.00)
            turtle.fd(300)
            turtle.lt(ang)
            turtle.fd(300)
            turtle.lt(-ang)
            turtle.pendown()
            turtle.circle(1)
            turtle.write('Z', align='right', font=('20'))
        else:
            turtle.penup()
            turtle.goto(-600.00, -300.00)
            turtle.fd(300)
            turtle.lt(ang)
            turtle.fd(300)
            turtle.lt(-ang)
            turtle.pendown()
            turtle.lt(90)
            turtle.fd(400)
            turtle.lt(135)
            turtle.fd(20)
            turtle.lt(180)
            turtle.fd(20)
            turtle.lt(270)
            turtle.fd(20)
            turtle.lt(180)
            turtle.fd(20)
            turtle.write('Z', font=('20'))
            turtle.lt(225)

        def directions():
            def res_dir():
                root.destroy()
                directions()

            global root
            set1 = screen.textinput("Settings", "Choose horizontal launch angle (in deg):\n (0 ≤ angle ≤ 360)")
            try:
                set1 = float(set1)
                if (set1 < 0 or set1 > 360) == True:
                    root=Tk()
                    error=Label(root, text='ERROR!\nChoose a value (0 ≤ angle ≤ 360)').pack()
                    restart=Button(root, text='Restart', command=res_dir).pack()
                    leave=Button(root, text='Leave', command=end).pack()
                    root.mainloop()
                else:
                    pass
            except:
                root=Tk()
                error=Label(root, text='ERROR!\nChoose a value (0 ≤ angle ≤ 360)').pack()
                restart=Button(root, text='Restart', command=res_dir).pack()
                leave=Button(root, text='Leave', command=end).pack()
                root.mainloop()

            set2 = screen.textinput("Settings", "Choose vertical launch angle (in deg):\n (0 ≤ angle ≤ 90)")
            try:
                set2 = float(set2)
                if (set2 < 0 or set2 > 90) == True:
                    root=Tk()
                    error=Label(root, text='ERROR!\nChoose a value (0 ≤ angle ≤ 360)').pack()
                    restart=Button(root, text='Restart', command=res_dir).pack()
                    leave=Button(root, text='Leave', command=end).pack()
                    root.mainloop()
                else:
                    pass
            except:
                root=Tk()
                error=Label(root, text='ERROR!\nChoose a value (0 ≤ angle ≤ 360)').pack()
                restart=Button(root, text='Restart', command=res_dir).pack()
                leave=Button(root, text='Leave', command=end).pack()
                root.mainloop()

            set3 = screen.textinput("Settings", "Choose launch speed (in kmh):")
            try:
                set3 = float(set3)
            except:
                root=Tk()
                error=Label(root, text='ERROR!\nChoose a value (0 ≤ angle ≤ 360)').pack()
                restart=Button(root, text='Restart', command=res_dir).pack()
                leave=Button(root, text='Leave', command=end).pack()
                root.mainloop()

            turtle.penup()
            turtle.goto(-600.00, -300.00)
            turtle.fd(300)
            turtle.lt(ang)
            turtle.fd(300)
            turtle.lt(-ang)
            turtle.pendown()

            if set1 < 0 or set1 > 360:
                root=Tk()
                error=Label(root, text='ERROR!\nChoose a value (0 ≤ angle ≤ 360)').pack()
                restart=Button(root, text='Restart', command=res_dir).pack()
                leave=Button(root, text='Leave', command=end).pack()
                root.mainloop()

            elif set1 <= 90:
                if set2 < 0 or set2 > 90:
                    root=Tk()
                    error=Label(root, text='ERROR!\nChoose a value (0 ≤ angle ≤ 360)').pack()
                    restart=Button(root, text='Restart', command=res_dir).pack()
                    leave=Button(root, text='Leave', command=end).pack()
                    root.mainloop()
                if set2 == 0:
                    turtle.color('red')
                    turtle.pensize(2)
                    turtle.lt((set1*ang)/90)
                    turtle.fd(set3)
                elif set2 == 90:
                    turtle.color('red')
                    turtle.pensize(2)
                    turtle.lt(90)
                    turtle.fd(set3)
                else:
                    turtle.pensize(1)
                    turtle.color('black')
                    turtle.lt((set1*ang)/90)
                    for i in range(2):
                        #Forward:
                        #-get green(cos red angle * set 3 = green)
                        green = (math.cos((((((set2*(90-((set1*ang)/90)))/90)+(set1*ang)/90)*math.pi)/180))*set3)
                        #-get forward(green / cos small angle  = forward)
                        turtle.fd(green/math.cos((((set1*ang)/90)*math.pi)/180))
                        turtle.lt(90-((set1*ang)/90))
                        #Up:
                        #-get blue (sin red angle * set3 =blue)
                        blue = (math.sin((((((set2*(90-((set1*ang)/90)))/90)+(set1*ang)/90)*math.pi)/180))*set3)
                        #-remove part (blue - (tan small angle * green))
                        turtle.fd(blue - ((math.tan((((set1*ang)/90)*math.pi)/180))*green))
                        turtle.lt(90+((set1*ang)/90))
                    turtle.pensize(2)
                    turtle.color('red')
                    turtle.lt((set2*(90-((set1*ang)/90)))/90)
                    turtle.fd(set3)

            elif set1 <= 180:
                if set2 < 0 or set2 > 90:
                    root=Tk()
                    error=Label(root, text='ERROR!\nChoose a value (0 ≤ angle ≤ 360)').pack()
                    restart=Button(root, text='Restart', command=res_dir).pack()
                    leave=Button(root, text='Leave', command=end).pack()
                    root.mainloop()
                if set2 == 0:
                    turtle.color('red')
                    turtle.pensize(2)
                    turtle.lt(ang+((set1-90)*(180-ang)/90))
                    turtle.fd(set3)
                elif set2 == 90:
                    turtle.color('red')
                    turtle.pensize(2)
                    turtle.lt(90)
                    turtle.fd(set3)
                else:
                    turtle.lt(ang+((set1-90)*(180-ang)/90))
                    turtle.pensize(1)
                    turtle.color('black')
                    if (ang+((set1-90)*(180-ang)/90)) < 90:
                        for i in range(2):
                            #Forward:
                            #angles:
                            ang_1= ang+((set1-90)*(180-ang)/90)
                            red = ((90-ang_1)*set2)/90 + ang_1
                            base = math.cos((red*math.pi)/180)*set3
                            turtle.fd(base/math.cos((ang_1*math.pi)/180))
                            turtle.lt(90-(ang+((set1-90)*(180-ang)/90)))
                            #Up:
                            #angles:
                            height = math.sin((red*math.pi)/180)*set3
                            turtle.fd(height-(math.tan((ang_1*math.pi)/180)*base))
                            turtle.lt(180-(90-(ang+((set1-90)*(180-ang)/90))))
                        turtle.pensize(2)
                        turtle.color('red')
                        turtle.lt(red-ang_1)
                        turtle.fd(set3)
                    if (ang+((set1-90)*(180-ang)/90)) == 90:
                        #Z
                        turtle.pensize(2)
                        turtle.color('red')
                        turtle.fd(set3)
                    if (ang+((set1-90)*(180-ang)/90)) > 90:
                        for i in range(2):
                            #after Z
                            #Forward:
                            #angles:
                            ang_1= 180-(ang+((set1-90)*(180-ang)/90))
                            red = ((90-ang_1)*set2)/90 + ang_1
                            base = math.cos((red*math.pi)/180)*set3
                            turtle.fd(base/math.cos((ang_1*math.pi)/180))
                            turtle.rt(90-ang_1)
                            #Up:
                            #angles:
                            height = math.sin((red*math.pi)/180)*set3
                            turtle.fd(height-(math.tan((ang_1*math.pi)/180)*base))
                            turtle.rt(90+ang_1)
                        turtle.pensize(2)
                        turtle.color('red')
                        turtle.lt(ang_1-red)
                        turtle.fd(set3)

            elif set1 <= 270:
                if set2 < 0 or set2 > 90:
                    root=Tk()
                    error=Label(root, text='ERROR!\nChoose a value (0 ≤ angle ≤ 360)').pack()
                    restart=Button(root, text='Restart', command=res_dir).pack()
                    leave=Button(root, text='Leave', command=end).pack()
                    root.mainloop()
                if set2 == 0:
                    turtle.pensize(2)
                    turtle.color('red')
                    turtle.lt(180+(((set1-180)*ang)/90))
                    turtle.fd(set3)
                elif set2 == 90:
                    turtle.pensize(2)
                    turtle.color('red')
                    turtle.lt(90)
                    turtle.fd(set3)
                else:
                    turtle.pensize(1)
                    turtle.color('black')
                    turtle.lt(180+(((set1-180)*ang)/90))
                    for i in range(2):
                        #Forward:
                        red_up=(180-((180+(((set1-180)*ang)/90))-(((((((set1-180)*ang)/90)+90)*set2)/90))))
                        red_down=((((set1-180)*ang)/90))
                        base=math.cos((red_up*math.pi)/180)*set3
                        turtle.fd(base / math.cos((red_down*math.pi)/180))
                        turtle.rt(90+(((set1-180)*ang)/90))
                        #Up:
                        op1=math.sin((red_up*math.pi)/180)*set3
                        op2=math.tan((red_down*math.pi)/180)*base
                        turtle.fd(op1+op2)
                        turtle.rt(90-(((set1-180)*ang)/90))
                    turtle.pensize(2)
                    turtle.color('red')
                    turtle.rt(((((((set1-180)*ang)/90)+90)*set2)/90))
                    turtle.fd(set3)


            elif set1 <= 360:
                if set2 < 0 or set2 > 90:
                    root=Tk()
                    error=Label(root, text='ERROR!\nChoose a value (0 ≤ angle ≤ 360)').pack()
                    restart=Button(root, text='Restart', command=res_dir).pack()
                    leave=Button(root, text='Leave', command=end).pack()
                    root.mainloop()
                if set2 == 0:
                    turtle.pensize(2)
                    turtle.color('red')
                    turtle.lt((180+ang)+((set1-270)*(180-ang)/90))
                    turtle.fd(set3)
                elif set2 == 90:
                    turtle.pensize(2)
                    turtle.color('red')
                    turtle.lt(90)
                    turtle.fd(set3)
                else:
                    ang_1=(((set1-270)*(180-ang))/90)
                    ang_2=((180+ang)+((set1-270)*(180-ang)/90))
                    turtle.lt((180+ang)+((set1-270)*(180-ang)/90))
                    turtle.pensize(1)
                    turtle.color('black')
                    if ((180+ang)+(ang_1)) > 270: #4th
                        for i in range(2):
                            #Forward:
                            #angles:
                            ang_3=90+(360-ang_2)
                            ang_up=((ang_3*set2)/90)
                            base=math.cos((((ang_up)-(360-ang_2))*math.pi)/180)*set3
                            turtle.fd(base/math.cos(((360-ang_2)*math.pi)/180))
                            turtle.lt(90+(360-ang_2))
                            #Up:
                            #angles:
                            height_1=math.sin((((ang_up)-(360-ang_2))*math.pi)/180)*set3
                            height_2=math.tan(((360-ang_2)*math.pi)/180)*base
                            turtle.fd(height_1+height_2)
                            turtle.lt(90-(360-ang_2))
                        turtle.pensize(2)
                        turtle.color('red')
                        turtle.lt(ang_up)
                        turtle.fd(set3)
                    if ((180+ang)+(ang_1)) == 270:
                        #Z
                        turtle.pensize(2)
                        turtle.color('red')
                        turtle.fd(set3)
                    if ((180+ang)+(ang_1)) < 270: #3rd
                        for i in range(2):
                            #after Z
                            #Forward:
                            #angles:
                            ang_3=ang_2-(180+ang)
                            ang_up=(((ang_2-90)*set2)/90)
                            red=ang_up-(ang_2-180)
                            base=(math.cos((red*math.pi)/180)*set3)
                            turtle.fd(base/math.cos(((ang_2-180)*math.pi)/180))
                            turtle.rt(180-(180-(ang_2-90)))
                            #Up:
                            #angles:
                            height_1 = (math.sin((red*math.pi)/180)*set3)
                            height_2 = (math.tan(((ang_2-180)*math.pi)/180)*base)
                            turtle.fd(height_1+height_2)
                            turtle.rt(180-(ang_2-90))
                        turtle.pensize(2)
                        turtle.color('red')
                        turtle.rt(ang_up)
                        turtle.fd(set3)



        directions()

        #projectile, SOON


        turtle.mainloop()
    program()


application()

#Dacops, 2021-02-24
