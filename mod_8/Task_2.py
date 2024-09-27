import pandas as pd
import matplotlib.pyplot as plt
import requests

# Pobieranie i wczytanie danych z pliku csv
url = 'fatal-police-shootings-data.csv'
df = pd.read_csv(url)

# Usunięcie wierszy z wartościami NaN -  czyszczenie danych
df = df.dropna()

# Przekształcenie danych
result_df = df.groupby(['race', 'signs_of_mental_illness']).size().reset_index(name='count')
result_df = result_df.sort_values('count', ascending=False)

# Wyświetlenie wyników
print("Liczba ofiar interwencji policji według rasy i objawów choroby psychicznej:")
print(result_df.to_string(index=False))
print("\n")

# Wizualizacja
plt.figure(figsize=(12, 6))

color_dict = {True: '#ff9999', False: '#66b3ff'}

for mental_illness in result_df['signs_of_mental_illness'].unique():
    race_counts = result_df[result_df['signs_of_mental_illness'] == mental_illness]['count']
    plt.bar(race_counts.index, race_counts.values, color=color_dict[mental_illness], label=f'Mental illness: {mental_illness}')

plt.xlabel('Race')
plt.ylabel('Number of Victims')
plt.title('Number of Police Shooting Victims by Race and Mental Health Indicators')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nAnaliza wyników:")
print(f"Suma ofiar: {result_df['count'].sum()}")
print(f"Najwięcej ofiar: {result_df.iloc[0]['race']} - {result_df.iloc[0]['count']}")
print(f"Najmniej ofiar: {result_df.iloc[-1]['race']} - {result_df.iloc[-1]['count']}")

# point 3
# Funkcja do obliczenia odsetka ofiar z oznakami choroby psychicznej dla każdej rasy
def calculate_percentage(result_df):
    # Grupowanie danych według rasy i obliczenie liczby ofiar z chorobą psychiczną oraz wszystkich ofiar
    total_by_race = result_df.groupby('race')['count'].sum()
    mentally_ill_by_race = result_df[result_df['signs_of_mental_illness'] == True].groupby('race')['count'].sum()

    # Obliczanie procentu osób z oznakami choroby psychicznej dla każdej rasy
    percentage = (mentally_ill_by_race / total_by_race * 100).fillna(0)

    # Mapowanie procentu do odpowiedniej kolumny w DataFrame
    result_df['percentage_mentally_ill'] = result_df['race'].map(percentage)

    return result_df


# Wywołanie funkcji
result_df = calculate_percentage(result_df)

# Sprawdzenie, która rasa charakteryzuje się największym odsetkiem osób z oznakami choroby psychicznej
max_mental_illness_race = result_df.groupby('race')['percentage_mentally_ill'].max().idxmax()
max_percentage = result_df['percentage_mentally_ill'].max()

print(result_df)
print(f"Rasa z największym odsetkiem: {max_mental_illness_race} ({max_percentage}%)")

# point 4
# Konwersja kolumny 'date' na format daty
df['date'] = pd.to_datetime(df['date'])

# Dodanie kolumny oznaczającej dzień tygodnia
df['day_of_week'] = df['date'].dt.day_name()

# Zliczanie interwencji według dnia tygodnia
day_of_week_counts = df['day_of_week'].value_counts().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], fill_value=0
)

# Tworzenie wykresu kolumnowego
plt.figure(figsize=(10, 6))
day_of_week_counts.plot(kind='bar', color='skyblue')
plt.title('Liczba interwencji według dnia tygodnia')
plt.xlabel('Dzień tygodnia')
plt.ylabel('Liczba interwencji')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# URL strony z danymi o populacji
url_population = "https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population"

# URL strony z danymi o skrótach stanów
url_abbreviations = "https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations"

# Pobierz dane z obu stron
response_population = requests.get(url_population)
response_abbreviations = requests.get(url_abbreviations)

# Odczyt tabeli do DataFrame
data_population = pd.read_html(response_population.text, header=0)[0]
data_incidents = pd.read_html(response_abbreviations.text, header=0)[1]

# Usunijmy spacje przed i po wartościach w kolumnie "State" w obu DataFrame'ach
data_population['State'] = data_population['State'].str.strip()
data_incidents['Name'] = data_incidents['Name'].str.strip()

# Porównajmy nazwy stanów w obu DataFrame'ach
common_columns = set(data_population.columns) & set(data_incidents.columns)
matching_columns = common_columns - {'Population'}

# Zmieńmy nazwę kolumny "Name" na "State" w drugim DataFrame'u
data_incidents = data_incidents.rename(columns={'Name': 'State'})

# Połączmy DataFrame'y
merged_data = pd.merge(data_population, data_incidents, on='State', how='left')

# Usunięcie wierszy z wartościami NaN -  czyszczenie danych
merged_data = merged_data.dropna()

# Zmieńmy nazwę kolumny "Name" na "State" w drugim DataFrame'u
merged_data = merged_data.rename(columns={'State': 'State_Name'})
merged_data = merged_data.rename(columns={'USPS': 'State'})
df = df.rename(columns={'state': 'State'})

# Połącz merged_data z df na podstawie kolumny "State"
merged_data = pd.merge(merged_data, df, on='State', how='left')
merged_data = merged_data.rename(columns={'Census population, April 1, 2020 [1][2]': 'Population'})

# Usunijmy brakujące wartości, jeśli wystąpią
merged_data = merged_data.dropna(subset=['Population'])

# Dodajmy kolumnę 'Number of incidents'
incidents_count = merged_data.groupby('State').size().reset_index(name='Number of incidents')
merged_data = pd.merge(merged_data, incidents_count, on='State', how='left')

# Zgrupujmy dane według stanu i policzmy liczbę incydentów
grouped_data = merged_data.groupby('State').agg({
    'Population': 'first',
    'Number of incidents': 'count'
}).reset_index()

# Wykonajmy liczenie incydentów na 1000 mieszkańców
grouped_data['Incidents_per_1000'] = grouped_data['Number of incidents'] / grouped_data['Population'] * 1000

# Uporządkujmy dane według liczby incydentów na 1000 mieszkańców
grouped_data = grouped_data.sort_values('Incidents_per_1000', ascending=False)

# Wydrukujmy wyniki działania
print(grouped_data[['State', 'Population', 'Number of incidents', 'Incidents_per_1000']].to_string(index=False))

# Wydrukujmy pierwsze 10 wierszy
print()
print("\nTop 10 states by incidents per 1000 residents:")
print(grouped_data[['State', 'Population', 'Number of incidents', 'Incidents_per_1000']].head(10).to_string(index=False))


