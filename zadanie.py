import csv
import numpy as np


def testy():
    """Funkcja testująca poprawność działania normalizacji Min-Max."""
    print("=== URUCHAMIANIE TESTÓW JEDNOSTKOWYCH ===")
    
    # Przykładowe dane testowe (2 kolumny, 3 wiersze)
    dane_testowe = np.array([
        [10.0, 20.0],
        [20.0, 40.0],
        [30.0, 60.0]
    ])
    
    # Oczekiwany wynik normalizacji Min-Max dla danych testowych
    oczekiwane = np.array([
        [0.0, 0.0],
        [0.5, 0.5],
        [1.0, 1.0]
    ])
    
    # Obliczenia testowe
    min_vals = dane_testowe.min(axis=0)
    max_vals = dane_testowe.max(axis=0)
    wynik_testowy = (dane_testowe - min_vals) / (max_vals - min_vals)
    
    # Sprawdzenie przy użyciu np.testing.assert_allclose
    np.testing.assert_allclose(wynik_testowy, oczekiwane, rtol=1e-5, atol=1e-5)
    print("Testy normalizacji przeszły pomyślnie!\n")


def waliduj(nazwy, dane):
    """Waliduje poprawność danych wejściowych postaci RPG."""
    # 1. Sprawdzenie wymiarów (oczekujemy dokładnie 4 kolumn statystyk)
    if dane.ndim != 2 or dane.shape[1] != 4:
        raise ValueError(
            f"Błąd wymiarów: Macierz statystyk musi mieć 2 wymiary i dokładnie 4 kolumny. "
            f"Aktualny kształt to {dane.shape}."
        )
    
    # 2. Sprawdzenie unikatowości nazw
    if len(np.unique(nazwy)) != len(nazwy):
        raise ValueError("Błąd walidacji: Nazwy postaci muszą być unikatowe!")
        
    # 3. Sprawdzenie braków ujemnych wartości
    if np.any(dane < 0):
        raise ValueError("Błąd walidacji: Statystyki postaci nie mogą zawierać ujemnych wartości!")
        
    print("Walidacja danych przebiegła pomyślnie.\n")


def okresl_role(stat_norm):
    """Przypisuje rolę postaci na podstawie znormalizowanych statystyk przy użyciu np.select."""
    hp = stat_norm[:, 0]
    atak = stat_norm[:, 1]
    obrona = stat_norm[:, 2]
    szybkosc = stat_norm[:, 3]
    
    warunki = [
        (atak > 0.5) & (szybkosc > 0.5),  # Szturmowiec: wysoki atak i szybkość
        (hp > 0.5) & (obrona > 0.5)        # Obrońca: wysokie HP i obrona
    ]
    wybory = ["Szturmowiec", "Obrońca"]
    
    return np.select(warunki, wybory, default="Wszechstronny")


def macierz_pojedynkow(sily):
    """Oblicza macierz szans na wygraną każdego bohatera z każdym innym przy użyciu funkcji logistycznej."""
    roznice = sily[:, np.newaxis] - sily[np.newaxis, :]
    macierz = 1 / (1 + np.exp(-roznice))
    return macierz


