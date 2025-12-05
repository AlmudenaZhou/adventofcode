def get_available_fresh_ids(ingredients_ids):
    sep_ranges = ingredients_ids.index("")

    fresh_ranges = ingredients_ids[:sep_ranges]
    available_ids = ingredients_ids[sep_ranges+1:]

    fresh_products = set()

    for fresh_range in fresh_ranges:
        start, end = fresh_range.split("-")
        for available_id in available_ids:
            if available_id not in fresh_products and int(start) <= int(available_id) <= int(end):
                fresh_products.add(available_id)
    return fresh_products


def get_compact_fresh_ranges(ingredients_ids):
    sep_ranges = ingredients_ids.index("")
    fresh_ranges = ingredients_ids[:sep_ranges]

    compact_fresh_ranges = []
    for fresh_range in fresh_ranges:
        start, end = fresh_range.split("-")
        start, end = int(start), int(end)
        to_append = True
        for compact_fresh_range in compact_fresh_ranges[::-1]:
            if compact_fresh_range[0] <= start <= compact_fresh_range[1]:
                start = compact_fresh_range[0]
                if end < compact_fresh_range[1]:
                    end = compact_fresh_range[1]
                compact_fresh_ranges.remove(compact_fresh_range)
            elif compact_fresh_range[0] >= start and end >= compact_fresh_range[1]:
                compact_fresh_ranges.remove(compact_fresh_range)
            elif compact_fresh_range[1] >= end >= compact_fresh_range[0]:
                end = compact_fresh_range[1]
                if start > compact_fresh_range[0]:
                    start = compact_fresh_range[0]
                compact_fresh_ranges.remove(compact_fresh_range)
            elif compact_fresh_range[0] <= start and compact_fresh_range[1] >= end:
                to_append = False
        if to_append:
            compact_fresh_ranges.append((start, end))
    return compact_fresh_ranges


with open("input.txt", "r") as f:
    ingredients_ids = [line.strip() for line in f.readlines()]

# Part 1
fresh_products = get_available_fresh_ids(ingredients_ids)
print("Part 1: ", len(fresh_products))

# Part 2
compact_fresh_ranges = get_compact_fresh_ranges(ingredients_ids)
fresh_ids = sum([end - start + 1 for start, end in compact_fresh_ranges])
print("Part 2: ", fresh_ids)
