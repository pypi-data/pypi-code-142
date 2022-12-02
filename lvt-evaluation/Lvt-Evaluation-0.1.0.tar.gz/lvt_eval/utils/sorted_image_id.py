
def sorted_image_id(data):
    """
    Sort the forecast results from small to large
    """
    results = sorted(data, key=lambda r: r["image_id"])
    return results