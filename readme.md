# Arbeidskrav 1 - Python

Navn: Steinar Martinussen

### Generelt om KI bruk:
Jeg har satt opp Claude med en Skill spesifikt for 
dette studiet. Den er oppfordret til å ikke komme med kodeforslag
uten at jeg spesifikt ber om det. 
Ved noen tilfeller i starten av Oppgave 1,
har den kommet med forslag med generisk kode for å løse en utfordring, men jeg 
har ved vært tilfelle kommenteret på dette, og modellen har korrigert sine egne 
retningslinjer ved flere tilfeller. 

Jeg gir den min kode, og den stiller spørsmål tilbake som:
"Hva hvis.."
"Har du tenkt på..."
"Har du testet med..."<funksjon>, se om du finner den"

Jeg laster i tillegg opp slides fra timene, samt oppgavene
som kontekst i form av .pdf / .md til et Claude CoWork prosjekt


## Oppgave 1
#### KI bruk relevant for oppgave:
Ingen kode kopiert, men forslag om å bruke divmod(),
er benyttet for tidskalkulering
https://docs.python.org/3/library/functions.html#divmod

Diskusjoner om splitting av funksjoner kan ha noe for seg eller ei.
Gjennomlest av Claude ved ferdig arbeid, kommentarer rundt PEP8 formattering (antall linjeskift etc)
og forslag om bruk av `divmod`

Forslag om å slå opp Try: og Except: for bedre logikk i kvalitetssikring av input av `int`

## Oppgave 2
#### KI bruk relevant for oppgave:
- Forslag om å lage en variabel for type annotation for å unngå mange repetisjoner kom ved gjennomlesing av oppgave-2.py
- For meny 5, byttet fra en separat funksjon for key, til lambda.
- Konseptuelle diskusjoner gjennom løsing av oppgavene, som har vist generiske forslag eller forklaring av funksjoner
som jeg har kunnet adaptere til bruk for løsning.

Gjennomføring:
Jeg valgte å lage en list med dict, da man da har en navngitt nøkkel å gjøre oppslag
mot. Samtidig vil det være mulig fremtiden å legge til nye felt med nye navn og
koden vil være mer oversiktlig og selvdokumenterende. 

Når jeg legger inn type annotations viser det også en begrensning med å velge
fleksibilitet. 

```study_sessions: list[dict[str, str | int]] = [```

sier bare at verdiene er enten `str` eller `int` inni der, men mangler mulighet for kvalitetssikring
der programmet vet at `duration_minutes` skal være `int`

Et eksempel på dette er at jeg har lagt inn kontroll selv, men med type annotation str | int
får jeg en advarsel i PyCharm. Jeg vet at programmet leverer korrekte verdier, men programmet selv
kan ikke garantere riktig resultat. 

Advarslene er:
`No overload of 'sum' matches the arguments. Argument types: (Generator[str | int, Any, None]). Expected one of: (iterable: Iterable[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, 0] | bool]), (iterable: Iterable[_SupportsSumNoDefaultT])`
`Member 'int' of 'str | int' does not have attribute 'lower'`

Dette kan gjerne løses med moduler som `typing` -> `TypedDict` eller `Pydantic`

Leste om sorted() her, som også gav meg tips om hvordan utarbeide
en `lambda` funksjon for sorteringskriterie. Lambda har jeg lært om tidligere og 
leste også her om metoden. 
https://docs.python.org/3.14/howto/sorting.html#key-functions
I utgangspunktet tenkte jeg å lage en egen funksjon som kunne gi
verdi til `key=`

Endte opp med et par hjelpefunksjoner for å kvalitetssikre input.
