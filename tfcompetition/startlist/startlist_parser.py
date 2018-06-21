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
        return Startlist(self.get_table())
