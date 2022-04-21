from Orders import Orders

class Upholstery(Orders):

    def __init__(self, workbook,  oso, com= True, sheet_index= 0):
        super().__init__(workbook, sheet_index=0)
        self.com = com
        self.oso = oso

    def select_order(self):
        if self.com:
            pass
        else:
            self.sheet_index = 1
        self.order(self.oso)
        
    def data_gen(self):
        self.select_order()
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

            