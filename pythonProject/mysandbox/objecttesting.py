values = {"one":1,"two":2,"three":3,"four":4}
class DictAndValue:
    def __init__(self):
        pass

    def loop_throug(self,position):
        for temp in position:
            print(f"Key: {temp} and its value: {values[temp]}")

testapp = DictAndValue()

value_number = ["one","two","three","four"]

testapp.loop_throug(value_number)