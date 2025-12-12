import sys


def parse_input(content):
    parts = content.strip().split('\n\n')
    shapes = {}
    regions = []

    for part in parts:
        lines = part.strip().splitlines()
        if not lines: continue

        header = lines[0]

        is_region_block = False
        if ':' in header:
            label = header.split(':')[0].strip()
            if 'x' in label:
                is_region_block = True

        if is_region_block:
            for line in lines:
                if ':' in line and 'x' in line:
                    p_meta, p_counts = line.split(':')
                    w, h = map(int, p_meta.split('x'))
                    counts = list(map(int, p_counts.strip().split()))
                    regions.append({'w': w, 'h': h, 'counts': counts})
        else:
            try:
                idx_str = header.split(':')[0].strip()
                idx = int(idx_str)
                grid_lines = lines[1:]
                coords = set()
                for r, row in enumerate(grid_lines):
                    for c, char in enumerate(row):
                        if char == '#':
                            coords.add((r, c))
                shapes[idx] = coords
            except ValueError:
                pass

    return shapes, regions


def normalize_shape(coords):
    sorted_coords = sorted(list(coords))
    if not sorted_coords:
        return tuple()

    r0, c0 = sorted_coords[0]
    normalized = []
    for r, c in sorted_coords:
        # Relativize all coordinates to the anchor
        normalized.append((r - r0, c - c0))
    return tuple(normalized)


def generate_variants(base_coords):
    variants = set()
    if not base_coords:
        return []

    # Transformations: (r, c) -> ...
    # Rotation 0, 90, 180, 270
    transforms = [
        lambda r, c: (r, c),
        lambda r, c: (-c, r),
        lambda r, c: (-r, -c),
        lambda r, c: (c, -r)
    ]

    # Base shape and its flipped version
    configs = [list(base_coords), [(r, -c) for r, c in base_coords]]

    for cfg in configs:
        for t in transforms:
            new_coords = set()
            for r, c in cfg:
                new_coords.add(t(r, c))
            # Normalize to ensure consistent anchor at (0,0)
            variants.add(normalize_shape(new_coords))

    return list(variants)


def solve(grid_flat, w, h, counts, all_variants, slack, start_idx):
    # Find the first empty cell in the grid
    idx = -1
    for i in range(start_idx, w * h):
        if not grid_flat[i]:
            idx = i
            break

    if idx == -1:
        # No empty cells left. Check if we have successfully placed all presents.
        # If any count > 0, we failed to place everything.
        if any(c > 0 for c in counts):
            return False
        return True

    # Current anchor position (r, c)
    r, c = divmod(idx, w)

    # Branch 1: Try to place a present anchored at this cell
    for s_idx, count in enumerate(counts):
        if count > 0:
            for variant in all_variants[s_idx]:
                fits = True
                indices_to_mark = []

                for dr, dc in variant:
                    nr, nc = r + dr, c + dc

                    # Boundary check
                    if not (0 <= nr < h and 0 <= nc < w):
                        fits = False
                        break

                    n_idx = nr * w + nc

                    # Overlap check
                    if grid_flat[n_idx]:
                        fits = False
                        break

                    indices_to_mark.append(n_idx)

                if fits:
                    # Place the present
                    for mark_idx in indices_to_mark:
                        grid_flat[mark_idx] = True

                    counts[s_idx] -= 1

                    # Recurse
                    if solve(grid_flat, w, h, counts, all_variants, slack, idx + 1):
                        return True

                    # Backtrack (Remove the present)
                    counts[s_idx] += 1
                    for mark_idx in indices_to_mark:
                        grid_flat[mark_idx] = False

    # Branch 2: Leave this cell empty (skip it)
    # We can only do this if we have "slack" (extra area) remaining.
    if slack > 0:
        grid_flat[idx] = True  # Mark as "filled" (skipped)
        if solve(grid_flat, w, h, counts, all_variants, slack - 1, idx + 1):
            return True
        grid_flat[idx] = False  # Backtrack

    return False


def main():
    try:
        with open('input.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return

    shapes_raw, regions = parse_input(content)

    if not shapes_raw:
        print(0)
        return

    # Precompute all variants for all shapes
    max_id = max(shapes_raw.keys())
    all_variants = [[] for _ in range(max_id + 1)]
    shape_areas = [0] * (max_id + 1)

    for sid, coords in shapes_raw.items():
        all_variants[sid] = generate_variants(coords)
        shape_areas[sid] = len(coords)

    success_count = 0

    for region in regions:
        w = region['w']
        h = region['h']
        counts = region['counts']

        # Calculate total area required by presents
        total_present_area = 0

        # Pad counts if the region list is shorter than the number of shape types
        current_counts = list(counts)
        if len(current_counts) < len(shape_areas):
            current_counts += [0] * (len(shape_areas) - len(current_counts))

        for sid, count in enumerate(current_counts):
            if sid < len(shape_areas):
                total_present_area += count * shape_areas[sid]

        # Immediate fail if presents are larger than region
        if total_present_area > w * h:
            continue

        # Calculate slack (allowed empty space)
        slack = (w * h) - total_present_area

        # Initialize flat grid
        grid = [False] * (w * h)

        if solve(grid, w, h, current_counts, all_variants, slack, 0):
            success_count += 1

    print(success_count)


if __name__ == '__main__':
    # Increase recursion limit for deep search trees
    sys.setrecursionlimit(5000)
    main()