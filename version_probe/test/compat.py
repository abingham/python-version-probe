import sys
import tempfile
import unittest

MAJOR_VERSION = sys.version_info[0]

if MAJOR_VERSION == 3:
    TemporaryDirectory = tempfile.TemporaryDirectory
    assert_raises = unittest.TestCase.assertRaises

elif MAJOR_VERSION == 2:
    import contextlib
    import shutil

    @contextlib.contextmanager
    def TemporaryDirectory():
        tempdir = tempfile.mkdtemp()
        try:
            yield tempdir
        finally:
            shutil.rmtree(tempdir,
                          ignore_errors=True)

    @contextlib.contextmanager
    def assert_raises(test_case, exc_type):
        try:
            yield
        except exc_type:
            pass
        else:
            test_case.assertFalse(
                'Expected exception of type {}'.format(exc_type))
