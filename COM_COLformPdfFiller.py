from fillpdf import fillpdfs
from UpholsteryOrder import Upholstery


def COM_COl_form_filler(oso, com=True):
    
    pdf_to_fill_path = '/Users/maximdiamond/Documents/DJ/forms_reference/forms/COM_COL Layout Instructions_Fillable.pdf'

    # oso = 23807
    workbook = 'COM-COL_PaperworkInfo'
    # com = True

    Order = Upholstery(oso, workbook, com)
    Order.data_gen()

    fields = {
    'dj_order_number': Order.order_id,
    'fabric_description': Order.material,
    'fabric_description_1': '',
    'fabric_description_2': '',
    'product': Order.product,
    'product_1': '',
    'product_2': '',
    'Regular': '',
    'Railroaded': ''
    }

    outPdf = '/Users/maximdiamond/Documents/DJ/forms_reference/forms/UpholsteryForms/{} COM_COL Layout Instructions.pdf'.format(Order.oso)

    fillpdfs.write_fillable_pdf(pdf_to_fill_path, outPdf, fields)