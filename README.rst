`Travis CI <https://travis-ci.org/abingham/python-version-probe>`_ |build-status|

======================
 python version probe
======================

A tool for detecting the Python major version for a body of source
code.

Installation
============

Install with *pip*::

    pip install python_version_probe


*easy_install*::


    easy_install python_version_probe


or manually::

    python setup.py install

Quickstart
==========

You can use the API::


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

or the `python_version_probe` command-line tool::


    % python_version_probe /projects/nuclear_launch_control
    3

.. Build status badge
.. |build-status|
   image:: https://secure.travis-ci.org/abingham/python-version-probe.png
           ?branch=master
   :target: http://travis-ci.org/abingham/python-version-probe
   :alt: Build Status
