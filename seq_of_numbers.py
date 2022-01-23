first_seq = set(int(x) for x in input().split())
second_seq = set(int(x) for x in input().split())
number_of_lines = int(input())
for line in range(number_of_lines):
    commands = input().split()
    command = commands[0]
    which = commands[1]
    if command == "Add":
        if which == "First":
            [first_seq.add(int(x)) for x in commands[2:]]
        else:
            [second_seq.add(int(x)) for x in commands[2:]]
    elif command == "Remove":
        if which == "First":
            first_seq = first_seq.difference([int(x) for x in commands[2:]])
        else:
            second_seq = second_seq.difference([int(x) for x in commands[2:]])
    else:
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print("True")
        else:
            print("False")
print(f"{', '.join(str(x) for x in sorted(first_seq))}")
print(f"{', '.join(str(x) for x in sorted(second_seq))}")
