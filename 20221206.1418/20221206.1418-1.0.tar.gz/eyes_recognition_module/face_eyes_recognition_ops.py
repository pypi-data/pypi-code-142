import face_recognition
import pickle
import cv2
import numpy as np
from imutils import paths
import os


def encode_faces(imagePathsStr, database="database.pickle", detection_method="cnn"):
    print("[INFO] quantifying faces...")
    imagePaths = list(paths.list_images(imagePathsStr))
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


def recognize_faces_image(frame, encodings="database.pickle", detection_method="cnn", toleranceval=0.40):
    print("[INFO] loading encodings...")
    data = pickle.loads(open(encodings, "rb").read())
    w = frame.shape[1]
    h = frame.shape[0]
    print("picture sizes{},{}".format(w, h))
    if w > 2000:
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    else:
        small_frame = frame
    rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    face_landmarks_list = face_recognition.face_landmarks(rgb)
    print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    print("[INFO] recognizing faces...")
    boxes = face_recognition.face_locations(rgb, model=detection_method)
    encodings = face_recognition.face_encodings(rgb, boxes)
    # initialize the list of names for each face detected
    names = []
    # loop over the facial embeddings
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(data["encodings"],
                                                 encoding, tolerance=toleranceval)
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
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            # determine the recognized face with the largest number of
            # votes (note: in the event of an unlikely tie Python will
            # select first entry in the dictionary)
            name = max(counts, key=counts.get)

        # update the list of names
        names.append(name)
    right_eye_list = []
    left_eye_list = []
    face_box_list = []
    name_list = []
    face_num = 0
    for ((top, right, bottom, left), name) in zip(boxes, names):
        # draw the predicted face name on the small_frame
        if name != "Unknown":
            face_contour = np.array([np.array([left, top]), np.array([right, top]), np.array([right, bottom]), np.array([left, bottom])])
            face_num = face_num + 1
            face_box_list.append([top, right, bottom, left])
            name_list.append(name)
            for face_landmarks in face_landmarks_list:
                centor_point = face_landmarks['nose_bridge'][0]
                exist = cv2.pointPolygonTest(face_contour, centor_point, True)
                if exist > 0:
                    right_eye_list.append(face_landmarks['right_eye'])
                    left_eye_list.append(face_landmarks['left_eye'])
                    break
    return face_num, name_list, face_box_list, right_eye_list, left_eye_list


def recognition_face_show(frame, name_list, face_box_list, right_eye_list, left_eye_list):
    w = frame.shape[1]
    h = frame.shape[0]
    print("picture sizes {},{}".format(w, h))
    if w > 2000:
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    else:
        small_frame = frame
    for box, name, right_eye, left_eye in zip(face_box_list, name_list, right_eye_list, left_eye_list):
        top = box[0]
        right = box[1]
        bottom = box[2]
        left = box[3]
        cv2.rectangle(small_frame, (left, top), (right, bottom), (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(small_frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 1)
        num = len(right_eye)
        index = 0
        while index < num - 1:
            cv2.line(small_frame, right_eye[index], right_eye[index + 1], (0, 0, 255), 2)
            cv2.line(small_frame, left_eye[index], left_eye[index + 1], (0, 0, 255), 2)
            index = index + 1
    cv2.imshow("Image", small_frame)
    cv2.waitKey(0)
