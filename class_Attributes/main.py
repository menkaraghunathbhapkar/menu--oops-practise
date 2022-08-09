class Item:
    pay_rate=0.8#  pay rate after 20% discount
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


    def apply_discount(self):
        self.price=self.price*self.pay_rate

item1=Item("menu",100,10)
item2=Item("sonu",200,20)
item2.has_numpad=False
print(item1.name)
print(item2.has_numpad)
print(item2.calculate_total_price())
print(item1.calculate_total_price())
print(Item.pay_rate)
print(item1.pay_rate)
# to see all attributes that are belonging to perticular instance
print(Item.__dict__)
print(item1.__dict__)

print(item1.price)
item1.apply_discount()
print(item1.price)


# we can assign class level Attribute to instance level Also
item2.pay_rate=0.5
print(item2.price)
item2.apply_discount()
print(item2.price)

item1=Item("Phone",100,1)
item2=Item("Laptop",1000,3)
item3=Item("Cable",10,5)
item4=Item("Mouse",50,5)
item5=Item("Keyboard",75,5)