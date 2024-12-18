import re

with open("Day17.txt", "r") as file:
    register_a = int(*re.findall("\\d+", file.readline()))
    register_b = int(*re.findall("\\d+", file.readline()))
    register_c = int(*re.findall("\\d+", file.readline()))
    file.readline()
    program = list(map(int, re.findall("\\d+", file.readline())))

# print(register_a, register_b, register_c, program)


def puzzle1():
    """
    We have 8 instructions.
    Each number in program is 0-7 denoting the operation.
    3 registers A, B, C.
    Each instruction also needs the next number as the input to that instructor
    called the operand.
    Instruction pointer reads the opcodes, starts at 0 and increases by 2 after
    each instructionexcept for jump instructions.
    If it tries to read an opcode past the end it just halts.
    The input number follows these rules.

    Combo operands 0 through 3 represent literal values 0 through 3.
    Combo operand 4 represents the value of register A.
    Combo operand 5 represents the value of register B.
    Combo operand 6 represents the value of register C.
    Combo operand 7 is reserved and will not appear in valid programs.


    """

    instruction_ptr = 0

    def get_combo(input):
        match input:
            case num if num <= 3:
                return input
            case 4:
                return register_a
            case 5:
                return register_b
            case 6:
                return register_c
            case 7:
                return 0

    output = []

    # opcode 0
    def adv(input):
        global register_a
        nonlocal instruction_ptr
        register_a //= 2 ** get_combo(input)
        instruction_ptr += 2

    # opcode 1
    def bxl(input):
        global register_b
        nonlocal instruction_ptr
        register_b ^= input
        instruction_ptr += 2

    # opcode 2
    def bst(input):
        global register_b
        nonlocal instruction_ptr
        register_b = get_combo(input) % 8
        instruction_ptr += 2

    # opcode 3
    def jnz(input):
        nonlocal instruction_ptr
        if register_a == 0:
            instruction_ptr += 2
            return
        instruction_ptr = input

    # opcode 4
    def bxc(input):
        global register_b
        nonlocal instruction_ptr
        register_b ^= register_c
        instruction_ptr += 2

    # opcode 5
    def out(input):
        nonlocal instruction_ptr
        output.append(get_combo(input) % 8)
        instruction_ptr += 2

    # opcode 6
    def bdv(input):
        global register_b
        nonlocal instruction_ptr
        register_b = register_a // 2 ** get_combo(input)
        instruction_ptr += 2

    # opcode 7
    def cdv(input):
        global register_c
        nonlocal instruction_ptr
        register_c = register_a // 2 ** get_combo(input)
        instruction_ptr += 2

    opcode = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}
    n = len(program)

    while instruction_ptr < n - 1:
        opcode[program[instruction_ptr]](program[instruction_ptr + 1])
        # print(register_a, register_b, register_c)

    return ",".join(map(str, output))


def puzzle2():
    """
    find an output to get the program input
    Figured out the bounds for the number of digits.
    After that I disected the numbers I noticed there is a pattern.
    I would go from the highest number of digits and increment with that
    thought the bounds.
    I would increment by 1e12 then 1e11 and so on.
    Each time I can see we are getting a smaller bound for the number
    """

    def num_digits_bound(digits):
        global register_a
        low, high = 0, int(1e18)
        while low <= high:
            mid = low + (high - low) // 2
            register_a = mid
            ans_digits = len(puzzle1().split(","))
            if ans_digits < digits:
                low = mid + 1
            else:
                high = mid - 1
        print(low)
        return low

    global register_a
    ans = 0
    goal = ",".join(map(str, program))
    lower_bound, upper_bound = num_digits_bound(16), num_digits_bound(17)

    index = 0
    n = len(program)
    break_count = 0
    for step in range(14, 1, -1):
        step **= 10
        new_lower_bound, new_upper_bound = upper_bound, 0
        for num in range(lower_bound, upper_bound, step):
            register_a = num
            ans = puzzle1()
            print(list(map(int, ans.split(",")))[n - index - 1 :])
            print(program[n - index - 1 :])
            if (
                list(map(int, ans.split(",")))[n - index - 1 :]
                == program[n - index - 1 :]
            ):
                new_lower_bound = min(num - step, new_lower_bound)
                new_upper_bound = num + step
                # print("HERE")
            elif new_upper_bound != 0:
                break

            print(ans, num)
            if ans == ",".join(map(str, program)):
                return num
        lower_bound = new_lower_bound
        upper_bound = new_upper_bound
        print(lower_bound, upper_bound)
        print("_________________________________________")
        index += 1
    return ans


# print(puzzle1())  # 7,0,7,3,4,1,3,0,1
# register_a = 156985331222018
# print(puzzle1())
print(puzzle2())  # 156985331222018
## I did it manually
