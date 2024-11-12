# Account
class rekening:
    aantal = 0

    def __init__(self, rekeningnummer, saldo):
        if saldo < 0:
            raise ValueError("Het saldo kan niet negatief zijn.")
        self.rekeningnummer = rekeningnummer
        self._saldo = saldo
        rekening.aantal += 1

    @classmethod
    def nieuw(cls):
        return cls.aantal

    @staticmethod
    def valideer(bedrag):
        return bedrag < 0

    @property
    def geld(self):
        return self._saldo

    @geld.setter
    def geld(self, waarde):
        if waarde < 0:
            raise ValueError("Saldo kan niet negatief zijn.")
        self._saldo = waarde

    def storten(self, stort):
        if rekening.valideer(stort):
            raise ValueError("Je kunt niet een bedrag minder dan 0 storten.")
        self._saldo += stort
        print(f"Je hebt {stort} gestort")

    def opname(self, op):
        if rekening.valideer(op):
            raise ValueError("Je kunt niet een negatief bedrag opnemen.")
        elif op > self._saldo:
            raise ValueError("Niet genoeg balans.")
        self._saldo -= op
        print(f"Je hebt {op} opgenomen")

    def __str__(self):
        return f"Het saldo van de bankrekening is momenteel {self._saldo}"

class spaarrekening(rekening):
    def __init__(self, rekeningnummer, saldo, rente):
        if saldo < 0:
            raise ValueError("Het saldo kan niet negatief zijn.")
        if rente < 0:
            raise ValueError("De rente kan niet negatief zijn.")
        self.rente = rente
        super().__init__(rekeningnummer, saldo)
        self._saldo += (self._saldo / 100 * rente)

    def __str__(self):
        return f"Het spaarsaldo is {self._saldo} met een rente van {self.rente}%"

class betaalrekening(rekening):
    def __init__(self, rekeningnummer, saldo, krediet):
        if saldo < 0:
            raise ValueError("Het saldo kan niet negatief zijn.")
        if krediet < 0:
            raise ValueError("Het krediet kan niet negatief zijn.")
        self.krediet = krediet
        super().__init__(rekeningnummer, saldo)

    @staticmethod
    def control(saldo, krediet, bedrag):
        return bedrag > saldo + krediet

    def pot(self, bedrag):
        if betaalrekening.control(self._saldo, self.krediet, bedrag):
            raise ValueError(f"Je kunt maximaal {self.krediet} staan.")
        self._saldo += bedrag
        return self._saldo
