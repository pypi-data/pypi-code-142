
import cv2
import mediapipe as mp

class Face_det:

    def __init__(self,mindetconf = 0.5):
        self.mindetconf = mindetconf
        self.mpfacedet = mp.solutions.face_detection
        self.mpdraw = mp.solutions.drawing_utils
        self.facedetect = self.mpfacedet.FaceDetection(self.mindetconf)

    def findfaces(self,img , draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.facedetect.process(imgRGB)
        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                cx, cy = bbox[0] + (bbox[2] // 2), \
                         bbox[1] + (bbox[3] // 2)
                bboxInfo = {"id": id, "bbox": bbox, "score": detection.score, "center": (cx, cy)}
                bboxs.append(bboxInfo)
                if draw:
                    img = cv2.rectangle(img, bbox, (0, 255, 0), 2)

                    cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                                (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                                2, (0, 0, 255), 2)
        return img, bboxs
    
def main():
    cap = cv2.VideoCapture(0)
    detector = Face_det()
    while True:
        success, img = cap.read()
        img, bboxs = detector.findfaces(img)

        if bboxs:
            # bboxInfo - "id","bbox","score","center"
            center = bboxs[0]["center"]
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
