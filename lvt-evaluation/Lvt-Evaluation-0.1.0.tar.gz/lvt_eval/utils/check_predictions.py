from lvt_eval.utils.general import save_json
import logging

logging.basicConfig(format='%(asctime)s [%(pathname)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


def check_predictions(pred_all_boxes):
    '''
    获取所有预测结果的image_id
    '''
    pred_img_ids = set([i["image_id"] for i in pred_all_boxes])

    return pred_img_ids


def check_json(pred_data, anno_data, threshold):
    '''
    pred_data-----List, anno_data---------Dict[list], threshold-------float
    :return 
    match_pred_sorted----与gt能匹配上的预测List, unmatch_pred_sorted-----未与gt能匹配上的预测List, 
    '''
    matched_pred_boxes = []
    matched_pred_boxes_img = []
    unmatch_pred_boxes = []
    unmatch_pred_imgs = []
    pred_len = len(pred_data)

    if anno_data["annotations"] and pred_data:  # 　预测框和gt框都有的情况
        # 取gt-json里的annotations的image_id
        anns_img_id_set = set(
            [i["image_id"] for i in anno_data["annotations"]])
        # 取gt-json里的images的id值
        all_imgs_set = set([i["id"] for i in anno_data["images"]])
        for i in range(pred_len):
            if pred_data[i]["image_id"] in anns_img_id_set and pred_data[i][
                    "score"] > threshold:
                matched_pred_boxes.append(pred_data[i])
                matched_pred_boxes_img.append(pred_data[i]["image_id"])
            elif pred_data[i]["image_id"] not in anns_img_id_set and pred_data[
                    i]["score"] > threshold:
                unmatch_pred_boxes.append(pred_data[i])
                unmatch_pred_imgs.append(pred_data[i]["image_id"])
        # 保存与gt匹配上的预测结果
        prediction_file = "./prediction_dirs/prediction_results_{}.json".format(
            threshold)
        # 保存未与gt匹配上的预测结果
        unmatch_file = "./prediction_dirs/unmatch_predictions.json"
        match_pred_sorted = sorted(matched_pred_boxes,
                                   key=lambda x: x.get('image_id'))
        unmatch_pred_sorted = sorted(unmatch_pred_boxes,
                                     key=lambda x: x.get('image_id'))
        matched_pred_boxes_img.sort()
        unmatch_pred_imgs.sort()
        save_json(match_pred_sorted, prediction_file)
        save_json(unmatch_pred_sorted, unmatch_file)

        return match_pred_sorted, unmatch_pred_sorted, set(
            unmatch_pred_imgs), set(matched_pred_boxes_img), all_imgs_set
