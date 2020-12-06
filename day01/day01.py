def get_data(filename) -> list:
    try:
        return open(filename, 'r').read().split()
    except FileNotFoundError:
        print("Fail not found")


def find_two_parts_of_given_number(nums, number):
    for num1 in nums:
        for num2 in nums:
            if int(num1) + int(num2) == number:
                return int(num1) * int(num2)


def find_three_parts_of_given_number(nums, number):
    for num1 in nums:
        num2_and_num3_product = find_two_parts_of_given_number(nums, number - int(num1))
        if num2_and_num3_product:
            return int(num1) * num2_and_num3_product


if __name__ == '__main__':
    data = get_data('data.txt')
    print(find_two_parts_of_given_number(data, 2020))  # 1014171
    print(find_three_parts_of_given_number(data, 2020))  # 46584630
