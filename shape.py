import cv2
import numpy as np

# ------------------- video ---------------------

# vid = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = vid.read()
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     edged = cv2.Canny(gray, 30, 200)
#     contours, hierarchy = cv2.findContours(edged,
#                                            cv2.RETR_EXTERNAL,
#                                            cv2.CHAIN_APPROX_NONE)
#     print(contours)
#     cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
#     cv2.imshow('video', frame)
# vid.release()
# cv2.destroyAllWindows()

# -------------------- photo -----------------------
'''
frame = cv2.imread("sqrods.jpg", 1)
frame = cv2.resize(frame, (512, 512))
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 30, 200)
contours, hierarchy = cv2.findContours(edged,
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)

rects = []
circles = []
rest_loc = []
cir_loc = []
for cont in contours:
    approx = cv2.approxPolyDP(cont, 0.01*cv2.arcLength(cont, True), True)
    area = cv2.contourArea(cont)
    if area >= 500:
        if len(approx) == 4:
            rects.append(approx)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            rest_loc.append((x, y))
        else:
            circles.append(approx)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            cir_loc.append((x, y))

for num, (approx, loc) in enumerate(zip(rects, rest_loc)):
    cv2.drawContours(frame, [approx], 0, (0, 0, 255), 3)
    cv2.putText(frame, f"r{num + 1}", (loc[0], loc[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
for num, (approx, loc) in enumerate(zip(circles, cir_loc)):
    cv2.drawContours(frame, [approx], 0, (240, 10, 17), 3)
    cv2.putText(frame, f"c{num + 1}", (loc[0], loc[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (110, 0, 100))


cv2.imshow('video', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# ------------------ video frames ----------------------

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if cv2.waitKey(1) & 0xFF == 27:
        break
    frame = cv2.resize(frame, (512, 512))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edged = cv2.Canny(gray, 30, 200)
    contours, hierarchy = cv2.findContours(edged,
                                           cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    rects = []
    rest_loc = []

    circles = []
    cir_loc = []
    for cont in contours:
        approx = cv2.approxPolyDP(cont, 0.01 * cv2.arcLength(cont, True), True)
        area = cv2.contourArea(cont)
        if area >= 100:
            if len(approx) == 4:
                rects.append(approx)
                x = approx.ravel()[0]
                y = approx.ravel()[1]
                rest_loc.append((x, y))
            else:
                circles.append(approx)
                x = approx.ravel()[0]
                y = approx.ravel()[1]
                cir_loc.append((x, y))

    for num, (approx, loc) in enumerate(zip(rects, rest_loc)):
        cv2.drawContours(frame, [approx], 0, (0, 0, 255), 3)
        cv2.putText(frame, f"r{num + 1}", (loc[0], loc[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    for num, (approx, loc) in enumerate(zip(circles, cir_loc)):
        cv2.drawContours(frame, [approx], 0, (240, 10, 17), 3)
        cv2.putText(frame, f"c{num + 1}", (loc[0], loc[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (110, 0, 100))
    cv2.imshow('video', frame)

vid.release()
cv2.destroyAllWindows()


