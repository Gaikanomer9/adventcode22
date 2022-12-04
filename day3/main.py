
if __name__=="__main__":
    # with open("day3/input.txt") as file:
    #     prios = 0
    #     count = 0
    #     data = file.readlines()
    #     for rucksack in data:
    #         rucksack = rucksack.replace("\n", "")
    #         size_rs = len(rucksack)
    #         symbols_prios = [0] * 200
    #         middle = int(size_rs / 2)
    #         for i in range(middle):
    #             symbols_prios[ord(rucksack[i])] = 1
    #         old_count = count
    #         for i in range(middle):
    #             letter = rucksack[size_rs - 1 - i]
    #             if symbols_prios[ord(letter)] == 1:
    #                 count += 1
    #                 change = 0
    #                 if ord(rucksack[size_rs - 1 - i]) < 92:
    #                     change = (ord(letter) - 38)
    #                 else:
    #                     change = (ord(letter) - 96)
    #                 prios += change
    #                 break
    #         if count == old_count:
    #             print(rucksack)
            
    #     print(len(data), count)
    #     print(prios)
    
    # task 2
    with open("day3/input.txt") as file:
        prios = 0
        data = file.readlines()
        group = []
        for rucksack in data:
            rucksack = rucksack.replace("\n", "")
            group.append(set(rucksack))
            if len(group)==3:
                letter = (group[0].intersection(group[1])).intersection(group[2])
                letter = letter.pop()
                if ord(letter) < 92:
                    change = (ord(letter) - 38)
                else:
                    change = (ord(letter) - 96)
                prios += change
                group=[]
        print(prios)



