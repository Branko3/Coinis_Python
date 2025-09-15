class Podkast :
    def __init__(self, naziv,br_pozitivni, br_negativni):
        self.naziv = naziv
        self.br_pozitivni = br_pozitivni
        self.br_negativni = br_negativni

def najgori_podkast(podkasti) :
    najgori_odnos = 0
    ime_podkasta = ''
    for podkast in podkasti :
        odnos = podkast.br_negativni / podkast.br_pozitivni
        if(odnos > najgori_odnos):
            najgori_odnos = odnos
            ime_podkasta = podkast.naziv
    print(ime_podkasta)

# espanol = Podkast("Español para principiantes", 1000, 10)
# filozofija = Podkast("Philophize This!", 500, 30)
# science = Podkast("Science VS. ", 600, 45)

# najgori_podkast([espanol, filozofija, science])


class Book :
    def __init__(self,naslov,autor,godina,broj_kopija) :
        self.naslov = naslov
        self.autor = autor
        self.godina = godina
        self.broj_kopija = broj_kopija

    def promijeniNaslov(self, naslov):
        self.naslov = naslov
    def promijeniAutora(self, autor):
        self.autor = autor
    def promijeniGodinu(self, godina):
        self.godina = godina
    def promijeniBroj_kopija(self, broj_kopija):
        self.broj_kopija = broj_kopija

    def getNaslov(self) :
        return self.naslov
    
    def getAutor(self) :
        return self.autor
    
    def getGodina(self) :
        return self.godina
    
    def getBrojKopija(self) :
        return self.broj_kopija
    
class Library :
    def __init__ (self, ime, listaKnjiga={}):
        self.ime = ime
        self.listaKnjiga = listaKnjiga

    def dodajKnjigu(self, knjiga) :    
        self.listaKnjiga.append(knjiga)

    def izbrisiKnjigu(self, knjiga):
        self.listaKnjiga.discard(knjiga)
    
    def getKnjiguPoNaslovu(self, naslov) :
        lista = []
        for knjiga in self.listaKnjiga:
            if(naslov in knjiga.getNaslov()) :
                lista.append(knjiga)
        return lista
    
    def getKnjiguPoAutoru(self, autor):
        lista = []
        for knjiga in self.listaKnjiga:
            if(autor in knjiga.getAutor()) :
                lista.append(knjiga)
        return lista

    def dostupneKnjige(self):
        return self.listaKnjiga


class Company:
    def __init__(self, name, area, balance, max_num_of_employees):
        self._name = name
        self._area = area
        self._employees = []
        self._balance = balance
        self._max_num_of_employees = max_num_of_employees

    def setName(self,name) :
        self.name = name
    def setArea(self,area) :
        self.area = area    
    def setBalance(self,balance) :
        if(balance > 0):
            self.balance = balance
    def setMaxNumOfEmployees(self,max_number_of_employees) :
        if(max_number_of_employees > 0) :  
            self.max_number_of_employees = max_number_of_employees

    def getBalance(self) :
        return self.balance
    
    def getName(self) :
        return self.name
    
    def getArea(self) :
        return self.area
    
    def getMaxNumberOfEmployees(self) :
        return self.max_number_of_employees
    
    def add_employee(self,employee) :
        if(len(self.employees) < self.max_number_of_employees) :
            self.employees.append(employee)
