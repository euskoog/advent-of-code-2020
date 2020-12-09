def analyze_xmas(xmas):
    preamble_size = 25
    preamble = []
    weakness = None
    i = 0

    while i < len(xmas):
        # add each number to the preamble list
        preamble.append(xmas[i])

        # check length of the preamble to see if analysis is required
        if len(preamble) > preamble_size:
            has_weakness = True
            target_number = preamble[-1]
            j = 0

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


def find_enc_weakness(xmas, weakness):
    enc_weakness = None
    weakness_index = xmas.index(weakness)
    contiguous_set = []
    locator = 0
    i = 0

    # loop through each contiguous set of numbers starting at each index
    while locator < weakness_index:
        contiguous_set.append(xmas[i])

        # compare the sum of the contiguous set with the weakness value
        if sum(contiguous_set) == weakness:
            enc_weakness = min(contiguous_set) + max(contiguous_set)
            break
        elif sum(contiguous_set) > weakness:
            contiguous_set = []
            locator += 1
            i = locator
        else:
            i += 1

    return enc_weakness


def main():
    xmas = []

    with open('input.txt') as file:
        for line in file:
            xmas.append(int(line))

    weakness = analyze_xmas(xmas)
    print("Weakness value:", weakness)
    enc_weakness = find_enc_weakness(xmas, weakness)
    print("Encryption weakness value:", enc_weakness)


if __name__ == "__main__":
    main()
