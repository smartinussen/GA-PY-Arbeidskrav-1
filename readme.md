# Arbeidskrav 1 - Python

Navn: Steinar Martinussen

### Generelt om KI bruk:
Jeg har satt opp Claude med en Skill spesifikt for 
dette studiet. Den er oppfordret til å ikke komme med kodeforslag
uten at jeg spesifikt ber om det. 
Ved noen tilfeller i starten av Oppgave 1,
har den kommet med forslag med generisk kode for å løse en utfordring, men jeg 
har ved hvert tilfelle kommenteret på dette, og modellen har korrigert sine egne 
retningslinjer ved flere tilfeller. 

Jeg gir den min kode, og den stiller spørsmål tilbake som:
"Hva hvis.."
"Har du tenkt på..."
"Har du testet med..."<funksjon>, se om du finner den"

Jeg laster i tillegg opp slides fra timene, samt oppgavene
som kontekst i form av .pdf / .md til et Claude CoWork prosjekt

Claude har lest gjennom kodefiler og dokumentasjon før innlevering. Skrivefeil, og manglende
type annotations er rettet etter dette.
---
#### Generelt om innleveringen:
Innleveringen kommer med .venv innstillinger med krav om Python >=3.14, samt at jeg også benytter Ty og Ruff for
kvalitetskontroll. I prosjektinnstillingene er Ruff bare satt med krav om lik eller nyere enn versjon 0.16.6, men 
for øyeblikket har jeg pinnet Ty med eksakt versjon, da denne er i Beta og muligens har breaking changes i hver eneste
nye versjon. Kjenner til andre verktøy, men har valgt å gå all-in på Astral sine Rust baserte assistanse verktøy.
UV spesielt gjør livet lettere.


## Oppgave 1

Kjør program med: `uv run oppgave-1.py`

### KI bruk relevant for oppgave:
Ingen kode kopiert, men forslag om å bruke divmod(),
er benyttet for tidskalkulering
https://docs.python.org/3/library/functions.html#divmod

Diskusjoner om splitting av funksjoner kan ha noe for seg eller ei.
Gjennomlest av Claude ved ferdig arbeid, kommentarer rundt PEP8 formattering (antall linjeskift etc)
og forslag om bruk av `divmod`

Forslag om å slå opp Try: og Except: for bedre logikk i kvalitetssikring av input av `int`



## Oppgave 2

Kjør program med: `uv run oppgave-2.py`

### KI bruk relevant for oppgave:
- Forslag om å lage en variabel for type annotation for å unngå mange repetisjoner kom ved gjennomlesing av oppgave-2.py
- For meny 5, byttet fra en separat funksjon for key, til lambda.
- Konseptuelle diskusjoner gjennom løsing av oppgavene, som har vist generiske forslag eller forklaring av funksjoner
som jeg har kunnet adaptere til bruk for løsning.
- Spurte om hjelp til å fikse en utfordring hvor min .gitignore file virker inaktiv
Prompt: "I have a side question. It seems that in this Pycharm project my .gitignore file in the project root is 
disregarded. I have put in the .idea/ folder in .gitignore but the Git commit always includes them anyway"

Fikk følgende kommandoer:
`git ls-files .idea/` - viser filer som er tracket av Git
`git rm -r --cached .idea/` - Fjerner tracking uten å slette

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

Advarslene er (var - Ble korrigert i siste utgave av Pycharm):
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

## Oppgave 3

Kjør program med: `uv run oppgave-3.py`

### KI bruk relevant for oppgave
- Har spurt om time: var en gyldig type-annotation for en funksjon

Kjør program med: `uv run oppgave-3.py`

Her har jeg hentet inn funksjoner fra datetime biblioteket, og klart
meg med `date, datetime, time, timedelta`.  
Jeg begynte med feil `time` fra stdlib, før jeg fant datetime. 
Dokumentasjonens tittel: `datetime — Basic date and time types`

Dokumentasjonens nettside: https://docs.python.org/3/library/datetime.html#datetime.datetime.now
Har også benyttet https://realpython.com/courses/python-datetime-module/

For at programmet skal fungere slik jeg har laget det, har jeg måttet
legge inn en fast dato variabel, slik at jeg kunne bruke datetime.combine()

`date.strptime` finnes fra Python >= 3.14, og har derfor satt dette som krav i pyproject.toml

Sekunder i klokkeslett input er bevisst utelatt.

Test tilfeller:
Funksjon 1 - Returner en gyldig dato

| Inndata  |Forventet   |Faktisk   | Vurdering  |
|---|---|---|---|
|29.02.2026|Ugyldig|Ugyldig og årsak|Godkjent| 
|12.12.2023|Gyldig|Gyldig, bekreftet|Godkjent|

Funksjon 2 - Starttidspunkt, legg til minutter og returner slutt tid

|Inndata 1|Inndata 2|Forventet|Faktisk|Vurdering|
|---|---|---|---|---|
|12:54|63 min|13:57|13:57|Godkjent|
|09:57|tre|Wrong input, only positive integers allowed|Wrong input, only positive integers allowed|Godkjent|

Funksjon 3 - To inndatoer, retur av differanse i dager som absolutt tall

|Inndata 1|Inndata 2|Forventet|Faktisk|Vurdering|
|---|---|---|---|---|
|28.01.1977|22.09.2026|18134|18134|Godkjent|
|22.09.2026|28.01.1977|18134|18134|Godkjent|
|34.34.1222|Ikke mulig|ValueError og forklaring     |ValueError: time data '34.34.1222' does not match format '%d.%m.%Y'     |Godkjent        |



