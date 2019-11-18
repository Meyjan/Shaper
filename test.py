import cv2
import numpy as np
import math
import clips


def execute_detection(filename):
    RESULT = []

    font = cv2.FONT_HERSHEY_COMPLEX

    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        POINTS = []
        LINES = []
        ANGLES = []

        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cv2.drawContours(img, [approx], 0, (0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        # GET POINTS
        for i in range(len(approx)):
            POINTS.append(approx[i][0])

        # GET LENGTH
        for i in range(len(POINTS)):
            if i == 0:
                point_1 = POINTS[len(POINTS) - 1]
                point_2 = POINTS[i]
            else:
                point_1 = POINTS[i-1]
                point_2 = POINTS[i]
            
            delta_x = point_2[0] - point_1[0]
            delta_y = (point_2[1] - point_1[1]) * -1

            if delta_x < 5 and delta_x > -5:
                delta_x = 0
            if delta_y < 5 and delta_y > -5:
                delta_y = 0
            LINES.append([delta_x, delta_y])
        
        # GET VERTEXES
        for i in range(len(LINES)):
            if i == 0:
                line_1 = LINES[len(LINES) - 1]
                line_2 = LINES[i]
            else:
                line_1 = LINES[i - 1]
                line_2 = LINES[i]
            
            if i != len(LINES) - 1:
                line_1[0] *= -1
                line_1[1] *= -1 
            
            numerator = line_1[0] * line_2[0] + line_1[1] * line_2[1]
            denumerator = math.sqrt(math.pow(line_1[0], 2) + math.pow(line_1[1], 2)) * math.sqrt(math.pow(line_2[0], 2) + math.pow(line_2[1], 2))

            cosine = numerator / denumerator
            result = np.arccos(cosine)
            ANGLES.append(round(math.degrees(result)))


        # Line fixing
        for i in range(len(LINES)):
            LINES[i][0] *= -1
            LINES[i][1] *= -1
            LINES[i] = math.sqrt(math.pow(LINES[i][0], 2) + math.pow(LINES[i][1], 2))
        
        RESULT.append([POINTS, LINES, ANGLES])
        return RESULT
        
execute_detection("shape.jpg")

    

    # FOR PAGE DRAWING ETC.

        # if len(approx) == 3:
        #     cv2.putText(img, "Triangle", (x, y), font, 1, (0))
        # elif len(approx) == 4:
        #     cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
        # elif len(approx) == 5:
        #     cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
        # elif 6 < len(approx) < 15:
        #     cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
        # else:
        #     cv2.putText(img, "Circle", (x, y), font, 1, (0))

    # cv2.imshow("shapes", img)
    # cv2.imshow("Threshold", threshold)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# def fact_processor(facts):
#     # Number of lines
#     VERTEX_COUNT = len(facts[0])
#     EDGE_COUNT = len(facts[1])

#     # Checking angle
#     OBTUSE = 0
#     RIGHT = 0
#     for i in range(facts[2]):
#         if facts[2][i] == 90:
#             RIGHT += 1
#         if facts[2][i] > 90:
#             OBTUSE += 1
    
#     ANGLE_PAIR = 0
#     for i in range(facts[2]):
#         if facts
