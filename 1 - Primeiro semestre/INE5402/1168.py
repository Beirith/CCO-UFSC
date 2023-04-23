n = int(input())
led = 0
for i in range(n):
    led = 0
    h = input()
    h = list(h)
    for i in range(len(h)):
        if h[i] == '2' or h[i] == '3' or h[i] == '5':
            led += 5
        if h[i] == '1':
            led += 2
        if h[i] == '4':
            led += 4
        if h[i] == '6' or h[i] == '9' or h[i] == '0':
            led += 6
        if h[i] == '7':
            led += 3
        if h[i] == '8':
            led += 7
    print("%d leds" % (led))