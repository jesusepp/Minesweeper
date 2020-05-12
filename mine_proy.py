from os import system as sys  # Operar en el terminal
#import timeit                 # Medir velocidad del codigo
from time import time as t    # Tiempo entre dos partes del codigo
#from secrets import choice    # Generar numeros aleatorios
#import string                 # Generar caracteres
import random                 # Generar pseudo random
# cd /home/jesusp/python_pruebas
sys('clear')

def mine_game(difficulty):
    # Tipo de dificultad
    if difficulty == '1':
        print('You have choosen EASY')
        size_table = 6
        num_minas = int(size_table*size_table/5)
    if difficulty == '2':
        print('You have choosen MEDIUM')
        size_table = 10
        num_minas = int(size_table*size_table/4.5)
    if difficulty == '3':
        print('You have choosen HARD')
        size_table = 14
        num_minas = int(size_table*size_table/4)
    # Definición de la leyenda superior del tablero
    tit_superior = []
    for i in range(size_table):
        tit_superior.append(f'{i}')
    minas = 0                     # Numero inicial de minas
    table = []                    # Tablero inicial
    ans_table = []                # Tablero de respuestas
    ans_unit = []                 # Variable para llenar a ans_table con (-)
    rows = []                     # Filas de las tablas
    table_extra = []              # Table extra para barajar las minas
    mine_type = '01'              # String con los tipos de variable
    # Generacion de los tableros de respuestas y de minas
    for i in range(size_table):
        for j in range(size_table):
            if minas < num_minas:
                actual_mine = int(random.choice(mine_type))
                rows.append(actual_mine)
                if actual_mine == 1:
                    minas += 1
            else:
                rows.append(0)
            ans_unit.append('-')
        table.append(rows)
        ans_table.append(ans_unit)
        rows = []
        ans_unit = []
    # Mostrar el tablero
    for j in ans_table:
        print(j)
    # Mover las celdas para mejorar la aleatoriedad del sistema
    random.shuffle(table)
    rows = []
    for i in range(size_table):
        for j in range(size_table):
            rows.append(table[j][i])
        table_extra.append(rows)
        rows = []
        random.shuffle(table_extra[i])
    table = table_extra
    max_turns = (size_table*size_table)-num_minas   # Definicion de la duracion del juego
    player_decisions = set()                        # Set de decisiones del usuario o casillas ya desbloqueadas
    auto_complete = set()                           # Set para autocompletar el tablero
    hint = 1                                        # Valor inicial para hint que sera el numero de minas que rodean una celda
    # Comienzo del juego
    for i in range(max_turns):
        # Si se puede autocompletar alguna celda
        if auto_complete != set() and hint != 0:
            actual_decision = auto_complete.pop()
            row = int(actual_decision[0])
            column = int(actual_decision[2])
        # Si la celda actual es de cero y no hay que autocompletar otras celdas
        elif hint == 0:
            if row+1 < size_table and row > 0 and column > 0 and column+1 < size_table:
                for j in range(3):
                    for k in range(3):
                        if f'{row-j+1},{column-k+1}' not in player_decisions:
                            auto_complete.add(f'{row-j+1},{column-k+1}')
                if auto_complete == set():
                    True
                else:
                    actual_decision = auto_complete.pop()
                    row = int(actual_decision[0])
                    column = int(actual_decision[2])
            elif row+1 < size_table and row > 0 and column > 0:
                for j in range(3):
                    for k in range(2):
                        if f'{row-j+1},{column-k}' not in player_decisions:
                            auto_complete.add(f'{row-j+1},{column-k}')
                if auto_complete == set():
                    True
                else:
                    actual_decision = auto_complete.pop()
                    row = int(actual_decision[0])
                    column = int(actual_decision[2])
            elif row+1 < size_table and row > 0 and column+1 < size_table:
                for j in range(3):
                    for k in range(2):
                        if f'{row-j+1},{column+k}' not in player_decisions:
                            auto_complete.add(f'{row-j+1},{column+k}')
                if auto_complete == set():
                    True
                else:
                    actual_decision = auto_complete.pop()
                    row = int(actual_decision[0])
                    column = int(actual_decision[2])
            elif row+1 < size_table and column > 0 and column+1 < size_table:
                for j in range(2):
                    for k in range(3):
                        if f'{row+j},{column-k+1}' not in player_decisions:
                            auto_complete.add(f'{row+j},{column-k+1}')
                if auto_complete == set():
                    True
                else:
                    actual_decision = auto_complete.pop()
                    row = int(actual_decision[0])
                    column = int(actual_decision[2])
            elif row > 0 and column > 0 and column+1 < size_table:
                for j in range(2):
                    for k in range(3):
                        if f'{row-j},{column-k+1}' not in player_decisions:
                            auto_complete.add(f'{row-j},{column-k+1}')
                if auto_complete == set():
                    True
                else:
                    actual_decision = auto_complete.pop()
                    row = int(actual_decision[0])
                    column = int(actual_decision[2])
            elif row > 0 and column > 0:
                for j in range(2):
                    for k in range(2):
                        if f'{row-j},{column-k}' not in player_decisions:
                            auto_complete.add(f'{row-j},{column-k}')
                if auto_complete == set():
                    True
                else:
                    actual_decision = auto_complete.pop()
                    row = int(actual_decision[0])
                    column = int(actual_decision[2])
            elif row > 0 and column+1 < size_table:
                for j in range(2):
                    for k in range(2):
                        if f'{row-j},{column+k}' not in player_decisions:
                            auto_complete.add(f'{row-j},{column+k}')
                if auto_complete == set():
                    True
                else:
                    actual_decision = auto_complete.pop()
                    row = int(actual_decision[0])
                    column = int(actual_decision[2])
            elif row+1 < size_table and column > 0:
                for j in range(2):
                    for k in range(2):
                        if f'{row+j},{column-k}' not in player_decisions:
                            auto_complete.add(f'{row+j},{column-k}')
                if auto_complete == set():
                    True
                else:
                    actual_decision = auto_complete.pop()
                    row = int(actual_decision[0])
                    column = int(actual_decision[2])
            elif row+1 < size_table and column+1 < size_table:
                for j in range(2):
                    for k in range(2):
                        if f'{row+j},{column+k}' not in player_decisions:
                            auto_complete.add(f'{row+j},{column+k}')
                if auto_complete == set():
                    True
                else:
                    actual_decision = auto_complete.pop()
                    row = int(actual_decision[0])
                    column = int(actual_decision[2])
        hint=0
        if auto_complete == set() and hint == 0:
            if i == 0:
                switch = False
                while switch == False:
                    try:
                        row = int(input('Choose a row (0,1,2,...): '))
                        column = int(input('Choose a column (0,1,2,...): '))
                    except ValueError:
                        print('You can\'t choose letters or symbols')
                        continue
                    actual_decision = f'{row},{column}'
                    try:
                        fail_switch = table[row][column]
                    except:
                        print('Dont choose a cell that does not exist.')
                        continue
                    if actual_decision in player_decisions:
                        print('You cant choose the same point twice!')
                        continue
                    else:
                        switch = True
            elif actual_decision in player_decisions:
                switch = False
                while switch == False:
                    try:
                        row = int(input('Choose a row (0,1,2,...): '))
                        column = int(input('Choose a column (0,1,2,...): '))
                    except ValueError:
                        print('You can\'t choose letters or symbols')
                        continue
                    actual_decision = f'{row},{column}'
                    try:
                        fail_switch = table[row][column]
                    except:
                        print('Dont choose a cell that does not exist.')
                        continue
                    if actual_decision in player_decisions:
                        print('You cant choose the same point twice!')
                        continue
                    else:
                        switch = True
        player_decisions.add(actual_decision)
        hint = 0
        # Perdiste si entras aqui
        if table[row][column] == 1:
            print('YOU LOOSE')
            break
        # Se desbloquea la celda y te muestra el numero de minas dependiendo de tu posicion en el tablero
        else:
            if row+1 < size_table and row > 0 and column > 0 and column+1 < size_table:
                for j in range(3):
                    for k in range(3):
                        if table[row+j-1][column+k-1] == 1:
                            hint += table[row+j-1][column+k-1]
                ans_table[row][column] = f'{hint}'
            elif row+1 < size_table and row > 0 and column > 0:
                for j in range(3):
                    for k in range(2):
                        if table[row+j-1][column-k] == 1:
                            hint += table[row+j-1][column-k]                
                ans_table[row][column] = f'{hint}'
            elif row+1 < size_table and row > 0 and column+1 < size_table:
                for j in range(3):
                    for k in range(2):
                        if table[row+j-1][column+k] == 1:
                            hint += table[row+j-1][column+k]
                ans_table[row][column] = f'{hint}'
            elif row+1 < size_table and column > 0 and column+1 < size_table:
                for j in range(2):
                    for k in range(3):
                        if table[row+j][column+k-1] == 1:
                            hint += table[row+j][column+k-1]
                ans_table[row][column] = f'{hint}'
            elif row > 0 and column > 0 and column+1 < size_table:
                for j in range(2):
                    for k in range(3):
                        if table[row-j][column+k-1] == 1:
                            hint += table[row-j][column+k-1]
                ans_table[row][column] = f'{hint}'
            elif row > 0 and column > 0:
                for j in range(2):
                    for k in range(2):
                        if table[row-j][column-k] == 1:
                            hint += table[row-j][column-k]
                ans_table[row][column] = f'{hint}'
            elif row > 0 and column+1 < size_table:
                for j in range(2):
                    for k in range(2):
                        if table[row-j][column+k] == 1:
                            hint += table[row-j][column+k]
                ans_table[row][column] = f'{hint}'
            elif row+1 < size_table and column > 0:
                for j in range(2):
                    for k in range(2):
                        if table[row+j][column-k] == 1:
                            hint += table[row+j][column-k]
                ans_table[row][column] = f'{hint}'
            elif row+1 < size_table and column+1 < size_table:
                for j in range(2):
                    for k in range(2):
                        if table[row+j][column+k] == 1:
                            hint += table[row+j][column+k]
                ans_table[row][column] = f'{hint}'
            print()
            print(' ',tit_superior)
            print()
            n = 0
            for j in ans_table:
                print(f'{n}',j)
                n += 1
            print('-----------------------------------------------------------------------')
    # Si sales del for, ganaste (solo si no tocaste una mina)
    if table[row][column] != 1:
        print('Congratulations, you have won.')
    return table

print(f"""
Welcome to this MINESWEEPER
""")
# False switch para errores de inicio de la dificultad
u=False
while u==False:
    try:
        diff = input('Choose a difficulty from 1 to 3 (1 = easy, 3 = hard): ')
        if int(diff) != 1 and int(diff) != 2 and int(diff) != 3:
            print('Choose a number between 1, 2 and 3')
            continue
    except ValueError:
        print('Choose a number')
        continue
    u=True
hello = mine_game(diff)

for i in hello:
    print(i)
