data_text = "Pies"


def analize(text):

    slownik = dict(length=len(text), letters=[key for key in data_text], big_letters=text.upper(),
                   smal_letters=text.lower())
    return slownik


print(analize(data_text))
