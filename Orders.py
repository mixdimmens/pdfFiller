import pandas as pd
import gspread
import re
from oauth2client.service_account import ServiceAccountCredentials


credentailsPath = '/Users/maximdiamond/Code/DJi/scripts/pdfScripts/production-report-api-739f8c22e6b8.json'
class Order(object):

    def __init__(self, oso, workbook, sheet_index= 0):
        self.oso = oso
        self.workbook = workbook
        self.sheet_index = sheet_index

    def get_sheet(self):
        # define the scope
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

        # add credentials to the account
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentailsPath, scope)

        # authorize the clientsheet 
        client = gspread.authorize(creds)

        self.workbook = client.open(self.workbook)
        self.sheet = pd.DataFrame(self.workbook.get_worksheet(self.sheet_index).get_all_records())
        self.sheet = self.sheet[self.sheet['M2 Job Code'].str.len() >= 1]

    def get_rows(self):
        self.get_sheet()
        self.order = self.sheet.loc[self.sheet['OSO'] == self.oso].to_dict('list')

    def data_strip(self):
        self.get_rows()
        for item in self.order:
            self.order[item] = re.sub("[^A-Za-z0-9#/,$.& -]", "", str(self.order[item]))

    def get_keys(self):
        self.data_strip()
        self.keys = self.order.keys()

    def __repr__(self):
        return str(self.order)

