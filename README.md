# 🌍 EkoBot - Twój Ekologiczny Pomocnik na Discordzie

EkoBot to interaktywny bot stworzony w Pythonie (discord.py), którego celem jest edukacja proekologiczna, pomoc w segregacji odpadów oraz monitorowanie stanu klimatu.

## 🚀 Funkcje
Bot oferuje szeroki wachlarz narzędzi:
- **Segregacja Odpadów:** Baza danych (`eko_bin`) oraz rozpoznawanie obrazu AI (`check`).
- **Monitoring CO2:** Aktualne dane z API oraz interaktywne mapy globalnej emisji.
- **Kalkulator Śladu Węglowego:** Obliczanie emisji CO2 na podstawie spalania samochodu.
- **Edukacja:** Ponad 50 losowych porad ekologicznych.
- **Multimedia:** Playlisty edukacyjne i linki do ważnych źródeł.

## 🛠️ Wymagania systemowe
Do uruchomienia bota potrzebujesz:
- Python 3.8+
- Biblioteki: `discord.py`, `requests`, `Pillow`, `tensorflow` (dla modelu Keras)
- Plik `keras_model.h5` oraz `labels.txt` w folderze bota.

## 📋 Lista Komend

| Komenda | Opis |
| :--- | :--- |
| `$hello` | Powitanie bota. |
| `$help_me` | Wyświetla listę dostępnych funkcji. |
| `$heh [tekst] [liczba]` | Powtarza podany tekst określoną ilość razy. |
| `$co2_porada` | Losuje jedną z 50 porad dotyczących ochrony środowiska. |
| `$eko_bin [NAZWA]` | Informuje, do którego pojemnika wyrzucić dany przedmiot. |
| `$check` | (Załącz zdjęcie) Rozpoznaje przedmiot i sugeruje śmietnik za pomocą AI. |
| `$co2` | Pobiera najnowsze dane o stężeniu dwutlenku węgla w ppm. |
| `$mapa` | Wysyła link do mapy emisji prądu na żywo. |
| `$obl [km] [spalanie] [paliwo]` | Oblicza emisję CO2 dla trasy (paliwa: benzyna, diesel, lpg). |
| `$play` | Wyświetla polecane playlisty o ekologii. |

## 📂 Struktura Projektu
- `main.py`: Główny kod bota i komendy Discord.
- `wherebin.py`: Moduł z funkcją `eko()` i słownikiem segregacji.
- `model.py`: Obsługa modelu AI do rozpoznawania zdjęć.
- `keras_model.h5`: Wytrenowany model klasyfikacji obrazów.

## 🛡️ Autor i Licencja
Projekt stworzony w celach edukacyjnych, aby promować świadomość ekologiczną wśród użytkowników Discorda.
