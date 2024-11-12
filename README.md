Na het volgen van verschillende basiscursussen Python wilde ik mijn opgedane kennis toepassen in een oefening. In deze oefening moesten de verschillende onderdelen van objectgeoriënteerd programmeren (OOP) terugkomen. Ik besloot een simulatie van een banksysteem te ontwikkelen, waarin je verschillende soorten rekeningen kunt beheren en de balans inzichtelijk kunt maken.

Tijdens het project vond ik het gebruik van staticmethod en classmethod het lastigst, omdat deze methoden anders werken dan reguliere instance-methoden. Door ze te implementeren heb ik echter meer inzicht gekregen in hun nut en toepassing binnen OOP. Dit project combineert diverse OOP-technieken en is een goede oefening in het bouwen van klassen en methoden.

- Rekening (Basisklasse)
- Spaarrekening (Afgeleide klasse)
- Betaalrekening (Afgeleide klasse)
- Gebruik van class methods, static methods, en inheritance.
OOP-technieken die zijn toegepast
1. Encapsulation (Insluiting)
   - Attributen zoals rekeningnummer, saldo, en krediet zijn onderdeel van de klassen en worden beheerd via methoden, wat de toegang tot deze data controleert.
2. Inheritance (Overerving)
 - Spaarrekening en Betaalrekening erven van de basisklasse Rekening. Hierdoor delen ze gemeenschappelijke attributen en methoden, zoals rekeningnummer en saldo.
3. Polymorphism (Polymorfisme)
 - De __str__-methoden zijn overschreven in zowel de Spaarrekening als Betaalrekening klassen. Dit geeft elk type rekening een eigen specifieke stringweergave.
4. Class Methods en Static Methods
 - @classmethod nieuw() geeft het aantal aangemaakte rekeningobjecten terug.
 - @staticmethod valideer() controleert of een bedrag geldig is (niet negatief) voor stortingen en opnames.
5. Data Hiding (Gegevensafscherming)
 - De attributen worden direct aangeroepen, maar je zou deze kunnen verbergen met een underscore _saldo voor meer bescherming, indien nodig.

Klassen en Functionaliteiten
Rekening (Basisklasse)
 - Attributen: rekeningnummer, saldo.
 - Methoden:
   - storten(stort): Voegt een bedrag toe aan het saldo na validatie.
   - opname(op): Neemt een bedrag op na controle.
   - __str__(): Geeft de huidige saldo-informatie weer.
Spaarrekening (Afgeleide klasse)
 -Extra attribuut: rente.
 - De __init__-methode past de rente toe op het saldo bij aanmaak.
 - Overschrijft __str__() om specifieke informatie over de spaarrekening te tonen.
Betaalrekening (Afgeleide klasse)
 - Extra attribuut: krediet.
 - Methode:
   - pot(bedrag): Controleert of het bedrag binnen de kredietlimiet valt voordat het wordt toegevoegd aan het saldo.
  - Statische methode control() om te valideren of het bedrag groter is dan het toegestane krediet.
