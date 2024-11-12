
Hier is een beschrijving voor je README.md bestand, inclusief de nadruk op de OOP-technieken die je hebt toegepast:

Bankrekening Project
Dit project bevat een eenvoudige simulatie van verschillende soorten bankrekeningen in Python, waarbij gebruik wordt gemaakt van objectgeoriënteerde programmeertechnieken (OOP). Het bevat klassen en methoden voor een standaard rekening, spaarrekening en betaalrekening, elk met hun eigen functionaliteiten.

Inhoud
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
