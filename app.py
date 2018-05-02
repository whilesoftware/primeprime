f = open('data/primes.txt', 'r')

n = 0
while True:
    l = f.readline()
    n = n + 1
    print(l, end='')
    if (n > 10):
        break
