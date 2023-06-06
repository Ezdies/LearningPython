from threading import Thread

panstwa = ['Polska', 'Niemcy', 'Szwecja', 'Islandia', 'Indie', 'Japonia', 'Tanzania', 'Kanada', 'Australia', 'Kolumbia']

def w_stolica(i):
    print()

threads = [Thread(target=w_stolica, args=(p,)) for p in panstwa]

for w in threads:
    w.start()

for w in threads:
    w.join()