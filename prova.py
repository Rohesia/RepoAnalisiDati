import os
import numpy as np
from utils import read, salva_csv
from funzioni import *
from Array_Mono import *

# File di output
out_csv = "risultati.csv"

# Reset file all'inizio
if os.path.exists(out_csv):
    os.remove(out_csv)
    print(f"File '{out_csv}' subisce reset.\n")

# Caricamento CSV
nome_csv = input("Inserisci il nome del CSV di riferimento: ")
dataset = read(nome_csv)
if dataset is None:
    exit()

# Nomi colonne
colonne = ["massa_molecolare","idrofobicità","punto_isoelettrico",
           "solubilità","stabilità","assorbimento_uv","densità"]

# Funzione per scegliere colonna (per analisi 1D)
def scegli_colonna(dataset, colonne):
    print("\n--- Seleziona colonna ---")
    for i, nome in enumerate(colonne):
        print(f"{i} - {nome}")
    scelta = int(input("Inserisci indice colonna: "))
    return dataset[:, scelta], colonne[scelta]

# STAMPA REPORT COMPLETO
def stampa_report(matrix, colonne):
    
    medie = media_colonne(matrix)
    deviazioni = std_colonne(matrix)
    minimi = np.min(matrix, axis=0)
    massimi = np.max(matrix, axis=0)
    
    print("\n=== REPORT ANALISI PROTEINE ===")
    print(f"Totale proteine analizzate: {matrix.shape[0]}")
    print(f"Numero di proprietà per proteina: {matrix.shape[1]}\n")
    
    print("=== Statistiche medie e deviazioni standard ===")
    for i, nome in enumerate(colonne):
        print(f"{nome.capitalize()}: media = {medie[i]:.2f}, std = {deviazioni[i]:.2f}")
    print()
    
    print("=== Valori estremi rilevanti ===")
    print(f"Proteina più idrofobica: {massimi[1]:.2f} (indice alto)")
    print(f"Proteina meno idrofobica: {minimi[1]:.2f} (indice basso)")
    print(f"Proteina più solubile: {massimi[3]:.3f}")
    print(f"Proteina meno solubile: {minimi[3]:.3f}")
    print(f"Massa molecolare più alta: {massimi[0]:.2f} Da")
    print(f"Massa molecolare più bassa: {minimi[0]:.2f} Da\n")
    
    print("=== Note ===")
    print("Le medie e deviazioni standard aiutano a interpretare tendenze e outlier.\n")

# MENU PRINCIPALE
funz = {
    "1": ("Somma colonne", somma_colonne),
    "2": ("Media colonne", media_colonne),
    "3": ("Somma righe", somma_righe),
    "4": ("Media righe", media_righe),
    "5": ("Norma matrice", norma),
    "6": ("Trasposta matrice", trasposta),
    "7": ("Covarianza", covarianza),
    "8": ("Report proteine", None),
    "9": ("Analisi 1D su una colonna", None),
    "0": ("Esci", None)
}

# MENU 1D
menu_1d = {
    "1": ("Valore minimo", val_min),
    "2": ("Valore massimo", val_max),
    "3": ("Media", media),
    "4": ("Deviazione standard", dev_std),
    "5": ("Indice valore minimo", indice_val_min),
    "6": ("Indice valore massimo", indice_val_max),
    "7": ("Mediana", mediana),
    "8": ("Posizione ordinata inserimento", posiz_ord_inserimento),
    "0": ("Torna indietro", None)
}
while True:
    print("\n=== SCEGLI TIPO DI ANALISI ===")
    print("1 - Analisi 2D (tutta la matrice)")
    print("2 - Analisi 1D (una colonna)")
    print("0 - Esci")
    
    tipo = input("Scegli un'opzione: ")

    if tipo == "0":
        print("Uscita dal programma.")
        break

    elif tipo == "1":  # Analisi 2D
        while True:
            print("\n=== MENU 2D ===")
            for key, (nome, _) in funz.items():
                if key != "9":  # Escludiamo l'opzione 1D nel menu 2D
                    print(f"{key} - {nome}")
            
            scelta2d = input("Scegli un'operazione 2D: ")

            if scelta2d == "0":
                break

            if scelta2d == "8":  # Report completo
                stampa_report(dataset, colonne)
                continue

            if scelta2d in funz and funz[scelta2d][1] is not None:
                nome_op, func = funz[scelta2d]
                risultato = func(dataset)
                print(f"\n--- Risultato {nome_op} ---")
                print(risultato)
                salva_csv({nome_op: risultato}, out_csv)
                print("Risultato salvato.")

    elif tipo == "2":  # Analisi 1D
        colonna, nome_col = scegli_colonna(dataset, colonne)

        while True:
            print(f"\n=== MENU 1D: Analisi colonna '{nome_col}' ===")
            for key, (nome, _) in menu_1d.items():
                print(f"{key} - {nome}")

            scelta1d = input("Scegli operazione 1D: ")

            if scelta1d == "0":
                break

            nome_op, func1d = menu_1d[scelta1d]

            # Caso con parametro extra (posizione ordinata inserimento)
            if scelta1d == "8":
                x = float(input("Valore da inserire: "))
                risultato = func1d(colonna, x)
            else:
                risultato = func1d(colonna)

            print(f"\n--- Risultato {nome_op} ---")
            print(risultato)
            salva_csv({f"{nome_op} ({nome_col})": risultato}, out_csv)
            print("Risultato salvato.\n")
