from random import choice

sort_list = ['moises', 'cajado', 'mar', 'porta', 'monitor']

selected_word = choice(sort_list)

guess_word = ['_' for _ in selected_word]

errors = 0

found_word = False

while errors != 3 and not found_word:
    print(' '.join(guess_word))
    guess = input('Informe seu Palpite: ')

    if len(guess)  == 1:
        if guess in selected_word:
            found_letter = False

            for i, letter in enumerate(selected_word):
                if guess  == letter:
                    guess_word[i] = letter
                    found_letter = True
                




