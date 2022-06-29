color_map = []


def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            aligned_color_map_string(i, j, major, minor)
    return len(major_colors) * len(minor_colors)


def aligned_color_map_string(i, j, major, minor):
    color_map.append('{:<10} | {:<10} | {:<10}.format(i, j, major, minor)')
    return color_map

