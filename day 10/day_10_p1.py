def analyze_adapters(adapters):
    one_jolt = 0
    two_jolt = 0
    three_jolt = 0
    i = 0

    # loop through each adapter and record the joltage difference
    while i < len(adapters) - 1:
        if adapters[i+1] - adapters[i] == 1:
            one_jolt += 1
            i += 1
        elif adapters[i+1] - adapters[i] == 2:
            two_jolt += 1
            i += 1
        elif adapters[i+1] - adapters[i] == 3:
            three_jolt += 1
            i += 1
        else:
            return "Incompatible adapter joltage"

    return one_jolt * three_jolt


def main():
    adapters = []

    with open('input.txt') as file:
        for line in file:
            adapters.append(int(line))

    # sort the adapters, append your personal device's joltage and the built-in effective outlet rating 0
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    product = analyze_adapters(adapters)
    print(product)


if __name__ == "__main__":
    main()
