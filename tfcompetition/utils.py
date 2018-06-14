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
