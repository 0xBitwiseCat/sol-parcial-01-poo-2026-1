from exchange import Stock, Order, BuyOrder, SellOrder, Transaction, ExchangeEngine


# stocks 
st1 = Stock('AAPL', 'Apple', 190.0)
st2 = Stock('TSLA', 'Tesla', 220.0)

# ordenes
c1 = BuyOrder('B1', 'Ana', 'AAPL', 10, 190.0)
s1 = SellOrder('S1', 'Luis', 'AAPL', 10, 190.0)

c2 = BuyOrder('B2', 'Maria', 'TSLA', 5, 210.0)
s2 = SellOrder('S2', 'Pedro', 'TSLA', 5, 225.0)


exchange_handler = ExchangeEngine()

for i in [c1, s1, c2, s2]:
    exchange_handler.place_order(i)

#exchange_handler.show_pending_orders()

transactions = exchange_handler.match_orders()
exchange_handler.show_pending_orders()

print("Transacciones...")
for i in transactions:
    i.get_summary()
                    
