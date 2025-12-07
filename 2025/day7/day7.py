def calc_split_beams_in_tachyon_manifold(tachyon_manifold):
    split_n = 0
    beams_idx = [tachyon_manifold[0].index("S")]
    for tachyon in tachyon_manifold[1:]:
        new_beams_idx = list(beams_idx)
        for idx, beam_idx in enumerate(beams_idx):
            if tachyon[beam_idx] == "^":
                new_beams_idx.append(new_beams_idx[idx] - 1)
                new_beams_idx[idx] += 1
                split_n += 1
        beams_idx = set(new_beams_idx)

    return split_n
            

# Part 1
with open("input.txt", "r") as f:
    tachyon_manifold = [line.strip() for line in f.readlines()]

split_n = calc_split_beams_in_tachyon_manifold(tachyon_manifold)
print("Part 1: ", split_n)
