
def main():
    kupno = {
        "Piekarnia": ["chleb", "bułki", "pączka"],
        "Warzywniak": ["marchew", "seler", "rukola"]
    }

    print("Lista zakupów")

    for sklep, produkty in kupno.items():
        print(f"Idę do {sklep.title()}, kupuję tu następujące rzeczy: {', '.join(p.title() for p in produkty)}.")

    suma_towarow = sum(len(produkty) for produkty in kupno.values())
    print(f"W sumie kupuję {suma_towarow} produktów.")

if __name__ == "__main__":
    main()