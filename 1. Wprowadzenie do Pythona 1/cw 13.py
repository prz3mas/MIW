lista = [
    {8: "Tymoteusz", 5: "Kazimierz", 4: "Wiola"},
    {12: "Johny", 14: "Stanislaw", 18: "Marian"},
    {23: "Zbych", 28: "Andrej", 21: "Katarina"}
    ]

for record in lista:
    for key in record:
        print("W pokoju nr %i mieszka %s" % (key, record[key]))

