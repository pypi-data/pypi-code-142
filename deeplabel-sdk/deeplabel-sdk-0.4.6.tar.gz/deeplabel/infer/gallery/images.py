from typing import Any, Dict, List, Optional
from pydantic import Field
import deeplabel.client
import deeplabel
from deeplabel.exceptions import InvalidIdError
import deeplabel.infer.gallery.gallery_tasks
from deeplabel.basemodel import DeeplabelBase, MixinConfig


class ImageResolution(MixinConfig):
    height: Optional[int]
    width: Optional[int]
class Image(DeeplabelBase):
    gallery_id: str
    project_id:str
    image_id:str
    image_url:str
    name:str
    parent_folder_id:Optional[str]
    resolution:ImageResolution = Field(default_factory=ImageResolution) #type: ignore

    @classmethod
    def from_search_params(cls, params:Dict[str, Any], client: "deeplabel.client.BaseClient") -> List["Image"]:
        resp = client.get("/images", params=params)
        images = resp.json()["data"]["images"]
        images = [cls(**image, client=client) for image in images]
        return images #type: ignore
    
    @classmethod
    def from_image_id(cls, image_id:str, client: "deeplabel.client.BaseClient")->"Image":
        image = cls.from_search_params({"imageId":image_id}, client=client)
        if not len(image):
            raise InvalidIdError(f"Failed to fetch video with videoId: {image_id}")
        return image[0]

    @classmethod
    def from_gallery_and_project_id(cls, gallery_id:str, project_id:str, client: "deeplabel.client.BaseClient")->List["Image"]:
        return cls.from_search_params({"galleryId":gallery_id,'projectId':project_id, "limit":"-1"}, client=client)
