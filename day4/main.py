

def check_overlap(i1, i2):
    i2_left_in_i1 = i1[0] <= i2[0] and i2[0] <= i1[1]
    i2_right_in_i1 = i1[0] <= i2[1] and i2[1] <= i1[1]
    i1_left_in_i2 = i2[0] <= i1[0] and i1[0] <= i2[1]
    i1_right_in_i2 = i2[0] <= i1[1] and i1[1] <= i2[1]
    contained = (i2_left_in_i1 and i2_right_in_i1) or\
                (i1_left_in_i2 and i1_right_in_i2)
    return contained

def overlap_at_all(i1, i2):
    i2_left_in_i1 = i1[0] <= i2[0] and i2[0] <= i1[1]
    i2_right_in_i1 = i1[0] <= i2[1] and i2[1] <= i1[1]
    i1_left_in_i2 = i2[0] <= i1[0] and i1[0] <= i2[1]
    i1_right_in_i2 = i2[0] <= i1[1] and i1[1] <= i2[1]
    if any([i2_left_in_i1, i2_right_in_i1,
        i1_left_in_i2, i1_right_in_i2]):
        return True


if __name__=="__main__":
    # with open("day4/input.txt") as file:
    #     data = file.readlines()
    #     count = 0
    #     for line in data:
    #         intervals = line.replace('\n', '').split(",")
    #         intervals[0] = list(map(lambda x: int(x), intervals[0].split('-')))
    #         intervals[1] = list(map(lambda x: int(x), intervals[1].split('-')))
    #         if check_overlap(intervals[0], intervals[1]):
    #             count += 1
    #     print(count)
    #part 2
    with open("day4/input.txt") as file:
        data = file.readlines()
        count = 0
        for line in data:
            intervals = line.replace('\n', '').split(",")
            intervals[0] = list(map(lambda x: int(x), intervals[0].split('-')))
            intervals[1] = list(map(lambda x: int(x), intervals[1].split('-')))
            if overlap_at_all(intervals[0], intervals[1]):
                count += 1
        print(count)