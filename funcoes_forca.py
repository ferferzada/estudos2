from random import choice

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
selected_word = draw_word()


guess_word = ['_' for _ in selected_word]

errors = 0

found_word = False

while errors != 3 and not found_word:
    print(' '.join(guess_word))
    guess = handle_input()

