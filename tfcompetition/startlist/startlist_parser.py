"""Parse a 'Startlijst' page on atletiek.nu."""


from .startlist import Startlist
from ..parser.parser import Parser
from ..table.table import Table
from ..utils import find_table


class StartlistParser(Parser):
    """
    Parse a 'Startlijst' page on atletiek.nu.

    The page shows one main table.
    The main table is one of the tables which have class 'deelnemerstabel'.
    """

    def __init__(self, schedule_url):
        """Initialise the oject."""
        super().__init__(schedule_url)

    def get_table(self):
        """Return the first table with given name with a proper header row."""
        return Table(find_table(self.tree,
                                classname='deelnemerstabel',
                                headerclass=None))

    def get_startlist(self):
        """Return the startlist."""
        return Startlist(self.get_table(), name=self.name,
                         time=self.time, location=self.location)

    @property
    def time(self):
        """Return the Time of the schedule item."""
        try:
            primary_content = self.tree.find(id='primarycontent')
            if primary_content.find_all('i', class_='fa fa-clock-o'):
                i_tag = primary_content.find('i', class_='fa fa-clock-o')
                tag = i_tag.next_sibling
                return tag.string.strip()
        except AttributeError:
            return None

    @property
    def location(self):
        """Return the Location of the schedule item."""
        try:
            primary_content = self.tree.find(id='primarycontent')
            if primary_content.find_all('i', class_='fa fa-map-marker'):
                i_tag = primary_content.find('i', class_='fa fa-map-marker')
                tag = i_tag.next_sibling
                return tag.string.strip()
        except AttributeError:
            return None
