class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):
    def test_initialization_without_data(self):
        numbers = IntegerList()
        self.assertEqual([], numbers._IntegerList__data)

    def test_initialization_with_wrong_data_type(self):
        numbers = IntegerList(7.50, "A")
        self.assertEqual([], numbers._IntegerList__data)

    def test_initialization(self):
        numbers = IntegerList(4, 7.50, "A", 8, 2, False)
        self.assertEqual([4, 8, 2], numbers._IntegerList__data)

    def test_get_data(self):
        numbers = IntegerList(8, 10)
        result = numbers.get_data()
        self.assertEqual([8, 10], result)

    def test_if_raises_error_for_adding_non_integer_element(self):
        numbers = IntegerList(4, 7.50, "A", 8, 2, False)

        with self.assertRaises(ValueError) as valer:
            numbers.add(7.5)
        self.assertEqual("Element is not Integer", str(valer.exception))

    def test_add_correct_data_adds_element(self):
        numbers = IntegerList(4, 7.50, "A", 8, 2, False)
        numbers.add(10)
        self.assertEqual([4, 8, 2, 10], numbers._IntegerList__data)

    def test_if_raises_error_for_remove_index_out_of_range(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_returns_element_at_the_removed_index(self):
        integer = IntegerList(5)
        result = integer.remove_index(0)
        self.assertEqual(5, result)

    def test_removes_element_correct(self):
        integer = IntegerList(5)
        integer.remove_index(0)
        self.assertEqual([], integer._IntegerList__data)

    def test_get_with_invalid_index(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.get(2)
        self.assertEqual("Index is out of range", str(ex.exception))
        with self.assertRaises(IndexError) as ex:
            integer.get(1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_valid_index_returns_element(self):
        integer = IntegerList(5)
        result = integer.get(0)

        self.assertEqual(5, result)

    def test_insert_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as ex:
            integer.insert(2, 10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_invalid_data_type_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(ValueError) as ex:
            integer.insert(0, 1.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_adds_element(self):
        integer = IntegerList(5)

        integer.insert(0, 10)
        self.assertEqual([10, 5], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(5, -2, 10, 8, 90, 6)
        result = integer.get_biggest()
        self.assertEqual(90, result)

    def test_get_index(self):
        integer = IntegerList(5, -2, 10, 8, 90, 6)
        result = integer.get_index(-2)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()
