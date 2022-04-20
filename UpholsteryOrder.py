from Orders import Order

class Upholstery(Order):

    def __init__(self, oso, workbook,  com= True, sheet_index= 0):
        super().__init__(oso, workbook, sheet_index=0)
        self.com = com

    def select_sheet(self):
        if self.com:
            pass
        else:
            self.sheet_index = 1
        self.data_strip()
        
    def data_gen(self):
        self.select_sheet()
        self.job_code = str(self.order['M2 Job Code'])
        self.opo = str(self.order['OPO'])
        self.order_id = 'OSO-' + str(self.oso) + '/' + 'OPO-' + self.opo + '/' + self.job_code
        self.product = str(self.order['Item']) + ', ' + str(self.order['Qty']) + 'x'
        if self.com:
            self.material = str(self.order['Mill']) + ' ' + str(self.order['Fabric Name']) + ' ' + str(self.order['Mfg. Code'])
        else:
            self.material = str(self.order['Tannery']) + ' ' + str(self.order['Leather Name']) + ' ' + str(self.order['Mfg. Code'])

    def __repr__(self):
        return 'job code: {}, opo: {}, oso: {}, order combo: {}, product: {}, material: {}'.format(self.job_code, self.opo, self.oso, self.order_id, self.product, self.material)

            