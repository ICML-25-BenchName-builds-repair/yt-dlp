from .common import InfoExtractor


class ElevenSportsIE(InfoExtractor):
    """
    Placeholder for ElevenSportsIE extractor
    """
    _VALID_URL = r'https?://(?:www\.)?elevensports\.(?:com|it)'
    IE_NAME = 'elevensports'

    def _real_extract(self, url):
        self.raise_no_formats('This extractor is not fully implemented yet', expected=True)
