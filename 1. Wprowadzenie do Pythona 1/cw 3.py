liczby = [3, 543, 12, 35, 67, 345]

print("{:>100}".format("Tu mamy przyklad wyrownania tekstu do prawej"))
print("{:.12}".format("Tu mamy przyklad uciecia tekstu do 12 znakow"))
print('{:.{prec1}} = {:.{prec2}f}'.format('PIliczba', 3.14159265359, prec1=2, prec2=4))
print('{l[3]}  {l[0]}  l{l[4]}'.format(l=liczby))
print('{:+d}'.format(42))
