import augmentation as am

class Flip(am.Augmentatation):
    def __init__(self, augment):
        self.augment = augment
        
    def execute():
        self.augment.execute()
        
        
        
    def _augmentation(self, image, segmentation_mask, augmente_type):
        image_aug = tf.image.flip_left_right(image)
        segmentation_mask_aug = tf.image.flip_left_right(segmentation_mask)
        return image_aug, segmentation_mask_aug