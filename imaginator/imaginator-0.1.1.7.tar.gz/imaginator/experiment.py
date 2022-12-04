"""
Experiment Runner

Brooke Hamilton
brookehamilton@gmail.com

This script contains an Experiment class that helps the user iterate on a specific piece of art more effectively.
"""
from PIL import Image
from imaginator.pipeline_utils import create_pipeline, run_pipeline

class Experiment():

    def __init__(self, prompt: str, init_image_path: str, strength: float = 0.75, guidance_scale: float = 7.5,
            negative_prompt: str = None, seed: int = None):
        self.pipeline = None
        self.prompt = prompt
        self.init_image_path = init_image_path
        self.strength = strength
        self.guidance_scale = guidance_scale
        self.negative_prompt = negative_prompt
        self.seed = seed

        # Post-init
        self.init_image = None
        self.downsized_init_image = None

    def change_prompt(self, new_prompt: str):
        """
        Modify the prompt being used to generate images
        """
        self.prompt = new_prompt

    def load_init_image(self):
        """
        Load the starting image
        """
        self.init_image = Image.open(self.init_image_path).convert("RGB")

    def downsize_init_image(self, width: int = 768, height: int = 512):
        """
        Downsize initial image
        """
        self.downsized_init_image = self.init_image.resize((width, height))

    def generate_quick_result(self):
        """
        Starting with the initial image and prompt, generate a quick, small image result
        """
        True

    def generate_image(self):
        """
        Generate an image using the provided starting image and parameters
        """
        if self.pipeline is None:
            create_pipeline()

        run_pipeline(
            init_image_path=self.init_image_path,
            prompt=self.prompt,
            pipe=self.pipe,
            negative_prompt=self.negative_prompt,
            num_inference_steps=15,
            seed=None,
            strength=self.strength,
            guidance_scale=7.5,
            safety_checker=False)
