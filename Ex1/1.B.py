def main(last_match: str, current_match: str, place: int) -> int:
    lm1, lm2 = map(int, last_match.split(':'))
    cm1, cm2 = map(int, current_match.split(':'))
    balls_1 = lm1 + cm1
    balls_2 = lm2 + cm2
    result = balls_2 - balls_1
    if place == 2:  # Значит текущая дома и нужно на один гол больше
        result += 1
    if result == 0:
        return 1
    elif result < 0:
        return 0
    return result


assert main('0:2', '0:3', 1) == 5
assert main('0:2', '0:3', 2) == 6
assert main('0:0', '0:0', 1) == 1
assert main('0:0', '0:0', 2) == 1
assert main('3:0', '2:0', 1) == 0
assert main('3:0', '2:0', 2) == 0

if __name__ == '__main__':
    last_match = input()
    current_match = input()
    place = int(input())  # 1 - первая игра дома, 2 - в гостях
    result = main(last_match, current_match, place)
    print(result)
