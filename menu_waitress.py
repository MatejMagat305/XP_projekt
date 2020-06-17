from Food import FoodDatabase
from Connection_database import Connection
from Objednavka import Objednavka

class menu_waitress:
    
    def __init__(self):
        self.food_database = FoodDatabase()
        self.menu_options = {1: "Zobraziť ponuku jedál",
                             2: "Zadať novú objednávku",
                             3: "Stornovať objednávku [Nie je nakodene]",
                             4: "Zobraziť nevyplatene stoly",
                             5: "Vyplatiť stôl po častiach",
                             6: "Vyplatiť stôl naraz",
                             0: "Koniec"}

        
    def start(self):
        run = True
        while(run):
            print("=== MENU CASNIK ===")
            for option in self.menu_options:
                print("{}. {}".format(option, self.menu_options[option]))

            answer = self.get_answer( "Akcie", range(0, len(self.menu_options) + 2) )
            run = self.do_action(answer)


    def do_action(self, answer):
        # Zobrazit ponuku jedal
        if(answer == 1):
            self.show_food_menu()
            return True

        # Zadať novú objednávku
        if(answer == 2):
            self.add_order()
            return True

        # Zobraziť nevyplatene stoly
        if(answer == 4):
            self.show_not_paid_orders_for_all_tables()
            return True

        # Vyplatiť stôl po častiach
        if(answer == 5):
            self.pay_table_pieces()
            return True

        # Vyplatiť stôl naraz
        if(answer == 6):
            self.pay_table_all()
            return True

        # Koniec
        if(answer == 0):
            return False


    def get_answer(self, question, input_range=None):
        while(True):
            try:
                answer = int(input("{0} > ".format(question)).strip())
                if(input_range is None or answer in input_range):
                    return answer
                else:
                    print("Neplatné čislo. Skús znova.")
            except:
                print("Zadaný vstup je neplatný. Musíš zadať číslo. Skús znova.")


    # 1 - Zobrazit ponuku jedal
    def show_food_menu(self):
        sql = "SELECT * FROM XPmenu"
        menu = Connection().executeQuery(sql)

        print("\nPonuka jedal:")
        for food in menu:
            fid, name, price = food
            print("{0} | {1}    {2}e".format(fid, name, price))
        print()


    # 2 - Zadať novú objednávku
    def exist_order_on_table(self, table_id, food_id):
        sql = "SELECT id FROM XPobjednavky WHERE stol_id = {0} AND jedlo_id = {1}".format(table_id, food_id)
        result = Connection().executeQuery(sql)
        if(result == []):
            return None
        return result[0][0]

    def insert_new_order_into_db(self, table_id, food_id, count_order):
        sql = "INSERT INTO XPobjednavky (stol_id, jedlo_id, pocet_objednanych, pocet_urobenych, pocet_zaplatenych) "
        sql += "VALUES ({0}, {1}, {2}, 0, 0)".format(table_id, food_id, count_order)
        Connection().execute(sql)

    def update_order(self, order_id, count_order):
        sql = "UPDATE XPobjednavky SET pocet_objednanych = pocet_objednanych + {0} WHERE id = {1}".format(count_order, order_id)
        Connection().execute(sql)
        
    def new_order(self, table_id, food_id, count_order):
        order_id = self.exist_order_on_table(table_id, food_id)

        if(order_id is not None):
            self.update_order(order_id, count_order)
        else:
            self.insert_new_order_into_db(table_id, food_id, count_order)
        

    def get_food_count(self):
        sql = "SELECT COUNT(*) FROM XPmenu"
        return Connection().executeQuery(sql)[0][0]
        
    def add_order(self):
        print()
        self.show_food_menu()
        
        table_id = self.get_answer("Zadaj cislo stola", range(1, self.get_table_count() + 1))
        food_id = self.get_answer("Zadaj id jedla", range(1, self.get_food_count() + 1))
        count_order = self.get_answer("Zadaj pocet kusov")

        self.new_order(table_id, food_id, count_order)
        print("Objednavka uspesne zadana")


    # 4 - Zobraziť nevyplatene stoly
    def get_table_count(self):
        sql = "SELECT COUNT(*) FROM XPstol"
        return Connection().executeQuery(sql)[0][0]
        
    def show_not_paid_orders_for_table(self, table_id):
        #sql_orders = "SELECT * FROM XPobjednavky WHERE stol_id = {} AND pocet_objednanych != pocet_zaplatenych"
        #orders = Connection().executeQuery(sql_orders, (table_id, ))
        sql_orders = "SELECT * FROM XPobjednavky WHERE stol_id = {0} AND pocet_objednanych != pocet_zaplatenych".format(table_id)
        orders = Connection().executeQuery(sql_orders)

        sql_food_price = "SELECT nazov, cena FROM XPmenu WHERE id = {0}"
        total_price = 0
        for o in orders:
            oid, table_id, food_id, count_order, count_made, count_paid = o
            food_name, food_price = Connection().executeQuery(sql_food_price.format(food_id))[0]
            print("({0}) {1} | Objednane = {2} | Zaplatene = {3} | Celkova nezaplatena suma = {4}x{5} = {6}e".format(oid, food_name, count_order, count_paid,
                                                          (count_order - count_paid), food_price, (count_order - count_paid) * food_price))
            total_price += (count_order - count_paid) * food_price
        print("- Ostava zaplatit {0}e".format(total_price))
        
    
    def show_not_paid_orders_for_all_tables(self):
        count = self.get_table_count()

        print()
        for c in range(1, count + 1):
            print("=== Stol c.{}".format(c))
            self.show_not_paid_orders_for_table(c)
        print()   

    # 5 - Vyplatiť stôl po častiach
    def get_open_orders_for_table(self, table_id):
        sql = "SELECT id FROM XPobjednavky WHERE pocet_objednanych != pocet_zaplatenych AND stol_id = {0}".format(table_id)
        result = []
        for order in Connection().executeQuery(sql):
            result.append(order[0])
        return result

    def get_price_of_food(self, food_id):
        sql = "SELECT cena FROM XPmenu WHERE id = {0}".format(food_id)
        return Connection().executeQuery(sql)[0][0]

    def make_payment(self, total_price_to_pay):
        amount = self.get_answer("Mas zaplatit {0}e. Kolko platis".format(total_price_to_pay))

        if(amount >= total_price_to_pay):
            print("Treba vydat {0}e".format(amount - total_price_to_pay))
            return True
        return False

    def pay_for_order(self, order_id):
        order = Objednavka(order_id)
        count_of_pieces_to_pay = self.get_answer("Kolko kusov chces zaplatit")

        # Nikdy sa nezaplati viac kusov, ako sa realne moze
        count_of_pieces_to_pay = min(count_of_pieces_to_pay, order.max_count_of_how_much_pieces_to_pay())

        total_price_to_pay = count_of_pieces_to_pay * self.get_price_of_food(order.food_id)
        if(self.make_payment(total_price_to_pay)):
            order.update_count_paid(count_of_pieces_to_pay)
            print("Objednavka uspesne zaplatena")
        else:
            print("Nedostatocna suma. Zaplatenie sa nepodarilo")
                  
    
    def pay_table_pieces(self):
        table_id = self.get_answer("Zadaj cislo stola", range(1, self.get_table_count() + 1))
        open_orders = self.get_open_orders_for_table(table_id)

        # Ak je na stole vsetko zaplatene
        if(open_orders == []):
            print("Dany stol c.{0} ma vsetky objednavky zaplatene".format(table_id))
            return
            

        print("\n=== Stol c.{}".format(table_id))
        self.show_not_paid_orders_for_table(table_id)
        print()

        while(True):
            open_orders = self.get_open_orders_for_table(table_id)  # Musim aktualizovat
            order_id = self.get_answer("Zadaj ID objednavky [-1 ak chcete ukoncit]")
            
            if(order_id == -1):
                break
            
            if(order_id in open_orders):
                self.pay_for_order(order_id)
            else:
                print("Tato objednavka nepatri tomuto stolu, alebo neexistuje")

    # 6 - Vyplatiť stôl naraz
    def pay_table_all(self):
        table_id = self.get_answer("Zadaj cislo stola", range(1, self.get_table_count() + 1))
        open_orders = self.get_open_orders_for_table(table_id)

        # Ak je na stole vsetko zaplatene
        if(open_orders == []):
            print("Dany stol c.{0} ma vsetky objednavky zaplatene".format(table_id))
            return
            

        print("\n=== Stol c.{}".format(table_id))
        self.show_not_paid_orders_for_table(table_id)
        print()

        total_price = 0
        orders = []
        for order_id in open_orders:
            order = Objednavka(order_id)
            orders.append(order)
            
            price = order.max_count_of_how_much_pieces_to_pay() * self.get_price_of_food(order.food_id)
            total_price += price

        if(self.make_payment(total_price)):
            for order in orders:
                order.update_count_paid(order.max_count_of_how_much_pieces_to_pay())
            print("Stol c.{0} uspesne zaplateny".format(table_id))
        else:
            print("Nedostatocna suma. Stol c.{0} sa nepodarilo zaplatit".format(table_id))
            
                

        

        

























    
        
        
