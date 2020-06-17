


class get_answer:
    def get(self):
        while True:
            try:
                return int(input("Akcia> "))
            except ValueError:
                print(self.bad_input)
