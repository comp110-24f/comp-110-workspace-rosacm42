"""CQ4 Part 2"""

___author___ = 730398449

"Print fromatted pairs of each character in two strings"
def get_coords(xs: str, ys: str) -> None:
    while (idx_x < len(xs)): 
         while (idx_y < len(ys)): 
             print("(" + xs[idx_x] + "," + ys[idx_y] + ")")
             idx_y += 1
    idx_y = 0
    idx_x += 1
