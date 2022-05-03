from Orders import Order
from UpholsteryOrder import Upholstery

book_name = 'COM-COL_PaperworkInfo'

# oso_23800 = Order(23663, book_name, 1)
# oso_23800.data_strip()

oso_23800 = Upholstery(23663, book_name, False)
oso_23800.data_gen()

print(oso_23800)

# keys = oso_23800.keys

# print(keys)