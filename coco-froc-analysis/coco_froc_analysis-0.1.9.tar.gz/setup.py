# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coco_froc_analysis', 'coco_froc_analysis.count', 'coco_froc_analysis.froc']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.2,<4.0.0',
 'numpy>=1.23.5,<2.0.0',
 'scipy>=1.9.3,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'coco-froc-analysis',
    'version': '0.1.9',
    'description': 'FROC analysis for COCO detections for Detectron(2) and OpenMMLab',
    'long_description': '# COCO FROC analysis\n\nFROC analysis for COCO annotations and Detectron(2) detection results. The COCO annotation style is defined [here](https://cocodataset.org/).\n\n### Installation\n\n```bash\npip install coco-froc-analysis\n```\n\n### About\n\nA single annotation record in the ground-truth file might look like this:\n\n```json\n{\n  "area": 2120,\n  "iscrowd": 0,\n  "bbox": [111, 24, 53, 40],\n  "category_id": 3,\n  "ignore": 0,\n  "segmentation": [],\n  "image_id": 407,\n  "id": 945\n}\n```\n\nWhile the prediction (here for bounding box) given by the region detection framework is such:\n\n```json\n{\n  "image_id": 407,\n  "category_id": 3,\n  "score": 0.9990422129631042,\n  "bbox": [\n    110.72555541992188,\n    13.9161834716797,\n    49.4566650390625,\n    36.65155029296875\n  ]\n}\n```\n\nThe FROC analysis counts the number of images, number of lesions in the ground truth file for all categories and then counts the lesion localization predictions and the non-lesion localization predictions. A lesion is localized by default if its center is inside any ground truth box and the categories match or if you wish to use IoU you should provide threshold upon which you can define the \'close enough\' relation.\n\n## Usage\n\n```python\nfrom froc_analysis import generate_froc_curve, generate_bootstrap_curves\n\n# For single FROC curve\ngenerate_froc_curve(gt_ann=\'<path-to-your-ground-thruth-annotation-file>\',\n                    pr_ann=\'<path-to-Detectron2-or-mmdetection-prediction-file>\',\n                    use_iou=False, iou_thres=.5, n_sample_points=75,\n                    plot_title=\'FROC\', plot_output_path=\'froc.png\')\n\n# For bootstrapped curves\ngenerate_bootstrap_curves(gt_ann=\'<path-to-your-ground-thruth-annotation-file>\',\n                          pr_ann=\'<path-to-Detectron2-or-mmdetection-prediction-file>\',\n                          n_bootstrap_samples=5,\n                          use_iou=False, iou_thres=.5, n_sample_points=25,\n                          plot_title=\'FROC\', plot_output_path=\'froc.png\')\n```\n\n## CLI Usage\n\n```bash\npython -m coco_froc_analysis [-h] [--bootstrap N_BOOTSTRAP_ROUNDS] --gt_ann GT_ANN --pred_ann PRED_ANN [--use_iou] [--iou_thres IOU_THRES] [--n_sample_points N_SAMPLE_POINTS]\n                        [--plot_title PLOT_TITLE] [--plot_output_path PLOT_OUTPUT_PATH]\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --bootstrap  N_ROUNDS Whether to do a single or bootstrap runs.\n  --gt_ann GT_ANN\n  --pred_ann PRED_ANN\n  --use_iou             Use IoU score to decide on `proximity` rather then using center pixel inside GT box.\n  --iou_thres IOU_THRES\n                        If IoU score is used the default threshold is arbitrarily set to .5\n  --n_sample_points N_SAMPLE_POINTS\n                        Number of points to evaluate the FROC curve at.\n  --plot_title PLOT_TITLE\n  --plot_output_path PLOT_OUTPUT_PATH\n```\n\nBy default centroid closeness is used, if the `--use_iou` flag is set, `--iou_thres` defaults to `.75` while the `--score_thres` score defaults to `.5`. The code outputs the FROC curve on the given detection results and GT dataset.\n\n## For developers\n\n### Running tests\n\n```bash\npython -m coverage run -m unittest discover --pattern "*_test.py" -v\npython -m coverage report -m\n```\n\n### Building and publishing (reminder)\n\n```bash\nace # for local CI pipeline\npdoc -d google coco_froc_analysis -o docs # build docs\npoetry publish --build -r testpypi # or without -r testpypi for publishing to pypi\n```\n\n@Regards, Alex\n',
    'author': 'Alex Olar',
    'author_email': 'olaralex666@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
