"""Objects which implement a track&field time schedule."""


class Schedule(object):
    """Implement a Time Schedule."""
    def __init__(self, table):
        """Initialise the object."""
        self._table = table
        self._colnames = []
        if table and table.header \
                 and len(table.header.rows) \
                 and len(table.header.rows[0].cells) > 0:
            #self._colnames = [cel.string for cel in table.header.rows[0]]
            header_row = table.header.rows[0].cells
            for i in range(len(header_row)):
                if header_row[i].string:
                    celname = header_row[i].string
                else:
                    celname = 'column_{}'.format(i)
                self._colnames.append(celname)
