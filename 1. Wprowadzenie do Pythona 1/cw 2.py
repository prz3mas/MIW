imie = "Przemyslaw"
nazwisko = "Markowski"

akapit = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz " \
         "pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków " \
         "później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował " \
         "się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, " \
         "a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na " \
         "komputerach osobistych, jak Aldus PageMaker "

print("W tekscie jest {0} liter {1} , oraz {2} liter {3} ".format(akapit.count(imie[2]), imie[2],
                                                                  akapit.count(nazwisko[3]), nazwisko[3]))
