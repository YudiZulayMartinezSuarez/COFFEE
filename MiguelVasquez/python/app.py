#sadsasdasd
import random
import string

i = 0

def id_generator(size=6, chars=string.ascii_uppercase):
   return ''.join(random.choice(chars) for _ in range(size))

#print(id_generator())
while True:
    search = id_generator()
    i = i + 1
    print(search,'[!]' ,i)
    if search == 'MIGUEL':
        exit()
