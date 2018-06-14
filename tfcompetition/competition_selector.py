"""Define an object which can select a T&F competition from atletiek.nu."""


from re import search


class CompetitionSelector(object):
    """
    Object which can select a Track and Field competition.

    Public members:
        competition (integer):
            Numerical ID of the chosen competition.
            0 if no competition has been chosen.
            -1 if user provided invalid input.
    """

    def __init__(self, initialise=True):
        """Initialise the object."""
        self.competition = 0
        if initialise:
            self.select()

    def select(self):
        """Let the user select a competition."""
        # self.competition = 17
        answer = input("Paste a link to the competition: ")
        if answer:
            # User provided an answer.
            found = search(r"(\d+)", answer)
            if found:
                self.competition = int(found.group(1))
            else:
                self.competition = -1
        else:
            # User did not provide an answer.
            self.competition = 0
