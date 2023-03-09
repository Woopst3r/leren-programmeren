def fibonacci(getal):
    getallen = [0, 1]
    for index in range(2, getal):
        getallen.append(getallen[index-1]+getallen[index-2])
    return getallen

def gulde_snede(fibonacci):
    laastegetal = fibonacci[-1]
    eenna_laastegetal = fibonacci[-2]
    return laastegetal / eenna_laastegetal

herhaal = 10
print(fibonacci(herhaal))
print(gulde_snede(fibonacci(herhaal)))