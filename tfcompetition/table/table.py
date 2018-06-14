"""Objects which implement a table."""


from ..utils import tag_has_class, string_from_tag


class Cell(object):
    """Implement a table cell."""
    def __init__(self, tag):
        """Initialise the object."""
        self._tag = tag

    @property
    def string(self):
        """Return the contents of the cell as a string."""
        return string_from_tag(self._tag)

    @property
    def link(self):
        """Return the href from the cell."""
        a = self._tag.find('a')
        if a:
            return a.get('href', '')
        return ''


class Row(object):
    """Implement a table row."""
    def __init__(self, tag):
        """Initialise the object."""
        self._tag = tag
        self._cells = [Cell(td) for td in tag.find_all('td')]

    @property
    def string(self):
        """Return the contents of the row as a string."""
        return str([cell.string for cell in self._cells])

    @property
    def link(self):
        """Return the href from the row."""
        return self._cells[-1].link


class HeaderRow(Row):
    """Implement a table row."""
    def __init__(self, tag):
        """Initialise the object."""
        self._tag = tag
        self._cells = [Cell(th) for th in tag.find_all('th')]


class Header(object):
    pass


class Details(object):
    pass


class Table(object):
    pass
