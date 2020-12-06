from data import get_data_from_fail


def is_correct_byr(byr):
    return byr.isdigit() and 1920 <= int(byr) <= 2002


def is_correct_iyr(iyr):
    return iyr.isdigit() and 2010 <= int(iyr) <= 2020


def is_correct_eyr(eyr):
    return eyr.isdigit() and 2020 <= int(eyr) <= 2030


def is_correct_hgt(hgt, unit):
    if unit == 'cm':
        return 150 <= int(hgt) <= 193
    if unit == 'in':
        return 59 <= int(hgt) <= 76


def is_correct_hcl(hcl):
    allowed_letters = ['a', 'b', 'c', 'd', 'e', 'f']
    if hcl[0] == '#':
        for i in range(1, len(hcl)):
            if hcl[i] not in allowed_letters and not hcl[i].isdigit():
                return False
        return True
    return False


def is_correct_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_correct_pid(pid):
    return pid.isdigit()


def are_required_field_present(passport):
    return 'byr' in passport and 'iyr' in passport and \
           'eyr' in passport and 'hgt' in passport and \
           'hcl' in passport and 'ecl' in passport and \
           'pid' in passport


def is_passport_valid(passport: str):
    if are_required_field_present(passport):
        if is_correct_byr(passport[passport.index('byr') + 4: passport.index('byr') + 8]) and \
                is_correct_iyr(passport[passport.index('iyr') + 4: passport.index('iyr') + 8]) and \
                is_correct_eyr(passport[passport.index('eyr') + 4: passport.index('eyr') + 8]) and \
                is_correct_pid(passport[passport.index('pid') + 4: passport.index('pid') + 13]) and \
                is_correct_ecl(passport[passport.index('ecl') + 4: passport.index('ecl') + 7]) and \
                is_correct_hcl(passport[passport.index('hcl') + 4: passport.index('hcl') + 11]):
            if 'in' in passport:
                unit = 'in'
            elif 'cm' in passport:
                unit = 'cm'
            else:
                return False
            if is_correct_hgt(passport[passport.index('hgt') + 4: passport.index(unit)], unit):
                return True
    return False


def get_num_of_valid_passports(passports: list):
    valid = 0
    for pp in passports:
        if is_passport_valid(pp):
            valid += 1
    return valid


if __name__ == '__main__':
    data = get_data_from_fail("data.txt", "\n\n")

    print(get_num_of_valid_passports(data))
# 140 is correct answer
