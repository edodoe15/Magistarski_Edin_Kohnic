# Magistarski_Edin_Kohnic

Predikcija klimatskih promjena u BiH pomoću LSTM i linearne regresije

Ovaj repozitorij sadrži kompletan projekat izgradnje modela za predikciju klimatskih promjena u Bosni i Hercegovini, koristeći dvije različite metode: LSTM neuronske mreže i linearnu regresiju. Projekat uključuje obradu podataka, treniranje modela, vizualizaciju rezultata i izlaganje predikcija putem REST API-ja.

## Sadržaj repozitorija

- **`notebooks/`**  
  - Jupyter notebook fajlovi sa implementacijom modela i analizom rezultata.
  
- **`data/`**  
  - `prosjek_linear.csv` – prosječne godišnje temperature prema linearnom modelu.  
  - `prosjek_lstm.csv` – prosječne godišnje temperature prema LSTM modelu.  
  - `predikcije_2026_2045.csv` – mjesečne predikcije za period 2026–2045 (LSTM model).

- **`my_flask_api.rar`**  
  - Flask aplikacija koja izlaže REST API za dohvat predikcija po godini i mjesecu. Koristi GUI za prikaz grafa sa podacima o predviđenim temperaturama (ovi podaci dolaze iz .csv-a u sklopu foldera, a dobijeni su     preko LSTM predikcionog modela. Folder se sastoji od /templates/index.html fajla, app.py fajla i csv-a sa podacima. 

## Korištene tehnologije

- Python (NumPy, Pandas, Matplotlib, TensorFlow/Keras, Scikit-learn)
- Flask za izradu API-ja
- Jupyter Notebook za eksperimentisanje i prikaz analiza

## Pokretanje aplikacije

1. Klonirati repozitorij:

   ```bash
   git clone https://github.com/edodoe15/Magistarski_Edin_Kohnic.git
   cd Magistarski_Edin_Kohnic

    Instalirati potrebne biblioteke:

   pip install -r requirements.txt

Pokrenuti Flask API:

    python app.py

    Pristupiti aplikaciji na http://localhost:5000

Napomene

    Projekat je izrađen u sklopu magistarskog rada, s fokusom na praktičnu primjenu naprednih modela dubokog učenja na okolišne podatke u BiH.
