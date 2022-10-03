from math import comb
expr= "(x+1)^2"

def expand(expr):
    for cos in expr:
        if cos.isalpha():
            zmienna = cos
            break
    idnawias = expr.index('(')
    idnawias2 = expr.index(")")
    astr = expr[idnawias + 1:expr.index(zmienna)]
    bstr= expr[expr.index(zmienna) + 1:idnawias2]
    print(astr,bstr)
    if astr == '-':
        a = int(-1)
    elif astr=='':
        a=1
    else:
        a= int(astr)
    b = int(bstr)
    n = int(expr[expr.index('^') + 1:])
    wynik=''
    for i in range(n+1):
        wspolczynnik = comb(n,i)
        awykladnik = n-i
        bywykladnik = i
        przedzmienna = str(wspolczynnik*a**awykladnik*b**bywykladnik)
        pozmienna = "^"+str(awykladnik)
        if przedzmienna=="1":
            przedzmienna=''
        elif przedzmienna =='-1':
            przedzmienna ='-'

        if awykladnik==1:
            pozmienna =''
        elif awykladnik==0:
            pozmienna=''
            zmienna=''
            if przedzmienna=='':
                przedzmienna='1'
            elif przedzmienna =='-':
                przedzmienna='-1'
        czesc = przedzmienna+zmienna+pozmienna
        if przedzmienna=="":
            wynik +=czesc
        elif przedzmienna[0]=='-':
            wynik+=czesc
        elif i==0:
            wynik +=czesc
        else:
            wynik+="+"+czesc
    return wynik
print(expand(expr))

