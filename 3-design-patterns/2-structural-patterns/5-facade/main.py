


class OrderSystem:
    def place_order(self, pizza_type : str) -> bool:
        print(f"Order placed for a {pizza_type} pizza.")
        return True


class PaymentSystem:
    def make_payment(self, amount : float) -> bool:
        print(f"Payment of ${amount} made successfully.")
        return True


class DeliverySystem:
    def schedule_delivery(self, address : str) -> bool:
        print(f"Delivery scheduled to {address}.")
        return True



class PizzaOrderingFacade:
    def __init__(self) -> None:
        self.order_system = OrderSystem()
        self.payment_system = PaymentSystem()
        self.delivery_system = DeliverySystem()
    
    def order_pizza(self, pizza_type : str, amount : float, address : str) -> None:
        if self.order_system.place_order(pizza_type):
            if self.payment_system.make_payment(amount):
                self.delivery_system.schedule_delivery(address)
                print("Pizza ordered successfully!")



if __name__ == '__main__':
    facade = PizzaOrderingFacade()
    facade.order_pizza("Margherita", 15, "123 Main Street")
