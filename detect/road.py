import cv2
import numpy as np

def draw_highlight_loop(img, center, radius_x, radius_y, color=(80, 220, 120),
                         thickness=6, points=60, wobble=3, seed=0):
    np.random.seed(seed)
    cx, cy = center
    angles = np.linspace(0, 2 * np.pi, points, endpoint=False)
    noise = wobble * np.sin(angles * 3 + seed) + np.random.normal(0, 1, points)

    pts = []
    for a, n in zip(angles, noise):
        x = int(cx + (radius_x + n) * np.cos(a))
        y = int(cy + (radius_y + n) * np.sin(a))
        pts.append([x, y])

    pts = np.array(pts, dtype=np.int32).reshape(-1, 1, 2)
    cv2.polylines(img, [pts], isClosed=True, color=color,
                  thickness=thickness, lineType=cv2.LINE_AA)
    return img


img = cv2.imread("image.png")  # 1189 x 858

# (center_x, center_y, radius_x, radius_y)
circles_to_draw = [
    (612, 187, 70, 60),   # enlarged gray pipe cluster near tractor
    (655, 335, 50, 65),   # blue pipes
    (798, 522, 55, 90),   # pole / wires
    (610, 715, 100, 95),  # pile + lone pipe
]

for i, (cx, cy, rx, ry) in enumerate(circles_to_draw):
    img = draw_highlight_loop(img, (cx, cy), rx, ry, seed=i)

cv2.imwrite("output.jpg", img)