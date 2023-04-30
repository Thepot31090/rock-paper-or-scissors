import time
import random






miPuntaje = 0
PcPuntaje = 0

n = int(input("select your language 1 for spanish and 2 for english, elige tu lenguaje, 1 para español y 2 para ingles"))


if n == 1:
    b = input("deseas elegir el modo batalla de bots? (si o no) FUNCION EN ALFA")
    if b == "si":
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        

        #seleccion de los bots

        if b == 1:
            print("BOT 1 ha elegido piedra")
        if b == 2:
            print("BOT 1 ha elegido papel")
        if b == 3:
            print("BOT 1 ha elegido tijera")
        
        if a == 1:
            print("BOT 2 ha elegido piedra")
        if a == 2:
            print("BOT 2 ha elegido papel")
        if a == 3:
            print("BOT 2 ha elegido tijera")
        time.sleep(2)
        #victoria del bot 1

        if a == 1 and b == 2:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif a == 2 and b == 3:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif a == 3 and b == 1:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif b == 1 and a == 2:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 2 and a == 3:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 3 and a == 1:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        else:
            print("ninguno de los bots ha ganado")
        
        time.sleep(2)
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        

        #seleccion de los bots

        if b == 1:
            print("BOT 1 ha elegido piedra")
        if b == 2:
            print("BOT 1 ha elegido papel")
        if b == 3:
            print("BOT 1 ha elegido tijera")
        
        if a == 1:
            print("BOT 2 ha elegido piedra")
        if a == 2:
            print("BOT 2 ha elegido papel")
        if a == 3:
            print("BOT 2 ha elegido tijera")
        time.sleep(2)
        #victoria del bot 1

        if a == 1 and b == 2:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif a == 2 and b == 3:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif a == 3 and b == 1:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif b == 1 and a == 2:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 2 and a == 3:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 3 and a == 1:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        else:
            print("ninguno de los bots ha ganado")
        
        time.sleep(2)
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        

        #seleccion de los bots

        if b == 1:
            print("BOT 1 ha elegido piedra")
        if b == 2:
            print("BOT 1 ha elegido papel")
        if b == 3:
            print("BOT 1 ha elegido tijera")
        
        if a == 1:
            print("BOT 2 ha elegido piedra")
        if a == 2:
            print("BOT 2 ha elegido papel")
        if a == 3:
            print("BOT 2 ha elegido tijera")
        time.sleep(2)
        #victoria del bot 1

        if a == 1 and b == 2:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif a == 2 and b == 3:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif a == 3 and b == 1:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif b == 1 and a == 2:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 2 and a == 3:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 3 and a == 1:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        else:
            print("ninguno de los bots ha ganado")
        
        time.sleep(2)
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        

        #seleccion de los bots

        if b == 1:
            print("BOT 1 ha elegido piedra")
        if b == 2:
            print("BOT 1 ha elegido papel")
        if b == 3:
            print("BOT 1 ha elegido tijera")
        
        if a == 1:
            print("BOT 2 ha elegido piedra")
        if a == 2:
            print("BOT 2 ha elegido papel")
        if a == 3:
            print("BOT 2 ha elegido tijera")
        time.sleep(2)
        #victoria del bot 1

        if a == 1 and b == 2:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif a == 2 and b == 3:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif a == 3 and b == 1:
            print("ha ganado el BOT 1")
            miPuntaje += 1
            time.sleep(2)
        elif b == 1 and a == 2:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 2 and a == 3:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 3 and a == 1:
            print("ha ganado el BOT 2")
            PcPuntaje += 1
            time.sleep(2)
        else:
            print("ninguno de los bots ha ganado")
        
        time.sleep(2)
    
        print("fin del juego, el puntaje del BOT 1 es:", miPuntaje, "y el puntaje del BOT 2 es:", PcPuntaje)
        time.sleep(3)
        if miPuntaje > PcPuntaje:
            print("ha ganado el BOT 1")
        if PcPuntaje > miPuntaje:
            print("ha ganado el BOT 2")
        if PcPuntaje == miPuntaje:
            print("han empatado")
            YT = input("deseas que juegen el desempate? si para que juegen no para que no juegen")
            
            if YT == "si":
                    a = random.randint(1, 3)
                    b = random.randint(1, 3)
                    

                    #seleccion de los bots

                    if b == 1:
                        print("BOT 1 ha elegido piedra")
                    if b == 2:
                        print("BOT 1 ha elegido papel")
                    if b == 3:
                        print("BOT 1 ha elegido tijera")
                    
                    if a == 1:
                        print("BOT 2 ha elegido piedra")
                    if a == 2:
                        print("BOT 2 ha elegido papel")
                    if a == 3:
                        print("BOT 2 ha elegido tijera")
                    time.sleep(2)
                    #victoria del bot 1

                    if a == 1 and b == 2:
                        print("ha ganado el BOT 1")
                        miPuntaje += 1
                        time.sleep(2)
                    elif a == 2 and b == 3:
                        print("ha ganado el BOT 1")
                        miPuntaje += 1
                        time.sleep(2)
                    elif a == 3 and b == 1:
                        print("ha ganado el BOT 1")
                        miPuntaje += 1
                        time.sleep(2)
                    elif b == 1 and a == 2:
                        print("ha ganado el BOT 2")
                        PcPuntaje += 1
                        time.sleep(2)
                    elif b == 2 and a == 3:
                        print("ha ganado el BOT 2")
                        PcPuntaje += 1
                        time.sleep(2)
                    elif b == 3 and a == 1:
                        print("ha ganado el BOT 2")
                        PcPuntaje += 1
                        time.sleep(2)
                    else:
                        print("ninguno de los bots ha ganado")
                        print("fin del juego, el puntaje del BOT 1 es:", miPuntaje, "y el puntaje del BOT 2 es:", PcPuntaje)
                        time.sleep(3)
                        if miPuntaje > PcPuntaje:
                            print("ha ganado el BOT 1")
                        if PcPuntaje > miPuntaje:
                            print("ha ganado el BOT 2")
            if YT == "no":
                print("bueno, los bots han empatado") 
            time.sleep(2)
                



        
        






    
    if b == "no":
        t = int(input("hay 2 modos, el normal o el troll, pulsa 1 para el normal y 2 para el troll"))
        if t == 1:
            print("consiste en 4 juegos de piedra papel o tijeras, tu contra la maquina la cual elegira aleatoriamente, vamos a ver si puedes vencer")
            time.sleep(2)
            a = random.randint(1,3)
            b = input("que eligers: piedra papel o tijera (escribe en minuscula)")
            time.sleep(2)
            if a == 1:
                print("la compu eligio piedra")
            elif a == 2:
                print("la compu eligio tijera")
            else:
                print("la compu eligio papel")
            time.sleep(2)
            
            #gana el jugador
            if a == 1 and b == "papel":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "piedra":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "tijera":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            #situaciones de empate
            if a == 1 and b == "piedra":
                print("empate")
                time.sleep(2)
            if a == 2 and b == "tijera":
                print("empate")
                time.sleep(2)
            if a == 3 and b == "papel":
                print("empate")
                time.sleep(2)
            #gana la compu
            elif a == 1 and b == "tijera":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora es", PcPuntaje)
            elif a == 2 and b == "papel":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            elif a == 3 and b == "piedra":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            time.sleep(2)
            a = random.randint(1,3)
            b = input("que eligers: piedra papel o tijera (escribe en minuscula)")
            time.sleep(2)
            if a == 1:
                print("la compu eligio piedra")
            elif a == 2:
                print("la compu eligio tijera")
            else:
                print("la compu eligio papel")
            time.sleep(2)
            
            #gana el jugador
            if a == 1 and b == "papel":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "piedra":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "tijera":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            #situaciones de empate
            if a == 1 and b == "piedra":
                print("empate")
                time.sleep(2)
            if a == 2 and b == "tijera":
                print("empate")
                time.sleep(2)
            if a == 3 and b == "papel":
                print("empate")
                time.sleep(2)
            #gana la compu
            elif a == 1 and b == "tijera":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora es", PcPuntaje)
            elif a == 2 and b == "papel":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            elif a == 3 and b == "piedra":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
                time.sleep(2)
            a = random.randint(1,3)
            b = input("que eligers: piedra papel o tijera (escribe en minuscula)")
            time.sleep(2)
            if a == 1:
                print("la compu eligio piedra")
            elif a == 2:
                print("la compu eligio tijera")
            else:
                print("la compu eligio papel")
            time.sleep(2)
            
            #gana el jugador
            if a == 1 and b == "papel":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "piedra":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "tijera":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            #situaciones de empate
            if a == 1 and b == "piedra":
                print("empate")
                time.sleep(2)
            if a == 2 and b == "tijera":
                print("empate")
                time.sleep(2)
            if a == 3 and b == "papel":
                print("empate")
                time.sleep(2)
            #gana la compu
            elif a == 1 and b == "tijera":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora es", PcPuntaje)
            elif a == 2 and b == "papel":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            elif a == 3 and b == "piedra":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            time.sleep(2)
            a = random.randint(1,3)
            b = input("que eligers: piedra papel o tijera (escrive en minuscula)")
            time.sleep(2)
            if a == 1:
                print("la compu eligio piedra")
            elif a == 2:
                print("la compu eligio tijera")
            else:
                print("la compu eligio papel")
            time.sleep(2)
            
            #gana el jugador
            if a == 1 and b == "papel":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "piedra":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "tijera":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            #situaciones de empate
            if a == 1 and b == "piedra":
                print("empate")
                time.sleep(2)
            if a == 2 and b == "tijera":
                print("empate")
                time.sleep(2)
            if a == 3 and b == "papel":
                print("empate")
                time.sleep(2)
            #gana la compu
            elif a == 1 and b == "tijera":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora es", PcPuntaje)
            elif a == 2 and b == "papel":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            elif a == 3 and b == "piedra":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            
            
            #Final del juego
                time.sleep(2)
            print("Fin del juego, el puntaje del jugador es:", miPuntaje, "y el puntaje de la compu es", PcPuntaje)
            if miPuntaje < PcPuntaje:
                print("gano la computadora")
            elif miPuntaje > PcPuntaje:
                print("ganaste Muy bien hecho")
            else:
                print("Empate, ten otra de desempate")
                time.sleep(2)
                a = random.randint(1,3)
                b = input("que eliges: piedra papel o tijera (escribe en minuscula)")
                time.sleep(2)
            if a == 1:
                print("la compu eligio piedra")
            elif a == 2:
                print("la compu eligio tijera")
            else:
                print("la compu eligio papel")
            time.sleep(2)
                
            if a == 1 and b == "papel":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "piedra":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "tijera":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            if a == 1 and b == "piedra":
                print("empate")
                time.sleep(2)
            if a == 2 and b == "tijera":
                print("empate")
                time.sleep(2)
            if a == 3 and b == "papel":
                print("empate")
                time.sleep(2)
                
            elif a == 1 and b == "tijera":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora es", PcPuntaje)
            elif a == 2 and b == "papel":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            elif a == 3 and b == "piedra":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            time.sleep(2)
            print("Fin del juego, el puntaje del jugador es:", miPuntaje, "y el puntaje de la compu es", PcPuntaje)
            if miPuntaje < PcPuntaje:
                print("gano la computadora")
            elif miPuntaje > PcPuntaje:
                print("ganaste Muy bien hecho")
        if t == 2:
            print("consiste en 4 juegos de piedra papel o tijeras, tu contra la maquina la cual elegira aleatoriamente, vamos a ver si puedes vencer")
            time.sleep(2)
            a = random.randint(1,3)
            b = input("que eligers: piedra papel o tijera (escribe en minuscula)")
            time.sleep(2)
            if a == 1:
                print("la compu eligio piedra")
            elif a == 2:
                print("la compu eligio tijera")
            else:
                print("la compu eligio papel")
            time.sleep(2)
            
            #gana el jugador
            if a == 1 and b == "papel":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "piedra":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "tijera":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            #situaciones de empate
            if a == 1 and b == "piedra":
                print("empate")
                time.sleep(2)
            if a == 2 and b == "tijera":
                print("empate")
                time.sleep(2)
            if a == 3 and b == "papel":
                print("empate")
                time.sleep(2)
            #gana la compu
            elif a == 1 and b == "tijera":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora es", PcPuntaje)
            elif a == 2 and b == "papel":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            elif a == 3 and b == "piedra":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            time.sleep(2)
            a = random.randint(1,3)
            b = input("que eligers: piedra papel o tijera (escribe en minuscula)")
            time.sleep(2)
            if a == 1:
                print("la compu eligio piedra")
            elif a == 2:
                print("la compu eligio tijera")
            else:
                print("la compu eligio papel")
            time.sleep(2)
            
            #gana el jugador
            if a == 1 and b == "papel":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "piedra":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "tijera":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            #situaciones de empate
            if a == 1 and b == "piedra":
                print("empate")
                time.sleep(2)
            if a == 2 and b == "tijera":
                print("empate")
                time.sleep(2)
            if a == 3 and b == "papel":
                print("empate")
                time.sleep(2)
            #gana la compu
            elif a == 1 and b == "tijera":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora es", PcPuntaje)
            elif a == 2 and b == "papel":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            elif a == 3 and b == "piedra":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            time.sleep(2)
            a = random.randint(1,3)
            b = input("que eligers: piedra papel o tijera (escribe en minuscula)")
            time.sleep(2)
            if a == 1:
                print("la compu eligio piedra")
            elif a == 2:
                print("la compu eligio tijera")
            else:
                print("la compu eligio papel")
            time.sleep(2)
            
            #gana el jugador
            if a == 2 and b == "papel":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "piedra":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 1 and b == "tijera":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            #situaciones de empate
            if a == 1 and b == "piedra":
                print("empate")
                time.sleep(2)
            if a == 2 and b == "tijera":
                print("empate")
                time.sleep(2)
            if a == 3 and b == "papel":
                print("empate")
                time.sleep(2)
            #gana la compu

            elif a == 3 and b == "tijera":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora es", PcPuntaje)
            elif a == 1 and b == "papel":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            elif a == 2 and b == "piedra":
                print("gano la compu")
                PcPuntaje += 1
                time.sleep(2)
            a = random.randint(1,3)
            b = input("que eligers: piedra papel o tijera (escribe en minuscula)")
            time.sleep(2)
            if a == 1:
                print("la compu eligio piedra")
            elif a == 2:
                print("la compu eligio tijera")
            else:
                print("la compu eligio papel")
            time.sleep(2)
            
            #gana el jugador
            if a == 1 and b == "papel":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "piedra":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "tijera":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            #situaciones de empate
            if a == 1 and b == "piedra":
                print("empate")
                time.sleep(2)
            if a == 2 and b == "tijera":
                print("empate")
                time.sleep(2)
            if a == 3 and b == "papel":
                print("empate")
                time.sleep(2)
            #gana la compu
            elif a == 1 and b == "tijera":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora es", PcPuntaje)
            elif a == 2 and b == "papel":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            elif a == 3 and b == "piedra":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            time.sleep(2)
            print("Fin del juego, el puntaje del jugador es:", miPuntaje, "y el puntaje de la compu es", PcPuntaje)
            if miPuntaje < PcPuntaje:
                print("gano la computadora")
            elif miPuntaje > PcPuntaje:
                print("ganaste Muy bien hecho")
            else:
                print("Empate, ten otra de desempate")
                time.sleep(2)
            a = random.randint(1,3)
            b = input("que eligers: piedra papel o tijera (escrive en minuscula)")
            time.sleep(2)
            if a == 1:
                print("la compu eligio piedra")
            elif a == 2:
                print("la compu eligio tijera")
            else:
                print("la compu eligio papel")
            time.sleep(2)
            
            #gana el jugador
            if a == 1 and b == "papel":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "piedra":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "tijera":
                print("ha ganado el jugador")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            #situaciones de empate
            if a == 1 and b == "piedra":
                print("empate")
                time.sleep(2)
            if a == 2 and b == "tijera":
                print("empate")
                time.sleep(2)
            if a == 3 and b == "papel":
                print("empate")
                time.sleep(2)
            #gana la compu
            elif a == 1 and b == "tijera":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora es", PcPuntaje)
            elif a == 2 and b == "papel":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            elif a == 3 and b == "piedra":
                print("gano la compu")
                PcPuntaje += 1
                print("el puntaje de la computadora ahora es", PcPuntaje)
            print("Fin del juego, el puntaje del jugador es:", miPuntaje, "y el puntaje de la compu es", PcPuntaje)
            if miPuntaje < PcPuntaje:
                print("gano la computadora")
            elif miPuntaje > PcPuntaje:
                print("ganaste Muy bien hecho")


    
    #Juego en ingles
    #scissors

    
    
