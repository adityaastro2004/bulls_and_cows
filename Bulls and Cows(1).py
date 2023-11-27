import random


def generate_number():
    while True:
        number = random.sample(range(10), 4)
        if number[0] != 0:
            return ''.join(map(str, number))


def play_game(secret_number):
    chances = 0

    while True:
        user_input = input('Guess the number: ')

        if not user_input.isdigit() or len(user_input) != 4:
            print('Please enter a valid 4-digit number.')
            continue

        chances += 1
        bulls = sum(user_digit == secret_digit for user_digit, secret_digit in zip(user_input, secret_number))
        cows = sum(user_digit in secret_number and user_digit != secret_digit for user_digit, secret_digit in
                   zip(user_input, secret_number))

        if bulls == 4:
            print(f'Congratulations!! You guessed correctly in {chances} chances.')
            play_again = input('If you want to play again, press "1". Otherwise, press any other key: ')
            if play_again != '1':
                break
            else:
                secret_number = generate_number()
                chances = 0
        else:
            print(f'Your guessed number has {bulls} bulls and {cows} cows.')


def main():
    print('BULLS AND COWS GAME')
    print('RULES:')
    print('1) Guess a 4-digit number.')
    print('2) Bulls: Right digit in the right place.')
    print('3) Cows: Right digit, but in the wrong place.')
    print('4) All digits must be different.')
    print()

    secret_number = generate_number()
    play_game(secret_number)


if __name__ == "__main__":
    main()
