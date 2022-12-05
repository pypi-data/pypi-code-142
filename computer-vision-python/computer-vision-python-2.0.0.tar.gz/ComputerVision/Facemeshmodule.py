import cv2
import mediapipe as mp
import math

class Face_mesh_det:
    def __init__(self,staticmode=False, maxfaces=2,mindetconf= 0.5,mintrackconf= 0.5):
        self.staticmode = staticmode
        self.maxfaces = maxfaces
        self.mindetconf = mindetconf
        self.mintrackconf = mintrackconf

        self.mpdraw =  mp.solutions.drawing_utils
        self.mpfacemesh = mp.solutions.face_mesh
        self.facemesh = self.mpfacemesh.FaceMesh(static_image_mode = self.staticmode,
                                                 max_num_faces = self.maxfaces,
                                                 min_detection_confidence = self.mindetconf,
                                                 min_tracking_confidence = self.mintrackconf)
        self.drawspec = self.mpdraw.DrawingSpec(thickness = 1, circle_radius = 1)
    
    def find_face_mesh(self, img, draw=True):
       
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.facemesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img, faceLms, self.mpfacemesh.FACEMESH_CONTOURS,
                                               self.drawspec, self.drawspec)
                face = []
                for id, lm in enumerate(faceLms.landmark):
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])
                faces.append(face)
        return img, faces
    def find_distance(self,p1, p2, img=None):
        

        x1, y1 = p1
        x2, y2 = p2
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        length = math.hypot(x2 - x1, y2 - y1)
        info = (x1, y1, x2, y2, cx, cy)
        if img is not None:
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            return length,info, img
        else:
            return length, info
        
def main():
    cap = cv2.VideoCapture(0)
    detector = Face_mesh_det(maxfaces=2)
    while True:
        success, img = cap.read()
        img, faces = detector.find_face_mesh(img)
        if faces:
            print(faces[0])
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
    