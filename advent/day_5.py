def find_seat_1d(text, min_num, max_num):
    if max_num == min_num:
        return max_num
    else:
        if text[0] == 'F' or text[0] == 'L':
            text = text[1:]
            return find_seat_1d(text, min_num, ((max_num - min_num) // 2) + min_num)
        elif text[0] == 'B' or text[0] == 'R':
            text = text[1:]
            return find_seat_1d(text, ((max_num - min_num) // 2) + min_num + 1, max_num)


def calculate_seat_id(row, col):
    return row * 8 + col


def find_missing_seat(list_of_seatids):
    for row in range(2, 127):  # 2 is hard coded via trial/error as we know the ticket cant be in the front
        for col in range(7):
            if (row, col) not in list_of_seatids:
                return row, col


def check_boarding_passes(path):
    max_seat_id = 0
    seat_id_list = []
    with open(path, 'r') as f:
        for boarding_pass in f:
            row_info = boarding_pass[:7]
            col_info = boarding_pass[7:]
            row = find_seat_1d(row_info, 0, 127)
            col = find_seat_1d(col_info, 0, 7)
            seat_id = calculate_seat_id(row, col)
            seat_id_list.append((row,col))
            if seat_id > max_seat_id:
                max_seat_id = seat_id
    sorted_seats = sorted(seat_id_list)
    missing_seat = find_missing_seat(sorted_seats)
    missing_seat_id = calculate_seat_id(missing_seat[0], missing_seat[1])
    return max_seat_id, missing_seat_id


if __name__ == '__main__':
    print(check_boarding_passes('../resources/day_5.txt'))