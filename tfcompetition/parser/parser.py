"""Parser base class for pages page on atletiek.nu."""


import urllib.request

from bs4 import BeautifulSoup

from ..utils import combined_content_from_tag


class Parser(object):
    """Parse a page on atletiek.nu."""

    def __init__(self, url):
        """Initialise the oject."""
        self.url = url
        self._tree = None

    @property
    def tree(self):
        """Return the html as a tree."""
        if not self._tree:
            try:
                try:
                    with urllib.request.urlopen(self.url) as fp:
                        html_doc = fp.read().decode("utf8")
                    soup = BeautifulSoup(html_doc, 'html.parser')
                except urllib.error.URLError:
                    raise ValueError('Cannot find page!')
                self._tree = soup
                # Check if competition exists
                if 'alert alert-error' in html_doc:
                    raise ValueError('No valid page!')
            except ValueError as e:
                # print('Error while getting HTML Tree: {}'.format(e.args[0]))
                self._tree = None
        return self._tree

    @property
    def title(self):
        """Return the Title of the page."""
        if self.tree:
            return self.tree.title.string
        else:
            return ''

    @property
    def name(self):
        """Return the Name of the page."""
        try:
            primary_content = self.tree.find(id='primarycontent')
            if primary_content.find_all('h1'):
                result = combined_content_from_tag(primary_content.h1)
            elif primary_content.find_all('h2'):
                result = combined_content_from_tag(primary_content.h2)
            elif primary_content.find_all('h3'):
                result = combined_content_from_tag(primary_content.h3)
            elif primary_content.find_all('h4'):
                result = combined_content_from_tag(primary_content.h4)
        except AttributeError:
            result = self.title
        return result
