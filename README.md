# bybit_insider
Trading library for Bybit exchange. You can use for mainnet testnet copy and copytestnet.

 The project has several methods that can be used to place orders, such as "market_order" and 
 "limit_order". It takes several parameters on initialization, including an API key and secret key, 
 which are used to authenticate with the Bybit API. 
 The script also uses the requests library to make HTTP requests to the Bybit API. 
 The script is designed to work in different modes, such as normal trading, 
 test trading, copy trading and copytest trading. 
 The script also allows to use different types of order such as stop loss and take profit.
 
 
 
#bybit_insider.bybit(api='xxxxxxxxxxxxxx' ,secret='xxxxxxxxxxxxxxxx',mode='normal'/'test'/'copy'/'copytest')
#mandatory parameters: api,secret
#note: Normal mode is default

#market_order(symbol='BTCUSDT',  side='Buy'/'Sell',  qty='0.001'/'10.0',  reduce_only=False/True ,idx=0/1/2,  params={})
#mandatory parameters: symbol,side,qty
#note: If your account in 'One-Way Mode' idx have to be 0 (defaut value). In 'Hedge Mode' you have to use 1 for buy and 2 in case of sell.
#note: In copytrading there is not one way mode!!!

#limit_order(symbol='BTCUSDT',  side='Buy'/'Sell',  qty='0.001'/'10.0', timeInForce='GoodTillCancel', reduce_only=False/True, idx=0/1/2,  params={}):
#mandatory parameters: symbol,side,qty,price
#other timeinForce options: 'GoodTillCancel'/ 'ImmediateOrCancel'/ 'FillOrKill'/ 'PostOnly'

#you can add sl and tp using params: params={"stopLoss": '25000','takeProfit': '100000'} !!the number must be in string format str()!!

To use the library you have to put bybit_insider.py into your project folder and import bybit_insider into your python file.
__Check exmple.py for basic usecases of this library.__
