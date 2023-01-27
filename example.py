import bybit_insider

client = bybit_insider.bybit(api='xxxxxxxxxxxxxxxxxxx' ,secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',mode='test')

#market order
client.market_order(symbol= "BTCUSDT",side="Buy",qty=0.1,reduce_only=False,params={"stopLoss": '10000'})

#limit order
client.limit_order(symbol= "BTCUSDT",side="Buy",price=19000,qty=0.1,reduce_only=False,params={"stopLoss": '10000',"takeProfit": '80000'})

#get orders
orders = client.get_orders() #will return to all recent and historical orders
orders =client.get_orders(type='Limit',status='New') #filtered orders







