from tkinter import *
root = Tk()
root.geometry('1920x1080')
root.resizable(width=False, height=False)
_rec_list = [[60, 20], [130, 160]]                         #array of coordinates of rectangle points
_tri_list = [[120, 300], [150, 315], [120, 330]]          #array of coordinates of triangle points
_circ_list = [[0, 0], [0, 0]]                             #array of coordinates of circle points
_point_list = [[]]

_circ_list[0][0] = _tri_list[1][0]
_circ_list[0][1] = _tri_list[1][1] - 5
_circ_list[1][0] = _tri_list[1][0] + 10
_circ_list[1][1] = _tri_list[1][1] + 5

#create canvas and menu
c = Canvas(root, width=1680, height=1080, bg='silver')
c.pack(side='left')
var=IntVar()
ent = Entry(width=30)
but = Button(text="нарисовать")
rbutton1=Radiobutton(root,text='Шифраторы',variable=var,value=1)
rbutton2=Radiobutton(root,text='Дешифраторы',variable=var,value=2)
rbutton3=Radiobutton(root,text='Мультиплексоры',variable=var,value=3)
rbutton1.place(x = 1700,y = 910)
rbutton2.place(x = 1700,y = 930)
rbutton3.place(x = 1700,y = 950)
ent.place(x = 1700,y = 975)
but.place(x = 1700,y = 1000)

def _set_DC():
    c.create_rectangle(_rec_list[0][0], _rec_list[0][1],
                       _rec_list[1][0], _rec_list[1][1],
                       fill='white', outline='black')
    i = 0
    k = 28
    while (i < 4):
        c.create_line(_rec_list[0][0] - 15, _rec_list[0][1]+k, _rec_list[0][0], _rec_list[0][1]+k,width=2)
        c.create_text(_rec_list[0][0] + 10, _rec_list[0][1]+k,text=i,justify=CENTER, font="Verdana 14")
        i += 1
        k+=25

def _set_NOT():
    c.create_oval(_circ_list[0][0], _circ_list[0][1], _circ_list[1][0], _circ_list[1][1],
                  width=1, fill='white', outline='black')

    c.create_polygon(_tri_list[0][0], _tri_list[0][1],
                     _tri_list[1][0], _tri_list[1][1],
                     _tri_list[2][0], _tri_list[2][1],
                     fill='white', outline='black')

def _set_CD():
    c.create_rectangle(_rec_list[0][0], _rec_list[0][1], _rec_list[1][0], _rec_list[1][1],
                       fill='white', outline='black')
    i = 0
    k = 28
    while (i < 4):
        c.create_line(_rec_list[1][0], _rec_list[0][1]+k, _rec_list[1][0]+10, _rec_list[0][1]+k,width=2)
        c.create_text(_rec_list[1][0] - 10, _rec_list[0][1]+k,text=i,justify=CENTER, font="Verdana 14")
        i += 1
        k+=25

def _set_MX():
    c.create_rectangle(_rec_list[0][0], _rec_list[0][1],
                       _rec_list[1][0], _rec_list[1][1],
                       fill='white', outline='black')
    i = 0
    k = 28
    while (i < 4):
        c.create_line(_rec_list[0][0]-15, _rec_list[0][1]+k, _rec_list[0][0], _rec_list[0][1]+k,width=2)
        c.create_text(_rec_list[0][0] + 10, _rec_list[0][1]+k,text=i,justify=CENTER, font="Verdana 14")
        i += 1
        k+=25
    c.create_text(_rec_list[0][0] + 25, _rec_list[1][1] - 10, text="s1", justify=CENTER, font="Verdana 14")
    c.create_line(_rec_list[0][0] + 25, _rec_list[1][1], _rec_list[0][0] + 25, _rec_list[1][1] + 15, width=2)
    c.create_text(_rec_list[0][0] + 55, _rec_list[1][1] - 10, text="s2", justify=CENTER, font="Verdana 14")
    c.create_line(_rec_list[0][0] + 55, _rec_list[1][1], _rec_list[0][0] + 55, _rec_list[1][1] + 15, width=2)

def _set_startPoint():
    pass


    #_set_menu()
    # _set_DC()
    # _set_NOT()
    # _set_CD()
    # _set_MX()


root.mainloop()


