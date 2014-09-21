import os
import tempfile
import unittest

import version_probe


class TestFiles(unittest.TestCase):
    def test_detects_python_v2(self):
        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write('print "llama"')
            f.flush()
            self.assertEqual(2, version_probe.detect_version(f.name))

    def test_detects_python_v3(self):
        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write('print("foobar")')
            f.flush()
            self.assertEqual(3, version_probe.detect_version(f.name))

    def test_file_has_syntax_error(self):
        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write('x = "asdf')
            f.flush()
            with self.assertRaises(ValueError):
                version_probe.detect_version(f.name)


class TestDirectories(unittest.TestCase):
    def test_no_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            version = version_probe.detect_version(temp_dir)
            self.assertEqual(version, 3)

    def test_single_python_v2_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            filename = os.path.join(temp_dir, 'python_v2.py')
            with open(filename, 'w') as f:
                f.write('print "llamas"')
            version = version_probe.detect_version(temp_dir)
            self.assertEqual(version, 2)

    def test_single_python_v3_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            filename = os.path.join(temp_dir, 'python_v3.py')
            with open(filename, 'w') as f:
                f.write('print("llamas")')
            version = version_probe.detect_version(temp_dir)
            self.assertEqual(version, 3)
