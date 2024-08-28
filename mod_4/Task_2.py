import logging

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    print("Podaj działanie:")
    print("1 - Dodawanie")
    print("2 - Odejmowanie")
    print("3 - Mnożenie")
    print("4 - Dzielenie")

    try:
        wybor = int(input("Podaj numer działania: "))

        if wybor < 1 or wybor > 4:
            raise ValueError("Nieprawidłowy numer działania.")

        ilosc_arg = int(input("Podaj liczbę argumentów: "))

        if ilosc_arg <= 0:
            raise ValueError("Musisz podać co najmniej jeden argument.")

        args = []
        for i in range(ilosc_arg):
            while True:
                try:
                    arg = float(input(f"Podaj argument {i + 1}: "))
                    args.append(arg)
                    break
                except ValueError:
                    print("Błąd: Podana wartość nie jest liczbą. Spróbuj ponownie.")

        match wybor:
            case 1:
                wynik = suma_liczb(args)
                operacja = "Dodawanie"
            case 2:
                wynik = odejmowanie_liczb(args)
                operacja = "Odejmowanie"
            case 3:
                wynik = monozenie_liczb(args)
                operacja = "Mnożenie"
            case 4:
                wynik = dielenie_liczb(args)
                operacja = "Dzielenie"
            case _:
                raise ValueError("Nieprawidłowy numer działania.")

        logging.info(f"Działanie: {operacja}")
        logging.info(f"Argumenty: {args}")

        print(f"Wynik: {wynik:.2f}")

    except ValueError as e:
        print(f"Błąd: {str(e)}")

def suma_liczb(args):
    return sum(args)

def odejmowanie_liczb(args):
    return args[0] - sum(args[1:])

def monozenie_liczb(args):
    wynik = 1
    for arg in args:
        wynik *= arg
    return wynik

def dielenie_liczb(args):
    wynik = args[0]
    for arg in args[1:]:
        wynik /= arg
    return wynik

if __name__ == "__main__":
    main()
