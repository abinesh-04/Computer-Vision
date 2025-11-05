import cv2

cap = cv2.VideoCapture("C:/Users/HP/Downloads/857263-hd_1920_1080_24fps.mp4")
if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

#read 1st frame here
ret, prev_frame = cap.read()
if not ret:
    print("Error: Cannot read first frame.")
    exit()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # abs difference
    diff = cv2.absdiff(prev_gray, gray)

    # motion mask threashholding
    _, motion_mask = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # highlighting motion areas
    contours, _ = cv2.findContours(motion_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:  # Filter smollmotion
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Motion Detection", frame)
    cv2.imshow("Motion Mask", motion_mask)

    prev_gray = gray.copy()

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
