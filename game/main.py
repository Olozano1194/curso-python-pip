import random

def choose_options():
    option = ('piedra', 'papel', 'tijera')

    user = input('Digite: piedra, papel o tijera: ').lower()

    aleatorio = random.choice(option)

    if not user in option:
        print('Opción invalida')
        #continue
        return None, None
    
    computer_option = aleatorio

    print('User option =>', user)
    print('Computer_option =>', computer_option)

    return user, computer_option

def check_rules(user, computer_option, user_wins, computer_wins):
    if user == computer_option:
        print('Empate')

    elif (user == 'piedra' and computer_option == 'tijera') or (user == 'papel' and computer_option == 'piedra') or (user == 'tijera' and computer_option == 'papel'):
        print(f'El jugador gano con {user}')
        user_wins += 1

    else:
        print(f'Perdio, gano la computadora, {computer_option}')
        computer_wins += 1
    return user_wins, computer_wins 

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
    
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 5)

        print('computer_wins', computer_wins)
        print('user_wins', user_wins)
    
        rounds += 1

        user, computer_option = choose_options()

        user_wins, computer_wins = check_rules(user, computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print('*' * 10)
            print('El ganador es la computadora')
            break
        if user_wins == 2:
            print('*' * 10)
            print('El ganador es el usuario')
            break

run_game()
