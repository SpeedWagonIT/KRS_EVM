from tkinter import *
root = Tk()
root.geometry('1920x1080')
root.title("Курсовая работа")
root.resizable(width=False, height=False)
_rec_list = list([[60, 20], [130, 160]])                         #array of coordinates of rectangle points
_tri_list = list([[0, 0], [0, 0], [0, 0]])           #array of coordinates of triangle points
_circ_list = list([[0, 0], [0, 0]])                              #array of coordinates of circle points
_point_list = [[]]
_port_list = list([[0,0],[0,0]])
i = 0
k = 28
j = 40

_circ_list[0][0] = _tri_list[1][0]
_circ_list[0][1] = _tri_list[1][1] - 5
_circ_list[1][0] = _tri_list[1][0] + 10
_circ_list[1][1] = _tri_list[1][1] + 5

#create canvas and menu
c = Canvas(root, width=1680, height=1080, bg='silver')
c.pack(side='left')
var=IntVar()
var.set(0)
ent = Entry(width=30)
but = Button(text="нарисовать")
rbutton1=Radiobutton(root, text='Шифраторы',variable=var,value=0)
rbutton2=Radiobutton(root, text='Дешифраторы',variable=var,value=1)
rbutton3=Radiobutton(root, text='Мультиплексоры',variable=var,value=2)
rbutton1.place(x = 1700,y = 910)
rbutton2.place(x = 1700,y = 930)
rbutton3.place(x = 1700,y = 950)
ent.place(x = 1700,y = 975)
but.place(x = 1700,y = 1000)
lbl = Label(root, text= '© Golovko Artyom Romanovich')
lbl.place(x = 1700, y = 1060)

def entry_scan(event):
    s = ent.get()
    s = s.split()
    i = var.get()
    print(s,i)

def _set_CD():
    c.create_rectangle(_rec_list[0][0], _rec_list[0][1],
                       _rec_list[1][0], _rec_list[1][1],
                       fill='white', outline='black')
    i = 3
    k = 28
    while (i >= 0):
        c.create_line(_rec_list[0][0] - 15, _rec_list[0][1]+k, _rec_list[0][0], _rec_list[0][1]+k,width=2)
        c.create_text(_rec_list[0][0] + 10, _rec_list[0][1]+k, text=i, justify=CENTER, font="Verdana 14")
        i -= 1
        k+=25

def _set_NOT():
    _tri_list[0][0] = _port_list[0][0]
    _tri_list[0][1] = _port_list[0][1] + 10
    _tri_list[1][0] = _port_list[0][0] + 15
    _tri_list[1][1] = _port_list[0][1]
    _tri_list[2][0] = _port_list[0][0]
    _tri_list[2][1] = _port_list[0][1] - 10

    _circ_list[0][0] += _tri_list[1][0]
    _circ_list[0][1] += _tri_list[1][1] + 1
    _circ_list[1][0] += _tri_list[1][0] - 1
    _circ_list[1][1] += _tri_list[1][1]

    _rec_list[0][0] = _tri_list[1][0]+10
    _rec_list[0][1] = _tri_list[1][1]
    _rec_list[1][0] = _rec_list[0][0]+15
    _rec_list[1][1] = _rec_list[0][1]

    c.create_polygon(_tri_list[0][0], _tri_list[0][1],
                     _tri_list[1][0], _tri_list[1][1],
                     _tri_list[2][0], _tri_list[2][1],
                     fill='white', outline='black')

    c.create_oval(_circ_list[0][0], _circ_list[0][1], _circ_list[1][0], _circ_list[1][1],
                  width=1, fill='white', outline='black')

    c.create_line(_rec_list[0][0], _rec_list[1][1], _rec_list[1][0], _rec_list[1][1], width=2)


def _set_DC():
    c.create_rectangle(_rec_list[0][0], _rec_list[0][1], _rec_list[1][0], _rec_list[1][1],
                       fill='white', outline='black')
    i = 3
    k = 28
    while (i >= 0):
        c.create_line(_rec_list[1][0], _rec_list[0][1]+k, _rec_list[1][0]+10, _rec_list[0][1]+k,width=2)
        c.create_text(_rec_list[1][0] - 10, _rec_list[0][1]+k,text=i,justify=CENTER, font="Verdana 14")
        if i == 2 or i == 1:
            c.create_line(_rec_list[0][0] - 15, _rec_list[0][1] + k, _rec_list[0][0], _rec_list[0][1] + k, width=2)
            c.create_text(_rec_list[0][0] + 13, _rec_list[0][1] + k, text="x"+str(i), justify=CENTER, font="Verdana 14")
        i -= 1
        k+=25

