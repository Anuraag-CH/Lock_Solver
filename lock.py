import re

class CodeCracker:
    def __init__(self):
        self.numbers = []

    def generate_numbers(self):
        for i in range(1000):
            num_str = str(i).zfill(3)
            self.numbers.append(num_str)

    def code_cracker_one(self, number, is_right):
        a = number[0]
        b = number[1]
        c = number[2]
        res = []

        for i in self.numbers:
            if i.count(a) < 2 and i.count(b) < 2 and i.count(c) < 2 and i.count(a) + i.count(b) + i.count(c) == 1:
                pattern = rf"^{a}\d*"
                y = re.findall(pattern, i)
                pattern = rf"^\d+{b}\d+$"
                x = re.findall(pattern, i)
                pattern = rf"\d*{c}$"
                z = re.findall(pattern, i)

                if (x or y or z) and is_right:
                    res.append(i)

                if not (x or y or z) and not is_right:
                    res.append(i)

        print(res)
        self.numbers = res

    def code_cracker_two(self, number, is_right):
        a = number[0]
        b = number[1]
        c = number[2]
        res = []

        for i in self.numbers:
            if i.count(a) < 2 and i.count(b) < 2 and i.count(c) < 2 and i.count(a) + i.count(b) + i.count(c) == 2:
                pattern = rf"^{a}\d*"
                y = re.findall(pattern, i)
                pattern = rf"^\d+{b}\d+$"
                x = re.findall(pattern, i)
                pattern = rf"\d*{c}$"
                z = re.findall(pattern, i)

                if (x or y or z) and is_right:
                    res.append(i)

                if not (x or y or z) and not is_right:
                    res.append(i)

        print(res)
        self.numbers = res

    def code_cracker_three(self, number):
        a = number[0]
        b = number[1]
        c = number[2]
        res = []

        for i in self.numbers:
            if (i.count(a) + i.count(b) + i.count(c)) == 0:
                res.append(i)

        print(res)
        self.numbers = res


cracker = CodeCracker()
cracker.generate_numbers()

total_num_of_statements = int(input("Enter total number of statements: "))

for _ in range(total_num_of_statements):
    number = input("Enter the number:")
    num_of_places = int(input("Enter number of places:"))
    placement_correct = input("Enter correctly or wrongly placed 'r' for right or 'w' for wrong:")


    print(number,num_of_places,placement_correct)

    if placement_correct == 'r':
        placement_correct = True
    else:
        placement_correct = False

    if num_of_places == 1:
        cracker.code_cracker_one(number, placement_correct)
    elif num_of_places == 2:
        cracker.code_cracker_two(number, placement_correct)
    elif num_of_places == 3:
        cracker.code_cracker_three(number)

print(cracker.numbers)
