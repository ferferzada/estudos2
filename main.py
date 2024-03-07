from random import choice

sort_list = ['moises', 'cajado', 'mar', 'porta', 'monitor']

selected_word = choice(sort_list)

blank_word  = []

print("_ " * len(selected_word))

errors = 0

found_word = False

found_char = []

while errors != 3 and not found_word :
    input_user = str(input('De um palpite'))
    if(len(input_user) > 1 and len(input_user) == len(selected_word)):
        print('DIGIRA CERTO EMBECIL')
        continue
    if(len(input_user) > 1):
        for i, char in selected_word:
            if char == input_user :




