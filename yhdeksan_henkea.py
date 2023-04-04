import random

lives = 9
words = ['pizza', 'keiju', 'sorsa', 'kieli', 'paita', 'kirje', 
         'jalka', 'pyörä', 'ankka', 'koivu', 'ahven', 'purje',
         'varsi', 'ruuvi', 'ruoka', 'ruusu', 'maito', 'lähde']
secret_word = random.choice(words)
clue = list('?????') 
heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print('Henkiä jäljellä: ' + heart_symbol * lives)
    guess = input(' Arvaa kirjain tai koko sana: ')
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Väärin. Menetit yhden hengen.')
        lives = lives - 1
        if lives == 0:
            print('Hävisit! Salainen sana oli: ' + secret_word)
    if guess == secret_word:
        guessed_word_correctly = True
        if guessed_word_correctly:
            print('Voitit! Salainen sana oli: ' + secret_word)
            break