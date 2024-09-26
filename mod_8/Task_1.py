import pandas as pd
import requests

# Pobierz dane z strony
url = 'https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/'
response = requests.get(url)

# Odczyt tabeli do DataFrame
data = pd.read_html(response.text, header=0)[0]

column_mapping = {
    'POS': 'POZYCJA',
    'TITLE': 'TYTUŁ',
    'ARTIST': 'ARTYSTA',
    'YEAR': 'ROK',
    'HIGH POSN': 'MAX POZ'
}

# Zastosuj mapowanie kolumn
data.rename(columns=column_mapping, inplace=True)

# Liczba pojedynchych artystów
single_artists_count = data['ARTYSTA'].value_counts().eq(1).sum()
print(f"\nLiczba pojedynczych artystów: {single_artists_count}")

# Najczęściej pojawiające się zespoły
grouped = data.groupby('ARTYSTA').size().sort_values(ascending=False)
top_groups = grouped[grouped > 1]
print("\nNajczęściej pojawiające się zespoły:")
for artist, count in top_groups.head(5).items():
    print(f"{artist}: {count}")

# Zmiana nagłówków kolumn
data.columns = [col.capitalize() for col in data.columns]

# Usunięcie kolumny 'MAX POZ'
data = data.drop('Max poz', axis=1)

# Rok z największą liczbą albumów
max_albums_year = data['Rok'].value_counts().idxmax()
print(f"\nRok z najwięcej albumów: {max_albums_year}")

# Liczba albumów między 1960 a 1990
albums_1960_1990 = data[(data['Rok'] >= 1960) & (data['Rok'] <= 1990)].shape[0]
print(f"Liczba albumów wydanych między 1960 a 1990: {albums_1960_1990}")

# Najmłodszy album na liście
min_album_year = data['Rok'].min()
print(f"Najmłodszy album na liście wydany w roku: {min_album_year}")

# Grupujemy dane przez Artystę i sortujemy według Roka
artist_first_albums = data.groupby('Artysta')['Rok'].min().reset_index()
artist_first_albums['Tytuł'] = data.groupby('Artysta')['Tytuł'].first().reset_index()['Tytuł']

# Wyświetlenie pierwszych kilku wyników dla każdego artysty
print("\nNajwcześniejsze albumy każdego artysty:")
print(artist_first_albums)

# Zapisanie danych do pliku CSV
data.to_csv('best_selling_albums.csv', index=False)
print("\nDane zapisano do pliku best_selling_albums.csv")


