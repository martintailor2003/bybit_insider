import requests
import time
import hashlib
import hmac
import json
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



#mode=/normal/test/copy/copytest
class bybit():
    def __init__(self,api,secret,mode='normal'):
        self=self
        self.api_key = api
        self.secret_key = secret
        self.mode = mode
        if self.mode == 'normal' or self.mode == 'copy':
            self.client_normal_copy()
        else:
            self.client_test()
            
    def client_normal_copy(self):
        self.httpClient=requests.Session()
        self.recv_window=str(5000)
        self.url="https://api.bybit.com"
    
    def client_test(self):
        self.httpClient=requests.Session()
        self.recv_window=str(5000)
        self.url="https://api-testnet.bybit.com"


    def HTTP_Request(self,endPoint,method,payload):
        global time_stamp
        time_stamp=str(int(time.time() * 10 ** 3))
        signature=self.genSignature(payload)
        headers = {
            'X-BAPI-API-KEY': self.api_key,
            'X-BAPI-SIGN': signature,
            'X-BAPI-SIGN-TYPE': '2',
            'X-BAPI-TIMESTAMP': time_stamp,
            'X-BAPI-RECV-WINDOW': self.recv_window,
            'Content-Type': 'application/json'
        }
        if(method=="POST"):
            response = self.httpClient.request(method, self.url+endPoint, headers=headers, data=payload)
        else:
            response = self.httpClient.request(method, self.url+endPoint+"?"+payload, headers=headers)
           
        return(response.text)

    def genSignature(self,payload):
        param_str= str(time_stamp) + self.api_key + self.recv_window + payload
        hash = hmac.new(bytes(self.secret_key, "utf-8"), param_str.encode("utf-8"),hashlib.sha256)
        signature = hash.hexdigest()
        return signature
            
    def market_order(self,symbol,side,qty,reduce_only=False,idx=0,params={}):
        #Create Order
        if self.mode == 'copy' or self.mode == 'copytest':
            endpoint="/contract/v3/private/copytrading/order/create"
        else:
            endpoint="/contract/v3/private/order/create"
 
        method="POST"
        reduceonly = 'false'
        if reduce_only:
            reduceonly = 'true'
                            
        params_f = {
            "symbol": symbol,
            "side": side,
            "positionIdx": idx,
            "orderType": "Market",
            "qty": str(qty),
            "reduce_only": reduceonly,
            **params
        }

        params_f = str(params_f).replace("'",'"')
        print(params_f)
        return self.HTTP_Request(endpoint,method,params_f)
    
    
    
    def limit_order(self,symbol,side,qty,price,timeInForce='GoodTillCancel',reduce_only=False,idx=0,params={}):
        #Create Order
        if self.mode == 'copy' or self.mode == 'copytest':
            endpoint="/contract/v3/private/copytrading/order/create"
        else:
            endpoint="/contract/v3/private/order/create"
            
        method="POST"        
        reduceonly = 'false'
        if reduce_only:
            reduceonly = 'true'
            
        params = {
            "symbol": symbol,
            "side": side,
            "price": str(price),
            "positionIdx": idx,
            "orderType": "Limit",
            "qty": str(qty),
            "reduce_only": reduceonly,
            "timeInForce": timeInForce,
            **params
        }
        params = str(params).replace("'" , '"')
        print(params)
        return self.HTTP_Request(endpoint,method,params)
    
    
    def get_orders(self,type=None,status=None,id=None):
        #Get orders
        if self.mode == 'copy' or self.mode == 'copytest':
            endpoint="/contract/v3/private/copytrading/order/list"
        else:
            endpoint="/contract/v3/private/order/list"
        
        method="GET"
        params= '' #settleCoin=USDT
        orders = json.loads(self.HTTP_Request(endpoint,method,params))['result']['list']

        selected_orders = []
        for order in orders:
            o_type = order['orderType']
            o_status = order['orderStatus']
            o_id = order['orderId']
            if (type==None or type==o_type) and (status==None or status==o_status) and (id==None or id==o_id):
                selected_orders.append(order)
               
                
        return selected_orders
