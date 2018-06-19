"""Parse a 'Tijdchema' page on atletiek.nu."""


from .schedule import Schedule
from ..parser.parser import Parser
from ..table.table import Table
from ..utils import find_table


class ScheduleParser(Parser):
    """
    Parse a 'Tijdschema' page on atletiek.nu.

    The page shows one main table.
    The main table is one of the tables which have class 'chronoloogtabel',
    and can be identified because its header cells have class 'header'.
    """

    def __init__(self, schedule_url):
        """Initialise the oject."""
        super().__init__(schedule_url)

    def get_table(self):
        """Return the first table with given name with a proper header row."""
        return Table(find_table(self.tree,
                                classname='chronoloogtabel',
                                headerclass='header'))

    def get_schedule(self):
        """Return the schedule."""
        return Schedule(self.get_table())
