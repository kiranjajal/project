import sqlite3
from tkinter import messagebox
import samp
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk,ImageFilter,ImageShow


def put(a, b, c, d):
    try:

        conn = sqlite3.connect("gallery.db")
        cur = conn.cursor()
        cur.execute("create table if not exists reguser (abc text,pqr text,xyz numeric)")
        cur.execute("insert into reguser values (?,?,?,?)", [a, b, d, c])
        cur.execute("select * from reguser")
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        print(rows)
        messagebox._show("message", "registration successful")
    except:
        messagebox._show("message", "username already exists")



def checkuser(a1, pw):

    try:
        conn = sqlite3.connect("gallery.db")
        cur = conn.cursor()
        cur.execute("select username,password from reguser where username like ? and password like ?", [a1,pw])
        rows = cur.fetchone()
        c1,c2=rows[0],rows[1]
        print(c1,c2)

        def OpenFile():
            name = askopenfilename(initialdir="C:/Users/Ajay/Pictures/",
                                   filetypes=(("All files", "*.*"), ("", "*.*")),
                                   title="Choose a file."
                                   )
            print(name)

            im = Image.open(name)
            imm = ImageTk.PhotoImage(im)

            a25 = Label(root5, image=imm)
            a25.image = imm
            a25.pack()

            def cropImg():
                def cr():
                    x1 = int(cropex1.get())
                    y1 = int(cropey1.get())
                    x2 = int(cropex2.get())
                    y2 = int(cropey2.get())
                    t1 = Toplevel()
                    crImg = im.crop((x1, y1, x2, y2))
                    cr1 = ImageTk.PhotoImage(crImg)
                    a2 = Label(t1, image=cr1)
                    a2.image = cr1

                    def sve1():
                        def sv():
                            eimg8 = eimg7.get()
                            e27 = "C:/Users/Ajay/Pictures/%s.jpg" % eimg8
                            crImg.save(e27)

                        nameimg6 = Toplevel()
                        nimg7 = Label(nameimg6, text='Enter name for edited image')
                        eimg7 = Entry(nameimg6)
                        bim7 = Button(nameimg6, text='Save', command=sv)

                        nimg7.pack()
                        eimg7.pack()
                        bim7.pack()

                    menu2 = Menu(t1)
                    t1.config(menu=menu2)
                    save = Menu(menu2)
                    save.add_command(label='Save', command=sve1)
                    menu2.add_cascade(label='Save', menu=save)
                    a2.pack()

                t = Toplevel()
                cropq = Label(t, text='Enter valid coordinates')
                cropex1 = Entry(t)
                cropey1 = Entry(t)
                cropex2 = Entry(t)
                cropey2 = Entry(t)
                croplx1 = Label(t, text='x1')
                croply1 = Label(t, text='y1')
                croplx2 = Label(t, text='x2')
                croply2 = Label(t, text='y2')
                cropq.pack()
                croplx1.pack()
                cropex1.pack()
                croply1.pack()
                cropey1.pack()
                croplx2.pack()
                cropex2.pack()
                croply2.pack()
                cropey2.pack()

                cropb = Button(t, text='Crop', command=cr)
                cropb.pack()

            def effect():
                t = Toplevel()
                eff = im.convert("L")
                eff2 = ImageTk.PhotoImage(eff)
                a1 = Label(t, image=eff2)
                a1.image = eff2

                def sve1():
                    def sv():
                        eimg7 = eimg6.get()
                        e26 = "C:/Users/Ajay/Pictures/%s.jpg" % eimg7
                        eff.save(e26)

                    nameimg5 = Toplevel()
                    nimg6 = Label(nameimg5, text='Enter name for edited image')
                    eimg6 = Entry(nameimg5)
                    bim6 = Button(nameimg5, text='Save', command=sv)

                    nimg6.pack()
                    eimg6.pack()
                    bim6.pack()

                menu1 = Menu(t)
                t.config(menu=menu1)
                save = Menu(menu1)
                save.add_command(label='Save', command=sve1)
                menu1.add_cascade(label='Save', menu=save)

                a1.pack()

                # eff.save("C:/Users/Ajay/Pictures/.jpg")

            # def si():
            #   im.save("C:/Users/Ajay/Pictures/cropped123.jpg")

            def rotateL():
                t = Toplevel()
                rl = im.rotate(90)
                r2 = ImageTk.PhotoImage(r1)
                a3 = Label(t, image=r2)
                a3.image = r2

                def sve1():
                    def sv():
                        eimg4 = eimg5.get()
                        e25 = "C:/Users/Ajay/Pictures/%s.jpg" % eimg4
                        r1.save(e25)

                    nameimg4 = Toplevel()
                    nimg5 = Label(nameimg4, text='Enter name for edited image')
                    eimg5 = Entry(nameimg4)
                    bim5 = Button(nameimg4, text='Save', command=sv)

                    nimg5.pack()
                    eimg5.pack()
                    bim5.pack()

                menu1 = Menu(t)
                t.config(menu=menu1)
                save = Menu(menu1)
                save.add_command(label='Save', command=sve1)
                menu1.add_cascade(label='Save', menu=save)

                a3.pack()

            def rotateR():
                t = Toplevel()
                rr = im.rotate(-90)
                rr1 = ImageTk.PhotoImage(rr)
                a4 = Label(t, image=rr1)
                a4.image = rr1

                def sve1():
                    def sv():
                        eimg3 = eimg4.get()
                        e24 = "C:/Users/Ajay/Pictures/%s.jpg" % eimg3
                        rr.save(e24)

                    nameimg3 = Toplevel()
                    nimg3 = Label(nameimg3, text='Enter name for edited image')
                    eimg4 = Entry(nameimg3)
                    bim3 = Button(nameimg3, text='Save', command=sv)

                    nimg3.pack()
                    eimg4.pack()
                    bim3.pack()

                menu1 = Menu(t)
                t.config(menu=menu1)
                save = Menu(menu1)
                save.add_command(label='Save', command=sve1)
                menu1.add_cascade(label='Save', menu=save)

                a4.pack()

            def flipH():
                t = Toplevel()
                fl = im.transpose(Image.FLIP_LEFT_RIGHT)
                f2 = ImageTk.PhotoImage(f1)
                a5 = Label(t, image=f2)
                a5.image = f2

                def sve1():
                    def sv():
                        eim2 = eim.get()
                        e25 = "C:/Users/Ajay/Pictures/%s.jpg" % eim2
                        f1.save(e25)

                    nameimg2 = Toplevel()
                    nimg1 = Label(nameimg2, text='Enter name for edited image')
                    eim = Entry(nameimg2)
                    bim1 = Button(nameimg2, text='Save', command=sv)

                    nimg1.pack()
                    eim.pack()
                    bim1.pack()

                menu1 = Menu(t)
                t.config(menu=menu1)
                save = Menu(menu1)
                save.add_command(label='Save', command=sve1)
                menu1.add_cascade(label='Save', menu=save)

                a5.pack()

            '''def flipV():
                fh=im.transpose(Image.FLIP_TOP_BOTTOM)
                fh.show()
               '''

            def flipV():
                t = Toplevel()
                rr = im.rotate(-180)
                f3 = ImageTk.PhotoImage(rr)
                a6 = Label(t, image=f3)
                a6.image = f3

                def sve1():
                    def sv():
                        eimg2 = eimg.get()
                        e23 = "C:/Users/Ajay/Pictures/%s.jpg" % eimg2
                        rr.save(e23)

                    nameimg = Toplevel()
                    nimg = Label(nameimg, text='Enter name for edited image')
                    eimg = Entry(nameimg)
                    bim = Button(nameimg, text='Save', command=sv)

                    nimg.pack()
                    eimg.pack()
                    bim.pack()

                menu1 = Menu(t)
                t.config(menu=menu1)
                save = Menu(menu1)
                save.add_command(label='Save', command=sve1)
                menu1.add_cascade(label='Save', menu=save)

                a6.pack()

            '''sve=Menu(menu)
            sve.add_command(label='Save', command=si)
            menu.add_cascade(label='Save', menu=sve)'''

            edit = Menu(menu)
            edit.add_command(label='Crop', command=cropImg)
            edit.add_command(label='Black and White', command=effect)
            edit.add_command(label='Rotate Left', command=rotateL)
            edit.add_command(label='Rotate Right', command=rotateR)
            edit.add_command(label='FlipHorizontal', command=flipH)
            edit.add_command(label='FlipVertical', command=flipV)

            menu.add_cascade(label='Edit', menu=edit)

        # def brow():
        root5 = Tk()
        Title = root5.title("IMAGE EDITOR")
        root5.geometry('2400x1800')

        '''im=Image.open("C:/Users/Ajay/Pictures/Ultra-HD-I-Phone-Wallpapers.jpg")
            i1=ImageTk.PhotoImage(im)

            #i2=i.resize(2400,1800)
            k=Label(root5,image=im.thumbnail((2400,1800)))
            k.image=im.thumbnail((2400,1800))
            k.pack()'''

        # Menu Bar

        menu = Menu(root5)
        root5.config(menu=menu)

        file = Menu(menu)

        file.add_command(label='Open', command=OpenFile)
        file.add_command(label='Exit', command=lambda: exit())

        menu.add_cascade(label='File', menu=file)
        root5.mainloop()

        conn.commit()
        conn.close()



    except:
        messagebox._show("message","Invalid username or password")


def lets():
    print('hello')

