
if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.readlines()
        stacks_len = int(float(len(data[0]) + 1) / 4)
        stacks = []
        for idx, line in enumerate(data):
            if line == "\n":
                break
            stacks.append([])
            for i in range(stacks_len):
                letter = line[i*4+1:i*4+2]
                if letter == " ":
                    stacks[idx].append(None)
                else:
                    stacks[idx].append(letter)
        stacks.pop()
        print(stacks)
        stacks.reverse()
        stacks = list(zip(*stacks))
        stacks = list(map(lambda l: [a for a in l if a is not None], stacks))
        print(stacks)
        print(idx)
        for i in range(idx+1, len(data)):
           instruct = data[i]
           cmds = list(map(lambda x: int(x) ,filter(lambda x: x.isnumeric(), instruct.replace("\n", "").split(" "))))
           el = stacks[cmds[1]-1][-cmds[0]:]
           stacks[cmds[2]-1].extend(el)
           for i in range(len(el)):
               stacks[cmds[1]-1].pop()
        #  day1  
        #  for repeat in range(cmds[0]):
        #        el = stacks[cmds[1]-1].pop()
        #        stacks[cmds[2]-1].append(el)
        print(stacks)
        ans = ""
        for st in stacks:
            ans += st[-1:][0]
        print(ans)
