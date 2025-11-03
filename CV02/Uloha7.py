def obdlznik(sirka, znak="*"):
    print(sirka*znak)
    print(znak, end="")
    print(" " * (sirka -2), end="")
    print(znak)
    print(sirka*znak)

obdlznik (30, "#")
obdlznik(6)
obdlznik(19, "0")
          