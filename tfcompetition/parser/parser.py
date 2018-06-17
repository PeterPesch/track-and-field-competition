"""Parser base class for pages page on atletiek.nu."""


import urllib.request

from bs4 import BeautifulSoup


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
            except ValueError:
                print('Error while getting HTML Tree!')
                self._tree = None
        return self._tree

    @property
    def name(self):
        """Return the Name of the page."""
        result = ''
        try:
            primary_content = self.tree.find(id='primarycontent')
            for c in primary_content.h4.contents:
                result += c.string
        except AttributeError:
            print('Error while getting page name')
            result = None
        return result

    @property
    def title(self):
        """Return the Title of the page."""
        if self.tree:
            return self.tree.title.string
        else:
            return ''
