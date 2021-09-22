



shopping_card = {
    'banana': 3,
    'apple':5,
    'milk':10,
    'beer':12
    }

price = 0

prices = {'banana': 0.60,
          'beer': 1.10,
          'milk': 1.70,
          'apple' :0.60,
          'coca cola': 1.20,
          'kiwi':0.70}

for i in shopping_card.keys():
    price = price + shopping_card[i] * prices[i]

print(price)

