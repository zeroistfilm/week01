

x, y, w, h = map(int, input().split())
print(min(x, w-x, y, h-y))

# def exit_rectangle(x, y, w, h):
#     minimum = x - 0
#     if w - x < minimum:
#         minimum = w - x
#     if y - 0 < minimum:
#         minimum = y - 0
#     if h - y < minimum:
#         minimum = h - y
#     return minimum
#
#
# print(exit_rectangle(x, y, w, h))

