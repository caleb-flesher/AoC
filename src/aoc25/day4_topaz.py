# THIS IS NOT MY SOLUTION!!
# This solution is from topaz - https://topaz.github.io/paste/#XQAAAQCZAwAAAAAAAAAjEkW1XgFn/E5D2tha5mUElmE4Qtzudc/Nxo8RilYYffVXgrKaWN68r0N3iP8uyTFDjNid4gOKW7NJSl1vPWVA9jGKmpWz+Cmavo3uS/Enkye+mOlwX2HO3ZW/0+PvNPgEWKGnuZGaPWOXinEKAnkKBzF3/ig6VjZUT2Z+YDzd94v7xZrMa3UMF31XwS67DFnaO4GtZDDbydp3fhO2B5pPHiWwIN4aO3ynW4M5q+Apsci3HBOT/acv5f6W14gMQb1QVwxEYn0bH5Nw/P670A30EA0ro6vsKN19AkySpFaenjfKd7pFzrseDi/h39kg6fJoQdBNeq+c1PLZtG9tHnEq7hzkEA7hCfOldpaCtTvI3U0UKlwS3k65f/u6kXAXTdZ59A8d0BRRlcnxAeXziLmYQ/MmzGHJwfxswf4Ud+6m58jlIMm0sZGOwp5V5OMC4xCkRYPwIDYVhgpZ9F4rJzCk/cMIUaccrsOsngRGpx1KMg+KdVOSyAWqLKaVQNC/5z4QhgP4ML53UbVYYzsNo55H6ZSNfl9m2vxaE5L/29caBA==
# I decided to switch to Python solutions to review some other languages

FILENAME = "inputData/day4_input.txt"
PAPER = "@"
# Check the 3 x 3 grid around a location
NEIGHBOURS = [-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j]

def parse_input(data):
    return {
        # The coordinates are stored when paper is found
        complex(i, j)
        for j, row in enumerate(data)
        for i, col in enumerate(row)
        # If the value at the position is paper, create the complex number
        if col == PAPER
    }

def part1(grid):
    # Store the coordinates of all paper as a set
    accessible = set()
    for pos in grid:
        # Check around the position for other paper
        neighbours = sum((pos + d) in grid for d in NEIGHBOURS)
        if neighbours < 4:
            accessible.add(pos)
    # Return all the coordinates as a set
    return accessible

def part2(grid):
    total_start = len(grid)
    # First pass
    accessible = part1(grid)
    # Loop until there aren't anymore accessible
    while accessible:
        # Remove the paper that is found to be accessible
        grid -= accessible
        accessible = part1(grid)
    return total_start - len(grid)

def main():
    with open(FILENAME) as input_file:
        data = input_file.read().split()
    grid = parse_input(data)
    # We want the length of the set, not the coordinates
    print(len(part1(grid)))
    print(part2(grid))

if __name__ == "__main__":
    main()
