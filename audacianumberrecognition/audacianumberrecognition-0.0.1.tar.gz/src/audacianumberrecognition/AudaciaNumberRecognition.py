from paddleocr import PaddleOCR,draw_ocr
from PIL import Image

class AudaciaNumberRecognition:
    use_angle_cls=True
    lang=''
    det_model_dir=''
    rec_model_dir=''

    paddleObject = None

    def __init__(self, use_angle_cls=True, lang='en',det_model_dir='./models/det',rec_model_dir='./models/rec'):
        self.use_angle_cls = use_angle_cls
        self.lang = lang
        self.det_model_dir = det_model_dir
        self.rec_model_dir = rec_model_dir

        self.paddleObject = PaddleOCR(use_angle_cls=self.use_angle_cls, lang=self.lang,det_model_dir=self.det_model_dir,rec_model_dir=self.rec_model_dir) # need to run only once to download and load model into memory

    def ocrDetect(self, img_path, output_path):
        result = self.paddleObject.ocr(img_path, det=True, cls=False,rec=True)
        self._drawResult(img_path, result=result, output_path=output_path)
    
    def _drawResult(self, img_path, result, output_path = 'result.jpg'):
        image = Image.open(img_path).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/Lato/Lato-Black.ttf')
        im_show = Image.fromarray(im_show)
        im_show.save(output_path)