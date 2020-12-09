def analyze_xmas(xmas):
    preamble_size = 25
    preamble = []
    weakness = None
    has_weakness = False
    # target_number = 0
    i = 0
    print(len(xmas))

    while i < len(xmas):
        # add each number to the preamble list
        preamble.append(xmas[i])

        # check length of the preamble to see if analysis is required
        if len(preamble) > preamble_size:
            target_number = preamble[-1]
            j = 0
            has_weakness = True

            # analyze the target number with the values from preamble
            while j < len(preamble):
                compliment = target_number - preamble[j]
                if compliment in preamble:
                    has_weakness = False
                j += 1

            # check to see if a weakness was found
            if has_weakness:
                weakness = target_number
                break

            # remove the first value from preamble to accommodate preamble size
            preamble = preamble[1:]

        i += 1
    return weakness


def main():
    xmas = []

    with open('input.txt') as file:
        for line in file:
            xmas.append(int(line))

    weakness = analyze_xmas(xmas)
    print(weakness)


if __name__ == "__main__":
    main()
