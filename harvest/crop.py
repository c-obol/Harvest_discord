import data

class crop():
    def __init__(self, first_sale_price, first_purchase_price, type, grow_time):
        self.type = type
        self.grow_time = grow_time

        self.sale_price = first_sale_price
        self.purchase_price = first_purchase_price

        self.recent_max = 10
        self.recent_list_type = []
        self.recent_list_amount = []

        self.sale_amount = 0
        self.purchase_amount = 0

    def sale(self, user_id):
        pass

    def purchase(self, user_id):
        pass

    def renew(self):
        pass