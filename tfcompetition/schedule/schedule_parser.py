"""Parse a 'Tijdchema' page on atletiek.nu."""


import urllib.request

from bs4 import BeautifulSoup

from .schedule import Schedule
from ..parser.parser import Parser
from ..table.table import Table
from ..utils import string_from_tag, tag_has_class

class ScheduleParser(Parser):
    """Parse a 'Tijdchema' page on atletiek.nu."""

    def __init__(self, schedule_url):
        """Initialise the oject."""
        super().__init__(schedule_url)

    def get_table(self, table_name):
        """Return the first table with given name with a proper header row."""
        if not self.tree:
            raise IndexError(
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
        return Table(found)

    def get_schedule(self):
        """Return the schedule."""
        return Schedule(self.get_table('chronoloogtabel'))
