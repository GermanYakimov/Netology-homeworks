import osa


def convert_temp(temperature, fromUnit, toUnit):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    return client.service.ConvertTemp(Temperature=temperature, FromUnit=fromUnit, ToUnit=toUnit)


def temperatures_get():
    temps = dict()
    with open('temps.txt', 'r') as file:
        start_temps = file.read()
        start_temps = start_temps.replace('F', 'degreeFahrenheit')
        start_temps = start_temps.replace('K', 'kelvin')
        start_temps = start_temps.replace('C', 'degreeCelcius')
        start_temps = start_temps.split('\n')

        for day, temp in enumerate(start_temps):
            tmp_temp = temp.split()
            temps['day' + str(day + 1)] = {'quantity': tmp_temp[1], 'value': int(tmp_temp[0])}

    return temps


def avg_count(temps):
    sum = 0

    for day in temps:
        sum += convert_temp(temps[day]['value'], temps[day]['quantity'], 'degreeCelsius')

    return int(sum/len(temps))


temps = temperatures_get()
print(avg_count(temps))
