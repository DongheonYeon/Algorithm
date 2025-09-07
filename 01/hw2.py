input = input()

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    shift = 0
    cur = string[0]
    for i in string:
        if i != cur:
            shift += 1
            cur = i
    return int(shift/2 + 0.5)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)