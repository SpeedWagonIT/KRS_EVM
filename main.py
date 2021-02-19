from tkinter import *
root = Tk()
root.geometry('1920x1080')
root.title("Курсовая работа")
root.resizable(width=False, height=False)

_rec_list = list([[100, 60], [170, 200]])         #array of coordinates of rectangle points
_tri_list = list([[0, 0], [0, 0], [0, 0]])        #array of coordinates of triangle points
_circ_list = list([[0, 0], [0, 0]])               #array of coordinates of circle points
_point_list = list([[0,0],[0,0]])

_start_X = list([[50, 160],[60,160]])
_start_Y = list([[50, 330],[60, 330]])
_start_Z = list([[50, 500],[60,500]])
_start_K = list([[50, 670],[60,670]])
_start_L = list([[50, 840],[60,840]])

_list_in = list([[0,0],[0,0]])
_list_out = list([[0,0],[0,0]])
_port_list = list([[0,0],[0,0],[0,0],[0,0]])

_circ_list[0][0] = _tri_list[1][0]
_circ_list[0][1] = _tri_list[1][1] - 5
_circ_list[1][0] = _tri_list[1][0] + 10
_circ_list[1][1] = _tri_list[1][1] + 5

_weight = _rec_list[0][0] - _rec_list[1][0]
_height = _rec_list[0][1] - _rec_list[1][1]

