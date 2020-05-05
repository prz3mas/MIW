

def temp(celc, temperature_type):
    if temperature_type == 'Fahrenheit':
        print('%i stopni celcjusa to %.3f Fahrenheitów ' % (celc, ((celc * 1.8) + 32)))
    elif temperature_type == 'Rankine':
        print('%i stopni celcjusa to %.3f Rankine' % (celc, ((celc + 273.15) * 1.8)))
    elif temperature_type == 'Kelvin':
        print('%i stopni celcjusa to %.3f Kelvinów' % (celc, (celc + 273.15)))
    else:
        print('Wprowadzono zły typ temperatury, proszę wybrać z: Fahrenheit, Rankine lub Kelvin')


temp(32, 'Fahrenheit')
temp(43, 'Rankine')
temp(76, 'Kelvin')
temp(54, 'Newton')