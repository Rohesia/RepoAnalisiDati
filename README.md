# RepoAnalisiDati - Analisi Dati Proteine

## Introduzione

Questo progetto nasce con l'obiettivo di analizzare in modo approfondito un dataset contenente informazioni sulle proteine. Il dataset è organizzato in formato CSV e include diverse proprietà chimico-fisiche di ciascuna proteina, come la massa molecolare, l'idrofobicità, il punto isoelettrico, la solubilità, la stabilità, l'assorbimento UV e la densità.

L'analisi dei dati è stata suddivisa in due approcci complementari: da un lato abbiamo esplorato le relazioni tra le diverse proprietà utilizzando operazioni su array bidimensionali, dall'altro abbiamo analizzato in dettaglio singole caratteristiche attraverso operazioni su array monodimensionali. Questa doppia prospettiva ci permette di ottenere sia una visione d'insieme del dataset che approfondimenti specifici su ciascuna variabile.

## Come funziona il progetto

Il cuore del progetto è rappresentato dal programma principale `prova.py`, che offre un'interfaccia interattiva per guidare l'utente attraverso le varie possibilità di analisi. All'avvio, il programma chiede di specificare il nome del file CSV da analizzare (nel nostro caso `proteine.csv`) e successivamente presenta un menu che permette di scegliere tra due modalità operative.

Nella **modalità 2D**, il programma lavora sull'intera matrice di dati, consentendo di eseguire operazioni che coinvolgono più proprietà contemporaneamente. Ad esempio, è possibile calcolare la media di ciascuna colonna per capire quali sono i valori tipici per ogni proprietà, oppure analizzare la matrice di covarianza per scoprire se esistono relazioni tra le diverse caratteristiche delle proteine. Questa modalità include anche un report automatico che fornisce una panoramica completa delle statistiche più rilevanti del dataset.

La **modalità 1D**, invece, si concentra su una singola proprietà alla volta. L'utente può selezionare una colonna specifica (ad esempio l'idrofobicità o la massa molecolare) e poi applicare diverse operazioni statistiche come il calcolo del valore minimo e massimo, la media, la deviazione standard o la mediana. Questa modalità è particolarmente utile quando si vuole approfondire il comportamento di una specifica caratteristica.

## Struttura del codice

Il progetto è organizzato in modo modulare per facilitare la manutenzione e la comprensione del codice:

**Array_Mono.py** contiene tutte le funzioni per l'analisi di array monodimensionali. Qui Rosy ha implementato funzioni che lavorano su un singolo vettore di dati, permettendo di estrarre informazioni statistiche di base come media, deviazione standard, valori estremi e le loro posizioni all'interno dell'array.

**funzioni.py** raccoglie invece le operazioni più complesse che riguardano l'intera matrice di dati. In questo modulo sono presenti funzioni per calcolare somme e medie per righe o colonne, per effettuare trasformazioni matriciali come la trasposta, per calcolare la norma della matrice o la matrice di covarianza. Questo modulo rappresenta il lavoro di Anna sulle analisi bidimensionali.

**utils.py** gestisce le operazioni di input/output, ovvero la lettura del file CSV iniziale e il salvataggio dei risultati. Questo modulo si occupa di convertire i dati dal formato CSV in array NumPy che possono essere elaborati dalle funzioni di analisi, e viceversa di salvare i risultati delle analisi in un nuovo file CSV chiamato `risultati.csv`.

**prova.py** è il programma principale che coordina tutti i moduli precedenti, gestisce l'interazione con l'utente attraverso un sistema di menu, e si occupa di chiamare le funzioni appropriate in base alle scelte effettuate.

## Il dataset

Il file `proteine.csv` contiene i dati di 300 proteine diverse, ciascuna caratterizzata da 7 proprietà numeriche. Ogni riga rappresenta una proteina, mentre ogni colonna rappresenta una specifica proprietà. Questa struttura tabellare si presta perfettamente ad essere analizzata sia come matrice complessiva che come insieme di vettori indipendenti.

Le proprietà incluse nel dataset sono state scelte perché rappresentano caratteristiche fondamentali che determinano il comportamento e la funzione delle proteine in ambito biologico. La massa molecolare ci dice quanto è grande la proteina, l'idrofobicità indica se tende a stare in acqua o a evitarla, il punto isoelettrico è il pH a cui la proteina ha carica netta zero, la solubilità misura quanto facilmente si scioglie, la stabilità indica quanto è robusta la sua struttura, l'assorbimento UV può essere utilizzato per quantificare la presenza della proteina, e la densità è legata alla sua compattezza strutturale.

## Come utilizzare il programma

Per utilizzare il programma è necessario avere Python installato insieme alla libreria NumPy. Una volta avviato il programma con `python prova.py`, l'utente viene guidato passo dopo passo attraverso le opzioni disponibili.

All'inizio viene richiesto il nome del file CSV da analizzare. Dopo aver caricato i dati, appare il menu principale dove si può scegliere tra analisi 2D o 1D. Se si sceglie l'analisi 2D, viene presentato un secondo menu con tutte le operazioni disponibili sulla matrice completa. Se invece si opta per l'analisi 1D, prima viene chiesto di selezionare quale colonna si vuole analizzare, e successivamente appare il menu con le operazioni disponibili per quella specifica proprietà.

Tutti i risultati vengono automaticamente salvati nel file `risultati.csv`, permettendo di conservare una traccia delle analisi effettuate. Il programma sovrascrive questo file ad ogni nuova esecuzione, quindi se si vogliono conservare i risultati di sessioni diverse è necessario rinominare il file prima di riavviare il programma.

## Note tecniche

Tutte le operazioni matematiche e statistiche sono implementate utilizzando NumPy, una libreria Python estremamente efficiente per il calcolo numerico. Questo garantisce che anche con dataset più grandi le operazioni vengano eseguite rapidamente. Il codice è stato scritto cercando di mantenere una struttura chiara e modulare, in modo che sia facile aggiungere nuove funzioni o modificare quelle esistenti.

Un aspetto interessante del programma è la funzione di report automatico, che genera una panoramica statistica completa del dataset evidenziando le informazioni più rilevanti come i valori medi, le deviazioni standard e i valori estremi per ciascuna proprietà. Questo report può essere particolarmente utile come primo approccio al dataset prima di procedere con analisi più specifiche.

## Il team

Questo progetto è il risultato della collaborazione di tre persone con competenze complementari:

**Rosy** 

**Anna** 

**Antonia**