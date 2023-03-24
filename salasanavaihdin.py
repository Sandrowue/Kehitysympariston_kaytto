import random
import string

def generate_password():
    nominit = ['pöytä', 'omena,', 'pyörä', 'ruusu', 'leppäkerttu',
    'kenkä', 'puhelin', 'radio', 'jauho', 'kynsi', 'vesi', 'kivi']

    adjektiivit = ['nopea', 'kiltti', 'iso', 'pimeä', 'tahmea', 'punainen',
    'hiljas', 'jännittävä', 'kylmä', 'tuulinen', 'komea', 'kevyt', 'kiero']
    
    while True:
        adjektiivi = random.choice(adjektiivit)
        nomini = random.choice(nominit)
        numero = str(random.randrange(10, 100))
        erikoismerkki = random.choice(string.punctuation)
        
        salasana = adjektiivi + nomini + numero + erikoismerkki

        print('salasanasi on: ' + salasana)
        return salasana

uusi_salasana = generate_password()
print(uusi_salasana)