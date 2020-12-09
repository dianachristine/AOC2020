class Dto:

    def __init__(self, filename, split_string):
        self.filename = filename
        self.split_string = split_string
        self.data = self.__get_data_from_fail()

    def __get_data_from_fail(self) -> list:
        try:
            return open(self.filename, 'r').read().split(self.split_string)
        except FileNotFoundError:
            print("Fail not found")

    def get_data(self):
        return self.data

    def get_data_in_ints(self) -> list:
        return list(map(int, self.data))
