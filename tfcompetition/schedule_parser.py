"""Parse a 'Tijdchema' page on atletiek.nu."""


import urllib.request

from bs4 import BeautifulSoup

from .utils import tag_has_class, string_from_tag
from .table.table import Row, HeaderRow


class ScheduleParser(object):
    """Parse a 'Tijdchema' page on atletiek.nu."""

    def __init__(self, schedule_url):
        """Initialise the oject."""
        self.url = schedule_url
        self._tree = None

    @property
    def tree(self):
        """Return the schedule html as a tree."""
        if not self._tree:
            try:
                try:
                    with urllib.request.urlopen(self.url) as fp:
                        html_doc = fp.read().decode("utf8")
                    soup = BeautifulSoup(html_doc, 'html.parser')
                except urllib.error.URLError:
                    raise ValueError('Cannot find competition!')
                self._tree = soup
                # Check if competition exists
                if 'alert alert-error' in html_doc:
                    raise ValueError('Cannot find competition!')
            except ValueError:
                print('Error while getting Schedule Tree!')
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

    def get_table(self, table_name):
        """Return the first table with given name with a proper header row."""
        if not self.tree:
            raise ValueError(
                'Error while finding {} table.'.format(table_name))
        # Find the table
        found = None
        for tbl in self.tree.find_all('table'):
            # Check whether the table has the correct name.
            if not tag_has_class(tbl, table_name):
                continue
            # Check whether the table has a header.
            elif not tbl.thead:
                continue
            # Check whether cells in header row are labeled 'header'.
            th = tbl.thead.find('th')
            if not th:
                continue
            elif tag_has_class(th, 'header'):
                found = tbl
                break
        if not found:
            raise IndexError('Did not find {} table.'.format(table_name))
        # Compose header as 2-dimensional list
        header = []
        for tr in found.thead.find_all('tr'):
            # add header row
            row = HeaderRow(tr)
            # row = []
            # for th in tr.find_all('th'):
            #     row.append(string_from_tag(th))
            header.append(row)
        # Compose details as list of Row objects
        details = []
        for tr in found.tbody.find_all('tr'):
            # Add detail row
            row = Row(tr)
            details.append(row)
        return (header, details)
