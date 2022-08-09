from urllib.parse import ParseResultBytes
from urllib.request import proxy_bypass


class Item:
    def total_price(self,x,y):
        return x*y


item1=Item()
item1.name="laptop"
item1.price=100
item1.quantity=10
result=item1.total_price(item1.price,item1.quantity)
print(f"Total price of laptop is:{result}")
