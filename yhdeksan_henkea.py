import random
import unittest

runtest = 1
def yhdeksan_henkea(guess_test):
    lives = 9
    words = ['pizza', 'keiju', 'sorsa', 'kieli', 'paita', 'kirje', 
            'jalka', 'pyora', 'ankka', 'koivu', 'ahven', 'purje',
            'varsi', 'ruuvi', 'ruoka', 'ruusu', 'maito', 'lahde']
    if runtest == 0:
        secret_word = random.choice(words)
    if runtest == 1:
        secret_word = guess_test
        print(secret_word)
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
        print('Henkia jaljella: ' + heart_symbol * lives)
        guess = input(' Arvaa kirjain tai koko sana: ')
        if guess in secret_word:
            update_clue(guess, secret_word, clue)
        else:
            print('Vaarin. Menetit yhden hengen.')
            lives = lives - 1
            if lives == 0:
                print('Havisit! Salainen sana oli: ' + secret_word)
        if guess == secret_word:
            guessed_word_correctly = True
            if guessed_word_correctly:
                print('Voitit! Salainen sana oli: ' + secret_word)
                break

if runtest == 0:
    yhdeksan_henkea('')

class test_yhdeksan_henkea(unittest.TestCase):
    def test_yhdeksan_henkea_success(self):
        actual = yhdeksan_henkea('pizza')