## Oppgave 4

Kjør program med: `uv run oppgave-4.py`

### KI bruk relevant for oppgave
- Etter et par utvekslinger for å forstå hvordan jeg kunne benytte en dict jeg hadde med kategori og tall
for å finne den mest populære uten hell, ble jeg servert med en lambda funksjon for max() som jeg kjenner såvidt til
kombinert med .get. Det ble presentert slik `return max(counts, key=counts.get)` og 
deretter revidert til `return max(categories, key=lambda x: categories[x])`. 
  - Her klarte jeg ikke helt å koble rett på egen hånd, men heller ikke forklare i detalj hvordan dette fungerer.
  - Endte derfor med å skrive 6 linjer med kode i en loop istedet for lambda, slik at jeg kan forklare og eier koden
- Ved kodegjennomlesning av Claude, fikk jeg tilbakemeldinger på type annotations som vanlig. Jeg prøver å lære
meg å skrive disse korrekt og konsekvent, noe som selvfølgelig gir litt ekstra feedback når jeg misser.
- Jeg hadde litt problemer med try/except for filhåndtering. Klarte å sette opp kriterier og feilmeldinger,
men hadde utfordringer med å bryte ut. Fikk forslag om å bare bruke `return`, men rettet dette til `return None`
da PyCharm viste advarsel om avvik ved bruk av kun `return`
- Manglet en `continue` i load_cases(). Dette ble påpekt av KI og deretter rettet av meg
- Et google søk om dict vs list, viste et KI svar som forenklet forståelsen min av hvordan jeg skulle lettest
lage `count_pr_category` med retur av Dict fremfor list of dicts.


Kommentarer for løsning av Oppgave 4:
- Mest populære kategori vil vise `første` treff ved to eller flere kategorier med samme antall henvendelser
- Etter en stund var flere av funksjonene gjenkjennelig fra tidligere oppgaver, og noe kode er gjenbrukt
- Har brukt YouTube, Python docs for csv, egne bøker og RealPython som kilder til informasjon om håndtering av csv filen.


Oppgave 4.4 - Finn og rett feil

```
def sum_resolved_minutes(requests: list[dict[str, str | int]]) -> int:
  total = 0
  for request in requests:
    if request["is_resolved"] = "yes":
       total = request["minutes"]
  return total_minutes
  
print(sum_resolved_minutes())
```

Her er samme kode korrigert med kommentarer og dummy data
Korreksjoner:
- samkjørt variabel navn inni funksjon. Beholdt det fra return statement da den var mest beskrivende
- endret `=` til `==` for sammenligning, ikke tildeling
- Lagt til addisjon som operasjon for minutter brukt, fremfor overskriving av variabelverdi i hver loop
- Manglet argument ved funksjonskall i print statement.

```
calls = [
    {'is_resolved': 'yes','minutes': 3},
    {'is_resolved': 'no', 'minutes': 2},
    {'is_resolved': 'yes', 'minutes': 6},
    {'is_resolved': 'no', 'minutes': 3}
]


def sum_resolved_minutes(requests: list[dict[str, str|int]]) -> int:
    total_minutes = 0  # Korrigert variabelnavn, tilsvarende return statement - Mest beskrivende navn
    for request in requests:
        if request["is_resolved"] == "yes":  # Må bruke == for sammenligning
            total_minutes += request["minutes"]  # Korrigert variabel navn, og rettet til addisjon av key for total minutes
    return total_minutes

print(sum_resolved_minutes(calls)) # Her må vi ha med inndata i funksjonskallet
```

# Oppgave 5

Kjør program med: `uv run oppgave-5.py`

### KI Bruk relevant for oppgave:
- Ved gjennomsyn av mitt forslag for menyvalg 1-4 foreslår Claude å bruke getattr, for å slå sammen flere
3 forgreninger med loops som gjorde det samme til en funksjon. Dette er var jeg selvfølgelig interessert i
og måtte slå opp på getattr, som var ukjent for meg. Fikk en korreksjon om å legge til .lower() ifb verdi sammenligning
3 loops ble til 1. Lærerikt
- Når jeg startet arbeided med menyvalgene, ble jeg gjort oppmerksom på at mye av koden var 
allerede skrevet i de foregående oppgavene. Jeg har kopiert, limt og korrigert der jeg så jeg kunne
spare tid basert på dette tipset. Jeg hadde nok sett dette selv innen kort tid med arbeid med meny
funksjonene.
- Sendte en funksjon jeg hadde problemer med til gjennomlesing av KI, fikk svar at jeg hadde `return None` feilplassert
Så over koden en gang til og forstod hvor feilen var.

### Eksterne kilder
Control Flow Structures - Real Python:
- https://realpython.com/python-control-flow/#matching-patterns-with-match-case
Python Docs - More control Flow (match statements)
- https://docs.python.org/3/tutorial/controlflow.html#match-statements


I oppgave-5 har jeg brukt match / case for menyen for
enkelt å kvalitetssikre brukerinput for menyvalg.

For menyvalg 5 har jeg valgt synkende sortering. En videre forbedring hadde vært å gi brukeren valget, og sendt
dette som parameter som valger reverse=False/True i sorteringsfunksjonen.



