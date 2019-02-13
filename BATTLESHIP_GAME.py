def clear_board_A(): #pole gracza A
    row = ['?' for cols in range(10)]
    field_A = [row[:] for rows in range(10)] #nazwa zmiennej nic nie mowi
    return field_A
ocean_A = clear_board_A()

def clear_board_B(): #pole gracza B      
    row = ['?' for cols in range(10)]
    field_B = [row[:] for rows in range(10)] 
    return field_B
ocean_B = clear_board_B()
#^^^niepotrzebne powtorzenie funkcji^^^

def shoot_board_A(): #pole do strzelania gracza B
    row = ['~' for cols in range(10)]
    field_A = [row[:] for rows in range(10)] #nazwa zmiennej nic nie mowi
    return field_A
battlefield_A = shoot_board_A()

def shoot_board_B(): #pole do strzelania gracza A
    row = ['~' for cols in range(10)]
    field_B = [row[:] for rows in range(10)]
    return field_B
battlefield_B = shoot_board_B()
#^^^niepotrzebne powtorzenie funkcji^^^

def print_board(board): #drukowanie pól w ładnej postaci 10x10
    for row in board:
        print (" ".join(row))

def column(orient): #wybór kolumny przez gracza #zmienic nazwe funkcji na bardziej zrozumiala np. check_column_value
    while True:
        x = input("Choose column: ")
        col = int(x) - 1
        if 0 <= col < 10 and int(x)+ss<11 and orient == 'h': # nie wiadomo co to 'ss'
            return col
        elif 0 <= col < 10 and int(x)+ss<11+ss and orient == 'v': # zamiast '11' uzywamy zmiennej 'WIELKOSC_PLANSZY = 10'
            return col
        else:
            print('You cannot place the ship over the edge of the board.')

def row(orient): #wybór wiersza przez gracza #zmienic nazwe funkcji na bardziej zrozumiala np. check_row_value
    while True:
        y = input("Choose row: ")
        row = int(y) - 1
        if 0 <= row < 10 and int(y)+ss<11 and orient == 'v': # niew wiadomo co to 'ss'
            return row
        elif 0 <= row < 10 and int(y)+ss<11+ss and orient == 'h':
            return row
        else:
            print('You cannot place the ship over the edge of the board.')
#^^^mozna pomylec czy polaczenie tych funkcji w jedna ma sens^^^
# lepiej nie uzywac "while True". zamiast 'True' wpisac zmienna ktora okresla ze dane sa poprawne

def orientation(): #wybór kierunku statku #zmienic nazwe funkcji na bardziej zrozumiala np. check_ship_orientation
    while True:
        orient = input("Choose orientation('h' for horizontal or 'v' for vertical): ")
        if orient == 'h': 
            return orient
        elif orient == 'v':
            return orient
        else:
            print('No such orientation.') 

def print_battleships_list():
    battleships_list = ['1. "Aircraft Carrier" - size 4',
                            '2. "Battleship" - size 4',
                            '3. "Submarine" - size 3',
                            '4. "Destroyer" - size 3',
                            '5. "Patrol Boat" - size 2',
                            '6. "Nie moglismy wymyslic nazwy Boat" - size 2']
    print('\n')
    print('Battleships list: \n')
    print('\n'.join(battleships_list))
    print('\n')

