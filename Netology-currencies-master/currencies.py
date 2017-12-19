import osa


def prices_get():
    flights = []
    with open('currencies.txt', 'r') as file:
        prices = file.read().replace(':', '').split('\n')

    for flight in prices:
        tmp_flight = flight.split()
        tmp_flight = {'from-to': tmp_flight[0], 'price': int(tmp_flight[1]), 'currency': tmp_flight[2]}

        flights.append(tmp_flight)

    return flights


def sum_price_count(flights):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')

    sum_price = 0
    for flight in flights:
        sum_price += client.service.ConvertToNum(
            amount=flight['price'], fromCurrency=flight['currency'], toCurrency='RUB', rounding=True)

    return int(sum_price)


# client.service.ConvertToNum(amount=amount, fromCurrency=fromCurrency, toCurrency=toCurrency, rounding=True)
flights = prices_get()
print(sum_price_count(flights))
