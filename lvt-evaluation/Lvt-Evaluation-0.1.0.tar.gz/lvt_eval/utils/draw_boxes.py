from tqdm import tqdm
import os
import cv2
import json
import numpy as np
import logging
from PIL import Image, ImageDraw, ImageFont
from lvt_eval.utils import *

logging.root.setLevel("INFO")
logging.debug("Запись.")


def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "lvt_eval/utils/fonts/SimSun.ttf", textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


def draw_groundtruth(gt_info, root_dir, output_dir, mapping):
    for i in tqdm(gt_info['annotations']):
        im_path = os.path.join(root_dir, "download_images",
                               mapping[str(i['image_id'])])
        gt_output_img = os.path.join(root_dir, output_dir,
                                     mapping[str(i['image_id'])])

        if not os.path.exists(gt_output_img):

            gt_out = cv2.imread(im_path)
            if gt_out is None:
                continue

        else:
            gt_out = cv2.imread(gt_output_img)

            if gt_out is None:
                continue
            # r, g, b = cv2.split(gt_out)
            # gt_out = cv2.merge([r, g, b])

        x, y, w, h = i["bbox"]
        x, y, w, h = int(x), int(y), int(w), int(h)
        x2, y2 = x + w, y + h
        cv2.rectangle(gt_out, (x, y), (x2, y2), (0, 0, 255),
                      thickness=2)  # red
        cv2.imencode('.jpg', gt_out)[1].tofile(gt_output_img)

    logging.info("Groundtruth done.")


def draw_predictions(pred_info, root_dir, output_dir, mapping, threshold, names):
    for p in tqdm(pred_info):
        img_path = os.path.join(root_dir, "download_images",
                                mapping[str(p['image_id'])])
        pred_output_img = os.path.join(root_dir, output_dir,
                                       mapping[str(p['image_id'])])

        score = p["score"]
        category = names[p['category_id']]

        if float(score) >= threshold:
            if not os.path.exists(pred_output_img):
                pred_out = cv2.imread(img_path)
                if pred_out is None:
                    continue

            else:
                pred_out = cv2.imread(pred_output_img)
                if pred_out is None:
                    continue

            x, y, w, h = p["bbox"]
            x, y, w, h = int(x), int(y), int(w), int(h)
            x2, y2 = x + w, y + h

            cv2.rectangle(pred_out, (x, y), (x2, y2), (0, 255, 0),
                          thickness=2)  # green
           
            pred_out = cv2AddChineseText(pred_out, "{}:{:.2f}".format(category, score), (x, y - 20),
                                         (124, 252, 0), 20)
            cv2.imencode('.jpg', pred_out)[1].tofile(pred_output_img)

    logging.info("Prediction done.")


def draw_box(gt_data, pred_data, filename, threshold, names, draw=True):
    if draw == True:
        gt_info = gt_data
        map_file = 'mapping_dirs/studio_image_id_mapping.json'
        if not os.path.exists(map_file):
            image_id_mapping = {}
            for i in gt_data['images']:
                image_id_mapping[i["id"]] = i['file_name']
            save_json(image_id_mapping, map_file)
        mapping = json.load(open(map_file))
        output_dir = os.path.join("draw_images_output", filename,
                                  str([threshold]))
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        # draw groundtruth
        root_dir = os.getcwd()
        draw_groundtruth(gt_info, root_dir, output_dir, mapping)

        # draw predictions
        pred_info = pred_data
        draw_predictions(pred_info, root_dir, output_dir,
                         mapping, threshold, names)


if __name__ == "__main__":
    gt_data = json.load(open(""))
    pred_data = json.load(open(""))
    clas = ['']
    threshold = [0.5]
    draw_box(gt_data, pred_data, clas[0], threshold[0])
