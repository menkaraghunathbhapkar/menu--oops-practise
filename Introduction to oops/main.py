class Item:
    pass
item1=Item()
item1.name="The Name is Menka Bhapkar"
item1.price=5
item1.quantity=20
item2=Item()
item2.name="The Name is Menu Bhapkar"
item2.price=5
item2.quantity=20


print(item1.name)
print(item1.price)
print(item1.quantity)
print(item2.name)
print(item2.price)
print(item2.quantity)
print(type(item2.name))
print(type(item2.price))
print(type(item2.quantity))
print((item1.__class__.__name__))
print(type(item1.__class__.__name__))