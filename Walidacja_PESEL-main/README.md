# Walidacja PESEL

## Opis projektu
Aplikacja Django do walidacji numeru PESEL, która umożliwia użytkownikowi sprawdzenie poprawności podanego numeru oraz wyświetla dodatkowe informacje, takie jak data urodzenia i płeć osoby.

## Funkcjonalności
- Walidacja poprawności numeru PESEL.
- Wyświetlenie daty urodzenia oraz płci na podstawie numeru PESEL.
- Prosty interfejs.

## Technologie
Projekt wykorzystuje:
- **Python** — język programowania,
- **Django** — framework webowy,
- **HTML** — struktura interfejsu.

## Instalacja i konfiguracja

   ```bash
   git clone https://github.com/MichalOkopny/Walidacja_PESEL.git
   cd pesel_validator
   python3 -m venv .venv
   source .venv/bin/activate  # Linux / macOS
   .venv\Scripts\activate     # Windows
   python manage.py migrate
   python manage.py runserver




  
