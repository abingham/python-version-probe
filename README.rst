======================
 python version probe
======================

A tool for detecting the Python major version for a body of source
code.

Quickstart
==========

```
from version_probe import detect_version

# Find the version used in sources files under ~/projects/ipv7
v = detect_version("~/projects/ipv7")

# something so advanced is, of course, written in Python 3
assert v == 3

v = detect_version("/opt/old_project")
assert v == 2

try:
    detect_version("~/projects/experimental")
except ValueError as e:
    print("Syntax error detected in the experimental project: {}".format(e))
```
