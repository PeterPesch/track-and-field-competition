"""Common functions to facilitate HTML parsing with bs4."""


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
