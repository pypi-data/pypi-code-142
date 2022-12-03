import json

import requests

from socialstats.constant import Constant
from socialstats.medium.medium_user import MediumUser


class MediumBuilder:
    """Medium stat builder class."""

    user = MediumUser()

    def __init__(self, username: str):
        """Construct builder."""
        self.user.username = username

    def _get_profile_data(self):
        """Get profile data from Medium API."""
        url = Constant.medium_endpoint.format(self.user.username)
        try:
            response = requests.get(url)
        except Exception:
            raise ValueError('Could not connect to the stackoverflow API')

        text_response = response.text.replace(Constant.json_hijacking_prefix, '')
        json_response = json.loads(text_response)
        if json_response:
            return json_response.get('payload')

    def build_profile(self):
        """Build user basic profile info."""
        user_data = self._get_profile_data()

        if not user_data:
            raise ValueError('No user data found.')
        self.user.id = user_data.get('user').get('userId')
        self.user.first_name = user_data.get('user').get('name')
        self.user.registration_unix_time = user_data.get('user').get('createdAt')
        self.user.image_id = user_data.get('user').get('imageId')
        self.user.bio = user_data.get('user').get('bio')
        self.user.medium_member_at = user_data.get('user').get('mediumMemberAt')
        self.user.language_code = user_data.get('user').get('languageCode')
        self.user.number_of_posts_published = user_data.get('userMeta').get('numberOfPostsPublished')
        self.user.follower = user_data.get('references').get('SocialStats').get(self.user.id).get('usersFollowedByCount')
        self.user.following = user_data.get('references').get('SocialStats').get(self.user.id).get('usersFollowedCount')

        return self

    def return_user(self):
        """Return an instance of user."""
        return self.user
