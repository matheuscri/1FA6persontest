# Loja - estoque dicionario, item sao as coisas, valores a quantidade de cada item
# Eu posso adicionar novos items, alterar a quantidade de todos os items, vender um item ( - 1 no estoque)
# Hard
# Eu posso somar duas lojas diferentes e o estoque resultante vai ser a combinacao dos dois,
# isso deve retornar uma nova loja

# comentar a classe

class Store:

    def __init__(self, stock):
        self.stock = stock

    def sell(self, item):

        if item in self.stock.keys() and self.stock[item] > 0:
            self.stock[item] = self.stock[item] - 1

        else:
            print("Item is not ablle to sell")

    def add(self, item):

        if item in self.stock.keys():
            self.stock[item] = self.stock[item] + 1
        else:
            self.stock[item] = 1

    def set(self, item, number):

        self.stock[item] = number

    def __str__(self):
        return str(self.stock)


if __name__ == "__main__":

    collector_items = {
        "apple": 3,
        "banana": 3,
        "pera": 3,
        "cream": 5
    }

    loja1 = Store(collector_items)
    print(loja1)
