
def rectangle_to_bbox(points):
    x1, y1 = map(float, points[0])
    x2, y2 = map(float, points[1])
    return (x1, y1, x2, y2)

def polygon_to_bbox(points):
    x_max = max(points, key=lambda p: p[0])[0]
    y_max = max(points, key=lambda p: p[1])[1]
    x_min = min(points, key=lambda p: p[0])[0]
    y_min = min(points, key=lambda p: p[1])[1]
    return (x_min, y_max, x_max, y_min)
def extract_bounding_box(shape):
    if shape['shape_type'] == 'polygon':
        return polygon_to_bbox(shape['points'])
    elif shape['shape_type'] == 'rectangle':
        return rectangle_to_bbox(shape['points'])