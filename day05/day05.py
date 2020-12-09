from dto import Dto


def decode_seat_code(seat_code: str, rows: int, columns: int) -> int:
    left_row = 0
    left_column = 0

    for char in seat_code[:7]:
        if char == "F":
            rows -= (rows - left_row) // 2
        if char == "B":
            left_row += (rows - left_row) // 2

    for char in seat_code[7:]:
        if char == "L":
            columns -= (columns - left_column) // 2
        if char == "R":
            left_column += (columns - left_column) // 2
    return left_row * 8 + left_column


def find_all_seat_ids(seat_codes: list, rows: int, columns: int) -> list:
    return [decode_seat_code(code, rows, columns) for code in seat_codes]


def find_highest_seat_id(seat_ids) -> int:
    return max(seat_ids)


def find_the_missing_seat_ids(seat_ids, rows, columns) -> list:
    last_id = (rows - 1) * 8 + (columns - 1)
    all_ids = list(range(0, last_id + 1))
    return [id for id in all_ids if id not in seat_ids]


if __name__ == '__main__':
    data = Dto("data.txt", "\n").get_data()

    ids = find_all_seat_ids(data, 128, 8)
    print(find_highest_seat_id(ids))  # 919

    print(find_the_missing_seat_ids(ids, 128, 8))
    # also prints some of the seats at the very front (0 - 79) and back (920 - 1023) of the plane
    # that don't exist on this aircraft
    # correct answer is 642
