import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def dot_product(a, b):
    return (a.x * b.x) + (a.y * b.y)

def cross_product(a, b):
    return a.x * b.y - a.y * b.x;
    
# return The minimum point in its x-coordinates
def minimum_point(points):
    MIN = float('inf')
    index = 0
    for i, point in enumerate(points):
        if point.x < MIN:
            MIN = point.x
            index = i
    return points[index]

def calculate_angles_and_sort(horizontal_line: Line, points: List[Point], min_y: Point) -> List[tuple[Point, float]]:
    sorted_points = []
    start_point = Point(horizontal_line.end.y - horizontal_line.start.y, horizontal_line.end.x - horizontal_line.start.x)
    for point in points:
        tmp = Point(point.y - horizontal_line.start.y, point.x - horizontal_line.start.x)
        cross_product = HelperMethods.cross_product(start_point, tmp)
        dot_product_val = dot_product(start_point, tmp)
        rad_angle = math.atan2(cross_product, dot_product_val)
        deg_angle = (180 / math.pi) * rad_angle
        sorted_points.append((point, deg_angle))
    sorted_points.sort(key=lambda x: x[1])
    sorted_points.append((min_y, 0))
    return sorted_points

def graham(points):
    # 
    if len(points) < 3:
        return []
    # 
    min_y = minimum_point(points)
    inti_point = Point(min_y.x + 1, min_y.y)
    horizontal_line = Line(min_y, inti_point)
    points.remove(min_y)
    sorted_points = calculate_angles_and_sort(horizontal_line, points, min_y)

    hull = [min_y, sorted_points[0][0]]
    i = 1

    while i < len(sorted_points):
        top = hull.pop()
        pre_top = hull.pop()
        hull.append(pre_top)
        hull.append(top)
        segment = Line(top, pre_top)

        while len(hull) > 2 and HelperMethods.check_turn(segment, sorted_points[i][0]) != Enums.TurnType.LEFT:
            hull.pop()
            top = hull.pop()
            pre_top = hull.pop()
            hull.append(pre_top)
            hull.append(top)
            segment = Line(top, pre_top)

        hull.append(sorted_points[i][0])
        i += 1

    hull.pop()  # Remove the duplicate point (min_y) from the end
    return hull

def main():
    # create Points
    points = [Point(0, 3), Point(2, 2), Point(1, 1), Point(2, 1), Point(3, 0), Point(0, 0), Point(3, 3)]
    # Run Convex Hull Graham
    convex_hull = graham(points)
    # Display the Convex Hull Points
    for point in convex_hull:
        print(f"({point.x}, {point.y})")


if __name__=="__main__":
    main()