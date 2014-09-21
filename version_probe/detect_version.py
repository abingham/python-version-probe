import os
import os.path
import subprocess


def detect_version(filename):
    """Attempt to detect the Python major version of the source code in
    `filename`.

    `filename` may refer to a file or a directory.

    Returns: `2` or `3`, depending on the detected version.

    Raises:
        ValueError: If a parsing error is detected.
    """

    filename = os.path.expanduser(filename)

    with open(os.devnull, 'w') as devnull:
        try:
            output = subprocess.check_output(['2to3', filename],
                                             stderr=devnull)
        except subprocess.CalledProcessError as e:
            raise ValueError('Error parsing {}: {}'.format(filename, e))

    changes = [o for o in output.split(b'\n') if len(o)]
    return 2 if len(changes) else 3
