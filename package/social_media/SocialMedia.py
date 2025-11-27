from package.document.Document import Document

class SocialMedia(Document):
    """Social Media base class"""

    def __init__(self, platform: str, username: str, text: str = ""):
        self.platform = platform
        self.username = username
        # Initialize Document with optional text (defaults to empty)
        super().__init__(text)