class ResultInfo:
    def __init__(self):
        self.result = []


def phoneNumberMnemonics(phoneNumber):
    keyboard = {0: ["0"],
                1: ["1"],
                2: ["a", "b", "c"],
                3: ["d", "e", "f"],
                4: ["g", "h", "i"],
                5: ["j", "k", "l"],
                6: ["m", "n", "o"],
                7: ["p", "q", "r", "s"],
                8: ["t", "u", "v"],
                9: ["w", "x", "y", "z"]}

    def solve(digit_index, output, info):
        if digit_index == len(phoneNumber):
            if output != "":
                info.result.append(output)
            return

        current_digit = int(phoneNumber[digit_index])
        for letter in keyboard[current_digit]:
            solve(digit_index + 1, output + letter, info)

    info = ResultInfo()
    solve(0, "", info)
    return info.result
