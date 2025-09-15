
def stanje(temp) : 
    if(temp > 0 and temp < 100): 
        return "tecno"
    elif(temp <= 0 and temp > -100): 
        return "cvrsto"
    else : 
        return "gasovito"


# def krug(x, y) :




def narcis(broj) :
    novi = broj
    temp = 0
    len = 0
    while(novi > 0) :
        novi //= 10
        len+=1
    novi = broj
    while(novi > 0) :
        mod = novi % 10
        temp+= mod ** len
        novi //= 10

    if (temp == broj) :
        return "DA"
    else :
        return "NE"
    

def razbijanje(niz, broj) : 
    lista = []
    i = 0
    while(i + broj < len(niz)) :
        lista.append(niz[i:i+broj])
        i+=broj
    
    if(i < len(niz)) :
        fali = broj - (len(niz) - i)
        print(fali)
        lista.append(niz[i:] + fali*'*')

    return lista
