class Stock: 
    def __init__(self, symbol, company, price):
        self.symbol = symbol
        self.company = company
        self.__price = price

    def get_price():
        return self.__price

    def set_price(price: float):
        # validar que el valor sea mayor a 0 si no asignar un valor por defecto
        if price < 0:
            self.__price = 0.0
        else:
            self.__price = price

class Order:
    def __init__(self, order_id, trader, symbol, quantity, price):
        self.order_id = order_id
        self.trader = trader 
        self.symbol = symbol
        self.quantity = quantity
        self.price = price

    def execute():
         pass

    def get_summary(self):
         print("****************************")
         print(f"Orden\n")
         print(f"Orden ID: {self.order_id}")
         print(f"Trader  : {self.trader}")
         print(f"Simbolo : {self.symbol}")
         print(f"Cantidad: {self.quantity}")
         print(f"Precio  : {self.price}\n")
         print(f"Fin de la orden")
         print("*****************************")

class BuyOrder(Order):
    def execute():
        print("Orden de compra ejecutada (?")

class SellOrder(Order):
    def execute():
        print("Orden de venta ejecutada (?")

class Transaction:
    def __init__(self, buy_order, sell_order, quantity, price):
        self.buy_order = buy_order
        self.sell_order = sell_order
        self.quantity = quantity
        self.price = price

    def get_summary(self):
        print("************************************")
        print("Resumen de la transaccion realizada")
        print("************************************")
        print("\n")
        self.buy_order.get_summary()
        print("\n")
        self.sell_order.get_summary()
        print("\n")
        print("************************************")

class ExchangeEngine:
    def __init__(self):
        self._buy_orders = []
        self._sell_orders = []

    def show_pending_orders(self):
        print("Ordenes pendientes para transacciones\n")
        print("Ordenes de compra:")
        for i in self._buy_orders:
             print(f"Orden ID: {i.order_id}, simbolo: {i.symbol}")
        print("\nOrdenes de venta:")
        for i in self._sell_orders:
             print(f"Orden ID: {i.order_id}, simbolo: {i.symbol}")
        print("Fin del resumen\n")

    def place_order(self, order):
        if isinstance(order, BuyOrder):
            self._buy_orders.append(order)
        if isinstance(order, SellOrder):
            self._sell_orders.append(order)

    def match_orders(self):
        matches = []
        transactions = []
        delete_i = False
        for i in range(len(self._buy_orders)):
            x = self._buy_orders[i]
            for j in range(len(self._sell_orders)):
                y = self._sell_orders[j]
                if y is None:
                    continue
                if x.symbol == y.symbol and x.price == y.price:
                    matches.append([x,y])
                    #print(f"Match between {x.order_id} and {y.order_id}")
                    self._sell_orders[j] = None
                    delete_i = True
                    break

            if delete_i:
                self._buy_orders[i] = None
                delete_i = False

        if len(matches) > 0:
            self._buy_orders = [i for i in self._buy_orders if i is not None]
            self._sell_orders = [i for i in self._sell_orders if i is not None]
            #print(f"{len(self._buy_orders)}, {len(self._sell_orders)}")
            for i in matches:
                tr = Transaction(i[0], i[1], i[0].quantity, i[0].price)
                transactions.append(tr)

        return transactions
