import sys


def main():
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return

    points = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 2:
            try:
                x = int(parts[0])
                y = int(parts[1])
                points.append((x, y))
            except ValueError:
                continue

    n = len(points)
    if n < 2:
        print(0)
        return

    max_area = 0

    # Iterate through all unique pairs of points
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            # Calculate width and height inclusive of the tiles themselves
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1

            area = width * height

            if area > max_area:
                max_area = area

    print(max_area)


if __name__ == '__main__':
    main()