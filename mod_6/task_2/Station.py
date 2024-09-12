import csv

from sqlalchemy import Column, Integer, String, Float

from mod_6.task_2.Database import Base


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
