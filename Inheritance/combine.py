import csv
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
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('codesnippets/items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),


            )
    @staticmethod # just similar to regular methods

    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False



class Phone(Item):

    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):# sepecify data types for incoming Input
        # call super() method to have access to all Attributes
        super().__init__(name,price,quantity)
        #assertion for incoming input before they get assigned to instance Attribnues
       
        assert broken_phones>=0, f"broken {broken_phones} is not more than zero"

        # Assignment of self Attibutes
        print(f"the object is created {name}")
      
        self.broken_phones=broken_phones

       
phone1=Phone("menu",100,1,1)

phone2=Phone("sonu",200,20,1)

print(phone1.calculate_total_price())
print(Item.all)
print(Phone.all)
