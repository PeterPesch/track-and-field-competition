"""Objects which implement a table."""


from ..utils import combined_string_from_tag, first_string_from_tag


class Cell(object):
    """Implement a table cell."""
    def __init__(self, tag):
        """Initialise the object."""
        self._tag = tag

    @property
    def string(self):
        """Return the contents of the cell as a string."""
        return first_string_from_tag(self._tag)

    @property
    def combined_string(self):
        """Return the contents of the cell as a string."""
        return combined_string_from_tag(self._tag)

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
        if len(self._cells) > 0:
            return self._cells[-1].link
        return ''

    @property
    def cells(self):
        """Return the cells of the row."""
        return self._cells

    def print(self):
        """Print the object."""
        print(self.string, self.link)


class HeaderRow(Row):
    """Implement a table row."""
    def __init__(self, tag):
        """Initialise the object."""
        self._tag = tag
        self._cells = [Cell(th) for th in tag.find_all('th')]


class Header(object):
    """Implement a table header."""
    def __init__(self, tag):
        """Initialise the object."""
        self._tag = tag
        self._rows = [HeaderRow(tr) for tr in tag.find_all('tr')]

    @property
    def rows(self):
        """Return the rows of the header."""
        return self._rows

    def print(self):
        """Print the object."""
        for row in self.rows:
            row.print()


class Body(object):
    """Implement Table body."""
    def __init__(self, tag):
        """Initialise the object."""
        self._tag = tag
        self._rows = [Row(tr) for tr in tag.find_all('tr')]

    @property
    def rows(self):
        """Return the rows of the table body."""
        return self._rows

    def print(self):
        """Print the object."""
        for row in self.rows:
            row.print()


class Table(object):
    """Implement Table body."""
    def __init__(self, tag):
        """Initialise the object."""
        self._tag = tag
        self._header = Header(tag.thead)
        self._body = Body(tag.tbody)

    @property
    def header(self):
        """Return the header of the table."""
        return self._header

    @property
    def body(self):
        """Return the body of the table."""
        return self._body

    def print(self):
        """Print the object."""
        self.header.print()
        self.body.print()
