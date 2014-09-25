import re


def find_matching_paren(s, start_idx):
    """Find the index of the close-paren matching the open-paren at `idx` in `s`.

    If `s[idx]` is not an open paren, throws `ValueError`. If there is
    no matching paren, throws `ValueError`.
    """
    if s[start_idx] != '(':
        raise ValueError('No open-paren at specified index')

    balance = 1
    for idx in range(start_idx + 1, len(s)):
        if s[idx] == '(':
            balance += 1
        elif s[idx] == ')':
            balance -= 1

        if balance == 0:
            return idx

    raise ValueError('Unbalance parentheses')


def find_all(s, substr):
    """Find the starting indices of all instances of `substr` in the
    string `s`.
    """
    return [m.start() for m in re.finditer(substr, s)]


def find_print_paren_indices(s):
    """Generates a sequence of (open-index, close-index) tuples every
    open/close-paren pair for `print` calls in a string.
    """
    for index in find_all(s, 'print\('):
        open_paren_index = index + len('print')
        try:
            close_paren_index = find_matching_paren(s, open_paren_index)
            yield (open_paren_index, close_paren_index)
        except ValueError:
            pass


def insert_substr(s, substr, index):
    """Insert `substr` into `s` at `index`.
    """
    return s[:index] + substr + s[index:]


def filter_tuple_printing(old_text, new_text, filename, equal):
    """This is a `VersionDetector` filter that tries to filter out the
    cases where 2to3 'upgrades' tuple printing. For example, 2to3 will
    turn `print(1, 2)` into `print((1,2))`. While this is technically
    fine from 2to3's point of view, it doesn't necessarily represent a
    version upgrade. This filter tries to deal with those.
    """

    for open_index, close_index in find_print_paren_indices(old_text):
        assert open_index < close_index, \
            'Open parens should always come before close parens.'
        subst = insert_substr(old_text, ')', close_index)
        subst = insert_substr(subst, '(', open_index)
        if subst == new_text:
            return False
    return True
