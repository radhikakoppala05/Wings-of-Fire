import cv2


img = cv2.imread('road.jpg')


color = (0, 0, 255)   
thickness = 8
line_type = cv2.LINE_AA


cv2.ellipse(img, center=(1020, 850), axes=(180, 620), angle=0,
            startAngle=0, endAngle=360, color=color, thickness=thickness, lineType=line_type)


cv2.ellipse(img, center=(2130, 780), axes=(190, 640), angle=0,
            startAngle=0, endAngle=360, color=color, thickness=thickness, lineType=line_type)


cv2.ellipse(img, center=(1620, 1330), axes=(190, 130), angle=0,
            startAngle=0, endAngle=360, color=color, thickness=thickness, lineType=line_type)


cv2.ellipse(img, center=(1443, 1920), axes=(330, 155), angle=0, startAngle=0, endAngle=360, color=color, thickness=thickness, lineType=line_type)


cv2.imwrite('road_annotated.jpg', img)
cv2.destroyAllWindows()