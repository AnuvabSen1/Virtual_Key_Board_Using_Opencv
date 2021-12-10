try:
    import cv2
    from cvzone.HandTrackingModule import HandDetector
    import cvzone
    from pynput.keyboard import Controller
    import imutils
    from time import sleep
    from configs import WIDTH, HEIGHT, FPS, INDEX_FINGER_TIP, MIDDLE_FINGER_TIP, DIST_INDEX_MID
except:
    print("Fulfil Requirements, use requirements.txt")


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,  HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]


keyboard = Controller()
buttonList = []
finalText = ""


def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (x, y, w, h),
                          20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h),
                      (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img


class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

    def __repr__(self) -> str:
        return f"pos -> {self.pos}, size -> {self.size}, text -> {self.text}"


def generate_buttons():
    global buttonList
    for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            buttonList.append(Button([100 * j + 50, 100 * i + 50], key))


def text_field():
    cv2.rectangle(img, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)


generate_buttons()
while True:
    success, img = cap.read()
    img = cv2.resize(img, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)
    hands, img = detector.findHands(img)
    img = drawAll(img, buttonList)

    if hands:
        hand1 = hands[0]
        lmlist1 = hand1["lmList"]  # List of 21 Landmark points
        bboxInfo1 = hand1["bbox"]  # Bounding box info x,y,w,h
        # centerPoint1 = hand1['center']  # center of the hand cx,cy
        # handType1 = hand1["type"]  # Handtype Left or Right

        if lmlist1:
            for button in buttonList:
                x, y = button.pos
                w, h = button.size

                if x < lmlist1[INDEX_FINGER_TIP][0] < x + w and y < lmlist1[INDEX_FINGER_TIP][1] < y + h:
                    cv2.rectangle(img, button.pos, (x + w, y + h),
                                  (0, 0, 255), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    l, _, _ = detector.findDistance(
                        lmlist1[INDEX_FINGER_TIP], lmlist1[MIDDLE_FINGER_TIP], img)

                    if l < DIST_INDEX_MID:
                        keyboard.press(button.text)
                        finalText += button.text

    text_field()
    cv2.imshow("Virtual Keyboard", img)
    cv2.waitKey(1)
