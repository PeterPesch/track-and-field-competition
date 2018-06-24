"""Objects which implement a track&field startlist."""


class Line(object):
    """Implement an Line within a startlist."""
    def __init__(self, **kwargs):
        """Initialise the object."""
        raise NotImplementedError

    def __str__(self):
        """Return the heat line as a string."""
        values = []
        return ', '.join([x for x in values if x is not None])


class Athlete(Line):
    """Implement an Athlete line within a startlist."""
    def __init__(self, **kwargs):
        """Initialise the object."""
        self.order = kwargs.pop('order', None)
        self.lane = kwargs.pop('lane', None)
        self.bib = kwargs.pop('bib', None)
        self.name = kwargs.pop('name', None)
        self.club = kwargs.pop('club', None)
        self.team = kwargs.pop('team', None)
        self.category = kwargs.pop('category', None)

    def __str__(self):
        """Return the athlete line as a string."""
        values = [self.order, self.lane, self.bib, self.name,
                  self.club, self.team, self.category]
        return ', '.join([x for x in values if x is not None])


class EmptyLane(Line):
    """Implement an Empty lane within a startlist."""
    def __init__(self, **kwargs):
        """Initialise the object."""
        self.lane = kwargs.pop('lane', None)

    def __str__(self):
        """Return the athlete line as a string."""
        values = [self.lane, 'Leeg']
        return ', '.join([x for x in values if x is not None])


class Heat(Line):
    """Implement an Heat line within a startlist."""
    def __init__(self, **kwargs):
        """Initialise the object."""
        self.heat = kwargs.pop('heat', None)

    def __str__(self):
        """Return the heat line as a string."""
        values = [self.heat]
        return ', '.join([x for x in values if x is not None])


class Startlist(object):
    """Implement a track%field startlist."""
    def __init__(self, table, name=None, time=None, location=None, url=None):
        """Initialise the object."""
        self._table = table
        self._colnames = []
        self.name = name
        self.time = time
        self.location = location
        self._url = url
        self._athlete_count = None
        self._heat_count = None
        # raw header
        if (table and table.header and
                table.header.rows and
                len(table.header.rows[0].cells) > 0):
            header_row = table.header.rows[0].cells
            for i in range(len(header_row)):
                if header_row[i].string:
                    celname = header_row[i].string.strip()
                else:
                    celname = 'column_{}'.format(i)
                self._colnames.append(celname)
        else:
            raise ValueError('No valid Startlist!')
        # identify columns
        self._header = []
        col_lane = -1
        col_name = -1
        col_order = -1
        col_bib = -1
        col_club = -1
        col_team = -1
        col_cat = -1
        for col in range(len(header_row)):
            hdr = header_row[col].string.strip()
            if hdr == 'Startvolgorde':
                col_order = col
                self._header.append(hdr)
            elif hdr == 'Baan':
                col_lane = col
                self._header.append(hdr)
            elif hdr == 'Snr':
                col_bib = col
                self._header.append(hdr)
            elif hdr == 'Naam':
                col_name = col
                self._header.append(hdr)
            elif hdr == 'Vereniging':
                col_club = col
                self._header.append(hdr)
            elif hdr == 'Team':
                col_team = col
                self._header.append(hdr)
            elif hdr == 'Categorie':
                col_cat = col
                self._header.append(hdr)
        # raw detail rows
        self._rows = []
        if table.body:
            for row in table.body.rows:
                if len(row.cells) < 1:
                    raise ValueError('No valid Startlist!')
                self._rows.append(
                    [(cel.string.strip(), cel.link) for cel in row.cells])
        else:
            return
        # create line objects
        self._lines = []
        max_col = max(col_order, col_bib, col_name,
                      col_club, col_team, col_cat)
        for row in table.body.rows:
            if len(row.cells) >= max_col:
                values = dict()
                if col_order > -1:
                    values['order'] = row.cells[col_order].string
                if col_lane > -1:
                    values['lane'] = row.cells[col_lane].string
                if col_bib > -1:
                    values['bib'] = row.cells[col_bib].string
                if col_name > -1:
                    values['name'] = row.cells[col_name].string
                if col_club > -1:
                    values['club'] = row.cells[col_club].string
                if col_team > -1:
                    values['team'] = row.cells[col_team].string
                if col_cat > -1:
                    values['category'] = row.cells[col_cat].string
                # Check for empty lane
                if values['name'].replace('-', '').strip() == '':
                    self._lines.append(EmptyLane(**values))
                else:
                    self._lines.append(Athlete(**values))
            elif len(row.cells) == 1:
                values = dict()
                if col_lane > -1:
                    values['heat'] = row.cells[col_lane].string
                self._lines.append(Heat(**values))

    def print(self):
        """Print the Startlist."""
        print('--------------')
        if self.time:
            print(self.time)
        if self.location:
            print(self.location)
        if self.name:
            print(self.name)
        if(self._url):
            print('Page: {}'.format(self._url))
        print(', '.join(self._header))
        print('--------------')
        for line in self._lines:
            print(line)
        print()
        print(self.size)
        print('--------------')

    @property
    def athlete_count(self):
        """Count the number of athletes on this startlist."""
        if not self._athlete_count:
            count = 0
            for line in self._lines:
                if isinstance(line, Athlete):
                    count += 1
            self._athlete_count = count
        return self._athlete_count

    @property
    def heat_count(self):
        """Count the number of heates in this startlist."""
        if not self._heat_count:
            count = 0
            for line in self._lines:
                if isinstance(line, Heat):
                    count += 1
            self._heat_count = count
        return self._heat_count

    @property
    def size(self):
        """Returns a string which describes the size of this startist."""
        if self.heat_count > 0:
            return '{} heats'.format(self.heat_count)
        elif self.athlete_count > 0:
            return '{} athletes'.format(self.athlete_count)
        else:
            return 'Size unknown.'
