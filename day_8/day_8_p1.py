class Command:
    def __init__(self, cmd, value):
        self.cmd = cmd
        self.value = value


def process_boot(commands):
    traveled_lines = set()
    accumulator = 0
    i = 0

    # Begin looping through the boot process
    while i < len(commands):
        selected_command = commands[i]

        # Check to see if the line has already been touched
        if i in traveled_lines:
            break

        # Add the line to the set of touched lines
        traveled_lines.add(i)

        # Execute the boot command action
        if selected_command.cmd == "acc":
            accumulator += selected_command.value
            i += 1
        elif selected_command.cmd == "jmp":
            i += selected_command.value
        else:
            i += 1

    return accumulator


def main():
    commands = []

    # Save the input as an iterable list, with Command objects for each entry
    with open('boot_code.txt') as file:
        for line in file:
            values = line.split()
            command = Command(values[0], int(values[1]))
            commands.append(command)

    # Process each boot command
    accumulator = process_boot(commands)
    print(accumulator)


if __name__ == "__main__":
    main()
