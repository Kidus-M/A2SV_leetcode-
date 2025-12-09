import sys


def is_between(val, low, high):
    """Check if val is strictly between low and high."""
    return min(low, high) < val < max(low, high)


def ranges_overlap(a_start, a_end, b_start, b_end):
    """Check if range A overlaps strictly with range B."""
    # Strict overlap means the intersection has length > 0
    start = max(min(a_start, a_end), min(b_start, b_end))
    end = min(max(a_start, a_end), max(b_start, b_end))
    return start < end


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
    if n < 4:  # Need at least 4 points to form a closed loop with area
        print(0)
        return

    # Build edges of the polygon
    edges = []
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        edges.append((p1, p2))

    max_area = 0

    # Iterate through all unique pairs of points to form candidate rectangles
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            # Calculate dimensions
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height

            # Optimization: Skip if area is not larger than current max
            if area <= max_area:
                continue

            # Define rectangle boundaries
            rx_min, rx_max = min(x1, x2), max(x1, x2)
            ry_min, ry_max = min(y1, y2), max(y1, y2)

            # 1. Check if any polygon edge cuts through the rectangle's interior
            # A rectangle is convex. If a polygon edge passes through it, it's invalid
            # (unless it lies on the boundary, which is allowed).
            intersects_interior = False
            for p_start, p_end in edges:
                if p_start[0] == p_end[0]:  # Vertical Polygon Edge
                    ex = p_start[0]
                    if is_between(ex, rx_min, rx_max):
                        # Check Y overlap
                        if ranges_overlap(p_start[1], p_end[1], ry_min, ry_max):
                            intersects_interior = True
                            break
                else:  # Horizontal Polygon Edge
                    ey = p_start[1]
                    if is_between(ey, ry_min, ry_max):
                        # Check X overlap
                        if ranges_overlap(p_start[0], p_end[0], rx_min, rx_max):
                            intersects_interior = True
                            break

            if intersects_interior:
                continue

            # 2. Check if the rectangle is inside the polygon (or on boundary)
            # Since we checked for edge intersections, we just need to test one point.
            # We test the geometric center.
            cx = (rx_min + rx_max) / 2.0
            cy = (ry_min + ry_max) / 2.0

            # Ray casting algorithm
            # Count intersections of ray from (cx, cy) to (infinity, cy) with vertical edges
            intersections = 0
            for p_start, p_end in edges:
                # Only check vertical edges for horizontal ray
                if p_start[0] == p_end[0]:
                    vx = p_start[0]
                    v_y1, v_y2 = p_start[1], p_end[1]

                    # Check if ray crosses this vertical segment
                    # Use strictly greater/less logic for Y to handle vertices consistently
                    # (Standard simulation of ray passing 'slightly above' vertices)
                    if vx > cx:
                        if (v_y1 <= cy < v_y2) or (v_y2 <= cy < v_y1):
                            intersections += 1

            # Odd intersections = Inside
            # Even intersections = Outside
            if intersections % 2 == 1:
                max_area = area

    print(max_area)


if __name__ == '__main__':
    main()