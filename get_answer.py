


class get_answer:
    bad_input = "nezadal si číslo! skúš ešte raz"
    def get(self):
        while True:
            try:
                return int(input("Akcia> "))
            except ValueError:
                print(self.bad_input)
