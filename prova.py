import os
import numpy as np
from utils import read, salva_csv
from funzioni import *

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

# Nomi delle colonne 
colonne = ["massa_molecolare","idrofobicità","punto_isoelettrico",
           "solubilità","stabilità","assorbimento_uv","densità"]

# Funzione per stampa report umano
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
    print("Le medie e deviazioni standard possono aiutare a valutare le proprietà generali")
    print("delle proteine nel dataset, mentre i valori estremi evidenziano i casi particolari.")


# Menu 
funz = {
    "1": ("Somma colonne", somma_colonne),
    "2": ("Media colonne", media_colonne),
    "3": ("Somma righe", somma_righe),
    "4": ("Media righe", media_righe),
    "5": ("Norma matrice", norma),
    "6": ("Trasposta matrice", trasposta),
    "7": ("Covarianza", covarianza),
    "8": ("Stampa report proteine", None),  # funzione speciale
    "0": ("Esci", None)
}

while True:
    print("\n--- Menu Analisi ---")
    for key, (nome, _) in funz.items():
        print(f"{key} - {nome}")
    
    scelta = input("Scegli un'operazione: ")

    if scelta == "0":
        print("Uscita dal programma.")
        break

    if scelta not in funz:
        print("Scelta non valida, riprova.")
        continue

    nome, func = funz[scelta]

    # Caso speciale per il report
    if scelta == "8":
        stampa_report(dataset, colonne)
        continue

    # Tutte le altre funzioni
    risultati = {nome: func(dataset)}

    # Mostra i risultati a video
    print("\n--- Risultati ---")
    for k, v in risultati.items():
        print(f"{k}:\n{v}\n")

    # Salva su CSV
    salva_csv(risultati, out_csv)
    print(f"Risultati aggiunti a '{out_csv}'")
