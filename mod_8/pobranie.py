import pandas as pd
import requests

# Pobierz stronę
url = 'https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/'
response = requests.get(url)

# Czytaj tabelę z strony
data = pd.read_html(response.text, header=0)

# Wybierz pierwszą tabelę (może być więcej niż jedna tabela na stronie)
df = data[0]

# Sprawdź, czy DataFrame nie jest pusty
if df.empty:
    print("Nie udało się znaleźć żadnej tabeli na stronie.")
else:
    # Wyświetl pierwsze kilka wierszy
    print(df.head())

    # Zapisz dane do pliku CSV
    df.to_csv('best_selling_albums.csv', index=False)

    print(f"Dane zapisano do pliku best_selling_albums.csv")

print("Operacja zakończona.")
