from dto import Dto


def is_given_pw_valid_by_old_rules(policy, password):
    range, letter = policy.split(" ")
    start, end = range.split("-")
    return int(start) <= password.count(letter) <= int(end)


def is_given_pw_valid(policy, password):
    positions, letter = policy.split(" ")
    first, second = positions.split("-")
    return password[int(first) - 1] == letter and password[int(second) - 1] != letter or \
           password[int(first) - 1] != letter and password[int(second) - 1] == letter


def get_num_of_valid_passwords(passwords: list, new_rules: bool) -> int:
    valid_passwords = 0
    for pw in passwords:
        policy, password = pw.split(": ")
        if new_rules:
            if is_given_pw_valid(policy, password):
                valid_passwords += 1
        else:
            if is_given_pw_valid_by_old_rules(policy, password):
                valid_passwords += 1
    return valid_passwords


if __name__ == '__main__':
    data = Dto("data.txt", "\n").get_data()

    print(get_num_of_valid_passwords(data, False))  # 378
    print(get_num_of_valid_passwords(data, True))  # 280
