import sys
import requests
from random import seed
from random import randint

def validate_room(ini, fim):
    for _ in range(ini, fim):
        link = 'https://playstation-test.webex.com/playstation-test/nobrowser.php?AT=JM&MK={0}'
        rnd = randint(ini, fim)
        filled_link = link.format(rnd)
        r = requests.get(filled_link)
        print(rnd)
        print(r.status_code)
        print(r.text)
        if (r.text == 'InvalidClientType'):
            with open('salas.txt', 'a') as f:
                f.write(str(rnd))
                f.write('\n')
        print(100*'-')

if __name__ == '__main__':
    seed(1)
    validate_room(int(sys.argv[1]), int(sys.argv[2]))
