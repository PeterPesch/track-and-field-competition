"""Show the number_of_athletes functionality of the TF Competition package."""


from tfcompetition.competition_selector import CompetitionSelector
from tfcompetition.tfcompetition import TFCompetition
from tfcompetition.schedule.schedule_parser import ScheduleParser
from tfcompetition.startlist.startlist_parser import StartlistParser

#from tfcompetition.startlist.startlist import Startlist


def main():
    """Perform the demonstration."""
    # Let the user choose the competition.
    sel = CompetitionSelector(initialise=False)
    sel.select()
    print('Competition ID:', sel.competition)
    if sel.competition <= 0:
        print('No valid competition chosen!')
        return
    # Show (part of) the time schedule.
    competition = TFCompetition(sel.competition)
    print('Schedule Page:', competition.schedule_url)
    parser = ScheduleParser(competition.schedule_url)
    print('Schedule Name:', parser.name)
    print('Schedule Title:', parser.title)
    try:
        table = parser.get_table()
    except IndexError as e:
        print(e.args[0])
        return
    print('==========================')
    schedule = parser.get_schedule()
    schedule.print()
    # Try to find a link to a startlist.
    print('==========================')
    found = None
    for item in schedule.items:
        if 'startlijst' in item._link:
            item.print()
            found = item._link
            break
    if not found:
        print('No startlist found!')
        return
    print('Startlist page: {}'.format(found))
    parser = StartlistParser(found)
    print('Startlijst Name:', parser.name)
    print('Startlijst Title:', parser.title)
    try:
        table = parser.get_table()
        print('Found the deelnemerstabel!')
    except IndexError as e:
        print(e.args[0])
        # print(parser.tree)
        return
    table.header.print()
    for row in table._tag.tbody.find_all('tr'):
        print('.', end='')
    print()
    startlist = parser.get_startlist()
    print('--------------')
    for athlete in startlist._athletes:
        print(athlete.__str__())


if __name__ == '__main__':
    main()
