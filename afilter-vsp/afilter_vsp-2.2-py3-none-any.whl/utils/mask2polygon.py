from PIL import Image
import numpy as np
from skimage import measure
from datetime import datetime
from shapely.geometry import Polygon
import json


def create_sub_masks(mask_image):
    width, height = mask_image.size

    # Initialize a dictionary of sub-masks indexed by RGB colors
    sub_masks = {}
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel
            pixel = mask_image.getpixel((x, y))[:3]

            # If the pixel is not black...
            if pixel != (0, 0, 0):
                # Check to see if we've created a sub-mask...
                pixel_str = str(pixel)
                sub_mask = sub_masks.get(pixel_str)
                if sub_mask is None:
                   # Create a sub-mask (one bit per pixel) and add to the dictionary
                    # Note: we add 1 pixel of padding in each direction
                    # because the contours module doesn't handle cases
                    # where pixels bleed to the edge of the image
                    sub_masks[pixel_str] = Image.new('1', (width+2, height+2))

                # Set the pixel value to 1 (default is 0), accounting for padding
                sub_masks[pixel_str].putpixel((x+1, y+1), 1)

    return sub_masks

def masks_pad(mask_images):
    for label, mask_image in mask_images.items():
        mask_images[label] = Image.fromarray(np.pad(np.asarray(mask_image), ((1,1),(1,1)))).convert('1')
    return mask_images

def create_sub_mask_ploy(label, sub_mask):
    # Find contours (boundary lines) around each sub-mask
    # Note: there could be multiple contours if the object
    # is partially occluded. (E.g. an elephant behind a tree)
    contours = measure.find_contours(np.array(sub_mask), 0.5, positive_orientation='low')

    shapes = []
    # polygons = []
    for contour in contours:
        shape = {"label": label, "points": [], "group_id": '', "shape_type": "polygon", "flags": {}}
        # Flip from (row, col) representation to (x, y)
        # and subtract the padding pixel
        for i in range(len(contour)):
            row, col = contour[i]
            contour[i] = (col - 1, row - 1)

        # Make a polygon and simplify it
        poly = Polygon(contour)
        poly = poly.simplify(1.0, preserve_topology=False)
        segmentation = np.array(poly.exterior.coords)
        segmentation = np.maximum(segmentation, 0).tolist()
        shape['points'] = segmentation
        shapes.append(shape)

    # Combine the polygons to calculate the bounding box and area
    # multi_poly = MultiPolygon(polygons)
    # if multi_poly.bounds == ():
    #     return "skip"
    # x, y, max_x, max_y = multi_poly.bounds
    # # x = max(0, x)
    # # y = max(0, y)
    # width = max_x - x
    # height = max_y - y
    # bbox = (x, y, width, height)
    # area = multi_poly.area

    return shapes

def get_annotation(mask_images):
    from afilter_vsp.version import __version__
    dataset = {"version": "4.5.6",
               "flags": {'time': str(datetime.now()), 'afilter_vsp': __version__},
               "shapes": [],
               "imagePath": "",
               "imageData": "",
               "imageHeight": '1536',
               "imageWidth": '2048'}

    # Create the annotations
    sub_masks = masks_pad(mask_images)
    for label, sub_mask in sub_masks.items():
        shapes = create_sub_mask_ploy(label, sub_mask)
        if shapes == "skip":
            continue
        dataset["shapes"].extend(shapes)
    jsondict = json.dumps(dataset, sort_keys=True, indent=4, separators=(',', ': '))
    # with open("/data/building1.json", "w") as f:
    #     f.write(jsondict)
    return jsondict
