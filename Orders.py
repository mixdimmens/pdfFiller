import pandas as pd
import gspread
import re
from oauth2client.service_account import ServiceAccountCredentials

class Orders(object):

    def __init__(self, workbook, sheet_index= 0):
        self.workbook = workbook
        self.sheet_index = sheet_index
    
    def get_sheet(self):
        # define the scope
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

        # add credentials to the account - json file must be located via at least a relative path
        creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/maximdiamond/Code/DJi/scripts/pdfScripts/production-report-api-739f8c22e6b8.json', scope)

        # authorize the clientsheet 
        client = gspread.authorize(creds)

        self.workbook = client.open(self.workbook)
        self.sheet = pd.DataFrame(self.workbook.get_worksheet(self.sheet_index).get_all_records())
        self.sheet = self.sheet[self.sheet['M2 Job Code'].str.len() >= 1]

        for col in self.sheet:
            self.sheet[col] = self.sheet[col].apply(str)
        
        for col in self.sheet:
            self.sheet[col] = self.sheet[col].apply(lambda xx : re.escape(xx))

    # order method not yet working
    def order(self, oso, dict= True):
        self.get_sheet()
        if not dict:
            self.order = self.sheet.loc[self.sheet['OSO'] == oso]
        else:
            self.order = self.sheet.loc[self.sheet['OSO'] == oso].to_dict('list')

    # def get_keys(self, ): # non-working at the moment
    #     self.order()
    #     self.keys = self.order.keys()

    def __repr__(self):
        return str(self.sheet)

