# Magistarski_Edin_Kohnic

Ovaj repozitorij sadrži kompletan projekat izgradnje modela za predikciju klimatskih promjena u Bosni i Hercegovini koristeći LSTM neuronske mreže i linearnu regresiju.

Sadržaj repozitorija:

Modeli: Implementacije LSTM i linearnih regresionih modela za predikciju temperatura.
Predikcioni model: Finalni model koji se koristi za generisanje predikcija.
CSV fajlovi:
prosjek_linear.csv i prosjek_lstm.csv — prosječne godišnje temperature po modelima.
predikcije_2026_2045.csv — mjesečne predikcije za period 2026-2045 (LSTM).

API aplikacija: app.py — Flask aplikacija sa REST API-jem za pristup predikcijama temperature po godini i mjesecu.
