from random import choice
errors = 0

found_word = False

def draw_word() -> str:
    sort_list = ['moises', 'cajado', 'mar', 'porta', 'monitor']
    return choice(sort_list)

def handle_input() ->str:
    guess = input('Informe seu Palpite: ')
    return guess.lower()

def validate_guess(guess:str)->bool:
    if not guess.isalpha():
        print('GEME MEU NOME')
        return False
    
    if len(guess) == 1 and guess in guess_word:
        print('falando dudu')
        return False
    
    return True

def check_guess(guess:str):
    global found_word
    if len(guess)  == 1 and guess in selected_word:
        for i, letter in enumerate(selected_word):
            if guess  == letter:
                guess_word[i] = letter
       
        found_word = "_" not in guess_word
    elif guess == selected_word:
        found_word = True
    else:
        show_error()

   

def show_error():
    global errors 
    errors += 1
    print("Palpite incorreto")

selected_word = draw_word()


guess_word = ['_' for _ in selected_word]



while errors != 3 and not found_word:
    print(' '.join(guess_word))
    guess = handle_input()

    if not validate_guess(guess):
        continue
    check_guess(guess)


if found_word:
    print('Parabens cabaço!')
else:
    print(f'NUM ACERTOU CABAÇO a áçabra é {selected_word}')
