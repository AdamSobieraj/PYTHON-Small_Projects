import csv

from sqlalchemy import create_engine, Column, String, Float, ForeignKey, Integer, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Station(Base):
    __tablename__ = 'stations'

    id = Column(Integer, primary_key=True)
    station_id = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    name = Column(String)
    country = Column(String)
    state = Column(String)
    measurements = relationship("Measurement", back_populates="station")

class Measurement(Base):
    __tablename__ = 'measurements'

    id = Column(Integer, primary_key=True)
    station_id = Column(String, ForeignKey('stations.station_id'))
    date = Column(String)
    precip = Column(Float)
    tobs = Column(Float)
    station = relationship("Station", back_populates="measurements")


# Tworzenie bazy danych
engine = create_engine('sqlite:///climate.db')
Base.metadata.create_all(engine)

# Tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

# Funkcja do ładowania danych z pliku CSV
def load_measurements_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            yield {
                'station_id': row[0],
                'date': row[1],
                'precip': float(row[2]),
                'tobs': float(row[3])
            }

# Funkcja do ładowania danych z pliku CSV
def load_stations_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            yield {
                'station_id': row[0],
                'latitude': float(row[1]),
                'longitude': float(row[2]),
                'elevation': float(row[3]),
                'name': row[4],
                'country': row[5],
                'state': row[6]
            }

data_to_load_measure = list(load_measurements_data('resources/clean_measure.csv'))
data_to_load_station = list(load_stations_data('resources/clean_stations.csv'))

for item in data_to_load_measure:
    new_measurement = Measurement(**item)
    session.add(new_measurement)

for item in data_to_load_station:
    new_station = Station(**item)
    session.add(new_station)

session.commit()

result = session.execute(text("SELECT * FROM stations LIMIT 5")).fetchall()

if result:
    for row in result:
        print(f"Stacja: {row[1]} - Lokalizacja: ({row[2]}, {row[3]}) - Wysokość: {row[4]:.2f} m - Państwo: {row[6]} - Stan: {row[7]}")
else:
    print("Nie znaleziono danych dla podanego ID stacji.")