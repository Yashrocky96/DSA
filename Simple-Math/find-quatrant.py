"""
Check the coordinates and say which quadrant it lies in
"""

def findQuadrant(x, y):
    if x >= 0:
        if y >= 0:
            return 1
        else: return 4
    else:
        if y >= 0:
            return 2
        else: return 3

# NOTE: Please do not modify this function
def main():
    x, y = map(float, input().split(' '))
    quadrant = findQuadrant(x, y)
    print(quadrant)


if __name__ == "__main__":
    main()
