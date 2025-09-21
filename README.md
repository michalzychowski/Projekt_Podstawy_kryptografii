# Projekt - Podstawy kryptografii
## Opis
Projekt na przedmiot "Podstawy kryptografii" na IV roku studiów inżynierskich na kierunku Informatyka i ekonometria na UR. Projekt demonstruje szyfr kwadratu Polibiusza oraz metodę automatycznego łamania szyfru przy użyciu heurystyki Hill Climbing wzbogaconej o metodę Shotgun. W repozytorium znajdują się: implementacja szyfru Polibiusza, moduł oceniający poprawność tekstu na podstawie n-gramów, skrypt ataku, który wykorzystuje algorytm Hill Climbing oraz Shotgun do odszyfrowania kryptotekstu, pliki z ngramami i przykładowymi kryptotekstami, prosty skrypt testowy do badania skuteczności ataku przy różnych długościach tekstu i czasie działania. Celem projektu jest pokazanie praktycznych technik analizy częstotliwościowej i heurystycznego łamania szyfrów prostych oraz ocena minimalnej długości kryptotekstu potrzebnej do skutecznego ataku.

## Technologie
Projekt został wykonany przy użyciu:
* Python
* Standardowe biblioteki Pythona
* Visual Studio Code

## Wymagania
Do uruchomienia projektu potrzebne są:
* Zainstalowany język Python (zalecane: 3.8 lub nowszy)
* Pliki danych:
  * zbiory n-gramów wykorzystywane do oceny jakości odszyfrowanego tekstu (`english_bigrams.txt`, `english_quadgrams_J2I.txt` lub własne odpowiedniki)
  * przykładowe zaszyfrowane teksty -nfragmenty literatury pięknej (`crypto_text1.txt`, `crypto_text2.txt` lub własne odpowiedniki)

## Instrukcja uruchomienia
1. Zainstaluj wymagane komponenty
2. Sklonuj repozytorium komendą `git clone https://github.com/michalzychowski/Projekt_Podstawy_kryptografii.git`
3. (Opcjonalnie) utwórz i aktywuj wirtualne środowisko:
   ```bash
   python -m venv venv
   venv\Scripts\activate
    ```
4. Uruchom skrypt ataku: `python attack.py`
5. Uruchom skrypt testowy: `python tests.py`

## Licencja
Projekt jest dostępny na licencji [MIT](LICENSE).