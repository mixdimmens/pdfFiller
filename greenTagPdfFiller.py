from fillpdf import fillpdfs
from UpholsteryOrder import Upholstery

def green_tag_filler(oso, com=True):


    pdf_to_fill_path = '/Users/maximdiamond/Documents/DJ/forms_reference/forms/Blank Green Tag.pdf'
    workbook = 'COM_COL_PaperworkInfo'

    # create order object
    Order = Upholstery(oso, workbook, com)
    Order.data_gen()

    # fields 
    fields = {
    'Decca_Code': Order.job_code,
    'Material_Name': Order.material,
    'Product': Order.product,
    'OSO_No': str(Order.oso),
    'OPO_No': Order.opo,
    'Log No': ''
    }

    outPdf = '/Users/maximdiamond/Documents/DJ/forms_reference/forms/UpholsteryForms/{} Green Tag.pdf'.format(fields['OSO_No'])

    fillpdfs.write_fillable_pdf(pdf_to_fill_path, outPdf, fields)