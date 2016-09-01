#----------------------------
# Hoja de trabajo 5
# Simulacio.py
# Axel Mazariegos, 131212
# Gustavo Orellana, 15073
#----------------------------

import simpy
import random


def proceso(env, tproceso, nombre, ram, memoria, instrucciones, velocidad):

    global tTotal
    global tiempos

    yield env.timeout(tproceso)
    print('%s cantidad a utilizar %d de RAM (new)' % (nombre, memoria))
    llegada = env.now

    yield ram.get(memoria)
    print('%s. Cantidad utilizada %d de RAM (admited)' % (nombre, memoria))


    ins_completadas = 0

    while ins_completadas < instrucciones:

        with cpu.request() as req:
            yield req

            if (instrucciones - ins_completadas) >= velocidad:
                efec = velocidad
            else:
                efec = (instrucciones - ins_completadas)

            print('%s CPU ejecutara %d instrucciones. (ready)' % (nombre, efec))

            yield env.timeout(efec/velocidad)


            ins_completadas += efec
            print('%s CPU (%d de %d) completado. (running)' % (nombre, ins_completadas, instrucciones))


        decision = random.randint(1,2)

        if decision == 1 and ins_completadas<instrucciones:

            with wait.request() as req2:
                yield req2
                yield env.timeout(1)
                print('%s. Operaciones realizadas I/O. (waiting)' % (nombre))


    yield ram.put(memoria)
    print('%s retorna %d de RAM. (terminated)' % (nombre, memoria))

    tTotal += (env.now - llegada)

    tiempos.append(env.now - llegada)



velocidad = 3.0
memoriaRAM = 100
procesos = 25
tTotal = 0.0
tiempos = []


env = simpy.Environment()
cpu = simpy.Resource(env, capacity=2)
ram = simpy.Container(env, init=memoriaRAM, capacity=memoriaRAM)
wait = simpy.Resource(env, capacity=2)


intervalo = 10
random.seed(2411)


for i in range(procesos):
    tproceso = random.expovariate(1.0 / intervalo)
    instrucciones = random.randint(1,10)
    memoria = random.randint(1,10)
    env.process(proceso(env, tproceso, 'Proceso %d' % i, ram, memoria, instrucciones, velocidad))


env.run()


print (" ")
prom=(tTotal/procesos)
print('Tiempo promedio de procesos: %f seg' % (prom))



sumatoria=0

for cont in tiempos:
    sumatoria+=(cont-prom)**2

desviacion = (sumatoria/(procesos-1))**0.5

print (" ")
print('La desviacion estandar es: %f seg' %(desviacion))
