import os
import tempfile
import unittest

import version_probe
import version_probe.test.compat as compat
import with_fixture


class TestFiles(with_fixture.TestCase):
    def withFixture(self):
        with tempfile.NamedTemporaryFile(mode='w') as self.f:
            yield

    def test_detects_python_v2(self):
        self.f.write('print "llama"')
        self.f.flush()
        self.assertEqual(2, version_probe.detect_version(self.f.name))

    def test_detects_python_v3(self):
        self.f.write('print("foobar")')
        self.f.flush()
        self.assertEqual(3, version_probe.detect_version(self.f.name))

    def test_file_has_syntax_error(self):
        self.f.write('x = "asdf')
        self.f.flush()
        with compat.assert_raises(self, ValueError):
            version_probe.detect_version(self.f.name)


class TestDirectories(with_fixture.TestCase):
    def withFixture(self):
        with compat.TemporaryDirectory() as self.temp_dir:
            yield

    def _write_to_file(self, contents, filename='test_file.py'):
        filename = os.path.join(self.temp_dir, filename)
        with open(filename, 'w') as f:
            f.write(contents)

    def test_no_files(self):
        version = version_probe.detect_version(self.temp_dir)
        self.assertEqual(version, 3)

    def test_single_python_v2_file(self):
        self._write_to_file('print "llamas"')
        version = version_probe.detect_version(self.temp_dir)
        self.assertEqual(version, 2)

    def test_single_python_v3_file(self):
        self._write_to_file('print("llamas")')
        version = version_probe.detect_version(self.temp_dir)
        self.assertEqual(version, 3)

    def test_syntax_error(self):
        self._write_to_file('x = "asdf')
        with compat.assert_raises(self, ValueError):
            version_probe.detect_version(self.temp_dir)


if __name__ == '__main__':
    unittest.main()
