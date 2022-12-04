from src import king


c = king.conic([0, 1, 2, 0, 3, 0])
# c = king.conic(p_list=king.point(p_list=[[3, 5], [-4, 2], [-4, 9], [0, 2], [5, 4]]))
# c = king.conic(p_list=king.point(p_list=[[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]))

print(c.conic_type)
