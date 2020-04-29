rom os import system as sys  # Operar en el terminal
#import timeit                 # Medir velocidad del codigo
from time import time as t    # Tiempo entre dos partes del codigo
#from secrets import choice    # Generar numeros aleatorios
#import string                 # Generar caracteres
import random                 # Generar pseudo random
# cd /home/jesusp/python_pruebas
#print(timeit.timeit('test1()', globals=globals(), number=10))
#os.system('clear')
sys('clear')

def mine_game(difficulty):
    if difficulty == '1':
        print('You have choosen EASY')
        size_table = 4
        num_minas = int(size_table*size_table/3.5)
    if difficulty == '2':
        print('You have choosen MEDIUM')
        size_table = 6
        num_minas = int(size_table*size_table/3.5)
    if difficulty == '3':
        print('You have choosen HARD')
        size_table = 8
        num_minas = int(size_table*size_table/3.5)
    minas = 0
    table = []
    ans_table = []
    ans_unit = []
    row = []
    for i in range(size_table):
        for j in range(size_table):
            if minas < num_minas:
                actual_mine = random.randrange(0,2)
                row.append(actual_mine)
                if actual_mine == 1:
                    minas += 1
            else:
                row.append(0)
            ans_unit.append('-')
        table.append(row)
        ans_table.append(ans_unit)
        row = []
        ans_unit = []
    for j in ans_table:
        print(j)
    random.shuffle(table)
    max_turns = (size_table*size_table)-num_minas
    player_decisions = set()
    #player_decisions.add(['',''])
    for i in range(max_turns):
        hint = 0
        switch = False
        while switch == False:
            row = int(input('Choose a row (0,1,2,...): '))
            column = int(input('Choose a column (0,1,2,...): '))
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
        if table[row][column] == 1:
            print('YOU LOOSE')
            break
        else:
            if row+1 < size_table and row > 0 and column > 0 and column+1 < size_table:
                hint += table[row+1][column]
                hint += table[row][column+1]
                hint += table[row-1][column]
                hint += table[row][column-1]
                # Esquinas
                hint += table[row-1][column-1]
                hint += table[row-1][column+1]
                hint += table[row+1][column-1]
                hint += table[row+1][column+1]
                ans_table[row][column] = f'{hint}'
            elif row+1 < size_table and row > 0 and column > 0:
                hint += table[row+1][column]
                hint += table[row-1][column]
                hint += table[row][column-1]
                # Esquinas
                hint += table[row+1][column-1]
                hint += table[row-1][column-1]
                ans_table[row][column] = f'{hint}'
            elif row+1 < size_table and row > 0 and column+1 < size_table:
                hint += table[row+1][column]
                hint += table[row][column+1]
                hint += table[row-1][column]
                # Esquinas
                hint += table[row-1][column+1]
                hint += table[row+1][column+1]
                ans_table[row][column] = f'{hint}'
            elif row+1 < size_table and column > 0 and column+1 < size_table:
                hint += table[row][column+1]
                hint += table[row][column-1]
                hint += table[row+1][column]
                # Esquinas
                hint += table[row+1][column-1]
                hint += table[row+1][column+1]
                ans_table[row][column] = f'{hint}'
            elif row > 0 and column > 0 and column+1 < size_table:
                hint += table[row][column+1]
                hint += table[row-1][column]
                hint += table[row][column-1]
                # Esquinas
                hint += table[row-1][column-1]
                hint += table[row-1][column+1]
                ans_table[row][column] = f'{hint}'
            elif row > 0 and column > 0:
                hint += table[row-1][column]
                hint += table[row][column-1]
                # Esquinas
                hint += table[row-1][column-1]
                ans_table[row][column] = f'{hint}'
            elif row > 0 and column+1 < size_table:
                hint += table[row-1][column]
                hint += table[row][column+1]
                # Esquinas
                hint += table[row-1][column+1]
                ans_table[row][column] = f'{hint}'
            elif row+1 < size_table and column > 0:
                hint += table[row+1][column]
                hint += table[row][column-1]
                # Esquinas
                hint += table[row+1][column-1]
                ans_table[row][column] = f'{hint}'
            elif row+1 < size_table and column+1 < size_table:
                hint += table[row+1][column]
                hint += table[row][column+1]
                # Esquinas
                hint += table[row+1][column+1]
                ans_table[row][column] = f'{hint}'
            for j in ans_table:
                print(j)
    print('Congratulations, you have won.')
    return table

print(f"""
Welcome to this MINESWEEPER
""")
diff = input('Choose a difficulty from 1 to 3 (1 = easy, 3 = hard): ')

hello = mine_game(diff)

for i in hello:
    print(i)
