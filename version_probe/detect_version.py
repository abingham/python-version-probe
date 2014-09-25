# The initial version of this code was written by cjwelborn in
# http://www.reddit.com/r/Python/comments/2h5pwa/version_probe_module_for_detecting_the_python/

from lib2to3 import refactor
from lib2to3.pgen2.parse import ParseError

from version_probe.filter_tuple_printing import filter_tuple_printing


class VersionDetector(refactor.RefactoringTool):
    """A lib2to3 refactoring tool designed to detect if the code being
    refactored is Python2 or Python3.

    All it does is looks for any change suggestions. When sees them,
    it takes that as an indication that the code is Python 2 (hence
    the need to update it to Python 3.)

    See: lib2to3.refactor.RefactoringTool
         lib2to3.main.StdoutRefactoringTool
    """

    def __init__(self, *args, **kwargs):
        refactor.RefactoringTool.__init__(self, *args, **kwargs)

        self._filters = []
        self.output = []

    @property
    def filters(self):
        """A sequence of filters that block outputs which don't actually
        represent major-version differences.

        Each filter in the sequence is called for each detected
        output. If it returns `False`, then that output is not counted
        as a change (i.e. it is not recorded in `output`.)
        """
        return self._filters

    def print_output(self, old_text, new_text, filename, equal):
        # You don't really have to save the output.
        # You could set a flag like: self.output = True
        if not equal:
            if all(f(old_text, new_text, filename, equal)
                   for f in self.filters):
                self.output.append(new_text)


def detect_version(filename):
    """Attempt to detect the Python major version of the source code in
    `filename`.

    `filename` may refer to a file or a directory.

    Returns: `2` or `3`, depending on the detected version.

    Raises:
        ValueError: If a parsing error is detected.
    """

    rt = VersionDetector(refactor.get_fixers_from_package('lib2to3.fixes'))
    rt.filters.append(filter_tuple_printing)
    try:
        # File to parse is the first argument given.
        rt.refactor([filename])
    except ParseError as ex:
        parseval = getattr(ex, 'value', None)
        if parseval in ('print', 'from', '**'):
            # Happens when parsing Python3 files
            # though this still needs investigating.
            return 3
        else:
            raise ValueError('Syntax/ParseError: {}'.format(ex))

    if rt.output:
        return 2
    else:
        return 3
