def age_Check():
    age = input("podaj wiek:\n")
    if age.isdigit() == False:
        exit("Wiek musi być liczbą albo podana liczba nie jest całkowita")
    if int(age) >= 120 or int(age) < 18:
        exit(f"Ludzi w wieku {age} nie obsługujemy")
    else:
        return int(age)

def gend_Check():
    gender = input("\nPodaj plec [K/M]:\n").upper()
    if gender == "K":
        print("Jesteś Kobietą")
    elif gender == "M":
        print("Jesteś Meżczyzną")
    else:
        exit("Wybor nieprawidlowy, wprowadz poprawnie K lub M")
    return gender

def regio_Check():
    region = input("\nWybierz region (EUR/USA):\n").upper()
    if region == "EUR":
        print("Wybrałeś region EUR (Europa)\n")
    elif region == "USA":
        print("Wybrałeś region USA (Stany Zjednoczone)\n")
    else:
        exit("Wybor nieprawidlowy, wprowadz poprawnie EUR lub USA")
    return region

def app_init():
    age = age_Check()
    gender = gend_Check()
    region = regio_Check()
    if region == "USA" and age < 21:
        exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
    if age >= 30 and gender == 'K':
        print("Otrzymujesz aperol spritz pierwszy gratis!\n")
    if int(age) < 40:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów\n")
    elif age >= 40:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów\n")
        print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem\n")

app_init()