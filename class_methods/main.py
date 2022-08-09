class Item:
    pay_rate=0.8#  pay rate after 20% discount
    all=[]
    def __init__(self,name:str,price:float,quantity=0):# sepecify data types for incoming Input

        # assertion for incoming input before they get assigned to instance Attribnues
        assert price>=0, f"price {price} is not more than zero"
        assert quantity>=0, f"quantity {quantity} is not more than zero"

        # Assignment of self Attibutes
        print(f"the object is created {name}")
        self.name=name
        self.price=price
        self.quantity=quantity

        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price*self.quantity


    def apply_discount(self):
        self.price=self.price*self.pay_rate

    def __repr__(self):  # This is a Magic Method  which is used to re
        return f"item('{self.name}',{self.price},{self.quantity})"
   


item1=Item("Phone",100,1)
item2=Item("Laptop",1000,3)
item3=Item("Cable",10,5)
item4=Item("Mouse",50,5)
item5=Item("Keyboard",75,5)

print(Item.all)

# print name attribute of all instances
for instance in Item.all:
    print(instance.name)
