import math
import random

s = 3
r = 5
n = 4
pc = 0.8
pm = 0.05
t_max = 200
num = 1000

def main(args):
    global s, r, n, pc, pm, t_max, num
    w = []
    inicioAleatorio(w);
    apt = []
    apt_gen = 0
    for i in range(n):
        apt.append(aptitud(w[i]))
        apt_gen += apt[i]

    apt_med = apt_gen/n

    print("Aptitud De La Generacion:", apt_gen, "\tAptitud Media:", apt_med)
    print(w)

    algoritmo(w)

def inicioAleatorio(w):
    for i in range(n):
        aux = []
        for j in range(r):
            aux.append(math.floor(random.random() * s))
        w.append(aux)

def aptitud(cad):
    count = 0
    for i in range(r):
        if(cad[i] == 2):
            count += 1
    return count

def algoritmo(w):
    t = 0
    apt = []
    apt_gen = 0
    apt_med = 0
    while(t < t_max):
        seleccion(w, apt)
        crossover(w)
        mutacion(w)
        t += 1
    apt.clear()
    apt_gen = 0
    for i in range(n):
        apt.append(aptitud(w[i]))
        apt_gen += apt[i]
    apt_med = apt_gen / n
    apt_med = apt_gen / n
    print("Aptitud De La Generacion {", t, "}:", apt_gen, "\tAptitud Media:", apt_med)

def seleccion(w, apt):
    apt.clear()
    apt_gen = 0
    p = []
    c = []
    interv = []
    for i in range(n):
        apt.append(aptitud(w[i]))
        apt_gen += apt[i]

    for i in range(n):
        aux = []
        p.append(apt[i]/apt_gen)
        c.append(p[i] * num + 1)
        if i == 0:
            aux.append(0)
            aux.append(c[0] - 1)
        else:
            aux.append(interv[i-1][1] + 1)
            aux.append(aux[0] + c[i] - 1)
        interv.append(aux)
    newW = []
    for i in range(n):
        rand = math.floor(random.random() * (num+n))
        for j in range(n):
            if(rand <= interv[j][1]):
                newW.append(w[j])
                break

    for i in range(len(w)):
        w[i] = newW[i]

def crossover(w):
    cross = []
    cut = math.floor(random.random() * (r-2) + 1)
    for i in range(n):
        aux = random.random()
        if(aux <= pc):
            cross.append(i)
    if(len(cross)%2 == 1):
        cross.pop()

    for i in range(0, len(cross), 2):
        for j in range(r):
            if(j >= cut):
                aux = w[i+1][j]
                w[i+1][j] = w[i][j]
                w[i][j] = aux

def mutacion(w):
    for i in range(n):
        for j in range(r):
            if(random.random() <= pm):
                orig = w[i][j]
                new = -1
                while(orig != new):
                    new = math.floor(random.random() * s)
                w[i][j] = new





main([])