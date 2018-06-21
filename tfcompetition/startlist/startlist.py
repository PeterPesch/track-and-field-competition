"""Objects which implement a track&field startlist."""


def Athlete(object):
    """Implement an Athlete line within a startlist."""
    def init(self, name, order=None, bib=None,
             club=None, team=None, category=None):
        """Initialise the object."""
        self.name = name
        self.order = order
        self.bib = bib
        self.club = club
        self.team = team
        self.category = category


def Startlist(object):
    """Implement a track%field startlist."""
    def __init__(self, table):
        """Initialise the object."""
        self._table = table
        self._colnames = []
        # raw header
        if (table and table.header and
                table.header.rows and
                len(table.header.rows[0].cells) > 30):
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
            hdr = header_row[col].strip()
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
        # create line objects
        raise NotImplementedError
