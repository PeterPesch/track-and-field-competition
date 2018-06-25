"""Objects which implement a track&field time schedule."""


from ..startlist.startlist_parser import StartlistParser


class Item(object):
    """Implement Items on a Time Schedule."""
    def __init__(self, time, event, category, startgroup, type, link):
        """Initialise the object."""
        self.time = time
        self._event = event
        self.category = category
        self.startgroup = startgroup
        self._type = type
        self._link = link
        self._startlist = None
        self._reason_no_startlist = ''

    @property
    def event(self):
        """Return the event of the schedule item."""
        return self._event

    def __str__(self):
        """Return a string representation of the schedule item."""
        return '{}: {} - {} / {}'.format(
            self.time, self.event, self.category, self.startgroup)

    def print(self, size=False):
        """Print the schedule item."""
        if not size:
            print(str(self))
        elif self.startlist:
            print('{} ({})'.format(str(self), self.startlist.size))
        else:
            print('{} ({})'.format(str(self), self._reason_no_startlist))

    @property
    def startlist(self):
        """Return a startlist for this schedule item, insofar possible."""
        if not self._startlist:
            if 'startlijst' not in self._link:
                self._reason_no_startlist = 'No startlist available'
                return self._startlist
            parser = StartlistParser(self._link)
            try:
                self._startlist = parser.get_startlist()
            except IndexError as e:
                self._reason_no_startlist = str(e.args[0])
        return self._startlist


class Schedule(object):
    """Implement a Time Schedule."""
    def __init__(self, table):
        """Initialise the object."""
        self._table = table
        self._colnames = []
        # raw header
        if (table and table.header and
                len(table.header.rows) and
                len(table.header.rows[0].cells) > 3):
            header_row = table.header.rows[0].cells
            for i in range(len(header_row)):
                if header_row[i].string:
                    celname = header_row[i].string.strip()
                else:
                    celname = 'column_{}'.format(i)
                self._colnames.append(celname)
        else:
            raise ValueError('No valid Time Schedule!')
        # raw detail rows
        self._rows = []
        if table.body:
            for row in table.body.rows:
                if len(row.cells) < 4:
                    raise ValueError('No valid Time Schedule!')
                self._rows.append(
                    [(cel.string.strip(), cel.link,
                      cel.combined_string.strip())
                        for cel in row.cells])
        # Examine column 3: Results or Startlist.
        self._col3 = [row[3][0] for row in self._rows]
        for cel in self._col3:
            if 'Startlijst' in cel:
                self._colnames[3] = 'Startlijst'
                break
            elif 'Uitslagen' in cel:
                self._colnames[3] = 'Uitslagen'
                break
        # Examine column 2: Startgroup may contain categories.
        self._col1 = [row[1][0] for row in self._rows]
        startgroups = sorted(list(set(self._col1)))  # sorted distinct list
        cur_cat = 'zzzzz'
        startgroupdict = {}
        for sg in startgroups:
            if cur_cat not in sg:
                cur_cat = sg
            startgroupdict[sg] = cur_cat
        self.items = []
        for row in self._rows:
            self.items.append(Item(
                time=row[0][0],
                event=row[2][2],
                category=startgroupdict[row[1][0]],
                startgroup=row[1][0],
                type=self._colnames[3],
                link=row[3][1]
            ))

    def print(self, size=False, filter=None):
        """
        Print the Time Schedule.

        Arguments:
        - size: If True, adds the number of heats or athletes.
        = filter: optjonal function
                  which takes an Item
                  and returns True if item should be printed
        """
        print('Tijd: Onderdeel - Categorie/Startgroep')
        for item in self.items:
            if (not filter) or (filter(item)):
                item.print(size)
