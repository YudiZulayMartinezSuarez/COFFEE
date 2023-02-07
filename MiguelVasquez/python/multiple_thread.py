#Path: /Documents/MiguelVasquez/Python
#threads
from threading import Thread
from time import sleep, perf_counter
#sadsasdasd
import random
import string

#i = 0

def id_generator(size=6, chars=string.ascii_uppercase):
   return ''.join(random.choice(chars) for _ in range(size))
   
start_time = perf_counter()
end_time = perf_counter()

def search():
    i = 0
    while True:
        search = id_generator()
        sleep(0.01)
        i = 1 + i
        print(search,'[!]' ,i)
        if search == 'MIGUEL':
            exit()

t1 = Thread(target=search)
t2 = Thread(target=search)

t1.start()
t2.start()

t1.join()
t2.join()
print(f'Tomo {end_time- start_time: 0.2f} segundo(s) para completar')

#RESULTS: NOTHING AS EXPECTED-