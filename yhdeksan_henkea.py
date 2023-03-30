import random

lives = 9
words = ['pizza', 'keiju', 'sorsa', 'kieli', 'paita', 'kirje', 
         'jalka', 'pyörä', 'ankka', 'koivu', 'ahven', 'purje']
secret_word = random.choice(words)
clue = list('?????') 
heart_symbol = u'\u2764'
guessed_word_correctly = False