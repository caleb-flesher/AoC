FILENAME = "inputData/day5_input.txt"

def parse_input(data):
    with open(data) as f:
        contents = f.read()

    # Split at the empty line
    rangeVals, output2 = contents.split('\n\n', 1)
    # Originally was going to make 2 sets for intersection
    freshVals = set()

    # Add fresh IDs to set
    for line in output2.splitlines():
        freshVals.add(int(line))

    # Return tuple
    return rangeVals, freshVals

def part1(inputResults):
    count = 0
    rangeVals, freshVals = inputResults

    # Double loop, compare the tuples for ranges for fresh
    for line in freshVals:
        for range in rangeVals.splitlines():
            parts = range.split('-')
            start = int(parts[0])
            end = int(parts[1])
            # If in the range, increase count and break loop
            if start <= line <= end:
                count += 1
                break

    return count

def part2(inputResults):
    count = 0
    # Extra value not needed for this part
    rangeVals, extra = inputResults
    rangeList = []

    # Append each range line as a tuple
    for line in rangeVals.splitlines():
        parts = line.split('-')
        rangeList.append((int(parts[0]), int(parts[1])))

    # Sort the ranges
    rangeList.sort()
    
    # Refactor the ranges to not overlap
    for i in range(len(rangeList)-1, 0, -1):
        if rangeList[i-1][1] >= rangeList[i][0]:
            rangeList[i-1] = (rangeList[i-1][0], rangeList[i][1])
            rangeList.pop(i)

    # Check the counts for the ranges and add 1 to include the first value
    for i in rangeList:
        count += (i[1] - i[0]) + 1

    return count


def main():
    print(part1(parse_input(FILENAME)))
    print(part2(parse_input(FILENAME)))

if __name__ == "__main__":
    main()