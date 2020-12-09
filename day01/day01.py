from dto import Dto


def find_two_parts_of_given_number(nums, number):
    for num1 in nums:
        for num2 in nums:
            if num1 + num2 == number:
                return num1 * num2


def find_three_parts_of_given_number(nums, number):
    for num1 in nums:
        num2_and_num3_product = find_two_parts_of_given_number(nums, number - num1)
        if num2_and_num3_product:
            return num1 * num2_and_num3_product


if __name__ == '__main__':
    data = Dto("data.txt", "\n").get_data_in_ints()

    print(find_two_parts_of_given_number(data, 2020))  # 1014171
    print(find_three_parts_of_given_number(data, 2020))  # 46584630
