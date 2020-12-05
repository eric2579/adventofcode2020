def find_valid_passports(path, total_fields, optional_fields):
    necessary_fields = list(set(total_fields) - set(optional_fields))
    with open(path, 'r') as f:
        raw_file = f.read()
        passport_list = raw_file.split('\n\n')
    valid_passport_count = 0
    secondary_check_count = 0
    for passport in passport_list:
        passport_dict = {}
        passport = passport.replace('\n', ' ')
        for field_value in passport.split():
            colon_locale = field_value.index(':')
            passport_dict[field_value[:colon_locale]] = field_value[colon_locale+1:]
        if all(field in list(passport_dict.keys()) for field in necessary_fields):
            valid_passport_count += 1
            if aggregate_secondary_check(passport_dict):
                secondary_check_count += 1
    return valid_passport_count, secondary_check_count


total_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_fields = ['cid']


def aggregate_secondary_check(passport):
    for field in total_fields:
        if field == 'byr':
            if not validate_numerical_intervals(passport[field], 1920, 2002):
                return False
        elif field == 'iyr':
            if not validate_numerical_intervals(passport[field], 2010, 2020):
                return False
        elif field == 'eyr':
            if not validate_numerical_intervals(passport[field], 2020, 2030):
                return False
        elif field == 'hgt':
            if not validate_height(passport[field]):
                return False
        elif field == 'hcl':
            if not validate_hair(passport[field]):
                return False
        elif field == 'ecl':
            if not validate_eye(passport[field]):
                return False
        elif field == 'pid':
            if not validate_passport_id(passport[field]):
                return False
    return True


# validation functions
def validate_numerical_intervals(text, minn, maxx):
    try:
        num = int(text)
        if (num >= minn) and (num <= maxx):
            return True
        return False
    except ValueError:
        return False


def validate_height(text):
    potential_unit = text[-2:]
    if potential_unit == 'in':
        return validate_numerical_intervals(text[:-2], 59, 76)
    elif potential_unit == 'cm':
        return validate_numerical_intervals(text[:-2], 150, 193)
    else:
        return False


def validate_hair(text):
    valid_chars = set('0123456789abcdef')
    if text[0] != '#':
        return False
    elif len(text[1:]) != 6:
        return False
    else:
        if all((c in valid_chars) for c in text[1:]):
            return True
        return False


def validate_eye(text):
    eye_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return any(text == eye_col for eye_col in eye_list)


def validate_passport_id(text):
    if len(text) != 9:
        return False
    try:
        num = int(text)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    print(find_valid_passports('../resources/day_4.txt', total_fields, optional_fields))
