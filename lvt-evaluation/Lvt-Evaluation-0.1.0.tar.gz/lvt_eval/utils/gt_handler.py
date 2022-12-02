from lvt_eval.tools.customcoco import CustomCOCO as _COCO


def get_classes_and_imgs(gt_json):
    '''
    从gt里获取类别的name组成names字典, classes列表
    '''
    names = {}
    # get categories
    coco_api = _COCO(gt_json)
    cat_ids = sorted(coco_api.getCatIds())
    cats = coco_api.loadCats(cat_ids)
    classes = [c["name"] for c in sorted(cats, key=lambda x: x["id"])]
    img_ids = coco_api.getImgIds()

    for c in cats:
        names[c["id"]] = c["name"]

    return names, classes, img_ids


def read_gt_img(gt_data):
    anno = _COCO(gt_data)
    img_ids = anno.getImgIds()
    img_len = len(img_ids)

    return img_len