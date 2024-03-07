from random import choice

sort_list = ['moises', 'cajado', 'mar', 'porta', 'monitor']

selected_word = choice(sort_list)

guess_word = ['_' for _ in selected_word]

errors = 0

found_word = False

while errors != 3 and not found_word:
    print(' '.join(guess_word))
    guess = input('Informe seu Palpite: ')
    guess = guess.lower()

    if not guess.isalpha():
        print('Você deve informar uma letra ou uma palavra')
        continue



    if len(guess)  == 1:
        if guess in guess_word:
            print("VOCÊ JA MAMA")
            continue
        
        if guess in selected_word:
            for i, letter in enumerate(selected_word):
                if guess  == letter:
                    guess_word[i] = letter
        else:
            print("Palpite incorreto")
            errors +=1

        if "_" not in guess_word:
            found_word = True
    else:
        if guess == selected_word:  
            found_word = True
        else:
            errors += 1
            print("Palpite incorreto")

if found_word:
    print('Parabens cabaço!')
else:
    print(f'NUM ACERTOU CABAÇO a áçabra é {selected_word}')



