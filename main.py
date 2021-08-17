from random import randint as rd

user_input = str()
opponent_choice = str()
user_score, opponent_score = 0, 0

# Начало игры
while user_input != '0':
    user_input = input('Выбери камень (к), ножницы (н) или бумагу (б)\nЕсли хочешь закончить игру, напиши 0\n')

    # Компьютер выбирает случайный вариант
    opponent_choice = rd(1, 3)

    # Выход из игры
    if user_input == '0':
        break

    # Проверка на дурака
    elif user_input != 'к' and user_input != 'н' and user_input != 'б':
        print('Такого варианта нет.')

    # Ничья
    elif (user_input == 'к' and opponent_choice == 1) or (user_input == 'н' and opponent_choice == 2) or (user_input == 'б' and opponent_choice == 3):
        if opponent_choice == 1:
            print('Ничья! Компьютер выбрал камень.')
            print(f'Счет: игрок - {user_score}, компьютер - {opponent_score}\n')
        elif opponent_choice == 2:
            print('Ничья! Компьютер выбрал ножницы.')
            print(f'Счет: игрок - {user_score}, компьютер - {opponent_score}\n')
        else:
            print('Ничья! Компьютер выбрал бумагу.')
            print(f'Счет: игрок - {user_score}, компьютер - {opponent_score}\n')

    # Победа игрока
    elif (user_input == 'к' and opponent_choice == 2) or (user_input == 'н' and opponent_choice == 3) or (user_input == 'б' and opponent_choice == 1):
        user_score += 1
        if opponent_choice == 1:
            print('Победа! Компьютер выбрал камень.')
            print(f'Счет: игрок - {user_score}, компьютер - {opponent_score}\n')
        elif opponent_choice == 2:
            print('Победа! Компьютер выбрал ножницы.')
            print(f'Счет: игрок - {user_score}, компьютер - {opponent_score}\n')
        else:
            print('Победа! Компьютер выбрал бумагу.')
            print(f'Счет: игрок - {user_score}, компьютер - {opponent_score}\n')

    # Победа компьютера
    else:
        opponent_score += 1
        if opponent_choice == 1:
            print('Поражение. Компьютер выбрал камень.')
            print(f'Счет: игрок - {user_score}, компьютер - {opponent_score}\n')
        elif opponent_choice == 2:
            print('Поражение. Компьютер выбрал ножницы.')
            print(f'Счет: игрок - {user_score}, компьютер - {opponent_score}\n')
        else:
            print('Поражение. Компьютер выбрал бумагу.')
            print(f'Счет: игрок - {user_score}, компьютер - {opponent_score}\n')
