import math 

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise

def convex_hull_graham(points):
    n = len(points)
    if n < 3:
        return []

    # Find the point with the lowest y-coordinate (and leftmost if tied)
    ymin = min(points, key=lambda p: (p[1], p[0]))

    def angle_cmp(p1, p2):
        # Calculate polar angle
        angle1 = math.atan2(p1[1] - ymin[1], p1[0] - ymin[0])
        angle2 = math.atan2(p2[1] - ymin[1], p2[0] - ymin[0])

        # Compare polar angles
        if angle1 < angle2:
            return -1
        elif angle1 > angle2:
            return 1
        else:
            return 0

    # Sort the points based on their polar angle with respect to the lowest point
    sorted_points = sorted(points, key=cmp_to_key(angle_cmp))

    # Initialize the stack with the first three points
    hull = [sorted_points[0], sorted_points[1]]

    for i in range(2, n):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i]) != 2:
            hull.pop()
        hull.append(sorted_points[i])

    return hull


# MIAN


# Create a list of points
# Create a list of points
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]

# Compute the convex hull using Graham's scan algorithm
convex_hull = convex_hull_graham(points)

# Print the convex hull points
for point in convex_hull:
    print(f"({point[0]}, {point[1]})")
