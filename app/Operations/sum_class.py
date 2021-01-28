class SumPerfect:

    def __init__(self):
        self.__list_total = {"sets": []}

    def sum_subsets(self, claves, sets, n, target):
        x = [0] * len(sets)
        j = len(sets) - 1

        while n > 0:
            x[j] = n % 2
            n = n // 2
            j -= 1

        suma = 0
        for i in range(len(sets)):
            if x[i] == 1:
                suma += sets[i]

        if suma == target:
            dict_match = dict(zip(claves, sets))
            dict_final = dict(zip(claves, x))
            my_collection = {}

            for a, b in dict_final.items():
                if b == 1:
                    my_collection[a] = dict_match[a]
            self.__list_total["sets"].append(my_collection)

    def find_subsets(self, claves, arr, K):
        x = pow(2, len(arr))
        for i in range(1, x):
            self.sum_subsets(claves, arr, i, K)
        return

    def get_list_total(self, claves, arr, K):
        self.find_subsets(claves, arr, K)
        return self.__list_total
