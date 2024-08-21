
def main():
    for liczba in range(101):
        if liczba == 0: continue
        if liczba % 5 == 0:
            print(liczba)
            print(liczba ** 3)


if __name__ == "__main__":
    main()
