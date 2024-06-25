from typing import Optional, Protocol, TypedDict



class Order(TypedDict):
    in_stock : bool 
    payment_successful : bool 
    address_valid : bool


class Handler(Protocol):
    def set_next(self, handler : "Handler") -> None: ...
    def handle(self, request : Order) -> None: ...
    
    
    
class BaseHandler(Handler):
    def __init__(self) -> None:
        self.next : Optional[Handler] = None
        
    def set_next(self, handler : Handler) -> None:
        self.next = handler
        
    def handle(self, request: Order) -> None:
        if self.next is not None:
            self.next.handle(request)
            
            
class StockCheckHandler(BaseHandler):
    def handle(self, request : Order) -> None:
        if request["in_stock"]:
            print("StockCheckHandler: Stock is available.")
            super().handle(request)
        else:
            print("StockCheckHandler: Out of stock, cannot process order.")
            
            
class PaymentCheckHandler(BaseHandler):
    def handle(self, request : Order) -> None:
        if request['payment_successful']:
            print("PaymentCheckHandler: Payment successful.")
            super().handle(request)
        else:
            print("PaymentCheckHandler: Payment failed, cannot process order.")
            
            
class AddressCheckHandler(BaseHandler):
    def handle(self, request : Order) -> None:
        if request['address_valid']:
            print("AddressCheckHandler: Address is valid.")
            super().handle(request)
        else:
            print("AddressCheckHandler: Invalid address, cannot process order.")






if __name__ == '__main__':
    address_handler = AddressCheckHandler()
    
    payment_handler = PaymentCheckHandler()
    payment_handler.set_next(address_handler)
    
    
    stock_handler = StockCheckHandler()
    stock_handler.set_next(payment_handler)
    
    order : Order = {"in_stock" : True, "payment_successful" : True, "address_valid" : True}
    
    stock_handler.handle(order)