from time import sleep
from random import randint
from threading import Thread, Lock, Condition

def produtor():
    global buffer
    global n_item

    for i in range(5):
        sleep(randint(0, 2))

        with lock:
            if len(buffer) == tam_buffer:
                print('>>> Buffer cheio. Produtor irá aguardar.')
                lugar_no_buffer.wait()

            item = 'item ' + str(n_item)
            n_item += 1
            buffer.append(item)
            print('Produzido %s (há %i itens no buffer)' % (item, len(buffer)))
            item_no_buffer.notify()


def consumidor():
    global buffer

    for i in range(5):
        with lock:
            if len(buffer) == 0:
                print('>>> Buffer vazio. Consumidor irá aguardar.')
                item_no_buffer.wait()

            item = buffer.pop(0)
            print('Consumido %s (há %i itens no buffer)' % (item, len(buffer)))
            lugar_no_buffer.notify()
            
        sleep(randint(0, 2))

buffer = []
n_item = 0

produtores = []
consumidores = []

tam_buffer = 5
lock = Lock()
lugar_no_buffer = Condition(lock)
item_no_buffer = Condition(lock)

for i in range(2):
    produtores.append(Thread(target=produtor))
    consumidores.append(Thread(target=consumidor))

    produtores[i].start()
    consumidores[i].start()
  
for i in range(2):
    produtores[i].join()
    consumidores[i].join()