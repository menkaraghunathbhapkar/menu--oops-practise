class Item:
    def __init__(self,name:str,price:float,quantity=0):# sepecify data types for incoming Input

        # assertion for incoming input before they get assigned to instance Attribnues
        assert price>=0, f"price {price} is not more than zero"
        assert quantity>=0, f"quantity {quantity} is not more than zero"

        # Assignment of self Attibutes
        print(f"the object is created {name}")
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def calculate_total_price(self):
        return self.price*self.quantity
item1=Item("menu",100,10)
item2=Item("sonu",200,20)
item2.has_numpad=False
print(item1.name)
print(item2.has_numpad)
print(item2.calculate_total_price())
print(item1.calculate_total_price())

