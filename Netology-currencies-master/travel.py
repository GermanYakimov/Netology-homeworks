import osa


def lengths_get():
    lengths = []
    with open('travel.txt', 'r') as file:
        lengths_tmp = file.read().replace(':', '').replace('mi', 'Miles').replace(',', '').split('\n')

    for length in lengths_tmp:
        tmp_length = length.split()
        tmp_length = {'from-to': tmp_length[0], 'length': float(tmp_length[1]), 'quantity': tmp_length[2]}

        lengths.append(tmp_length)

    return lengths


def lengths_count(lengths):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    sum_length = 0

    for length in lengths:
        sum_length += client.service.ChangeLengthUnit(
            LengthValue=length['length'], fromLengthUnit=length['quantity'], toLengthUnit='Kilometers')

    return int(sum_length)


lengths = lengths_get()
print(lengths_count(lengths))

# print(client.service.ChangeLengthUnit(LengthValue=length, fromLengthUnit=fromUnit, toLengthUnit=toUnit))