def main():
    # 0. Uruchomienie testów jednostkowych
    testy()

    # Dane postaci
    postacie = [
        {"nazwa": "Wojownik", "hp": 120, "atak": 28, "obrona": 18, "szybkosc": 9},
        {"nazwa": "Mag", "hp": 75, "atak": 44, "obrona": 6, "szybkosc": 13},
        {"nazwa": "Łucznik", "hp": 95, "atak": 34, "obrona": 10, "szybkosc": 17},
        {"nazwa": "Paladyn", "hp": 140, "atak": 25, "obrona": 22, "szybkosc": 7},
        {"nazwa": "Łotrzyk", "hp": 80, "atak": 39, "obrona": 8, "szybkosc": 21},
        {"nazwa": "Berserker", "hp": 110, "atak": 42, "obrona": 7, "szybkosc": 12},
        {"nazwa": "Druid", "hp": 105, "atak": 26, "obrona": 15, "szybkosc": 14},
        {"nazwa": "Strażnik", "hp": 155, "atak": 18, "obrona": 26, "szybkosc": 5},
    ]

    # 1. Przekształcenie na tablice NumPy
    nazwy = np.array([p["nazwa"] for p in postacie])
    statystyki = np.array([
        [p["hp"], p["atak"], p["obrona"], p["szybkosc"]] 
        for p in postacie
    ], dtype=float)

    # 2. Walidacja danych
    waliduj(nazwy, statystyki)

    # 3. Normalizacja Min-Max
    min_vals = statystyki.min(axis=0)
    max_vals = statystyki.max(axis=0)
    statystyki_norm = (statystyki - min_vals) / (max_vals - min_vals)

    # 4. Określenie ról postaci
    role = okresl_role(statystyki_norm)

    # 5. Obliczenie siły
    wagi = np.array([0.1, 2.0, 1.5, 1.0])
    sily = np.dot(statystyki_norm, wagi)

    # 6. Analiza pojedynków
    macierz_duel = macierz_pojedynkow(sily)
    srednie_szanse = macierz_duel.mean(axis=1) * 100

    # 7. Statystyki grupy (np.min, np.mean, np.max)
    print("=== STATYSTYKI GRUPY ===")
    etykiety_kolumn = ["HP", "Atak", "Obrona", "Szybkość"]
    min_grupa = np.min(statystyki, axis=0)
    srednia_grupa = np.mean(statystyki, axis=0)
    max_grupa = np.max(statystyki, axis=0)
    
    for etykieta, mn, sr, mx in zip(etykiety_kolumn, min_grupa, srednia_grupa, max_grupa):
        print(f"- {etykieta}: Min = {mn:.1f} | Średnia = {sr:.1f} | Max = {mx:.1f}")
    print()

    # 8. Filtrowanie postaci za pomocą masek boole'owskich NumPy
    # Maska: Postacie elitarne (siła powyżej średniej siły grupy)
    srednia_sily = np.mean(sily)
    maska_elita = sily > srednia_sily
    elitarne_postacie = nazwy[maska_elita]
    print(f"=== ELITA GRUPY (Siła > Średnia: {srednia_sily:.2f}) ===")
    print(", ".join(elitarne_postacie))
    print()

    # 9. Wyświetlanie kompletnego rankingu
    print("=== PEŁNY RANKING POSTACI ===")
    for nazwa, sila, rola, sr_szansa in zip(nazwy, sily, role, srednie_szanse):
        print(f"{nazwa} [{rola}] — Siła: {sila:.2f} | Średnia szansa wygranej: {sr_szansa:.1f}%")

    najlepsza_idx = np.argmax(sily)
    print(f"\nNajsilniejsza postać: {nazwy[najlepsza_idx]} ({role[najlepsza_idx]})")
    print(f"Średnia siła grupy: {srednia_sily:.2f}")

    # 10. Eksport raportu do pliku CSV (kodowanie utf-8-sig, separator ;)
    nazwa_pliku = "raport_postaci.csv"
    with open(nazwa_pliku, mode="w", encoding="utf-8-sig", newline="") as plik_csv:
        writer = csv.writer(plik_csv, delimiter=";")
        writer.writerow(["Nazwa", "Rola", "HP", "Atak", "Obrona", "Szybkość", "Siła", "Średnia szansa wygranej (%)"])
        
        for nazwa, rola, stat, sila, szansa in zip(nazwy, role, statystyki, sily, srednie_szanse):
            writer.writerow([
                nazwa, 
                rola, 
                int(stat[0]), 
                int(stat[1]), 
                int(stat[2]), 
                int(stat[3]), 
                f"{sila:.2f}", 
                f"{szansa:.1f}"
            ])
            
    print(f"\nRaport został pomyślnie wyeksportowany do pliku '{nazwa_pliku}'.")


if __name__ == "__main__":
    main()