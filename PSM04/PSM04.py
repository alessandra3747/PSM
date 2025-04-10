import math

import matplotlib.pyplot as plt


def midPoint(dt, alfa, r, m, g, sx, sy, v, ik, w, b):

    t = 0

    wartosci_t = []
    wartosci_sx = []
    wartosci_sy = []
    wartosci_b = []

    while (t <= 5):
        #PRZYSPIESZENIE KULI/SFERY
        acc = g * math.sin(alfa) / (1 + ik / (m * r**2))

        #POŁOWA ZMIANY PRĘDKOŚCI KULI/SFERY W 1 KROKU CZASOWYM
        vd = acc * dt / 2

        deltaV = acc * dt
        deltaSx = (v + vd) * dt

        sx += deltaSx
        sy = r
        v += deltaV

        #PRZYSPIESZENIE KĄTOWE KULI/SFERY WOKÓŁ JEJ OSI OBROTU
        eps = acc / r

        deltaW = eps * dt

        deltaB = (w + deltaW / 2) * dt

        b += deltaB
        w += deltaW

        # RESETOWANIE KĄTA PO PEŁNYM OBROCIE
        if b >= 2 * math.pi:
            b -= 2 * math.pi

        wartosci_t.append(t)
        wartosci_sx.append(sx)
        wartosci_sy.append(sy)
        wartosci_b.append(math.degrees(b))

        t += dt

    return wartosci_t, wartosci_sx, wartosci_sy, wartosci_b



def main():

    # PARAMETRY
    alfa = math.radians(45)  # Kąt nachylenia równi
    dt = 0.01  # Krok czasu
    h = 20 #Wysokość równi
    r = 2  # Promień kuli/sfery
    m = 1  # Masa kuli/sfery
    g = 9.81  # Grawitacja
    sx = 0  # Położenie początkowe x
    sy = 2  # Położenie początkowe y
    v = 0  # Prędkość początkowa kuli/sfery
    w = 0  # Prędkość kątowa
    b = 0  # Kąt obrotu

    #MOMENTY BEZWŁADNOŚCI WOKÓŁ OSI OBROTU KULI/SFERY
    ik_kuli = 2 / 5 * m * r**2
    ik_sfery = 2 / 3 * m * r ** 2


    t_kula, sx_kula, sy_kula, b_kula = midPoint(dt, alfa, r, m, g, sx, sy, v, ik_kuli, w, b)
    t_sfera, sx_sfera, sy_sfera, b_sfera = midPoint(dt, alfa, r, m, g, sx, sy, v, ik_sfery, w, b)


    #WYKRESY
    fig, ax = plt.subplots(3, 2, figsize=(10, 8))

    #DLA KULI
    ax[0, 0].plot(t_kula, sx_kula)
    ax[0, 0].set_xlabel('Czas (s)')
    ax[0, 0].set_ylabel('sx kuli (m)')
    ax[0, 0].set_title('Położenie x kuli w czasie')
    ax[0, 0].grid(True)

    ax[1, 0].plot(t_kula, sy_kula)
    ax[1, 0].set_xlabel('Czas (s)')
    ax[1, 0].set_ylabel('sy kuli (m)')
    ax[1, 0].set_title('Położenie y kuli w czasie')
    ax[1, 0].grid(True)

    ax[2, 0].plot(t_kula, b_kula)
    ax[2, 0].set_xlabel('Czas (s)')
    ax[2, 0].set_ylabel('Kąt (°)')
    ax[2, 0].set_title('Kąt obrotu kuli w czasie')
    ax[2, 0].grid(True)

    #DLA SFERY
    ax[0, 1].plot(t_sfera, sx_sfera)
    ax[0, 1].set_xlabel('Czas (s)')
    ax[0, 1].set_ylabel('sx sfery (m)')
    ax[0, 1].set_title('Położenie x sfery w czasie')
    ax[0, 1].grid(True)

    ax[1, 1].plot(t_sfera, sy_sfera)
    ax[1, 1].set_xlabel('Czas (s)')
    ax[1, 1].set_ylabel('sy sfery (m)')
    ax[1, 1].set_title('Położenie y sfery w czasie')
    ax[1, 1].grid(True)

    ax[2, 1].plot(t_sfera, b_sfera)
    ax[2, 1].set_xlabel('Czas (s)')
    ax[2, 1].set_ylabel('Kąt (°)')
    ax[2, 1].set_title('Kąt obrotu sfery w czasie')
    ax[2, 1].grid(True)


    fig.tight_layout()
    plt.show()


main()