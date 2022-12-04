import uuid
from typing import List, Optional

import requests
from pydantic import BaseModel, Field, ValidationError

from koo_api.constants import URL_POSTS, URL_PROFILE


class KooAccountNotFoundException(Exception):
    pass


class KooProfile(BaseModel):
    id: uuid.UUID
    handle: str
    name: str
    koos_count: int = Field(alias="kusCount")
    likes_count: int = Field(alias="likesCount")
    comments_count: int = Field(alias="commentsCount")
    rekoos_count: int = Field(alias="rekoosCount")
    description: str
    created_at: int = Field(alias="createdAt")
    region: str = Field(alias="user_reg_country")
    follower_count: int = Field(alias="followerCount")
    following_count: int = Field(alias="followingCount")


class KooPost(BaseModel):
    """
    Koo post.

    Attributes:
        uuid: Koo post uuid.
        name: Post creater Koo user name.
        creator_id: Koo user uuid.
        content: Koo post text contents.
        created_at: Koo post creation date.
        modified_at: Koo post modified date.
        likes_count: Koo post likes count.
        nrekoos_count: Koo post rekoos count.
    """

    id: str
    name: str
    creator_id: str = Field(alias="creatorId")
    content: str = Field(alias="title")
    created_at: int = Field(alias="createdAt")
    modified_at: Optional[int] = Field(alias="modifiedAt")
    likes_count: int = Field(alias="nlikes")
    rekoos_count: int = Field(alias="nreKoos")


class KooAccount:
    """Representation of a Koo user profile/account."""

    def __init__(self, user_name: str):
        self.session = requests.Session()
        profile_url = URL_PROFILE.format(user_name=user_name)
        response = self._get(profile_url)
        profile_json = response.json()
        try:
            self.profile = KooProfile(**profile_json)
        except ValidationError as e:
            # TODO: Properly check if the user doesn't exist or if it was another error
            # We want to know if they API just changed so we can update our code
            raise KooAccountNotFoundException(f"Could not find Koo account with user name {user_name}") from e

    def _get(self, url: str, **kwargs) -> requests.Response:
        return self.session.get(url, **kwargs)

    def get_posts(self, limit: int = 10, **params) -> List[KooPost]:
        """
        Fetches the posts of the account.

        :param limit int: The maximum number of posts to return. Defaults to 10.
        :param params dict: Additional parameters to pass to the API.
        :rtype List[KooPost]: A list of posts.
        """
        posts_url = URL_POSTS.format(user_uuid=self.profile.id)
        request_params = {
            "limit": limit,
            "offset": 0,
            "showPoll": False,
            "showMultiLangKoo": True,
        }
        request_params.update(params)
        koos_json = requests.get(posts_url, params=request_params).json()
        koos = []
        for koo in koos_json.get("feed", []):
            # TODO properly parse the feed and handle multikoos or whatever they are:
            # if koo["sectionType"] == "single_koo":
            post = koo["items"][0]
            koos.append(KooPost(**post))
        return koos
