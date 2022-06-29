class short_rectangle:
    x = 2
    y = 4
    width = 1
    length = 4


class long_rectangle:
    x = 0
    y = 0
    width = 10
    length = 4


def touching_rectangles(rect1, rect2):
    left_rectangle = rect1
    right_rectangle = rect2
    # Determine which triangle is to the left
    if (rect1.x - rect2.x > 0):
        left_rectangle = rect2
        right_rectangle = rect1

    x1, y1 = left_rectangle.x, left_rectangle.y

    # Find each points of the rectangle
    left = x1
    right = x1 + left_rectangle.width
    top = y1
    bottom = y1 - left_rectangle.length

    # The top left point of the right rectangle
    x2, y2 = right_rectangle.x, right_rectangle.y
    # The bottom left point of the right rectangle
    xb, yb = right_rectangle.x - \
        right_rectangle.width, right_rectangle.x - right_rectangle.length

    # Check if the top left point OR the bottom left point is overlapping the left rectangle
    if left <= x2 <= right and (bottom <= y2 <= top or bottom <= yb <= top):
        return "The rectangles do touch"
    else:
        return "They do not touch"


print(touching_rectangles(long_rectangle, short_rectangle))
