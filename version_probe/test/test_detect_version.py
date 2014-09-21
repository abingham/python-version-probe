import tempfile
import unittest

import version_probe

class TestDetectVersion(unittest.TestCase):
    def test_no_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            version = version_probe.detect_version(temp_dir)
            self.assertEqual(version, None)
