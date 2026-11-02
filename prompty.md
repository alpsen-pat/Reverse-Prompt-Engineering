1. Przepisz kod wykorzystując bibliotekę numpy. Przekształć dane postaci (NAZWY i STATYSTYKI) na tablice np.array. Zastosuj wektorowe obliczenie siły postaci na podstawie znormalizowanych statystyk (metoda min-max) oraz stałych wag dla poszczególnych kolumn (HP, atak, obrona, szybkość). Zachowaj wypisywanie rankingu i średniej.

Opis zmian: Przepisanie logiki z tradycyjnych pętli na tablice numpy, wdrożenie wektorowych obliczeń siły oraz normalizacji min-max z uwzględnieniem stałych wag statystyk.

2. Rozbuduj dotychczasowy kod o funkcję waliduj(nazwy, dane), która upewni się, że macierz ma odpowiedni wymiar (np. dokładnie 4 statystyki), nazwy są unikatowe i nie ma ujemnych wartości. Dodaj też prostą funkcję testy() z użyciem np.testing.assert_allclose, która sprawdzi poprawność działania normalizacji na przykładowych danych przed uruchomieniem głównego programu.

Opis zmian: Zabezpieczenie kodu przed błędnymi danymi wejściowymi (walidacja wymiarów, unikatowości i wartości ujemnych) oraz dodanie testów jednostkowych sprawdzających poprawność normalizacji.

3. Dołącz do istniejącego skryptu funkcję okresl_role(dane), która na podstawie progów statystyk (np. wysoki atak i szybkość -> Szturmowiec, wysokie HP i obrona -> Obrońca, a w pozostałych przypadkach -> Wszechstronny) przypisze każdemu bohaterowi odpowiednią rolę za pomocą np.select. Uwzględnij tę rolę w końcowym podsumowaniu wypisywanym na ekranie.

Opis zmian: Wprowadzenie automatycznego system klasyfikacji postaci na role (Szturmowiec, Obrońca, Wszechstronny) za pomocą warunkowego wyboru np.select.

4. Dodaj do programu funkcję macierz_pojedynkow(sila), która obliczy macierz szans na wygraną każdego bohatera z każdym innym przy użyciu funkcji logistycznej (funkcji sigmoidalnej opartej na różnicach siły). Przekątna macierzy powinna wynosić 0.5 (walka z samym sobą). Na tej podstawie oblicz średnią szansę wygranej dla każdej postaci w starciu z całą grupą i dołącz ją do wydruków.

Opis zmian: Dodanie systemu symulacji walk między postaciami i wyznaczania macierzy szans na wygraną przy użyciu funkcji logistycznej (sigmoidalnej).

5. Sfinalizuj projekt, organizując kod w funkcję main(). Dodaj: Obliczanie statystyk grupy (min, średnia, max dla każdej kolumny za pomocą funkcji np.min, np.mean, np.max). Filtrowanie postaci spełniających określone wymagania przy użyciu masek boole'owskich NumPy. Eksport kompletnego rankingu wraz z rolami i szansami na wygraną do pliku raport_postaci.csv z kodowaniem utf-8-sig i średnikiem jako separatorem.

Opis zmian: Strukturyzacja kodu w funkcję główną main(), dodanie podsumowań grupowych (min/mean/max), filtrowania za pomocą masek boole'owskich oraz eksportu wyników do pliku CSV.

------------------------------

Nie korektowalem żadnego prompta bo działa z tego co widze (ale to tylko na oko). Jest to za to drugie podejście, pierwsze prompty które daly niedziałający kod wiec je skasowałem i zmieniłem ai do którego dawałem prompty. nie mam dostępu do pierwszych promptow ale porównywanie do nowych nie miało by raczej sensu bo były zupełnie inne (chyba) w tym w kolejności robionych poprawek.