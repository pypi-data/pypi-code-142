import augmentation as am
import flip as

# image augmentation 은 type별로 다양한 설정이 필요함
# 다양한 설정들과 사용할 augment type을 하나의 구조체로 입력을 받으면
class AugmentMgmt():
    def get_augment(self, augment_config):
        
        for augconf in augment_config:
            if flip = augconf.type:
                self.augment = flipAugmentation()
            if augconf.type = flip:
            
        if true == flipAugmentation:
            
  
        if () self.augment = ATypeAugmentation(self.augment)
        if () self.augment = BTypeAugmentation(self.augment)
        if () self.augment = CTypeAugmentation(self.augment)

        return self.augment
    
    
    def visualize(original, augmented):
        fig = plt.figure()
        plt.subplot(1,2,1)
        plt.title('Original image')
        plt.imshow(original)

        plt.subplot(1,2,2)
        plt.title('Augmented image')
        plt.imshow(augmented)

        
        
        
        
        
        
        
        
        
        
# tf.image.adjust_brightness	
# tf.image.adjust_contrast	
# tf.image.adjust_gamma	
# tf.image.adjust_hue	
# tf.image.adjust_saturation	
# tf.image.central_crop	Crop factor must be a compile-time constant.
# tf.image.convert_image_dtype	
# tf.image.flip_left_right	
# tf.image.flip_up_down	
# tf.image.grayscale_to_rgb	
# tf.image.hsv_to_rgb	
# tf.image.resize_bilinear	Only align_corners=True is available. size must be a compile-time constant.
# tf.image.random_brightness	
# tf.image.random_contrast	
# tf.image.random_flip_left_right	
# tf.image.random_flip_up_down	
# tf.image.random_hue	
# tf.image.random_saturation	
# tf.image.rgb_to_hsv	
# tf.image.rgb_to_grayscale	
# tf.image.rot90	
# tf.image.total_variation	
# tf.image.transpose_image