"""
A module for managing a phone book.
"""

# This module is provided as part of Exercise Set 3.3

from typing import Optional
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def is_phone_number(number:str)->bool:
    """
    Checks if the argument is an 8-digit phone number.

    >>> is_phone_number('12345678')
    True

    >>> is_phone_number('12 34 56 78')
    True
    """
    no_spaces = number.replace(" ", "")
    return len(no_spaces) == 8 and no_spaces.isdigit()
       


def format_phone_number(number:str)->str:
    """
    Returns a string with the given phone number formatted grouping pairs of digits.

    Precondition: the string number is a phone number (see is_phone_number)

    >>> is_phone_number('12345678')
    '12 34 56 78'
    """
    assert is_phone_number(number), "number must be phone number"
    no_spaces = number.replace(" ", "")
    pairs = [ no_spaces[i:i+2] for i in range(0,8,2) ]
    return " ".join(pairs)

def get(name:str)->Optional[str]:
    """
    Returns the contact information for the given name or None if  there is no contact under the given name.
    """
    if is_present(name):
        return __contacts[name]
    else:
        return None

def add_or_update(name:str,phone:str)->None:
    """
    Add or updates (if already present) the contact information for the given name.

    Raises: ValueError if phone is not in 8-digit format.
    """
    if is_phone_number(phone):
        __contacts[name] = format_phone_number(phone)
    else:
        raise ValueError(f'{phone!r} is not in 8-digit format.')

def delete(name:str)->None:
    """
    Removes the contact information for the given name.

    Precondition: name is present.
    """
    del __contacts[name]

def is_present(name:str)->bool:
    """
    Returns whether there is a contact for the given name.
    """
    return name in __contacts

# This module is stateful, it uses the following data structure to maintain the
# phone book. This structure is meant to for internal use only.
__contacts: dict[str, str] = {}

def list_all() -> None:
    if not __contacts:
        print('der er ingen')
    for name, phone in __contacts.items():
        print(f'{name}, {phone}')

def main():
    yesno = input('Hvad vil du \n1, Brug phonebook\n2. Exit\n')
    clear()
    if yesno == 1 or yesno == "1":
        while yesno == "1":
            clear()
            print("hej velkommen til din phonebook")
            print("Hvad vil du????\n1.Se alle kontakter.\n2. Tilføj kontakt")

            n = input("Vælg: ")
            
            clear()
            match n:
                case 1 | "1":
                    print("liste over kontakter: \n")
                    list_all()
                    
                case 2 | "2":
                    name = input("indtast navn: ")
                    number = input("Indtast nummer: ").strip()
                    try:
                        add_or_update(name, number)
                        print('Personen er nu tilføjet')
                        
                    except ValueError as Wheee:
                        print(f'{Wheee}')
                    
                case _:
                    print('ugyldigt')
            yesno = input('Vil du fortsætte? \n1, Brug phonebook\n2. Exit\n')


                
    elif yesno == 2 or yesno == "2":
        clear()
    else:
        print('forkert input, prøv igen!\n')
        clear()
        main()
    clear()    


if __name__ == "__main__":
    main()
