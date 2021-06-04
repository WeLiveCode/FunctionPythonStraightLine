import math


def y_co_ordinate():
    y = float(input("Faka isilungelelanisi sika Y"))
    return y


def x_co_ordinates():
    x = float(input("Faka isilungelanisi sika X"))
    return x


def point_name():
    name = input("Faka igama lalendawo")
    return name


def distance(x,y):
    x_origin = 0
    y_origin = 0
    dist = math.sqrt((x-x_origin)**2+(y-y_origin)**2)
    return dist


def x_ref_x_axis(x):
    x_ref = x * -1
    return x_ref


def y_ref_y_axis(y):
    y_ref = y * -1
    return y_ref


def determine_quad(x_input, y_input):
    if y_input > 0 and x_input > 0 :
        quad = "Mntla Mpuma"
    elif y_input > 0 and x_input < 0 :
        quad = "Mntla Ntshona"
    elif y_input < 0 and x_input < 0 :
        quad = "Mzantsi Ntshona"
    elif y_input < 0 and x_input > 0 :
        quad = "Mzantsi Mpuma"
    elif y_input > 0 and x_input ==0 :
        quad ="Mntla"
    elif y_input == 0 and x_input < 0 :
        quad = "Ntshona"
    elif y_input < 0 and x_input == 0 :
        quad = "Mzantsi"
    elif y_input == 0 and x_input > 0 :
        quad = "Mpuma"
    elif y_input == 0 and x_input == 0 :
        quad = "Orijini"
    return quad


def equation_str(x_inp, y_inp):
    #equation of a straight line...y = mx + c
    x_ori = 0
    y_ori = 0
    m = (y_inp-y_ori)/(x_inp-x_ori)
    c = y_inp - m*x_inp
    return f'y = {m}x + {c}'


def output(dis,ref_x_x_axis,ref_y_y_axis,x,y,quad,equa_straight,name):
    print("Umgama ophakathi kweOrijini nendawo efakwe ngumntu ngu", dis)
    print("Uguqulelo lwendawo efakwe ngumntu kwiiAsi zika X ngu ",name,"(", ref_x_x_axis,",",y,")")
    print("Uguqulelo lwendawo efakwe ngumntu kwiiAsi zikaY ngu ",name,"(", x, ",",ref_y_y_axis,")")
    print("Lendawo ifakwe ngumntu ise " + quad)
    print("IEquation yomgca ongqalileyo ngu  " + equa_straight)


if __name__ == '__main__':
    y = y_co_ordinate()
    x = x_co_ordinates()
    name = point_name()
    dis = distance(x, y)
    ref_x_x_axis = x_ref_x_axis(x)
    ref_y_y_axis = y_ref_y_axis(y)
    quadrant = determine_quad(x, y)
    equa_straight = equation_str(x, y)
    output(dis, ref_x_x_axis, ref_y_y_axis, x, y, quadrant, equa_straight,name)

