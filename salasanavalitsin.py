import random
import string

def generate_password():
    nominit = ['pöytä', 'tuoli', 'omena,', 'päärynä', 'pyörä', 'ruuvi', 
               'ruusu', 'neilikka', 'leppäkerttu', 'perhonen',
               'kenkä', 'sukka', 'puhelin', 'kello', 'radio', 'telkkari', 'jauho', 
               'jyvä', 'kynsi', 'tukka', 'vesi', 'öljy', 'kivi', 'puurunko']

    adjektiivit = ['nopea', 'hitas', 'kiltti', 'tuhma', 'iso', 'pieni', 'pimeä',
                   'vaalea', 'tahmea', 'liukas', 'punainen', 'sininen',
                   'hiljas', 'äänekäs', 'jännittävä', 'tylsä', 'kylmä', 'lämmin', 'tuulinen', 
                   'tyyni', 'komea', 'ruma', 'kevyt', 'painava', 'kiero', 'suora']
    
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

# Testit
