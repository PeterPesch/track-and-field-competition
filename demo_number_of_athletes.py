"""Show the number_of_athletes functionality of the TF Competition package."""


from tfcompetition.competition_selector import CompetitionSelector
from tfcompetition.tfcompetition import TFCompetition
from tfcompetition.schedule.schedule_parser import ScheduleParser
from tfcompetition.startlist.startlist_parser import StartlistParser
from tfcompetition.utils import eventsort_key, get_event, int_from_prompt, \
        is_jumping_event, is_relay_event, is_running_event, is_throwing_event

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
    # Show the types of event
    print('==========================')
    found_relay = False
    found_run = False
    found_jump = False
    found_throw = False
    events = [get_event(item.event) for item in schedule.items]
    for event in sorted(set(events), key=eventsort_key):
        print(event)
        if is_relay_event(event):
            found_relay = True
        elif is_running_event(event):
            found_run = True
        elif is_jumping_event(event):
            found_jump = True
        elif is_throwing_event(event):
            found_throw = True
        else:
            raise ValueError('Unknown event: "{}"'.format(event))
    # Let User choose a type of event.
    print('==========================')
    print('Events found:')
    if found_relay:
        print('(1) Relay events')
    if found_run:
        print('(2) Track events found.')
    if found_jump:
        print('(3) Jump events found.')
    if found_throw:
        print('(4) Throw events found.')
    choice = int_from_prompt('Choose Type of event: ')
    if choice == 1:
        print('Relays chosen!')
        checker = is_relay_event
    elif choice == 2:
        print('Track events chosen!')
        checker = is_running_event
    elif choice == 3:
        print('Jump events chosen!')
        checker = is_jumping_event
    elif choice == 4:
        print('Throw events chosen!')
        checker = is_throwing_event
    else:
        print('Bye bye!')
        return
    # Print the chosen events.
    print('==========================')
    #found = None
    for item in schedule.items:
        if not checker(item.event):
            continue
        if 'startlijst' in item._link:
            print('---------------------------')
            item.print()
            print('Startlist page: {}'.format(item._link))
            parser = StartlistParser(item._link)
            print('Startlijst Name:', parser.name)
            print('Startlijst Title:', parser.title)
            try:
                table = parser.get_table()
            except IndexError as e:
                print(e.args[0])
                continue
            table.header.print()
            print()
            startlist = parser.get_startlist()
            print('--------------')
            for line in startlist._lines:
                print(line)
    #if not found:
    #    print('No startlist found!')
    #    return


if __name__ == '__main__':
    main()
