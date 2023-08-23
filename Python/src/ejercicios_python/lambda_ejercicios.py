def sum_ten():
    def add(value):
        return value + 10
    return add

add_value = sum_ten()
print(add_value(5))