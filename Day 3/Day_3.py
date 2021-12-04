
# --- Day 3: Binary Diagnostic ---
# Part 1

file = open('Day_3_Input', "r")
raw_data = file.read()
binary_data = raw_data.split("\n")


def binary_conversion(binary_value):
    decimal_value = 0
    counter_binary = 0
    calculation_max = len(binary_value) - 1

    while counter_binary < len(binary_value):
        decimal_value = decimal_value + ((int(binary_value[counter_binary]))*(2**calculation_max))
        calculation_max -= 1
        counter_binary += 1
    return decimal_value


gamma_binary = ""
epsilon_binary = ""
zero_1 = 0
one_1 = 0
counter = 0

while counter < len(binary_data[0]):
    zero_1 = 0
    one_1 = 0
    for row in binary_data:
        if int(row[counter]) == 0:
            zero_1 += 1
        if int(row[counter]) == 1:
            one_1 += 1
    if zero_1 > one_1:
        gamma_binary += "0"
        epsilon_binary += "1"
    if one_1 > zero_1:
        gamma_binary += "1"
        epsilon_binary += "0"
    counter += 1

gamma = binary_conversion(gamma_binary)
epsilon = binary_conversion(epsilon_binary)
print("Part 1 Answer:", gamma * epsilon)


# Part 2


def pop_lists(variable_list, pop_value, index):
    returned_list = list(filter(lambda x: int(x[index]) == pop_value, variable_list))
    return returned_list


def count_binary(binary_list, index):
    zero_part_2 = 0
    one_part_2 = 0
    for variables in binary_list:
        if int(variables[index]) == 0:
            zero_part_2 += 1
        if int(variables[index]) == 1:
            one_part_2 += 1
    return zero_part_2, one_part_2


counter = 0
oxygen = binary_data.copy()
co2 = binary_data.copy()

while len(oxygen) > 1:
    zero_oxygen, one_oxygen = count_binary(oxygen, counter)
    if zero_oxygen > one_oxygen:
        oxygen = pop_lists(oxygen, 1, counter)
    if one_oxygen > zero_oxygen:
        oxygen = pop_lists(oxygen, 0, counter)
    if zero_oxygen == one_oxygen:
        oxygen = pop_lists(oxygen, 0, counter)
    counter += 1


counter = 0
while len(co2) > 1:
    zero_co2, one_co2 = count_binary(co2, counter)
    if zero_co2 > one_co2:
        co2 = pop_lists(co2, 0, counter)
    if one_co2 > zero_co2:
        co2 = pop_lists(co2, 1, counter)
    if zero_co2 == one_co2:
        co2 = pop_lists(co2, 1, counter)
    counter += 1

# print("Oxygen Binary:", oxygen[0], "Co2 Binary:", co2[0])
# print("Oxygen Decimal:", binary_conversion(oxygen[0]), "Co2 Decimal:", binary_conversion(co2[0]))
print("Part 2 Answer:", binary_conversion(oxygen[0]) * binary_conversion(co2[0]))