def _set_MX():
    c.create_rectangle(_rec_list[0][0], _rec_list[0][1],
                       _rec_list[1][0], _rec_list[1][1],
                       fill='white', outline='black')
    i = 3
    k = 28
    while (i >= 0):
        c.create_line(_rec_list[0][0]-15, _rec_list[0][1]+k, _rec_list[0][0], _rec_list[0][1]+k,width=2)
        c.create_text(_rec_list[0][0] + 10, _rec_list[0][1]+k,text=i,justify=CENTER, font="Verdana 14")
        i -= 1
        k+=25
    c.create_text(_rec_list[0][0] + 25, _rec_list[1][1] - 10, text="s1", justify=CENTER, font="Verdana 14")
    c.create_line(_rec_list[0][0] + 25, _rec_list[1][1], _rec_list[0][0] + 25, _rec_list[1][1] + 15, width=2)
    c.create_text(_rec_list[0][0] + 55, _rec_list[1][1] - 10, text="s2", justify=CENTER, font="Verdana 14")
    c.create_line(_rec_list[0][0] + 55, _rec_list[1][1], _rec_list[0][0] + 55, _rec_list[1][1] + 15, width=2)

def _set_startPoint():
    pass


def _set_OR():
    if var == 0:  # coder
        pass
    if var == 1:  # decoder
        pass
    if var == 2:  # multiplexer
        pass


def _set_XOR():
    if var == 0:  # coder
        pass
    if var == 1:  # decoder
        _set_DC()
        i = 3
        k = 28
        while (i >= 0):
            if i==1 or i == 2:
                c.create_line(_rec_list[1][0]+10, _rec_list[0][1] + k, _rec_list[1][0] + j, _rec_list[0][1] + k, width=2)
            else:
                c.create_line(_rec_list[1][0], _rec_list[0][1] + k, _rec_list[1][0] + 10, _rec_list[0][1] + k, width=2)
                c.create_polygon(_rec_list[1][0]+10, _rec_list[0][1]+k,
                                   _rec_list[1][0]+15, _rec_list[0][1]+k-5,
                                   _rec_list[1][0] + 20, _rec_list[0][1] + k,
                                   _rec_list[1][0] + 15, _rec_list[0][1] + k + 5,
                                   fill='black', outline='black')
            i -= 1
            k += 25
        tmp = _rec_list[1][0] - _rec_list[0][0]
        _rec_list[0][0] = _rec_list[1][0] + j
        _rec_list[1][0] = _rec_list[0][0] + tmp
        _set_DC()

        i = 3
        k = 28
        while (i >= 0):
            if i != 0:
                c.create_line(_rec_list[1][0], _rec_list[0][1] + k, _rec_list[1][0] + 10, _rec_list[0][1] + k, width=2)
                c.create_polygon(_rec_list[1][0] + 10, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k - 5,
                                 _rec_list[1][0] + 20, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            else:
                c.create_line(_rec_list[1][0] + 10, _rec_list[0][1] + k, _rec_list[1][0] + j, _rec_list[0][1] + k,
                              width=2)
                _port_list[0][0] = _rec_list[1][0] + j
                _port_list[0][1] = _rec_list[0][1] + k
                _set_NOT()



            i -= 1
            k += 25

    if var == 2:  # multiplexer
        pass

def _set_AND():

    if var == 0:#coder
        pass
    if var == 1:#decoder
        _set_DC()
        i = 3
        k = 28
        while (i >= 0):
            if i==1 :
                c.create_line(_rec_list[1][0]+10, _rec_list[0][1] + k, _rec_list[1][0] + 30, _rec_list[0][1] + k, width=2)
            else:
                c.create_line(_rec_list[1][0], _rec_list[0][1] + k, _rec_list[1][0] + 10, _rec_list[0][1] + k, width=2)
                c.create_polygon(_rec_list[1][0]+10, _rec_list[0][1]+k,
                                   _rec_list[1][0]+15, _rec_list[0][1]+k-5,
                                   _rec_list[1][0] + 20, _rec_list[0][1] + k,
                                   _rec_list[1][0] + 15, _rec_list[0][1] + k + 5,
                                   fill='black', outline='black')
            i -= 1
            k += 25
        pass
    if var == 2:#multiplexer
        pass


but.bind('<Button-1>',  entry_scan)

#_set_DC()
#_set_NOT()
#_set_CD()
#_set_MX()
#_set_OR()
#_set_AND()
var = 1
_set_XOR()
root.mainloop()


