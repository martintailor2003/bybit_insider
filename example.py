import bybit_insider

client = bybit_insider.bybit(api='xxxxxxxxxxxxxxxxxxx' ,secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',mode='test')

client.market_order(symbol= "BTCUSDT",side="Buy",qty=0.1,reduce_only=False,params={"stopLoss": '10000'})

client.limit_order(symbol= "BTCUSDT",side="Buy",price=19000,qty=0.1,reduce_only=False,params={"stopLoss": '10000',"takeProfit": '80000'})



