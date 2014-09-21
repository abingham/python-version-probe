import os
import os.path
import subprocess


def detect_file_version(filename):
    """Attempt to detect the major version of the Python code in
    `filename`.

    Returns: `2` or `3`, depending on the detected version.

    Raises:
        ValueError: If a parsing error is detected.
    """
    with open(os.devnull, 'w') as devnull:
        try:
            output = subprocess.check_output(['2to3', filename],
                                             stderr=devnull)
        except subprocess.CalledProcessError:
            raise ValueError('Error parsing {}'.format(filename))

    changes = [o for o in output.split(b'\n') if len(o)]
    return 2 if len(changes) else 3


def detect_version(directory):
    """Attempt to detect the Python major version of the source code in
    `directory`.
    """

    version_map = {filename: detect_file_version(filename)
                   for root, dirs, files in os.walk(directory)
                   for filename in (os.path.join(root, f) for f in files)}
    versions = set(version_map.values())
    if not versions:
        return None
    elif len(versions) == 2:
        return None
    else:
        return next(iter(versions))
