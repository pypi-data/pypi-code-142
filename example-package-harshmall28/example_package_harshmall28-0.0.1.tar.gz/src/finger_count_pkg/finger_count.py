import cv2
import mediapipe as mp
import numpy as np
import base64
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

class FingerCounts:
    def is_fingerCount(self, im_b64):
        with mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
            im_bytes = base64.b64decode(im_b64)
            # print(im_bytes)
            im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
            image = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
            # image = cv2.imread("./new.jpeg")
            # print(image)
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Initially set finger count to 0 for each cap
            fingerCount = 0

            if results.multi_hand_landmarks:

                for hand_landmarks in results.multi_hand_landmarks:
                    # Get hand index to check label (left or right)
                    handIndex = results.multi_hand_landmarks.index(hand_landmarks)
                    handLabel = results.multi_handedness[handIndex].classification[0].label

                    # Set variable to keep landmarks positions (x and y)
                    handLandmarks = []

                    # Fill list with x and y positions of each landmark
                    for landmarks in hand_landmarks.landmark:
                        handLandmarks.append([landmarks.x, landmarks.y])

                    # Test conditions for each finger: Count is increased if finger is 
                    #   considered raised.
                    # Thumb: TIP x position must be greater or lower than IP x position, 
                    #   deppeding on hand label.
                    if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                        fingerCount = fingerCount+1
                    elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                        fingerCount = fingerCount+1

                    # Other fingers: TIP y position must be lower than PIP y position, 
                    #   as image origin is in the upper left corner.
                    if handLandmarks[8][1] < handLandmarks[6][1]:       #Index finger
                        fingerCount = fingerCount+1
                    if handLandmarks[12][1] < handLandmarks[10][1]:     #Middle finger
                        fingerCount = fingerCount+1
                    if handLandmarks[16][1] < handLandmarks[14][1]:     #Ring finger
                        fingerCount = fingerCount+1
                    if handLandmarks[20][1] < handLandmarks[18][1]:     #Pinky
                        fingerCount = fingerCount+1
                    return fingerCount
                    # print(fingerCount)
if __name__ == '__main__':
    np = FingerCounts()