ships_numbers_A = ['1','2','3','4','5','6'] #ta lista sie zmniejsza gdy gracz A ustawi statek'''
ships_numbers_B = ['1','2','3','4','5','6'] #ta lista sie zmniejsza gdy gracz B ustawi statek"""
def ship_size(): #wybór wielkości statku
    while True:
        ships = {"Aircraft Carrier": 4, #zmienic nazwe zmiennej na wielkosc_statku 
                    "Battleship": 4,
                    "Submarine": 3,
                    "Destroyer": 3,
                    "Patrol Boat": 2,
                    "Nie moglismy wymyslic nazwy Boat":2} #pomylec nad polaczeniem w jeden slownik
        battleships = { 1:"Aircraft Carrier",
                        2:"Battleship",
                        3:"Submarine", 
                        4:"Destroyer",
                        5:"Patrol Boat",
                        6:"Nie moglismy wymyslic nazwy Boat"}
        print_battleships_list()
        if player == 1:
            a=int(input('Write ship number to choose: ')) 
            #sprobowac zrobic jedna funkcje ktora w zaleznosci od gracza zmienia liste A lub liste B'''
            if str(a) in ships_numbers_A:
                ship_s= ships[battleships[a]]
                ships_numbers_A.remove(str(a))
                return ship_s
            elif ships_numbers_A == []: #lista do ograniczenia liczby statkow
                print('All ships placed.')
                break
            else:
                print('\nShip placed already. Choose another ship.')
        if player == 2:
            a=int(input('Write ship number to choose: '))
            if str(a) in ships_numbers_B:
                ship_s= ships[battleships[a]]
                ships_numbers_B.remove(str(a))
                return ship_s
            elif ships_numbers_B == []:
                print('All ships placed.')
                break
            else:
                print('Ship placed already. Choose another ship.')

ship=[] #zmienic nazwe listy na koordynaty_punktow_statku
def ship_coordinates(ship_size): #stworzenie listy z koordynatami wszystkich części statku    
    coordinates=[co,ro] 
    for i in range(ship_size):
        ship.append(coordinates)    
        if orient=='h':
            coordinates=[coordinates[0]+1,coordinates[1]]
        elif orient=='v':
            coordinates=[coordinates[0],coordinates[1]+1]
    return ship

COORD_Y = 1
COORD_X = 0

def ship_checker(): #sprawdzenie czy nowo ustawiany statek nie nachodzi na inne statki    
    l = [] #po co stworzylem ta liste?
    for i in ship:
        if ocean[i[COORD_Y]][i[COORD_X]]=='?':
            l.append('b')
            continue
        else:
            print('Cannot place ship. You tried to place on another ship.')
            break
    if len(l) == len(ship):
        return True
    else: 
        return False

def print_ship(): #umieszczanie statku na planszy
    for i in ship:
        ocean[i[1]][i[0]]='#'

player_1_HP = ['hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp']
player_2_HP = ['hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp','hp']

def shot(x, y, player):  # Replacing question marks f
    x = int(input("Which column? "))
    y = int(input("Which row?"))
    col = x - 1
    row = y - 1
    if player == 1:
        if 0 > x > 11 and 0 > y > 11:
            return False
        else:
            if ocean[row][col] == "#":
                print("Hit!")
                ocean[row][col] = "X"
            elif ocean[row][col] == "?":
                print("The bullet made the water splash!")
                ocean[row][col] = "O"
            elif ocean[row][col] == "O" or ocean[row][col] == "X":
                print("You've already shot here, what a waste!")
    elif player == 2:
        if 0 > x > 11 and 0 > y > 11:
            return False
        else:
            if ocean[row][col] == "#":
                print("Hit!")
                ocean[row][col] = "X"
            elif ocean[row][col] == "?":
                print("The bullet made the water splash!")
                ocean[row][col] = "O"
            elif ocean[row][col] == "O" or ocean[row][col] == "X":
                print("You've already shot here, what a waste!")

print('\n\nPLAYER 1 TURN\n\n')
print('SHIPS SETTING\n\n')
player=1
ocean=ocean_A
print_board(ocean)
for i in range(6):
        ss = ship_size()
        orient = orientation()
        co = column(orient)
        ro = row(orient)
        ship = []
        ship_coord = ship_coordinates(ss) #polaczyc w jedna ustawianie statku w zaleznosci od gracza
        sc = ship_checker()
        if sc == True:
            print_ship()
            print_board(ocean)
        else:
            continue

print('\n\nPLAYER 2 TURN\n\n')
print('SHIPS SETTING\n\n')
player=2
ocean=ocean_B
print_board(ocean)
for i in range(6):
        ss = ship_size()
        orient = orientation()
        co = column(orient)
        ro = row(orient)
        ship = []
        ship_coord = ship_coordinates(ss)
        sc = ship_checker()
        if sc == True:
            print_ship()
            print_board(ocean)
        else:
            continue

