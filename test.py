
def seven():
    test = 0
    for i in range(0,100):
        if i % 7 ==0:
            test = test + 1
            print(test)


def dictionaries():
    dict = {"name":"lol", "name1":"lol", "name2":"lol"}
    print(dict.values())

if __name__ == "__main__":
    seven()
    dictionaries()