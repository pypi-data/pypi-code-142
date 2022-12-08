import face_recognition
import pickle
import cv2
import imutils
import os

known_faces_encodings = {}


def encode_faces(imagePathsStr, database="database.pickle", detection_method="cnn"):
    print("[INFO] quantifying faces...")
    imagePaths = list(imutils.paths.list_images(imagePathsStr))
    knownEncodings = []
    knownNames = []
    for (i, imagePath) in enumerate(imagePaths):
        # extract the person name from the image path
        print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
        name = imagePath.split(os.path.sep)[-2]
        # load the input image and convert it from BGR (OpenCV ordering)
        # to dlib ordering (RGB)
        image = cv2.imread(imagePath)
        w = image.shape[1]
        h = image.shape[0]
        print("picture sizes {},{}".format(w, h))
        # 图片太大会很耗时
        if w > 2000:
            image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input image
        boxes = face_recognition.face_locations(rgb, model=detection_method)
        # compute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb, boxes)
        # loop over the encodings
        for encoding in encodings:
            # add each encoding + name to our set of known names and
            # encodings
            knownEncodings.append(encoding)
            knownNames.append(name)
    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open(database, "wb")
    f.write(pickle.dumps(data))


def load_encode(encodings="database.pickle"):
    global known_faces_encodings
    known_faces_encodings = pickle.loads(open(encodings, "rb").read())


def recognize_faces_image(frame, detection_method="cnn", toleranceval=0.40, display=1):

    global known_faces_encodings
    w = frame.shape[1]
    h = frame.shape[0]
    #print("picture sizes{},{}".format(w, h))
    if w > 720:
        small_frame = imutils.resize(frame, width=720)
        r = frame.shape[1] / float(small_frame.shape[1])
    else:
        small_frame = frame
        r = 1
    rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    #print("[INFO] recognizing faces...")
    boxes = face_recognition.face_locations(rgb, model=detection_method)
    encodings = face_recognition.face_encodings(rgb, boxes)
    # initialize the list of names for each face detected
    names = []
    # loop over the facial embedding
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(known_faces_encodings["encodings"], encoding, tolerance=toleranceval)
        name = "Unknown"
        # check to see if we have found a match
        if True in matches:
            # find the indexes of all matched faces then initialize a
            # dictionary to count the total number of times each face
            # was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                name = known_faces_encodings["names"][i]
                counts[name] = counts.get(name, 0) + 1
            # determine the recognized face with the largest number of
            # votes (note: in the event of an unlikely tie Python will
            # select first entry in the dictionary)
            name = max(counts, key=counts.get)
        # update the list of names
        names.append(name)
        # loop over the recognized faces
    face_num = 0
    name_list = []
    eyes_point_list = []

    for ((top, right, bottom, left), name) in zip(boxes, names):
        # rescale the face coordinates
        if name != "Unknown":
            face_num = face_num + 1
            name_list.append(name)
            top = int(top * r)
            right = int(right * r)
            bottom = int(bottom * r)
            left = int(left * r)
            crop_img = frame[top:bottom, left:right]
            face_landmarks_list = face_recognition.face_landmarks(crop_img)
            # draw the predicted face name on the image
            cv2.rectangle(frame, (left, top), (right, bottom),
                          (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.65, (0, 255, 0), 1)

            for face_landmarks in face_landmarks_list:
                left_eye_real_x = face_landmarks['left_eye'][0][0] + left
                left_eye_real_y = face_landmarks['left_eye'][0][1] + top
                right_eye_real_x = face_landmarks['right_eye'][3][0] + left
                right_eye_real_y = face_landmarks['right_eye'][3][1] + top
                eyes_point_list.append([(left_eye_real_x,left_eye_real_y),(right_eye_real_x,right_eye_real_y)])
                if display > 0:
                    cv2.line(frame, (left_eye_real_x,left_eye_real_y),(right_eye_real_x,right_eye_real_y),(0, 0, 255), 2)
    if display > 0:
        cv2.imshow("Frame", frame)

    return face_num, name_list, eyes_point_list

