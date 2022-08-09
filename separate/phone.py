from item import Item
class Phone(Item):

    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):# sepecify data types for incoming Input
        # call super() method to have access to all Attributes
        super().__init__(name,price,quantity)
        #assertion for incoming input before they get assigned to instance Attribnues
       
        assert broken_phones>=0, f"broken {broken_phones} is not more than zero"

        # Assignment of self Attibutes
        print(f"the object is created {name}")
      
        self.broken_phones=broken_phones