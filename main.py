from COM_COLformPdfFiller import COM_COl_form_filler
from greenTagPdfFiller import green_tag_filler

# input OSO number here:
oso = 23788

# var is True if COM, False if COL
com = True

# functions to create the documents
green_tag_filler(oso, com)
COM_COl_form_filler(oso, com)