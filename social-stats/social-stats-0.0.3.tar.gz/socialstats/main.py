from socialstats.factories.user_factory import UserFactory


def get_stat(platform: str, username: str, token: str = '') -> dict:
    """Return user information in dictionary format."""
    user = UserFactory.create_user(platform=platform, username=username, token=token)
    return dict(user)
