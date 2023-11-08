def romanNumeral(num):
    if num > 999 or num < 0:
        return False

    romanNumber = ''
    
    centenas = int(num / 100)
    match centenas: 
        case 9 :
            romanNumber += 'CM'
        case 8 | 7 | 6 | 5:
            romanNumber += 'D' + ('C' * (centenas-5))
        case 4 :
            romanNumber += 'CD'
        case 3 | 2 | 1:
            romanNumber += 'C' * centenas
        case 0 :
            romanNumber += ''
    
    num = num - (centenas * 100)

    dezenas = int((num/10))
    match dezenas: 
        case 9 :
            romanNumber += 'XC'
        case 8 | 7 | 6 | 5:
            romanNumber += 'L' + ('X' * (dezenas-5))
        case 4 :
            romanNumber += 'XL'
        case 3 | 2 | 1:
            romanNumber += 'XXX' * dezenas
        case 0 :
            romanNumber += ''

    num = num - (dezenas * 10)

    unidades = num
    match unidades: 
        case 9 :
            romanNumber += 'IX'
        case 8 | 7 | 6 | 5:
            romanNumber += 'V' + ('I' * (unidades-5))
        case 4 :
            romanNumber += 'IV'
        case 3 | 2 | 1:
            romanNumber += 'III' * unidades
        case 0 :
            romanNumber += ''
    
    return romanNumber


number = int(input('indique um número: '))
print(number, "corresponde a", romanNumeral(number), "em numeração romana")