s = 'Ala ma kota'
b = b'Ala ma kota'
l = [1, 2, "pies"]
k = (3, 4, "kot")

s[-5]

#minusowe elementy to liczymy index od końca

s[2:4]

#slice - bierzemy zakres od 2-4, ale 4 nie wchodzi w zakres
s[:8]
s[8:]
s[::-1] #od końca
s[::2] #co drugi element

lis = 10 * l #10 razy powtórzone elementy listy

#set jest nieiterowalny, bo nie mają kolejności

"z" in s #zwraca True lub False w zależności czy się zawiera czy nie

#jak chcemy zapisać polskie znaki, to robimy .endcode('utf-8)
#w print znak końca linii jako end = ""
#po przecinku rozdziela się spacją
#.split() rozdziela stringi i zwraca listę
#.join rozdziela elementy listy tym co jest przed kropką
#strip usuwa 
#zip jak pair w c++ - jest on iteratorem
