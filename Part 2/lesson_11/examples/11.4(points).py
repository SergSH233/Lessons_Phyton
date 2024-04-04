class Axes:
    def __init__(self, axis_x, axis_y):
        self.axis_x = axis_x
        self.axis_y = axis_y


class Plane:
    def __init__(self):
        self.plane = []

    def add_point_in_plane(self):
        x_point = int(input("Enter x-axis:"))
        y_point = int(input("Enter y-axis:"))
        self.plane.append(Axes(x_point, y_point))
        print("Point added in plane!")

    def count_point_info(self):
        print("Points in the plane are equal: {}".format(len(self.plane)))



new_plane = Plane()
new_plane.count_point_info()
new_plane.add_point_in_plane()
new_plane.add_point_in_plane()
new_plane.count_point_info()

