#Account
class rekening:
    aantal = 0

    def __init__ (self, rekeningnummer, saldo):
        self.rekeningnummer = rekeningnummer
        self.saldo = saldo
        rekening.aantal += 1

    @classmethod
    def nieuw(cls):
        return cls.aantal

    @staticmethod
    def valideer(stort):
        return stort < 0

    def storten(self, stort):
        self.stort = stort
        if rekening.valideer(stort) == True:
            raise ValueError("je kunt niet een bedrag minder dan 0 storten")
        self.saldo += self.stort
        print(f"je hebt {self.stort} gestort")

    @staticmethod
    def valideer(op):
        return op < 0

    def opname(self, op):
        self.op = op
        if olivier.valideer(op) == True:
            raise ValueError ("Je kunt niet een negatief getal opnemen")
        elif self.op > self.saldo:
            raise ValueError ("niet genoeg belans")
        self.saldo -= self.op
        print(f"je hebt {self.op} opgenomen")

    def __str__(self):
        return f"het saldo van op de bankerekening is momenteel {self.saldo}"

class spaarrekening(rekening):
    def __init__ (self, rekeningnummer,saldo, rente):
        self.rente = rente
        super().__init__(rekeningnummer, saldo)
        self.saldo += (self.saldo/100 * rente)

    def __str__(self):
        return f"het spaarsaldo is {self.saldo}"

class betaalrekening(rekening):
    def __init__ (self, rekeningnummer, saldo, krediet):
        self.krediet = krediet
        super().__init__(rekeningnummer, saldo)

    @staticmethod
    def control(saldo, krediet, bedrag):
        return bedrag > saldo + krediet

    def pot(self, bedrag):
        if betaalrekening.control(self.saldo, self.krediet, bedrag) == True:
            raise ValueError(f"Je kunt maximaal {self.krediet}staan")
            self.saldo += bedrag
            return self.saldo

olivier = rekening("INGB008855686", 500)
loan = rekening("INGB008855644", 600)
Henry = betaalrekening("INGB008855686", 200,500 )

