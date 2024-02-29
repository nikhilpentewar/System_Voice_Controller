import cv2
import mediapipe as mp
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import numpy as np
import time
from math import hypot

# Initialize WebCam and Hand Attributes
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Initialize System Audio and Get the Volume Range
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[:2]

# Initialize Timer and Position
start_time = None
in_position = False

while True:
    # Capture a frame from the WebCam
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Find Hand
    results = hands.process(imgRGB)
    lmList = []

    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            # Extract Landmark Info for Each Detected Hand
            for id, lm in enumerate(handlandmark.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                # Draw Landmarks on Hand Image
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

        if lmList:
            # Find Thumb Tip
            x1, y1 = lmList[4][1], lmList[4][2]
            # Find Index Finger Tip
            x2, y2 = lmList[8][1], lmList[8][2]

            # Draw Circle on Thumb Position
            cv2.circle(img, (x1, y1), 15, (255, 0, 0), cv2.FILLED)
            # Draw Circle on Index Finger Position
            cv2.circle(img, (x2, y2), 15, (255, 0, 0), cv2.FILLED)
            # Draw a line Thumb and Index Finger
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

            # Calculate the Length (distance between Thumb Tip Position and Index Finger Tip Position)
            # hypotenuse of a right triangle when you know the lengths of the other two sides
            # It calculates the Euclidean norm (L2 norm) of a 2D vector, which is essentially
            # the distance between two points in a Cartesian coordinate system.
            length = hypot(x2 - x1, y2 - y1)
            # Map the distance or length to Volume Range
            vol_level = np.interp(length, [15, 220], [volMin, volMax])

            print("Vol: " + str(vol_level) + ", Length: " + str(length))
            # Set System Volume based on the Calculated Length
            volume.SetMasterVolumeLevel(vol_level, None)

            # Check if hand is in a position for 10 seconds
            if length < 15:
                if not in_position:
                    in_position = True
                    start_time = time.time()
                else:
                    if time.time() - start_time >= 10:
                        final_volume = volume.GetMasterVolumeLevelScalar()
                        print(f'Final Volume: {final_volume}')
            else:
                in_position = False

    # Display the Image with annotations
    cv2.imshow('Image', img)

    # Break the Loop and Exit when 'x' is pressed
    if cv2.waitKey(1) & 0xff == ord('x'):
        break

# Release the WebCam and close OpenCV window
cap.release()
cv2.destroyAllWindows()