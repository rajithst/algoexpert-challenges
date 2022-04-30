class TreeInfo:
    def __init__(self):
        self.result = []


def generateDivTags(numberOfTags):
    # Write your code here.
    def generate(output, n, open_divs, closed_divs, current, info):
        if current == n * 2:
            info.result.append(output)
            return
        if open_divs < n:
            generate(output + "<div>", n, open_divs + 1, closed_divs, current + 1, info)
        if closed_divs < open_divs:
            generate(output + "</div>", n, open_divs, closed_divs + 1, current + 1, info)

    info = TreeInfo()
    generate("", numberOfTags, 0, 0, 0, info)
    return info.result
