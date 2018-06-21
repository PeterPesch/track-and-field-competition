"""Objects which implement a track&field startlist."""


class Athlete(object):
    """Implement an Athlete line within a startlist."""
    def __init__(self, **kwargs):
        """Initialise the object."""
        self.name = kwargs.pop('name', None)
        self.order = kwargs.pop('order', None)
        self.bib = kwargs.pop('bib', None)
        self.club = kwargs.pop('club', None)
        self.team = kwargs.pop('team', None)
        self.category = kwargs.pop('category', None)

    def __str__(self):
        """Return the athlete line as a string."""
        values = [self.order, self.bib, self.name,
                  self.club, self.team, self.category]
        return ', '.join([x for x in values if x is not None])


class Startlist(object):
    """Implement a track%field startlist."""
    def __init__(self, table):
        """Initialise the object."""
        self._table = table
        self._colnames = []
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
            elif hdr == 'Snr':
                col_bib = col
            elif hdr == 'Naam':
                col_name = col
            elif hdr == 'Vereniging':
                col_club = col
            elif hdr == 'Team':
                col_team = col
            elif hdr == 'Categorie':
                col_cat = col
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
        self._athletes = []
        max_col = max(col_order, col_bib, col_name,
                      col_club, col_team, col_cat)
        for row in table.body.rows:
            if len(row.cells) >= max_col:
                values = dict()
                if col_order > -1:
                    values['order'] = row.cells[col_order].string
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
                self._athletes.append(Athlete(**values))
