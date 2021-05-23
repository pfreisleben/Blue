# 04 - Utilizando funções e listas faça um programa que receba uma data no formato
# DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Valide a data e
#  retorne NULL caso a data seja inválida.
dataLista = []


def dataEmLista(data):
    for i in data:
        if i in '1234567890':
            dataLista.append(i)
        elif i != '/':
            print(f'Data informada incorreta.')
            return "NULL"
            break


def retornaMes(mes):
    if mes == '01':
        return 'Janeiro'
    elif mes == '02':
        return 'Fevereiro'
    elif mes == '03':
        return 'Março'
    elif mes == '04':
        return 'Abril'
    elif mes == '05':
        return 'Maio'
    elif mes == '06':
        return 'Junho'
    elif mes == '07':
        return 'Julho'
    elif mes == '08':
        return 'Agosto'
    elif mes == '09':
        return 'Setembro'
    elif mes == '10':
        return 'Outubro'
    elif mes == '11':
        return 'Novembro'
    elif mes == '12':
        return 'Dezembro'


def rodar():
    data = input("Informe a data em formado de dd/mm/aaaa: ")
    dataEmLista(data)
    dia = dataLista[0]+dataLista[1]
    mes = retornaMes(dataLista[2] + dataLista[3])
    ano = dataLista[4] + dataLista[5] + dataLista[6] + dataLista[7]
    extenso = dia + " de " + mes + " de " + ano
    return extenso


print(rodar())
