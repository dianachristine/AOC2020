from dto import Dto


def is_sum_of_two_in_nums(nums: list, next_num: int):
    for num1 in nums:
        for num2 in nums:
            if num1 != num2 and num1 + num2 == next_num:
                return True
    return False


def find_first_incorrect_num(nums: list, preamble: int):
    for i in range(preamble, len(nums)):
        if not is_sum_of_two_in_nums(nums[i-preamble:i], nums[i]):
            return nums[i]


def find_contiguous_set_of_nums(nums: list, given_num: int):
    for i in range(len(nums)):
        nums_sum = 0
        i2 = i
        while nums_sum < given_num:
            nums_sum += nums[i2]
            i2 += 1
        if nums_sum == given_num:
            return nums[i:i2]


def find_encryption_weakness(nums: list):
    return min(nums) + max(nums)


if __name__ == '__main__':
    data = Dto("data.txt", "\n").get_data_in_ints()

    first_incorrect = find_first_incorrect_num(data, 25)
    print(first_incorrect)  # 18272118

    contiguous_set = find_contiguous_set_of_nums(data[:data.index(first_incorrect)], first_incorrect)
    print(find_encryption_weakness(contiguous_set))  # 2186361
