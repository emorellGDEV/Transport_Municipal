from pymongo import MongoClient
from pprint import pprint

# Connexió amb la base de dades
client = MongoClient('mongodb+srv://emorelldam:emorelldam@transport.49dur1e.mongodb.net/test')
db = client['Transport']


# Funcions per gestionar les operacions

def llistar_persones():
    pprint("Llistant les dades personals de les persones de la plantilla...")
    col_persones = db['persones']
    cursor = col_persones.find({})
    for document in cursor:
        pprint(document)


def llistar_linies():
    pprint("Llistant les línies disponibles...")
    col_linies = db['linies']
    cursor = col_linies.find({})
    for document in cursor:
        pprint(document)


def llistar_preus():
    pprint("Llistant l'històric de preus...")
    col_preus = db['historic_preus']
    cursor = col_preus.find({})
    for document in cursor:
        pprint(document)


def llistar_linies_utilitzades():
    pprint("Llistant les línies ordenades de més a menys utilitzada...")
    col_us_linies = db['us_linies']
    cursor = col_us_linies.aggregate([
        {"$group": {"_id": "$numero_linia", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}}
    ])
    for document in cursor:
        pprint(document)


def passatgers_per_data_i_linia():
    data = input("Introdueix la data (YYYY-MM-DD): ")
    linia = input("Introdueix el número de la línia: ")
    pprint(f"Passatgers que han utilitzat la línia {linia} durant la data {data}:")
    col_us_linies = db['us_linies']
    cursor = col_us_linies.find({"data": data, "numero_linia": linia})
    for document in cursor:
        pprint(document)


def nombre_passatgers_per_data_i_linia():
    data = input("Introdueix la data (YYYY-MM-DD): ")
    linia = input("Introdueix el número de la línia: ")
    col_us_linies = db['us_linies']
    count = col_us_linies.count_documents({"data": data, "numero_linia": linia})
    pprint(f"Número de passatgers que han utilitzat la línia {linia} durant la data {data}: {count}")


def ingressos_per_dates():
    data_inicial = input("Introdueix la data inicial (YYYY-MM-DD): ")
    data_final = input("Introdueix la data final (YYYY-MM-DD): ")
    col_us_linies = db['us_linies']
    cursor = col_us_linies.aggregate([
        {"$match": {"data": {"$gte": data_inicial, "$lte": data_final}}},
        {"$group": {"_id": "$data", "total": {"$sum": "$preu"}}}
    ])
    for document in cursor:
        pprint(document)


def insert_demo_data():
    persones = [
        {"nom": "John Doe", "edat": 30, "departament": "Conductor"},
        {"nom": "Jane Smith", "edat": 25, "departament": "Controladora"},
        {"nom": "David Johnson", "edat": 35, "departament": "Manteniment"},
        {"nom": "Mary Jones", "edat": 40, "departament": "Conductora"},
        {"nom": "James Williams", "edat": 45, "departament": "Controlador"},
        {"nom": "Patricia Brown", "edat": 50, "departament": "Manteniment"},
        {"nom": "Michael Miller", "edat": 55, "departament": "Conductor"},
        {"nom": "Linda Wilson", "edat": 60, "departament": "Controladora"},
        {"nom": "Barbara Moore", "edat": 65, "departament": "Manteniment"},
        {"nom": "William Taylor", "edat": 70, "departament": "Conductor"},
        {"nom": "Elizabeth Anderson", "edat": 75, "departament": "Controladora"},
    ]
    db['persones'].insert_many(persones)

    linies = [
        {"numero": 1, "nom": "Línia 1", "origen": "Poble Nou", "desti": "Centre"},
        {"numero": 2, "nom": "Línia 2", "origen": "Gràcia", "desti": "Barceloneta"},
        {"numero": 3, "nom": "Línia 3", "origen": "Sants", "desti": "Forum"},
    ]
    db['linies'].insert_many(linies)

    preus = [
        {"data": "2023-01-01", "preu": 2.5},
        {"data": "2023-01-02", "preu": 2.5},
        {"data": "2023-01-03", "preu": 2.5},
        {"data": "2023-01-04", "preu": 2.5},
        {"data": "2023-01-05", "preu": 2.5},
        {"data": "2023-01-06", "preu": 2.5},
        {"data": "2023-01-07", "preu": 2.5},
    ]
    db['historic_preus'].insert_many(preus)

    usos_linies = [
        {"data": "2023-01-01", "numero_linia": 1, "preu": 2.5, "passatgers": 10},
        {"data": "2023-01-01", "numero_linia": 2, "preu": 2.5, "passatgers": 8},
        {"data": "2023-01-02", "numero_linia": 1, "preu": 2.5, "passatgers": 12},
        {"data": "2023-01-02", "numero_linia": 2, "preu": 2.5, "passatgers": 10},
        {"data": "2023-01-03", "numero_linia": 1, "preu": 2.5, "passatgers": 14},
        {"data": "2023-01-03", "numero_linia": 2, "preu": 2.5, "passatgers": 12},
        {"data": "2023-01-04", "numero_linia": 1, "preu": 2.5, "passatgers": 16},
        {"data": "2023-01-04", "numero_linia": 2, "preu": 2.5, "passatgers": 14},
        {"data": "2023-01-05", "numero_linia": 1, "preu": 2.5, "passatgers": 18},
        {"data": "2023-01-05", "numero_linia": 2, "preu": 2.5, "passatgers": 16},
        {"data": "2023-01-06", "numero_linia": 1, "preu": 2.5, "passatgers": 20},
        {"data": "2023-01-06", "numero_linia": 2, "preu": 2.5, "passatgers": 18},
        {"data": "2023-01-07", "numero_linia": 1, "preu": 2.5, "passatgers": 22},
        {"data": "2023-01-07", "numero_linia": 2, "preu": 2.5, "passatgers": 20},
    ]
    db['us_linies'].insert_many(usos_linies)

    pprint("Dades de demostració inserides amb èxit.")


def run_menu():
    pprint("Gestió de Transport Municipal - Menú")
    pprint("1. Llistar les dades personals de les persones de la plantilla")
    pprint("2. Llistar les línies disponibles")
    pprint("3. Llistar l'històric de preus")
    pprint("4. Llistar les línies ordenades de més a menys utilitzada")
    pprint("5. Passatgers que han utilitzat una línia en una data determinada")
    pprint("6. Número de passatgers que han utilitzat una línia en una data determinada")
    pprint("7. Ingressos per un rang de dates")
    pprint("8. Sortir")
    opcio = input("Introdueix una opció: ")

    if opcio == "1":
        llistar_persones()
    elif opcio == "2":
        llistar_linies()
    elif opcio == "3":
        llistar_preus()
    elif opcio == "4":
        llistar_linies_utilitzades()
    elif opcio == "5":
        passatgers_per_data_i_linia()
    elif opcio == "6":
        nombre_passatgers_per_data_i_linia()
    elif opcio == "7":
        ingressos_per_dates()
    elif opcio == "8":
        pprint("Sortint...")
        exit()
    elif opcio == "9":
        pprint("Inserint dades de demostració...")
        insert_demo_data()
    else:
        pprint("Opció incorrecta")

    pprint("")
    pprint("Premi una ENTER per continuar...")
    wait = input()

    run_menu()


if __name__ == "__main__":
    run_menu()
