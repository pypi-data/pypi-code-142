from src import king

count = 14


@king.geometries_generate(classes=[king.KingPoint], numbers=[count])
def point_intersect_line_conic(depends=(), essential_data=None):
    c = depends[0].basic_data[0]
    a_list = [(0, 0)]

    for i in range(count):
        a_list.append((i + 1, a_list[i][1] ** 2 / 2 + c))
        print(i)

    return a_list


cp = king.point(1, -3)
point_intersect_line_conic(depends=[cp])
