from .sum_class import SumPerfect


class SetData:

    def __init__(self, my_set):
        self.my_set = my_set

    def execute_operation(self):
        # Each my_set
        new_set = {}

        for i in range(len(self.my_set)):
            sum_perfect = SumPerfect()
            first_key = list(self.my_set[i].keys())[0]
            amount = self.my_set[i]["amount"]
            my_set = self.my_set[i][first_key]
            my_keys = my_set.keys()
            my_values = list(my_set.values())
            new_set[list(self.my_set[i].keys())[0]] = sum_perfect.get_list_total(my_keys, my_values, amount)

        return new_set
