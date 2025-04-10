import math
from matplotlib import pyplot as plt

#s30395

#ZMIENNE DO OBLICZEŃ
G = 6.6743e-11

Ms = 1.989e30
Mz = 5.972e24
Mk = 7.347e22

Rzs = 1.5e8 * 1000
Rzk = 384400 * 1000

dt = 3600
t_max = math.ceil(365.25 * 24 * 60 * 60)


def ziemia_slonce():
    t = 0
    lista_x = []
    lista_y = []

    Sx = 0
    Sy = Rzs

    Vx = math.sqrt(G * Ms / Rzs)
    Vy = 0

    while t < t_max:
        Wx = -Sx
        Wy = -Sy
        Dzs = math.sqrt(Wx**2 + Wy**2)

        Ux = Wx / Dzs
        Uy = Wy / Dzs

        a = G * Ms / Dzs**2
        ax = Ux * a
        ay = Uy * a

        Vx_2 = Vx + ax * dt / 2
        Vy_2 = Vy + ay * dt / 2

        DSx = Vx_2 * dt
        DSy = Vy_2 * dt

        Sx_2 = Sx + Vx_2 * dt / 2
        Sy_2 = Sy + Vy_2 * dt / 2

        lista_x.append(Sx_2 / 10)
        lista_y.append(Sy_2 / 10)

        Wx_2 = -Sx_2
        Wy_2 = -Sy_2
        Dzs_2 = math.sqrt(Wx_2**2 + Wy_2**2)

        Ux_2 = Wx_2 / Dzs_2
        Uy_2 = Wy_2 / Dzs_2

        a_2 = G * Ms / Dzs_2**2
        ax_2 = Ux_2 * a_2
        ay_2 = Uy_2 * a_2

        DVx = ax_2 * dt
        DVy = ay_2 * dt

        Sx += DSx
        Sy += DSy
        Vx += DVx
        Vy += DVy
        t += dt

    return lista_x, lista_y


def ksiezyc_ziemia():
    t = 0
    lista_x = []
    lista_y = []

    Sx = 0
    Sy = Rzk

    Vx = math.sqrt(G * Mz / Rzk)
    Vy = 0

    while t < t_max:
        Wx = -Sx
        Wy = -Sy
        Dzk = math.sqrt(Wx ** 2 + Wy ** 2)

        Ux = Wx / Dzk
        Uy = Wy / Dzk

        a = G * Mz / Dzk ** 2
        ax = Ux * a
        ay = Uy * a

        Vx_2 = Vx + ax * dt / 2
        Vy_2 = Vy + ay * dt / 2

        DSx = Vx_2 * dt
        DSy = Vy_2 * dt

        Sx_2 = Sx + Vx_2 * dt / 2
        Sy_2 = Sy + Vy_2 * dt / 2

        lista_x.append(Sx_2)
        lista_y.append(Sy_2)

        Wx_2 = -Sx_2
        Wy_2 = -Sy_2
        Dzk_2 = math.sqrt(Wx_2 ** 2 + Wy_2 ** 2)

        Ux_2 = Wx_2 / Dzk_2
        Uy_2 = Wy_2 / Dzk_2

        a_2 = G * Mz / Dzk_2 ** 2
        ax_2 = Ux_2 * a_2
        ay_2 = Uy_2 * a_2

        DVx = ax_2 * dt
        DVy = ay_2 * dt

        Sx += DSx
        Sy += DSy
        Vx += DVx
        Vy += DVy
        t += dt

    return lista_x, lista_y


def ksiezyc_slonce():
    x = []
    y = []

    x1, y1 = ziemia_slonce()
    x2, y2 = ksiezyc_ziemia()

    for i in range(len(x1)):
        x.append(x1[i] + x2[i])
        y.append(y1[i] + y2[i])

    return x, y


def main():
    x1, y1 = ziemia_slonce()
    x2, y2 = ksiezyc_slonce()

    fig, ax = plt.subplots()
    ax.plot(x1, y1, label = 'Ziemia', color = 'b')
    ax.plot(x2, y2, label = 'Ksiezyc', color = 'r')

    ax.legend()
    plt.grid(True)
    plt.show()


#WYWOŁANIE PROGRAMU
main()