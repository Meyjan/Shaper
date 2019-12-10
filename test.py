import cv2
import numpy as np
import math
import clips

array_facts = []
array_shapes = []
array_rules = []
all_rules = []

# API
def getFacts():
    return array_facts

def getShapes():
    return array_shapes

def getRules():
    return array_rules

def getAllRules():
    return all_rules

# --------------------------------------------------------------

def printArray(arr):
    for element in arr:
        print(element)

# Method for parsing an array into shapes, rules, and facts
def parseArrayShapesAndRules(facts):
    for fact in facts:
        tempFact = ""

        if (fact[0] == "f"):
            tempFact = fact[8:]
        else:
            tempFact = fact

        if ("(shape" in fact):
            tempFact = tempFact.replace("(shape ", "").replace(")", "")
            array_shapes.append(tempFact)
        elif ("(rule_used" in fact):
            tempFact = tempFact.replace("(rule_used ", "").replace(")", "")
            array_rules.append(tempFact)
        else:
            continue

def filter_image(array_points):
    shape_valid = True
    temp_array = []

    for point in array_points:
        if (point[0] == 0 or point[1] == 0):
            shape_valid = False
            break
        else:
            point_valid = True
            for temp_point in temp_array:
                # Checking if there is a point which located too near with each other
                if abs(temp_point[0] - point[0]) < 4 and abs(temp_point[1] - point[1]) < 4:
                    point_valid = False
                    break

            if point_valid:
                temp_array.append(point)

    if (len(temp_array) < 2):
        return (False, temp_array)
    if (shape_valid):
        return (True, temp_array)
    else:
        return (False, temp_array)


# Executing image detection and getting liens and angles
def execute_detection(filename):
    RESULT = []

    font = cv2.FONT_HERSHEY_COMPLEX

    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imwrite("assets_result/temp.jpg", img)

    for cnt in contours:
        POINTS = []
        LINES = []
        ANGLES = []
        GRADIENT = []

        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cv2.drawContours(img, [approx], 0, (0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1]


        # GET POINTS
        for i in range(len(approx)):
            POINTS.append(approx[i][0])

        image_filtered = filter_image(POINTS)
        if (image_filtered[0]):
            POINTS = image_filtered[1]
        else:
            continue

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

            if (delta_x == 0):
                GRADIENT.append(math.inf)
            else:
                GRADIENT.append(round((delta_y / delta_x), 2))

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
            LINES[i] = int(math.sqrt(math.pow(LINES[i][0], 2) + math.pow(LINES[i][1], 2)))

        RESULT.append([POINTS, LINES, ANGLES, GRADIENT])

    if (len(RESULT) > 0):
        processed_fact = []
        for res in RESULT:
            processed_fact.append(fact_processing(res))
        return (True, processed_fact)
    else:
        return (False, RESULT)

# Change facts into something that can be inserted into clips
def fact_processing(facts):
    environment = clips.Environment()
    environment.load("test.clp")

    fact = '(count_vertex ' + str(len(facts[0])) + ')'
    environment.assert_string(fact)

    for i in range (len(facts[1])):
        fact = '(detected_shape (id ' + str(i + 1) + ') (angle ' + str(facts[2][i]) + ') (length ' + str(facts[1][i]) + ') (gradient ' + str(facts[3][i]) + '))'
        environment.assert_string(fact)

    environment.run()

    for result_fact in environment.facts():
        array_facts.append(str(result_fact))

    for result_rule in environment.rules():
        all_rules.append(str(result_rule))

    return (array_facts, all_rules)

facts = execute_detection("assets/shape.jpg")
parseArrayShapesAndRules(array_facts)
print("- facts :")
printArray(array_facts)
print()
print("- shapes :")
printArray(array_shapes)
print()
print("- rules :")
printArray(array_rules)

# fact_processing(facts)

# assert(count_vertex 3)
# assert(detected_shape (id 1) (length 2) (angle 90))



#     FOR PAGE DRAWING ETC.

#         if len(approx) == 3:
#             cv2.putText(img, "Triangle", (x, y), font, 1, (0))
#         elif len(approx) == 4:
#             cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
#         elif len(approx) == 5:
#             cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
#         elif 6 < len(approx) < 15:
#             cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
#         else:
#             cv2.putText(img, "Circle", (x, y), font, 1, (0))

#     cv2.imshow("shapes", img)
#     cv2.imshow("Threshold", threshold)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
