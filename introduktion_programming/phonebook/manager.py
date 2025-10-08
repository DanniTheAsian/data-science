import phone_book as wawawu

def main():
    yesno = input('Hvad vil du \n1, Brug phonebook\n2. Exit\n')
    wawawu.clear()
    if yesno == 1 or yesno == "1":
        while yesno == "1":
            wawawu.clear()
            print("hej velkommen til din phonebook")
            print("Hvad vil du????\n1. Se alle kontakter.\n2. Tilføj kontakt\n3. Find person \n4. Fjern person")

            n = input("Vælg: ")
            
            wawawu.clear()
            match n:
                case 1 | "1":
                    print("liste over kontakter:")
                    wawawu.list_all()
                    print("\n")
                case 2 | "2":
                    name = input("indtast navn: ")
                    number = input("Indtast nummer: ").strip()
                    try:
                        wawawu.add_or_update(name, number)
                        print('Personen er nu tilføjet eller opdateret')
                        
                    except ValueError as Wheee:
                        print(f'{Wheee}')
                case 3 | "3":
                    name = input("Hvem vil du finde?: ")

                    contact = wawawu.get(name)
                    print(f"telefon til {name} er {contact}")
                case 4 | "4":
                    name = input("hvem vil du slette?\n")
                    if name in wawawu.__contacts:
                        yesno = input("hvaaaa er du sikker på vil slette en kontaktperson?\n1. Ja\n2. Nej\n").lower()

                        match yesno:
                            case 1 | "1" | "ja":
                                wawawu.delete(name)
                                print(f"{name} er nu slettet for altid... Selv tak!")
                            case 2 | "2" | "nej":
                                print("nåår du valgte at fortryde.. tænkte det nok.. Stupido")
                            case _:
                                print('Forkert input!! Start forfra')
                    elif name not in wawawu.__contacts:
                        print(f"personen: {name} kan ikke slettes da han ikke eksisterer i din bog")
                case 5 | "5":
                    name = input("find ud af om personen eksisterer:\n")
                    if name in wawawu.__contacts:
                        print("Ja personen eksisterer sgu")
                    else:
                        print("Næ, personen eksisterer ikke")
                case _:
                    print('ugyldigt')
            yesno = input('Vil du fortsætte? \n1, Brug phonebook\n2. Exit\n')
           
    elif yesno == 2 or yesno == "2":
        wawawu.clear()
    else:
        print('forkert input, prøv igen!\n')
        wawawu.clear()
        main()
    wawawu.clear()    


if __name__ == "__main__":
    main()