if n == 2:

    B = input("Do you want to select battle of bots? (yes or no) it`s in Alfa")
    if B == "yes":
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        

        #seleccion de los bots

        if b == 1:
            print("BOT 1 has selected stone")
        if b == 2:
            print("BOT 1 has selected paper")
        if b == 3:
            print("BOT 1 has selected scissors")
        
        if a == 1:
            print("BOT 2 has selected stone")
        if a == 2:
            print("BOT 2 has selected paper")
        if a == 3:
            print("BOT 2 has selected scissors")
        time.sleep(2)
        #victoria del bot 1

        if a == 1 and b == 2:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif a == 2 and b == 3:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif a == 3 and b == 1:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif b == 1 and a == 2:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 2 and a == 3:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 3 and a == 1:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        else:
            print("none wins, it`s a tie ")
        
        time.sleep(2)
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        

        #seleccion de los bots

        if b == 1:
            print("BOT 1 has selected stone")
        if b == 2:
            print("BOT 1 has selected paper")
        if b == 3:
            print("BOT 1 has selected scissors")
        
        if a == 1:
            print("BOT 2 has selected stone")
        if a == 2:
            print("BOT 2 has selected paper")
        if a == 3:
            print("BOT 2 has selected scissors")
        time.sleep(2)
        #victoria del bot 1

        if a == 1 and b == 2:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif a == 2 and b == 3:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif a == 3 and b == 1:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif b == 1 and a == 2:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 2 and a == 3:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 3 and a == 1:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        else:
            print("none wins, it`s a tie ")
        
        time.sleep(2)
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        

        #seleccion de los bots

        if b == 1:
            print("BOT 1 has selected stone")
        if b == 2:
            print("BOT 1 has selected paper")
        if b == 3:
            print("BOT 1 has selected scissors")
        
        if a == 1:
            print("BOT 2 has selected stone")
        if a == 2:
            print("BOT 2 has selected paper")
        if a == 3:
            print("BOT 2 has selected scissors")
        time.sleep(2)
        #victoria del bot 1

        if a == 1 and b == 2:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif a == 2 and b == 3:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif a == 3 and b == 1:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif b == 1 and a == 2:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 2 and a == 3:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 3 and a == 1:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        else:
            print("none wins, it`s a tie ")
        
        time.sleep(2)
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        

        #seleccion de los bots

        if b == 1:
            print("BOT 1 has selected stone")
        if b == 2:
            print("BOT 1 has selected paper")
        if b == 3:
            print("BOT 1 has selected scissors")
        
        if a == 1:
            print("BOT 2 has selected stone")
        if a == 2:
            print("BOT 2 has selected paper")
        if a == 3:
            print("BOT 2 has selected scissors")
        time.sleep(2)
        #victoria del bot 1

        if a == 1 and b == 2:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif a == 2 and b == 3:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif a == 3 and b == 1:
            print("Bot 1 has win")
            miPuntaje += 1
            time.sleep(2)
        elif b == 1 and a == 2:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 2 and a == 3:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        elif b == 3 and a == 1:
            print("Bot 2 has win")
            PcPuntaje += 1
            time.sleep(2)
        else:
            print("none wins, it`s a tie ")
        
        time.sleep(2)
        print("End of the game, bot 1`s goal it is:", miPuntaje, "and Bot 2`s goal it is:", PcPuntaje)
        time.sleep(3)
        if miPuntaje > PcPuntaje:
            print("BOT 1 WINS")
        if PcPuntaje > miPuntaje:
             print("BOT 2 WINS")
        if PcPuntaje == miPuntaje:
            print("it`s a tie")
            YT = input("do you wish they play another y/n")
            if YT == "n":
                print("well it was your desition, IT IS A TIE")
            if YT == "y":
                    
                    a = random.randint(1, 3)
                    b = random.randint(1, 3)
                    

                    #seleccion de los bots

                    if b == 1:
                        print("BOT 1 has selected stone")
                    if b == 2:
                        print("BOT 1 has selected paper")
                    if b == 3:
                        print("BOT 1 has selected scissors")
                    
                    if a == 1:
                        print("BOT 2 has selected stone")
                    if a == 2:
                        print("BOT 2 has selected paper")
                    if a == 3:
                        print("BOT 2 has selected scissors")
                    time.sleep(2)
                    #victoria del bot 1

                    if a == 1 and b == 2:
                        print("Bot 1 has win")
                        miPuntaje += 1
                        time.sleep(2)
                    elif a == 2 and b == 3:
                        print("Bot 1 has win")
                        miPuntaje += 1
                        time.sleep(2)
                    elif a == 3 and b == 1:
                        print("Bot 1 has win")
                        miPuntaje += 1
                        time.sleep(2)
                    elif b == 1 and a == 2:
                        print("Bot 2 has win")
                        PcPuntaje += 1
                        time.sleep(2)
                    elif b == 2 and a == 3:
                        print("Bot 2 has win")
                        PcPuntaje += 1
                        time.sleep(2)
                    elif b == 3 and a == 1:
                        print("Bot 2 has win")
                        PcPuntaje += 1
                        time.sleep(2)
                    else:
                        print("none wins, it`s a tie ")
                    
                    time.sleep(2)
                    print("End of the game, bot 1`s goal it is:", miPuntaje, "and Bot 2`s goal it is:", PcPuntaje)
                    time.sleep(3)
                    if miPuntaje > PcPuntaje:
                        print("BOT 1 WINS")
                    if PcPuntaje > miPuntaje:
                        print("BOT 2 WINS")
        time.sleep(2)






    if B == "no":

        o = int(input("there are 2 game modes, troll and normal, for troll use 2 and for normal 1"))
        if o == 1:
            time.sleep(2)
            a = random.randint(1,3)
            b = input("what do you select, stone, paper or scissors (write in low letter)")
            time.sleep(2)
            if a == 1:
                print("The pc select stone")
            elif a == 2:
                print("The pc select scissors")
            else:
                print("The pc select paper")
            time.sleep(2)
                
            if a == 1 and b == "paper":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "stone":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "scissors":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            if a == 1 and b == "stone":
                print("tie")
                time.sleep(2)
            if a == 2 and b == "scissors":
                print("tie")
                time.sleep(2)
            if a == 3 and b == "paper":
                print("tie")
                time.sleep(2)
                
            elif a == 1 and b == "scissors":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 2 and b == "paper":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 3 and b == "stone":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
                time.sleep(2)
            a = random.randint(1,3)
            b = input("what do you select, stone, paper or scissors (write in low letter)")
            time.sleep(2)
            if a == 1:
                print("The pc select stone")
            elif a == 2:
                print("The pc select scissors")
            else:
                print("The pc select paper")
            time.sleep(2)
                
            if a == 1 and b == "paper":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "stone":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "scissors":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            if a == 1 and b == "stone":
                print("tie")
                time.sleep(2)
            if a == 2 and b == "scissors":
                print("tie")
                time.sleep(2)
            if a == 3 and b == "paper":
                print("tie")
                time.sleep(2)
                
            elif a == 1 and b == "scissors":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 2 and b == "paper":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 3 and b == "stone":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            
            time.sleep(2)
            print("End of the game, the player`s goal it is:", miPuntaje, "and the Pc`s goal it is", PcPuntaje)
            if miPuntaje < PcPuntaje:
                print("PC wins")
            elif miPuntaje > PcPuntaje:
                print("You win congratulations")
            else:
                print("tie, you have one chanse more")
                time.sleep(2)
                time.sleep(2)
            a = random.randint(1,3)
            b = input("what do you select, stone, paper or scissors (write in low letter)")
            time.sleep(2)
            if a == 1:
                print("The pc select stone")
            elif a == 2:
                print("The pc select scissors")
            else:
                print("The pc select paper")
            time.sleep(2)
                
            if a == 1 and b == "paper":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "stone":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "scissors":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            if a == 1 and b == "stone":
                print("tie")
                time.sleep(2)
            if a == 2 and b == "scissors":
                print("tie")
                time.sleep(2)
            if a == 3 and b == "paper":
                print("tie")
                time.sleep(2)
                
            elif a == 1 and b == "scissors":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 2 and b == "paper":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 3 and b == "stone":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            
            time.sleep(2)
            print("End of the game, the player`s goal it is:", miPuntaje, "and the Pc`s goal it is", PcPuntaje)
            if miPuntaje < PcPuntaje:
                print("PC wins")
            elif miPuntaje > PcPuntaje:
                print("You win congratulations")
            else:
                print("tie, you have one chanse more")
                time.sleep(2)
                time.sleep(2)
            a = random.randint(1,3)
            b = input("what do you select, stone, paper or scissors (write in low letter)")
            time.sleep(2)
            if a == 1:
                print("The pc select stone")
            elif a == 2:
                print("The pc select scissors")
            else:
                print("The pc select paper")
            time.sleep(2)
                
            if a == 1 and b == "paper":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 2 and b == "stone":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "scissors":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            if a == 1 and b == "stone":
                print("tie")
                time.sleep(2)
            if a == 2 and b == "scissors":
                print("tie")
                time.sleep(2)
            if a == 3 and b == "paper":
                print("tie")
                time.sleep(2)
                
            elif a == 1 and b == "scissors":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 2 and b == "paper":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 3 and b == "stone":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            

            
            
            time.sleep(2)
            print("End of the game, the player`s goal it is:", miPuntaje, "and the Pc`s goal it is", PcPuntaje)
            if miPuntaje < PcPuntaje:
                print("PC wins")
            elif miPuntaje > PcPuntaje:
                print("You win congratulations")
            else:
                print("tie, you have one chanse more")
                time.sleep(2)
                time.sleep(2)
                a = random.randint(1,3)
                b = input("what do you select, stone, paper or scissors (write in low letter)")
                time.sleep(2)
                if a == 1:
                    print("The pc select stone")
                elif a == 2:
                    print("The pc select scissors")
                else:
                    print("The pc select paper")
                time.sleep(2)
                    
                if a == 1 and b == "paper":
                    print("Player wins")
                    miPuntaje += 1
                    print(miPuntaje)
                    time.sleep(2)
                if a == 2 and b == "stone":
                    print("Player wins")
                    miPuntaje += 1
                    print(miPuntaje)
                    time.sleep(2)
                if a == 3 and b == "scissors":
                    print("Player wins")
                    miPuntaje += 1
                    print(miPuntaje)
                    time.sleep(2)
                
                if a == 1 and b == "stone":
                    print("tie")
                    time.sleep(2)
                if a == 2 and b == "scissors":
                    print("tie")
                    time.sleep(2)
                if a == 3 and b == "paper":
                    print("tie")
                    time.sleep(2)
                    
                elif a == 1 and b == "scissors":
                    print("PC wins")
                    PcPuntaje += 1
                    print("The goal of the PC no is", PcPuntaje)
                elif a == 2 and b == "paper":
                    print("PC wins")
                    PcPuntaje += 1
                    print("The goal of the PC no is", PcPuntaje)
                elif a == 3 and b == "stone":
                    print("PC wins")
                    PcPuntaje += 1
                    print("The goal of the PC no is", PcPuntaje)
                
                time.sleep(2)
                print("End of the game, the player`s goal it is:", miPuntaje, "and the Pc`s goal it is", PcPuntaje)
                if miPuntaje < PcPuntaje:
                    print("PC wins")
                elif miPuntaje > PcPuntaje:
                    print("You win congratulations")
                else:
                    print("tie, you have one chanse more")
                    time.sleep(2)

            
                    
        if o == 2:
            time.sleep(2)
            a = random.randint(1,3)
            b = input("what do you select, stone, paper or scissors (write in low letter)")
            time.sleep(2)
            if a == 1:
                print("The pc select stone")
            elif a == 2:
                print("The pc select scissors")
            else:
                print("The pc select paper")
            time.sleep(2)
                
            if a == 2 and b == "paper":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "stone":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 1 and b == "scissors":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            if a == 1 and b == "stone":
                print("tie")
                time.sleep(2)
            if a == 2 and b == "scissors":
                print("tie")
                time.sleep(2)
            if a == 3 and b == "paper":
                print("tie")
                time.sleep(2)
                
            elif a == 3 and b == "scissors":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 1 and b == "paper":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 2 and b == "stone":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
                time.sleep(2)
            time.sleep(2)
            a = random.randint(1,3)
            b = input("what do you select, stone, paper or scissors (write in low letter)")
            time.sleep(2)
            if a == 1:
                print("The pc select stone")
            elif a == 2:
                print("The pc select scissors")
            else:
                print("The pc select paper")
            time.sleep(2)
                
            if a == 2 and b == "paper":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "stone":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 1 and b == "scissors":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            if a == 1 and b == "stone":
                print("tie")
                time.sleep(2)
            if a == 2 and b == "scissors":
                print("tie")
                time.sleep(2)
            if a == 3 and b == "paper":
                print("tie")
                time.sleep(2)
                
            elif a == 3 and b == "scissors":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 1 and b == "paper":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 2 and b == "stone":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
                time.sleep(2)
            time.sleep(2)
            a = random.randint(1,3)
            b = input("what do you select, stone, paper or scissors (write in low letter)")
            time.sleep(2)
            if a == 1:
                print("The pc select stone")
            elif a == 2:
                print("The pc select scissors")
            else:
                print("The pc select paper")
            time.sleep(2)
                
            if a == 2 and b == "paper":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "stone":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 1 and b == "scissors":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            if a == 1 and b == "stone":
                print("tie")
                time.sleep(2)
            if a == 2 and b == "scissors":
                print("tie")
                time.sleep(2)
            if a == 3 and b == "paper":
                print("tie")
                time.sleep(2)
                
            elif a == 3 and b == "scissors":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 1 and b == "paper":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 2 and b == "stone":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
                time.sleep(2)
            time.sleep(2)
            a = random.randint(1,3)
            b = input("what do you select, stone, paper or scissors (write in low letter)")
            time.sleep(2)
            if a == 1:
                print("The pc select stone")
            elif a == 2:
                print("The pc select scissors")
            else:
                print("The pc select paper")
            time.sleep(2)
                
            if a == 2 and b == "paper":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "stone":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 1 and b == "scissors":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            if a == 1 and b == "stone":
                print("tie")
                time.sleep(2)
            if a == 2 and b == "scissors":
                print("tie")
                time.sleep(2)
            if a == 3 and b == "paper":
                print("tie")
                time.sleep(2)
                
            elif a == 3 and b == "scissors":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 1 and b == "paper":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 2 and b == "stone":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
                time.sleep(2)
            print("End of the game, the player`s goal it is:", miPuntaje, "and the Pc`s goal it is", PcPuntaje)
            if miPuntaje < PcPuntaje:
                print("PC wins")
            elif miPuntaje > PcPuntaje:
                print("You win congratulations")
            else:
                print("tie, you have one chanse more")
            a = random.randint(1,3)
            b = input("what do you select, stone, paper or scissors (write in low letter)")
            time.sleep(2)
            if a == 1:
                print("The pc select stone")
            elif a == 2:
                print("The pc select scissors")
            else:
                print("The pc select paper")
            time.sleep(2)
                
            if a == 2 and b == "paper":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 3 and b == "stone":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            if a == 1 and b == "scissors":
                print("Player wins")
                miPuntaje += 1
                print(miPuntaje)
                time.sleep(2)
            
            if a == 1 and b == "stone":
                print("tie")
                time.sleep(2)
            if a == 2 and b == "scissors":
                print("tie")
                time.sleep(2)
            if a == 3 and b == "paper":
                print("tie")
                time.sleep(2)
                
            elif a == 3 and b == "scissors":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 1 and b == "paper":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
            elif a == 2 and b == "stone":
                print("PC wins")
                PcPuntaje += 1
                print("The goal of the PC no is", PcPuntaje)
                time.sleep(2)
                print("End of the game, the player`s goal it is:", miPuntaje, "and the Pc`s goal it is", PcPuntaje)
            if miPuntaje < PcPuntaje:
                print("PC wins")
            elif miPuntaje > PcPuntaje:
                print("You win congratulations")
