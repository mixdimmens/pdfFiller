from Orders import Orders
from UpholsteryOrder import Upholstery

book_name = 'DJ Production DB'

oso_23800 = Orders(book_name, 1)
oso_23800.get_sheet()
# oso_23800.data_strip()

print(oso_23800.sheet.loc[oso_23800.sheet['OSO'] == '23665'])
# print(oso_23800.order('23665'))

# oso_23800 = Upholstery(23663, book_name, False)
# oso_23800.data_gen()

# keys = oso_23800.keys

# print(keys)