import multiprocessing

def rotina1():
    for i in range(50):
        print("1 " + str(i))

def rotina2():
    for i in range(50):
        print("2 " + str(i))


def main():
    processo1 = multiprocessing.Process(target=rotina1)
    processo2 = multiprocessing.Process(target=rotina2)

    processo1.start()
    processo2.start()
    processo1.join()
    processo2.join()

if __name__ == '__main__':
    main()
