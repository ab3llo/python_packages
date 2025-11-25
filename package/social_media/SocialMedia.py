from package.Document import Document

class SocialMedia(Document):
    """Social Media base class"""

    def __init__(self, platform: str, username: str):
        self.platform = platform
        self.username = username