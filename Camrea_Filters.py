import cv2

def Effects(frame, effect):
    if effect == "gray":
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif effect == "canny":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 100, 200)
    elif effect == "mirror":
        return cv2.flip(frame, 1)
    else:
        return frame  # normal

def Change_effects(key):
    if key == ord('q'):  # quit
        return "False"
    elif key == ord('g'):  # grayscale
        return "gray"
    elif key == ord('c'):  # canny
        return "canny"
    elif key == ord('m'):  # mirror
        return "mirror"
    elif key == ord('n'):  # normal
        return "normal"
    return None  # no change

cap = cv2.VideoCapture(0)
effect = "normal"

while effect != "False":
    ret, frame = cap.read()
    if not ret:
        break

    # Apply effect and update frame
    frame = Effects(frame, effect)

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF
    new_effect = Change_effects(key)
    if new_effect is not None:
        effect = new_effect

cap.release()
cv2.destroyAllWindows()