from .common import InfoExtractor


class EllenTubeIE(InfoExtractor):
    """
    Placeholder for EllenTubeIE extractor
    """
    _VALID_URL = r'https?://(?:www\.)?ellentube\.com/video/'
    IE_NAME = 'ellentube'

    def _real_extract(self, url):
        self.raise_no_formats('This extractor is not fully implemented yet', expected=True)


class EllenTubeVideoIE(InfoExtractor):
    """
    Placeholder for EllenTubeVideoIE extractor
    """
    _VALID_URL = r'https?://(?:www\.)?ellentube\.com/video/'
    IE_NAME = 'ellentube:video'

    def _real_extract(self, url):
        self.raise_no_formats('This extractor is not fully implemented yet', expected=True)


class EllenTubePlaylistIE(InfoExtractor):
    """
    Placeholder for EllenTubePlaylistIE extractor
    """
    _VALID_URL = r'https?://(?:www\.)?ellentube\.com/playlist/'
    IE_NAME = 'ellentube:playlist'

    def _real_extract(self, url):
        self.raise_no_formats('This extractor is not fully implemented yet', expected=True)
