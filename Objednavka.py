from Connection_database import Connection


class Objednavka():
    def __init__(self, order_id):
        sql = "SELECT * FROM XPobjednavky WHERE id = {0}".format(order_id)
        order = Connection().executeQuery(sql)[0]

        self.id = order[0]
        self.table_id = order[1]
        self.food_id = order[2]
        self.count_order = order[3]
        self.count_made = order[4]
        self.count_paid = order[5]
        

    def max_count_of_how_much_pieces_to_pay(self):
        return self.count_order - self.count_paid


    def update_count_paid(self, count_of_pieces_to_pay):
        sql = "UPDATE XPobjednavky SET pocet_zaplatenych = pocet_zaplatenych + {0} WHERE id = {1}".format(
            count_of_pieces_to_pay, self.id)
        Connection().execute(sql)

    

    
