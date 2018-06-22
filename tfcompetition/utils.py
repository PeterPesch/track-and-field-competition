"""Common functions to facilitate HTML parsing with bs4."""

import re


def tag_has_class(tag, cls):
    """Check whether tag has class cls."""
    classlist = tag.get('class')
    if not classlist:
        return False
    for c in classlist:
        if c == cls:
            return True
    return False


def string_from_tag(tag):
    """Get a string representation from the tag."""
    total = ' '
    for s in tag.stripped_strings:
        total += s + ' '
    return total[:-1]


def first_string_from_tag(tag):
    """Get the first string representation from the tag."""
    for s in tag.stripped_strings:
        return s
    return ''


def combined_string_from_tag(tag):
    """Get a combined string representation from the tag."""
    strings = list(tag.stripped_strings)
    if len(strings) == 0:
        return ''
    elif len(strings) == 1:
        return strings[0]
    else:
        return '{} ({})'.format(
            strings[0],
            ', '.join(strings[1:])
        )


def find_table(tree, classname=None, headerclass=None):
    """Return tag from the first table which compies to the conditions."""
    if not tree:
        raise IndexError(
            'Error while finding {} table.'.format(classname))
    # Find the table
    found = None
    for tbl in tree.find_all('table'):
        if classname:
            # Check whether the table has the correct classname.
            if not tag_has_class(tbl, classname):
                continue
        if headerclass:
            # Check whether the table has a header.
            if not tbl.thead:
                continue
            # Check whether cells in header row are labeled 'header'.
            th = tbl.thead.find('th')
            if not th:
                continue
            elif not tag_has_class(th, 'header'):
                continue
        # All checke completed
        found = tbl
        break
    if not found:
        raise IndexError('Did not find {} table.'.format(classname))
    return found


def get_event(event):
    """Isolate the name of the event from the full event string."""
    if not event:
        return ''
    # Assume that the first word is the eventname.
    return event.split()[0]


def eventsort_key(eventname):
    """Return a sorting key which makes sense in Track and Field."""
    def is_relay_event(event):
        if '4x' in event:
            return True
        return False

    def is_running_event(event):
        if re.match(r"\d", event.strip()):
            return True
        return False

    def is_jumping_event(event):
        event = event.strip().lower()
        if 'ver' in event:
            return True
        if 'hoog' in event:
            return True
        if 'pols' in event:
            return True
        if 'hink' in event or 'hss' in event:
            return True
        return False

    def is_throwing_event(event):
        event = event.strip().lower()
        if 'kogel' in event:
            return True
        if 'speer' in event:
            return True
        if 'discus' in event:
            return True
        if 'hamer' in event:
            return True
        if 'slinger' in event:
            return True
        if 'gewicht' in event:
            return True
        return False

    def relay_key(event):
        return event.lower()

    def run_key(event):
        if 'H' in event:
            return '2' + event.strip().lower()
        else:
            return '4' + event.strip().lower()

    def jump_key(event):
        return event.lower()

    def throw_key(event):
        return event.lower()

    if is_relay_event(eventname):
        return '2' + relay_key(eventname)
    elif is_running_event(eventname):
        return '4' + run_key(eventname)
    elif is_jumping_event(eventname):
        return '6' + jump_key(eventname)
    elif is_throwing_event(eventname):
        return '8' + throw_key(eventname)
    else:
        return '0' + str(eventname).lower()