#create canvas and menu
c = Canvas(root, width=1680, height=1080, bg='silver')
c.pack(side='left')
var=IntVar()
ent = Entry(width=30)
but = Button(text="Нарисовать")
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
    c.delete("all")
    s = ent.get()
    upd_list()
    lst = []

    for i in range(len(s)):
        lst.append(s[i])
    c.create_line(_start_X[0][0], _start_X[0][1], _start_X[1][0], _start_X[1][1], width=2)
    c.create_text(_start_X[0][0]-5, _start_X[0][1]-15, text="X", justify=CENTER, font="Verdana 14")
    c.create_line(_start_Y[0][0], _start_Y[0][1], _start_Y[1][0], _start_Y[1][1], width=2)
    c.create_text(_start_Y[0][0]-5, _start_Y[0][1] - 15, text="Y", justify=CENTER, font="Verdana 14")
    c.create_line(_start_Z[0][0], _start_Z[0][1], _start_Z[1][0], _start_Z[1][1], width=2)
    c.create_text(_start_Z[0][0] -5, _start_Z[0][1] - 15, text="Z", justify=CENTER, font="Verdana 14")
    c.create_line(_start_K[0][0], _start_K[0][1], _start_K[1][0], _start_K[1][1], width=2)
    c.create_text(_start_K[0][0] -5, _start_K[0][1] - 15, text="K", justify=CENTER, font="Verdana 14")
    c.create_line(_start_L[0][0], _start_L[0][1], _start_L[1][0], _start_L[1][1], width=2)
    c.create_text(_start_L[0][0] -5, _start_L[0][1] - 15, text="L", justify=CENTER, font="Verdana 14")


    for i in range(len(lst)):
        if lst[i] == "!":
            if lst[i+1] == "X" or lst[i+1] == "x":
                _point_list[0][0] = _start_X[1][0]
                _point_list[0][1] = _start_X[1][1]
                _set_NOT()
                _start_X[1][0] = _point_list[1][0]
                _start_X[1][1] = _point_list[1][1]


            if lst[i+1] == "Y" or lst[i+1] == "y":
                _point_list[0][0] = _start_Y[1][0]
                _point_list[0][1] = _start_Y[1][1]
                _set_NOT()
                _start_Y[1][0] = _point_list[1][0]
                _start_Y[1][1] = _point_list[1][1]

            if lst[i+1] == "Z" or lst[i+1] == "z":
                _point_list[0][0] = _start_Z[1][0]
                _point_list[0][1] = _start_Z[1][1]
                _set_NOT()
                _start_Z[1][0] = _point_list[1][0]
                _start_Z[1][1] = _point_list[1][1]

            if lst[i+1] == "K" or lst[i+1] == "k":
                _point_list[0][0] = _start_K[1][0]
                _point_list[0][1] = _start_K[1][1]
                _set_NOT()
                _start_K[1][0] = _point_list[1][0]
                _start_K[1][1] = _point_list[1][1]

            if lst[i+1] == "L" or lst[i+1] == "l":
                _point_list[0][0] = _start_L[1][0]
                _point_list[0][1] = _start_L[1][1]
                _set_NOT()
                _start_L[1][0] = _point_list[1][0]
                _start_L[1][1] = _point_list[1][1]

    for i in range (len(lst)):
        if lst[i] == "*":
            if (lst[i-1] == "X" or lst[i-1]== "x") and (lst[i+1] == "Y" or lst[i+1] == "y" or lst[i+2] == "Y" or lst[i+2] == "y"):
                if _list_out[0][0] >_start_X[1][1] :
                    c.create_line(_start_X[1][0], _start_X[1][1], _list_out[0][0]+30,  _start_X[1][1], width=2)
                    _start_X[1][0] = _list_out[0][0]+30
                    _koeff = _start_X[1][0] - _start_X[0][0]
                else:
                    _koeff = 150
                if _start_X[1][0] < _start_Y[1][0]:
                    _rec_list[0][0] = _start_X[1][0] + _koeff/1.3
                else:
                    _rec_list[0][0] = _start_Y[1][0] + _koeff/1.3

                if _start_K[1][0]>_start_Y[1][0]:
                    _start_Y[1][0] = _start_K[1][0]
                    _start_Y[1][1] = _start_K[1][1]

                if _start_L[1][0] > _start_Y[1][0]:
                    _start_Y[1][0] = _start_L[1][0]
                    _start_Y[1][1] = _start_L[1][1]
                _rec_list[0][1] = _start_X[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_AND()
                if(_start_X[1][0] < _start_Y[1][0]):
                    c.create_line(_start_Y[1][0], _start_Y[1][1], _start_Y[1][0], _start_Y[1][1]-90, width=2)
                    c.create_line(_start_Y[1][0], _start_Y[1][1]-90, _list_in[1][0], _start_Y[1][1]-90, width=2)
                    c.create_line(_list_in[1][0], _start_Y[1][1]-90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_Y[1][0], _start_Y[1][1], _start_Y[1][0], _list_in[1][1], width=2)
                    c.create_line(_start_Y[1][0], _list_in[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_X[1][0], _start_X[0][1], _start_X[1][0], _list_in[0][1], width=2)
                c.create_line(_start_X[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_X[1][0] = _list_out[0][0]
                _start_X[1][1] = _list_out[0][1]
                _start_Y[1][0] = _list_out[0][0]
                _start_Y[1][1] = _list_out[0][1]
                

            if (lst[i-1] == "Y" or lst[i-1] == "y") and (lst[i+1] == "Z" or lst[i+1] == "z" or lst[i+2] == "Z" or lst[i+2] == "z"):
                if _list_out[0][0] > _start_Y[1][1]:
                    c.create_line(_start_Y[1][0], _start_Y[1][1], _list_out[0][0] + 30, _start_Y[1][1], width=2)
                    _start_Y[1][0] = _list_out[0][0] + 30
                    _koeff = _start_Y[1][0] - _start_Y[0][0]
                else:
                    _koeff = 150

                print(_koeff)
                _rec_list[0][0] = _start_Y[1][0] + _koeff / 1.2
                if _start_L[1][0] > _start_Z[1][0]:
                    _start_Z[1][0] = _start_L[1][0]
                    _start_Z[1][1] = _start_L[1][1]

                _rec_list[0][1] = _start_Y[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_AND()
                if (_start_Y[1][0] < _start_Z[1][0]):
                    c.create_line(_start_Z[1][0], _start_Z[1][1], _start_Z[1][0], _start_Z[1][1] - 90, width=2)
                    c.create_line(_start_Z[1][0], _start_Z[1][1] - 90, _list_in[1][0], _start_Z[1][1] - 90, width=2)
                    c.create_line(_list_in[1][0], _start_Z[1][1] - 90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_Z[1][0], _start_Z[1][1], _list_in[1][0], _start_Z[1][1], width=2)
                    c.create_line(_list_in[1][0], _start_Z[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_Y[1][0], _start_Y[1][1], _start_Y[1][0], _list_in[0][1], width=2)
                c.create_line(_start_Y[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_Y[1][0] = _list_out[0][0]
                _start_Y[1][1] = _list_out[0][1]
                _start_Z[1][0] = _list_out[0][0]
                _start_Z[1][1] = _list_out[0][1]


            if (lst[i-1] == "Z" or lst[i-1] == "z") and (lst[i+1] == "K" or lst[i+1] == "k" or lst[i+2] == "K" or lst[i+2] == "k"):
                if _list_out[0][0] > _start_Z[1][1]:
                    c.create_line(_start_Z[1][0], _start_Z[1][1], _list_out[0][0] + 30, _start_Z[1][1], width=2)
                    _start_Z[1][0] = _list_out[0][0] + 30
                    _koeff = _start_Z[1][0] - _start_Z[0][0]
                else:
                    _koeff = 150

                print(_koeff)
                _rec_list[0][0] = _start_Z[1][0] + _koeff / 2.3
                if _start_L[1][0] > _start_K[1][0]:
                    _start_K[1][0] = _start_L[1][0]
                    _start_K[1][1] = _start_L[1][1]

                _rec_list[0][1] = _start_Z[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_AND()
                if (_start_Z[1][0] < _start_K[1][0]):
                    c.create_line(_start_K[1][0], _start_K[1][1], _start_K[1][0], _start_K[1][1] - 90, width=2)
                    c.create_line(_start_K[1][0], _start_K[1][1] - 90, _list_in[1][0], _start_K[1][1] - 90, width=2)
                    c.create_line(_list_in[1][0], _start_K[1][1] - 90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_K[1][0], _start_K[1][1], _list_in[1][0], _start_K[1][1], width=2)
                    c.create_line(_list_in[1][0], _start_K[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_Z[1][0], _start_Z[1][1], _start_Z[1][0], _list_in[0][1], width=2)
                c.create_line(_start_Z[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_Z[1][0] = _list_out[0][0]
                _start_Z[1][1] = _list_out[0][1]
                _start_K[1][0] = _list_out[0][0]
                _start_K[1][1] = _list_out[0][1]

            if (lst[i-1] == "K" or lst[i-1] == "k") and (lst[i+1] == "L" or lst[i+1] == "l" or lst[i+2] == "L" or lst[i+2] == "l"):
                if _list_out[0][0] > _start_K[1][1]:
                    c.create_line(_start_K[1][0], _start_K[1][1], _list_out[0][0] + 30, _start_K[1][1], width=2)
                    _start_K[1][0] = _list_out[0][0] + 30
                    _koeff = _start_K[1][0] - _start_K[0][0]
                else:
                    _koeff = 150

                print(_koeff)
                _rec_list[0][0] = _start_K[1][0] + _koeff / 2.7

                _rec_list[0][1] = _start_K[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_AND()
                if (_start_K[1][0] < _start_K[1][0]):
                    c.create_line(_start_L[1][0], _start_L[1][1], _start_L[1][0], _start_L[1][1] - 90, width=2)
                    c.create_line(_start_L[1][0], _start_L[1][1] - 90, _list_in[1][0], _start_L[1][1] - 90, width=2)
                    c.create_line(_list_in[1][0], _start_L[1][1] - 90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_L[1][0], _start_L[1][1], _list_in[1][0], _start_L[1][1], width=2)
                    c.create_line(_list_in[1][0], _start_L[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_K[1][0], _start_K[1][1], _start_K[1][0], _list_in[0][1], width=2)
                c.create_line(_start_K[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_K[1][0] = _list_out[0][0]
                _start_K[1][1] = _list_out[0][1]
                _start_L[1][0] = _list_out[0][0]
                _start_L[1][1] = _list_out[0][1]

    for i in range (len(lst)):
        if lst[i] == "+":
            if (lst[i-1] == "X" or lst[i-1]== "x") and (lst[i+1] == "Y" or lst[i+1] == "y" or lst[i+2] == "Y" or lst[i+2] == "y"):
                if _list_out[0][0] >_start_X[1][1] :
                    c.create_line(_start_X[1][0], _start_X[1][1], _list_out[0][0]+30,  _start_X[1][1], width=2)
                    _start_X[1][0] = _list_out[0][0]+30
                    _koeff = _start_X[1][0] - _start_X[0][0]
                else:
                    _koeff = 150
                if _start_X[1][0] < _start_Y[1][0]:
                    _rec_list[0][0] = _start_X[1][0] + _koeff/1.5
                else:
                    _rec_list[0][0] = _start_Y[1][0] + _koeff/1.3

                if _start_K[1][0]>_start_Y[1][0]:
                    _start_Y[1][0] = _start_K[1][0]
                    _start_Y[1][1] = _start_K[1][1]

                if _start_L[1][0] > _start_Y[1][0]:
                    _start_Y[1][0] = _start_L[1][0]
                    _start_Y[1][1] = _start_L[1][1]
                _rec_list[0][1] = _start_X[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_XOR()
                if(_start_X[1][0] < _start_Y[1][0]):
                    c.create_line(_start_Y[1][0], _start_Y[1][1], _start_Y[1][0], _start_Y[1][1]-90, width=2)
                    c.create_line(_start_Y[1][0], _start_Y[1][1]-90, _list_in[1][0], _start_Y[1][1]-90, width=2)
                    c.create_line(_list_in[1][0], _start_Y[1][1]-90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_Y[1][0], _start_Y[1][1], _start_Y[1][0], _list_in[1][1], width=2)
                    c.create_line(_start_Y[1][0], _list_in[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_X[1][0], _start_X[0][1], _start_X[1][0], _list_in[0][1], width=2)
                c.create_line(_start_X[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_X[1][0] = _list_out[0][0]
                _start_X[1][1] = _list_out[0][1]
                _start_Y[1][0] = _list_out[0][0]
                _start_Y[1][1] = _list_out[0][1]

            if (lst[i-1] == "Y" or lst[i-1]== "y") and (lst[i+1] == "Z" or lst[i+1] == "z" or lst[i+2] == "Z" or lst[i+2] == "z"):
                if _list_out[0][0] > _start_Y[1][1]:
                    c.create_line(_start_Y[1][0], _start_Y[1][1], _list_out[0][0] + 30, _start_Y[1][1], width=2)
                    _start_Y[1][0] = _list_out[0][0] + 30
                    _koeff = _start_Y[1][0] - _start_Y[0][0]
                else:
                    _koeff = 250

                _rec_list[0][0] = _start_Y[1][0] + _koeff / 1.8
                if _start_L[1][0] > _start_Z[1][0]:
                    _start_Z[1][0] = _start_L[1][0]
                    _start_Z[1][1] = _start_L[1][1]

                _rec_list[0][1] = _start_Y[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_XOR()
                if (_start_Z[1][0] < _start_K[1][0]):
                    c.create_line(_start_Z[1][0], _start_Z[1][1], _start_Z[1][0], _start_Z[1][1] - 90, width=2)
                    c.create_line(_start_Z[1][0], _start_Z[1][1] - 90, _list_in[1][0], _start_Z[1][1] - 90, width=2)
                    c.create_line(_list_in[1][0], _start_Z[1][1] - 90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_Z[1][0], _start_Z[1][1], _list_in[1][0], _start_Z[1][1], width=2)
                    c.create_line(_list_in[1][0], _start_Z[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_Y[1][0], _start_Y[1][1], _start_Y[1][0], _list_in[0][1], width=2)
                c.create_line(_start_Y[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_Y[1][0] = _list_out[0][0]
                _start_Y[1][1] = _list_out[0][1]
                _start_Z[1][0] = _list_out[0][0]
                _start_Z[1][1] = _list_out[0][1]

            if (lst[i-1] == "Z" or lst[i-1]== "z") and (lst[i+1] == "K" or lst[i+1] == "k" or lst[i+2] == "K" or lst[i+2] == "k"):
                if _list_out[0][0] > _start_Z[1][1]:
                    c.create_line(_start_Z[1][0], _start_Z[1][1], _list_out[0][0] + 30, _start_Z[1][1], width=2)
                    _start_Z[1][0] = _list_out[0][0] + 30
                    _koeff = _start_Z[1][0] - _start_Z[0][0]
                else:
                    _koeff = 250

                _rec_list[0][0] = _start_Z[1][0] + _koeff / 2.3
                if _start_L[1][0] > _start_K[1][0]:
                    _start_K[1][0] = _start_L[1][0]
                    _start_K[1][1] = _start_L[1][1]

                _rec_list[0][1] = _start_Z[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_XOR()
                if (_start_Y[1][0] < _start_Z[1][0]):
                    c.create_line(_start_K[1][0], _start_K[1][1], _start_K[1][0], _start_K[1][1] - 90, width=2)
                    c.create_line(_start_K[1][0], _start_K[1][1] - 90, _list_in[1][0], _start_K[1][1] - 90, width=2)
                    c.create_line(_list_in[1][0], _start_K[1][1] - 90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_K[1][0], _start_K[1][1], _list_in[1][0], _start_K[1][1], width=2)
                    c.create_line(_list_in[1][0], _start_K[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_Z[1][0], _start_Z[1][1], _start_Z[1][0], _list_in[0][1], width=2)
                c.create_line(_start_Z[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_Z[1][0] = _list_out[0][0]
                _start_Z[1][1] = _list_out[0][1]
                _start_K[1][0] = _list_out[0][0]
                _start_K[1][1] = _list_out[0][1]

            if (lst[i - 1] == "K" or lst[i - 1] == "k") and (lst[i+1] == "L" or lst[i+1] == "l" or lst[i+2] == "L" or lst[i+2] == "l"):
                if _list_out[0][0] > _start_K[1][1]:
                    c.create_line(_start_K[1][0], _start_K[1][1], _list_out[0][0] + 30, _start_K[1][1], width=2)
                    _start_K[1][0] = _list_out[0][0] + 30
                    _koeff = _start_K[1][0] - _start_K[0][0]
                else:
                    _koeff = 250

                _rec_list[0][0] = _start_K[1][0] + _koeff / 2.7

                _rec_list[0][1] = _start_K[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_XOR()
                if (_start_K[1][0] < _start_L[1][0]):
                    c.create_line(_start_L[1][0], _start_L[1][1], _start_L[1][0], _start_L[1][1] - 90, width=2)
                    c.create_line(_start_L[1][0], _start_L[1][1] - 90, _list_in[1][0], _start_L[1][1] - 90, width=2)
                    c.create_line(_list_in[1][0], _start_L[1][1] - 90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_L[1][0], _start_L[1][1], _list_in[1][0], _start_L[1][1], width=2)
                    c.create_line(_list_in[1][0], _start_L[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_K[1][0], _start_K[1][1], _start_K[1][0], _list_in[0][1], width=2)
                c.create_line(_start_K[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_K[1][0] = _list_out[0][0]
                _start_K[1][1] = _list_out[0][1]
                _start_L[1][0] = _list_out[0][0]
                _start_L[1][1] = _list_out[0][1]

    for i in range (len(lst)):
        if lst[i] == "^":
            if (lst[i-1] == "X" or lst[i-1]== "x") and (lst[i+1] == "Y" or lst[i+1] == "y" or lst[i+2] == "Y" or lst[i+2] == "y"):
                if _list_out[0][0] >_start_X[1][1] :
                    c.create_line(_start_X[1][0], _start_X[1][1], _list_out[0][0]+30,  _start_X[1][1], width=2)
                    _start_X[1][0] = _list_out[0][0]+30
                    _koeff = _start_X[1][0] - _start_X[0][0]
                else:
                    _koeff = 150
                if _start_X[1][0] < _start_Y[1][0]:
                    _rec_list[0][0] = _start_X[1][0] + _koeff/1.5
                else:
                    _rec_list[0][0] = _start_Y[1][0] + _koeff/1.3

                if _start_K[1][0]>_start_Y[1][0]:
                    _start_Y[1][0] = _start_K[1][0]
                    _start_Y[1][1] = _start_K[1][1]

                if _start_L[1][0] > _start_Y[1][0]:
                    _start_Y[1][0] = _start_L[1][0]
                    _start_Y[1][1] = _start_L[1][1]
                _rec_list[0][1] = _start_X[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_OR()
                if(_start_X[1][0] < _start_Y[1][0]):
                    c.create_line(_start_Y[1][0], _start_Y[1][1], _start_Y[1][0], _start_Y[1][1]-90, width=2)
                    c.create_line(_start_Y[1][0], _start_Y[1][1]-90, _list_in[1][0], _start_Y[1][1]-90, width=2)
                    c.create_line(_list_in[1][0], _start_Y[1][1]-90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_Y[1][0], _start_Y[1][1], _start_Y[1][0], _list_in[1][1], width=2)
                    c.create_line(_start_Y[1][0], _list_in[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_X[1][0], _start_X[0][1], _start_X[1][0], _list_in[0][1], width=2)
                c.create_line(_start_X[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_X[1][0] = _list_out[0][0]
                _start_X[1][1] = _list_out[0][1]
                _start_Y[1][0] = _list_out[0][0]
                _start_Y[1][1] = _list_out[0][1]

            if (lst[i-1] == "Y" or lst[i-1]== "y") and (lst[i+1] == "Z" or lst[i+1] == "z" or lst[i+2] == "Z" or lst[i+2] == "z"):
                if _list_out[0][0] > _start_Y[1][1]:
                    c.create_line(_start_Y[1][0], _start_Y[1][1], _list_out[0][0] + 30, _start_Y[1][1], width=2)
                    _start_Y[1][0] = _list_out[0][0] + 30
                    _koeff = _start_Y[1][0] - _start_Y[0][0]
                else:
                    _koeff = 250

                _rec_list[0][0] = _start_Y[1][0] + _koeff / 1.8
                if _start_L[1][0] > _start_Z[1][0]:
                    _start_Z[1][0] = _start_L[1][0]
                    _start_Z[1][1] = _start_L[1][1]

                _rec_list[0][1] = _start_Y[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_OR()
                if (_start_Z[1][0] < _start_K[1][0]):
                    c.create_line(_start_Z[1][0], _start_Z[1][1], _start_Z[1][0], _start_Z[1][1] - 90, width=2)
                    c.create_line(_start_Z[1][0], _start_Z[1][1] - 90, _list_in[1][0], _start_Z[1][1] - 90, width=2)
                    c.create_line(_list_in[1][0], _start_Z[1][1] - 90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_Z[1][0], _start_Z[1][1], _list_in[1][0], _start_Z[1][1], width=2)
                    c.create_line(_list_in[1][0], _start_Z[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_Y[1][0], _start_Y[1][1], _start_Y[1][0], _list_in[0][1], width=2)
                c.create_line(_start_Y[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_Y[1][0] = _list_out[0][0]
                _start_Y[1][1] = _list_out[0][1]
                _start_Z[1][0] = _list_out[0][0]
                _start_Z[1][1] = _list_out[0][1]

            if (lst[i-1] == "Z" or lst[i-1]== "z") and (lst[i+1] == "K" or lst[i+1] == "k" or lst[i+2] == "K" or lst[i+2] == "k"):
                if _list_out[0][0] > _start_Z[1][1]:
                    c.create_line(_start_Z[1][0], _start_Z[1][1], _list_out[0][0] + 30, _start_Z[1][1], width=2)
                    _start_Z[1][0] = _list_out[0][0] + 30
                    _koeff = _start_Z[1][0] - _start_Z[0][0]
                else:
                    _koeff = 250

                _rec_list[0][0] = _start_Z[1][0] + _koeff / 2.3
                if _start_L[1][0] > _start_K[1][0]:
                    _start_K[1][0] = _start_L[1][0]
                    _start_K[1][1] = _start_L[1][1]

                _rec_list[0][1] = _start_Z[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_OR()
                if (_start_Y[1][0] < _start_Z[1][0]):
                    c.create_line(_start_K[1][0], _start_K[1][1], _start_K[1][0], _start_K[1][1] - 90, width=2)
                    c.create_line(_start_K[1][0], _start_K[1][1] - 90, _list_in[1][0], _start_K[1][1] - 90, width=2)
                    c.create_line(_list_in[1][0], _start_K[1][1] - 90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_K[1][0], _start_K[1][1], _list_in[1][0], _start_K[1][1], width=2)
                    c.create_line(_list_in[1][0], _start_K[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_Z[1][0], _start_Z[1][1], _start_Z[1][0], _list_in[0][1], width=2)
                c.create_line(_start_Z[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_Z[1][0] = _list_out[0][0]
                _start_Z[1][1] = _list_out[0][1]
                _start_K[1][0] = _list_out[0][0]
                _start_K[1][1] = _list_out[0][1]

            if (lst[i - 1] == "K" or lst[i - 1] == "k") and (lst[i+1] == "L" or lst[i+1] == "l" or lst[i+2] == "L" or lst[i+2] == "l"):
                if _list_out[0][0] > _start_K[1][1]:
                    c.create_line(_start_K[1][0], _start_K[1][1], _list_out[0][0] + 30, _start_K[1][1], width=2)
                    _start_K[1][0] = _list_out[0][0] + 30
                    _koeff = _start_K[1][0] - _start_K[0][0]
                else:
                    _koeff = 250

                _rec_list[0][0] = _start_K[1][0] + _koeff / 2.7

                _rec_list[0][1] = _start_K[1][1] - 10
                _rec_list[1][0] = _rec_list[0][0] - _weight
                _rec_list[1][1] = _rec_list[0][1] - _height
                _set_OR()
                if (_start_K[1][0] < _start_L[1][0]):
                    c.create_line(_start_L[1][0], _start_L[1][1], _start_L[1][0], _start_L[1][1] - 90, width=2)
                    c.create_line(_start_L[1][0], _start_L[1][1] - 90, _list_in[1][0], _start_L[1][1] - 90, width=2)
                    c.create_line(_list_in[1][0], _start_L[1][1] - 90, _list_in[1][0], _list_in[1][1], width=2)
                else:
                    c.create_line(_start_L[1][0], _start_L[1][1], _list_in[1][0], _start_L[1][1], width=2)
                    c.create_line(_list_in[1][0], _start_L[1][1], _list_in[1][0], _list_in[1][1], width=2)
                c.create_line(_start_K[1][0], _start_K[1][1], _start_K[1][0], _list_in[0][1], width=2)
                c.create_line(_start_K[1][0], _list_in[0][1], _list_in[0][0], _list_in[0][1], width=2)
                _start_K[1][0] = _list_out[0][0]
                _start_K[1][1] = _list_out[0][1]
                _start_L[1][0] = _list_out[0][0]
                _start_L[1][1] = _list_out[0][1]


def upd_list():
    global i
    global k
    global j
    global _rec_list
    global _tri_list
    global _circ_list
    global _point_list
    global _port_list
    global _start_X
    global _start_Y
    global _start_Z
    global _start_K
    global _start_L
    global _list_in
    global _list_out
    _rec_list = list([[100, 60], [170, 200]])  # array of coordinates of rectangle points
    _tri_list = list([[0, 0], [0, 0], [0, 0]])  # array of coordinates of triangle points
    _circ_list = list([[0, 0], [0, 0]])  # array of coordinates of circle points
    _point_list = list([[0, 0], [0, 0]])
    _port_list = list([[0, 0], [0, 0], [0, 0], [0, 0]])
    _list_in = list([[0, 0], [0, 0]])
    _list_out = list([[0, 0], [0, 0]])
    _start_X = list([[50, 160], [60, 160]])
    _start_Y = list([[50, 330], [60, 330]])
    _start_Z = list([[50, 500], [60, 500]])
    _start_K = list([[50, 670], [60, 670]])
    _start_L = list([[50, 840], [60, 840]])
    i = 3
    k = 28
    j = 40

    _circ_list[0][0] = _tri_list[1][0]
    _circ_list[0][1] = _tri_list[1][1] - 5
    _circ_list[1][0] = _tri_list[1][0] + 10
    _circ_list[1][1] = _tri_list[1][1] + 5



def _set_CD():
    c.create_rectangle(_rec_list[0][0], _rec_list[0][1],
                       _rec_list[1][0], _rec_list[1][1],
                       fill='white', outline='black')
    i = 3
    k = 28
    while (i >= 0):
        c.create_line(_rec_list[0][0] - 15, _rec_list[0][1]+k, _rec_list[0][0], _rec_list[0][1]+k,width=2)
        c.create_text(_rec_list[0][0] + 10, _rec_list[0][1]+k, text=i, justify=CENTER, font="Verdana 14")
        if i == 2 or i == 1:
            c.create_line(_rec_list[1][0], _rec_list[0][1] + k, _rec_list[1][0]+15, _rec_list[0][1] + k, width=2)
            c.create_text(_rec_list[1][0] - 10, _rec_list[0][1] + k, text=i, justify=CENTER, font="Verdana 14")
        _port_list[i][0] = _rec_list[0][0] - 15
        _port_list[i][1] = _rec_list[0][1] + k
        i -= 1
        k+=25

def _set_NOT():
    c.create_line(_point_list[0][0], _point_list[0][1], _point_list[0][0] + 20, _point_list[0][1], width=2)
    _point_list[0][0] += 20

    _tri_list[0][0] = _point_list[0][0]
    _tri_list[0][1] = _point_list[0][1] + 10
    _tri_list[1][0] = _point_list[0][0] + 15
    _tri_list[1][1] = _point_list[0][1]
    _tri_list[2][0] = _point_list[0][0]
    _tri_list[2][1] = _point_list[0][1] - 10

    _circ_list[0][0] = _tri_list[1][0]
    _circ_list[0][1] = _tri_list[1][1]+5
    _circ_list[1][0] = _tri_list[1][0]+10
    _circ_list[1][1] = _tri_list[1][1]-5

    _point_list[0][0] = _tri_list[1][0]+10
    _point_list[0][1] = _tri_list[1][1]
    _point_list[1][0] = _point_list[0][0]+15
    _point_list[1][1] = _point_list[0][1]

    c.create_polygon(_tri_list[0][0], _tri_list[0][1],
                     _tri_list[1][0], _tri_list[1][1],
                     _tri_list[2][0], _tri_list[2][1],
                     fill='white', outline='black')

    c.create_oval(_circ_list[0][0], _circ_list[0][1], _circ_list[1][0], _circ_list[1][1],
                  width=1, fill='white', outline='black')

    _point_list[0][0] = _tri_list[1][0]+10
    _point_list[0][1] = _tri_list[1][1]
    _point_list[1][0] = _point_list[0][0]+15
    _point_list[1][1] = _point_list[0][1]

    c.create_line(_point_list[0][0], _point_list[1][1], _point_list[1][0], _point_list[1][1], width=2)


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
            c.create_text(_rec_list[0][0] + 13, _rec_list[0][1] + k, text=i, justify=CENTER, font="Verdana 14")
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
        if i == 2:
            c.create_line(_rec_list[1][0], _rec_list[0][1] + k, _rec_list[1][0]+10, _rec_list[0][1] + k, width=2)
            _list_out[0][0] = _rec_list[1][0]+10
            _list_out[0][1] = _rec_list[0][1] + k
            c.create_text(_rec_list[1][0] - 10, _rec_list[0][1] + k, text="Y", justify=CENTER, font="Verdana 14")
        _port_list[i][0] = _rec_list[0][0]-15
        _port_list[i][1] =  _rec_list[0][1]+k
        i -= 1
        k+=25

    _point_list[0][0] = _rec_list[0][0] + 25
    _point_list[0][1] = _rec_list[1][1] + 15
    _point_list[1][0] = _rec_list[0][0] + 55
    _point_list[1][1] = _rec_list[1][1] + 15

    c.create_text(_rec_list[0][0] + 25, _rec_list[1][1] - 10, text="a0", justify=CENTER, font="Verdana 14")
    c.create_line(_rec_list[0][0] + 25, _rec_list[1][1], _rec_list[0][0] + 25, _rec_list[1][1] + 15, width=2)
    c.create_text(_rec_list[0][0] + 55, _rec_list[1][1] - 10, text="a1", justify=CENTER, font="Verdana 14")
    c.create_line(_rec_list[0][0] + 55, _rec_list[1][1], _rec_list[0][0] + 55, _rec_list[1][1] + 15, width=2)

    c.create_line(_point_list[0][0], _point_list[0][1], _point_list[0][0] - 50, _point_list[0][1], width=2)
    _point_list[0][0] -= 50
    c.create_line(_point_list[0][0], _point_list[0][1], _point_list[0][0], _port_list[2][1], width=2)
    _point_list[0][1] = _port_list[2][1]
    c.create_line(_point_list[0][0], _point_list[0][1], _point_list[0][0] - 20, _point_list[0][1], width=2)
    _list_in[0][0] = _point_list[0][0] - 20
    _list_in[0][1] = _point_list[0][1]
    c.create_line(_point_list[1][0], _point_list[1][1], _point_list[1][0], _point_list[1][1] + 5, width=2)
    _point_list[1][1] += 5
    c.create_line(_point_list[1][0], _point_list[1][1], _point_list[1][0] - 90, _point_list[1][1], width=2)
    _point_list[1][0] -= 90
    c.create_line(_point_list[1][0], _point_list[1][1], _point_list[1][0], _port_list[1][1], width=2)
    _point_list[1][1] = _port_list[1][1]
    c.create_line(_point_list[1][0], _point_list[1][1], _point_list[1][0] - 10, _port_list[1][1], width=2)
    _list_in[1][0] = _point_list[1][0] - 10
    _list_in[1][1] = _port_list[1][1]
def _set_OR():
    if var.get() == 0:  # coder
        _set_CD()
        i = 3
        k = 28
        while (i >= 0):
            if i == 0 or i == 1:
                _point_list[0][0] = _rec_list[0][0] - 60
                _point_list[0][1] = _rec_list[0][1] + k
                if i ==1 :
                    _list_in[0][0] = _rec_list[0][0]
                    _list_in[0][1] = _rec_list[0][1]+k
                if i == 0:
                    _list_in[1][0] = _rec_list[0][0] - 15
                    _list_in[1][1] = _rec_list[0][1]+k
            if i == 3:
                c.create_polygon(_rec_list[0][0] - 10, _rec_list[0][1] + k,
                                 _rec_list[0][0] - 15, _rec_list[0][1] + k - 5,
                                 _rec_list[0][0] - 20, _rec_list[0][1] + k,
                                 _rec_list[0][0] - 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            if i == 2:
                c.create_text(_port_list[2][0] + 5, _port_list[2][1] - 10, text=1, justify=CENTER, font="Verdana 8")
                c.create_polygon(_rec_list[1][0] + 10, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k - 5,
                                 _rec_list[1][0] + 20, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            if i == 1:
                _point_list[0][0] = _rec_list[1][0]
                _point_list[0][1] = _port_list[1][1]
                _set_NOT()
                _list_out[0][0] =  _point_list[1][0]
                _list_out[0][1] =  _point_list[1][1]

            i -= 1
            k += 25

    if var.get() == 1:  # decoder
        _set_DC()
        i = 3
        k = 28
        while (i >= 0):
            if i == 1:
                _list_in[1][0] = _rec_list[1][0] + _weight - 15
                _list_in[1][1] = _rec_list[0][1] + k
            if i == 2:
                _list_in[0][0] = _rec_list[1][0] + _weight - 15
                _list_in[0][1] = _rec_list[0][1] + k
            if i != 0:
                c.create_line(_rec_list[1][0], _rec_list[0][1] + k, _rec_list[1][0] + 10, _rec_list[0][1] + k, width=2)
                c.create_polygon(_rec_list[1][0] + 10, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k - 5,
                                 _rec_list[1][0] + 20, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            else:
                _point_list[0][0] = _rec_list[1][0]
                _point_list[0][1] = _rec_list[0][1] + k
                _set_NOT()
                _list_out[0][0] =  _point_list[1][0]
                _list_out[0][1] =  _point_list[1][1]

            i -= 1
            k += 25


    if var.get() == 2:  # multiplexer
        _set_MX()
        c.create_text(_port_list[0][0] + 5, _port_list[0][1] - 10, text=0, justify=CENTER, font="Verdana 8")
        c.create_text(_port_list[1][0] + 5, _port_list[1][1] - 10, text=1, justify=CENTER, font="Verdana 8")
        c.create_text(_port_list[2][0] + 5, _port_list[2][1] - 10, text=1, justify=CENTER, font="Verdana 8")
        c.create_text(_port_list[3][0] + 5, _port_list[3][1] - 10, text=1, justify=CENTER, font="Verdana 8")

def _set_XOR():
    if var.get() == 0:  # coder
        _rec_list[0][0] +=30
        _rec_list[1][0] +=30
        _set_CD()
        i = 3
        k = 28
        while (i >= 0):
            if i == 0 or i == 1:
                _point_list[0][0] = _rec_list[0][0] - 60
                _point_list[0][1] = _rec_list[0][1] + k
                _set_NOT()
            if i == 3:
                c.create_polygon(_rec_list[0][0] - 10, _rec_list[0][1] + k,
                                 _rec_list[0][0] - 15, _rec_list[0][1] + k - 5,
                                 _rec_list[0][0] - 20, _rec_list[0][1] + k,
                                 _rec_list[0][0] - 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            if i == 2:
                c.create_text(_port_list[2][0] + 5, _port_list[2][1] - 10, text=1, justify=CENTER, font="Verdana 8")
                c.create_polygon(_rec_list[1][0] + 10, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k - 5,
                                 _rec_list[1][0] + 20, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            if i == 1:
                _point_list[0][0] = _rec_list[0][0] - 70
                _point_list[0][1] = _rec_list[0][1] + k
                c.create_line(_point_list[0][0], _point_list[0][1], _point_list[0][0] + 10, _point_list[0][1], width=2)
                c.create_line(_point_list[0][0], _point_list[0][1], _point_list[0][0], _point_list[0][1] + k, width=2)

            if i == 0:
                _point_list[0][0] = _rec_list[0][0] - 60
                _point_list[0][1] = _rec_list[0][1] + k
                c.create_line(_point_list[0][0], _point_list[0][1], _point_list[0][0], _point_list[0][1] + k - 40, width=2)

            i -= 1
            k += 25

        tmp = _rec_list[1][1] - _rec_list[0][1]
        _rec_list[0][1] = _rec_list[1][1] + 10
        _rec_list[1][1] =_rec_list[0][1] + tmp
        _set_CD()
        i = 3
        k = 28
        while (i >= 0):
            if i == 0 or i == 1:
                _point_list[0][0] = _rec_list[0][0] - 60
                _point_list[0][1] = _rec_list[0][1] + k
                c.create_line(_point_list[0][0],_point_list[0][1],_rec_list[0][0],_rec_list[0][1]+k,width=2)
            if i == 3:
                c.create_polygon(_rec_list[0][0] - 10, _rec_list[0][1] + k,
                                 _rec_list[0][0] - 15, _rec_list[0][1] + k - 5,
                                 _rec_list[0][0] - 20, _rec_list[0][1] + k,
                                 _rec_list[0][0] - 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            if i == 2:
                c.create_text(_port_list[2][0] + 5, _port_list[2][1] - 10, text=1, justify=CENTER, font="Verdana 8")
                c.create_polygon(_rec_list[1][0] + 10, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k - 5,
                                 _rec_list[1][0] + 20, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            if i == 0:
                _point_list[0][0] = _rec_list[0][0] - 70
                _point_list[0][1] = _rec_list[0][1] + k
                c.create_line(_point_list[0][0], _point_list[0][1]-25, _point_list[0][0], _point_list[0][1] - k, width=2)
                c.create_line(_point_list[0][0], _point_list[0][1] - k-14, _point_list[0][0] - 10, _point_list[0][1] - k-14, width=2) #port 2
                _list_in[0][0] = _point_list[0][0] - 10
                _list_in[0][1] = _point_list[0][1] - k-14
            if i == 1:
                c.create_line(_point_list[0][0], _point_list[0][1], _point_list[0][0] - 10, _point_list[0][1], width=2)
                c.create_line(_point_list[0][0], _point_list[0][1]+25, _point_list[0][0], _point_list[0][1] - k, width=2)
                c.create_line(_point_list[0][0], _point_list[0][1] - k+14, _point_list[0][0] - 20, _point_list[0][1] - k+14, width=2) #port1
                _list_in[1][0] = _point_list[0][0] - 20
                _list_in[1][1] = _point_list[0][1] - k+14


            i -= 1
            k += 25

        _rec_list[0][0] = _rec_list[1][0] + 90
        _rec_list[1][0] = _rec_list[0][0] + 70
        tmp = _rec_list[1][1] - _rec_list[0][1]
        _rec_list[0][1] = _rec_list[1][1] - 200
        _rec_list[1][1] = _rec_list[0][1] + tmp
        _set_CD()
        i = 3
        k = 28
        while (i >= 0):
            if i == 0 or i == 1:
                _point_list[0][0] = _rec_list[0][0] - 60
                _point_list[0][1] = _rec_list[0][1] + k
                c.create_line(_point_list[0][0],_point_list[0][1],_rec_list[0][0],_rec_list[0][1]+k,width=2)
            if i == 3:
                c.create_polygon(_rec_list[0][0] - 10, _rec_list[0][1] + k,
                                 _rec_list[0][0] - 15, _rec_list[0][1] + k - 5,
                                 _rec_list[0][0] - 20, _rec_list[0][1] + k,
                                 _rec_list[0][0] - 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            if i == 2:
                c.create_text(_port_list[2][0] + 5, _port_list[2][1] - 10, text=1, justify=CENTER, font="Verdana 8")
                c.create_polygon(_rec_list[1][0] + 10, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k - 5,
                                 _rec_list[1][0] + 20, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            if i == 1:
                c.create_line(_point_list[0][0], _point_list[0][1], _point_list[0][0],_point_list[0][1] - 90, width=2)
                c.create_line(_point_list[0][0], _point_list[0][1] - 90, _point_list[0][0] - 15, _point_list[0][1] - 90, width=2)
                _list_out[0][0] = _port_list[1][0] - _weight+30
                _list_out[0][1] = _port_list[1][1]
            if i == 0:
                c.create_line(_point_list[0][0], _point_list[0][1], _point_list[0][0], _point_list[0][1] + 35, width=2)
                c.create_line(_point_list[0][0], _point_list[0][1] + 35, _point_list[0][0] - 15, _point_list[0][1] + 35, width=2)
            i -= 1
            k += 25

    if var.get() == 1:  # decoder
        _set_DC()
        i = 3
        k = 28
        j=40
        while (i >= 0):
            if i == 2:
                _list_in[0][0] = _rec_list[1][0] + _weight - 15
                _list_in[0][1] = _rec_list[0][1] + k
            if i == 1:
                c.create_line(_rec_list[1][0] + 10, _rec_list[0][1] + k, _rec_list[1][0] + 30, _rec_list[0][1] + k,
                              width=2)
                _list_in[1][0] = _rec_list[1][0] + _weight - 15
                _list_in[1][1] = _rec_list[0][1] + k
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
            if i != 3:
                c.create_line(_rec_list[1][0], _rec_list[0][1] + k, _rec_list[1][0] + 10, _rec_list[0][1] + k, width=2)
                c.create_polygon(_rec_list[1][0] + 10, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k - 5,
                                 _rec_list[1][0] + 20, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            else:
                _point_list[0][1] =_rec_list[0][1] + k
                _point_list[0][0] = _rec_list[1][0] + 10
                _set_NOT()
                _list_out[0][0] = _point_list[1][0]
                _list_out[0][1] = _point_list[1][1]

            i -= 1
            k += 25

    if var.get() == 2:  # multiplexer
        _set_MX()

        c.create_text(_port_list[0][0] + 5, _port_list[0][1] - 10, text=0, justify=CENTER, font="Verdana 8")
        c.create_text(_port_list[1][0] + 5, _port_list[1][1] - 10, text=1, justify=CENTER, font="Verdana 8")
        c.create_text(_port_list[2][0] + 5, _port_list[2][1] - 10, text=1, justify=CENTER, font="Verdana 8")
        c.create_text(_port_list[3][0] + 5, _port_list[3][1] - 10, text=0, justify=CENTER, font="Verdana 8")


def _set_AND():

    if var.get() == 0:#coder
        _set_CD()
        i = 3
        k = 28
        while (i>=0):
            if i == 0 or i == 1:
                _point_list[0][0] = _rec_list[0][0] - 60
                _point_list[0][1] = _rec_list[0][1] + k
                if i == 0:
                    _list_in[1][0] = _rec_list[0][0] - 60
                    _list_in[1][1] = _rec_list[0][1] + k
                if i == 1:
                    _list_in[0][0] = _rec_list[0][0] - 60
                    _list_in[0][1] = _rec_list[0][1] + k
                    _list_out[0][0] = _rec_list[0][0]-_weight+15
                    _list_out[0][1] = _rec_list[0][1] + k

                _set_NOT()
            if i == 3:
                c.create_polygon(_rec_list[0][0] - 10, _rec_list[0][1] + k,
                                 _rec_list[0][0] - 15, _rec_list[0][1] + k - 5,
                                 _rec_list[0][0] - 20, _rec_list[0][1] + k,
                                 _rec_list[0][0] - 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            if i == 2:
                c.create_text(_port_list[2][0] + 5, _port_list[2][1] - 10, text=1, justify=CENTER, font="Verdana 8")
                c.create_polygon(_rec_list[1][0] + 10, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k - 5,
                                 _rec_list[1][0] + 20, _rec_list[0][1] + k,
                                 _rec_list[1][0] + 15, _rec_list[0][1] + k + 5,
                                 fill='black', outline='black')
            i -=1
            k+=25
    if var.get() ==1:#decoder
        _set_DC()
        i = 3
        k = 28
        while (i >= 0):
            if i == 2:
                _list_in[0][0] = _rec_list[1][0] + _weight - 15
                _list_in[0][1] = _rec_list[0][1] + k
                pass
            if i==1 :
                c.create_line(_rec_list[1][0]+10, _rec_list[0][1] + k, _rec_list[1][0] + 30, _rec_list[0][1] + k, width=2)
                _list_out[0][0] = _rec_list[1][0] + 30
                _list_out[0][1] = _rec_list[0][1] + k
                _list_in[1][0] = _rec_list[1][0] + _weight - 15
                _list_in[1][1] = _rec_list[0][1] + k
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
    if var.get() == 2:#multiplexer
        _set_MX()

        c.create_text(_port_list[0][0] + 5, _port_list[0][1] - 10, text=0, justify=CENTER, font="Verdana 8")
        c.create_text(_port_list[1][0] + 5, _port_list[1][1] - 10, text=0, justify=CENTER, font="Verdana 8")
        c.create_text(_port_list[2][0] + 5, _port_list[2][1] - 10, text=0, justify=CENTER, font="Verdana 8")
        c.create_text(_port_list[3][0] + 5, _port_list[3][1] - 10, text=1, justify=CENTER, font="Verdana 8")



but.bind('<Button-1>',  entry_scan)
#_set_DC()
#_set_NOT()
#_set_CD()
#_set_MX()
#_set_OR()
#_set_AND()
#_set_XOR()
#_set_MX()

root.mainloop()


