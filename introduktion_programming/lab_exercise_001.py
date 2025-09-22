def round_up(x:float)-> int:
    """
    FUNCTION:
    Rounds the given number upwards

    ARGS:
    x (float): the given number

    RETURN:
    int: a positive number greater or equal to x
    """
    return int(-(-x//1))

def bill_quota(bill:float, tip:float, people:int) -> int:
    """
    FUNCTION:
    Calculates how much a person should pay to cover the bill including tips

    ARGS:
    bill (float): amount a person has to pay
    tip (float): amount a person wants to tip in decimal
    people (int): amount of people who has to pay
    
    RETURN:
    quota that round up the total amount of each person needs to pay

    """
    if tip > 1:
        return "CANNOT BE GREATER THAN 1, DUMMY, TRY AGAIN!!!"
    if not isinstance(people, int):
        return"IT NEEDS TO BE AN INTERGER, DUMMY, TRY AGAIN"
    if people < 0:
        return " A PERSON  CANNOT BE 0, DUMMY"
    total = bill + bill * tip
    quota = round_up(total / people)
    return quota

print (bill_quota(200, 1,1.2))

    
