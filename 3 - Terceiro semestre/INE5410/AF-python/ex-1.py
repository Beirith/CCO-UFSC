from time import sleep
from random import randint
from threading import Thread, Lock, Condition

def produtor():
    global buffer
    global n_item

    for i in range(5):
        sleep(randint(0, 2))
        item = 'item ' + str(n_item)

        with lock:
            while len(buffer) == tam_buffer:
                print('>>> Buffer cheio. Produtor irá aguardar.')
                lugar_no_buffer.wait()
            
            n_item += 1
            buffer.append(item)
            print('Produzido %s (há %i itens no buffer)' % (item, len(buffer)))
            item_no_buffer.notify()


def consumidor():
    global buffer

    for i in range(5):
        with lock:
            while len(buffer) == 0:
                print('>>> Buffer vazio. Consumidor irá aguardar.')
                item_no_buffer.wait()

            item = buffer.pop(0)
            print('Consumido %s (há %i itens no buffer)' % (item, len(buffer)))
            lugar_no_buffer.notify()
            
        sleep(randint(0, 2))

buffer = []
n_item = 0

tam_buffer = 5
lock = Lock()
lugar_no_buffer = Condition(lock)
item_no_buffer = Condition(lock)

produtor1 = Thread(target=produtor)
consumidor1 = Thread(target=consumidor)

produtor2 = Thread(target=produtor)
consumidor2 = Thread(target=consumidor)

produtor1.start()
consumidor1.start()

produtor2.start()
consumidor2.start()

produtor1.join()
consumidor1.join()

produtor2.join()
consumidor2.join()