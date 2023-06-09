## Gestió de Transport Municipal

Aquest és un projecte de gestió de transport municipal que utilitza una base de dades MongoDB per emmagatzemar les dades
relacionades amb les persones de la plantilla, les línies de transport, els preus dels bitllets i els registres d'ús de
les línies.

## Requisits

Per poder executar aquest projecte, cal tenir instal·lat Python 3 i les següents llibreries:

- pymongo
- pprint

Pots instal·lar les llibreries amb pip mitjançant la següent comanda:

```
pip install pymongo pprint
```

## Configuració de la connexió amb la base de dades

Abans de començar a utilitzar el projecte, cal configurar la connexió amb la base de dades MongoDB. A la línia següent
del codi, substitueix `<URI>` pel teu URI de connexió proporcionat per MongoDB:

```
pythonclient = MongoClient('<URI>')
```

En aquest projecte, s'utilitza una base de dades anomenada `Transport` amb les següents col·leccions:

- 'persones'
- 'linies'
- 'us_linies'
- 'historic_preus'

## Funcionalitats

El projecte proporciona les següents funcionalitats:

1. Llistar les dades personals de les persones de la plantilla
2. Llistar les línies disponibles
3. Llistar l'històric de preus
4. Llistar les línies ordenades de més a menys utilitzada
5. Mostrar els passatgers que han utilitzat una línia en una data determinada
6. Mostrar el nombre de passatgers que han utilitzat una línia en una data determinada
7. Mostrar els ingressos per un rang de dates
8. Sortir

## Ús

Executar el fitxer `main.py` per iniciar el programa. S'iniciarà un menú amb les diferents opcions disponibles. Per
seleccionar una opció, introdueix el número corresponent i prem la tecla "Enter".

## Dades de demostració

El projecte inclou una funció per inserir dades de demostració a la base de dades. Per utilitzar aquesta funció, pots
seleccionar l'opció "9" al menú. Això afegirà un conjunt de dades de prova per a les persones de la plantilla, les
línies de transport, els preus dels bitllets i els registres d'ús de les línies.

## Contribucions

Les contribucions són benvingudes! Si tens suggeriments d'implementació de noves funcionalitats o millores del codi
existent, si us plau, fes una bifurcació del repositori i envia una sol·licitud de tirada amb els teus canvis.


---

#### Autor: Eduardo Morell