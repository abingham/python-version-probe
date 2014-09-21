from setuptools import setup

version = 0.1

with open('README.rst', 'r') as readme:
    long_description = readme.read()

setup(
    name="version_probe",
    packages=["version_probe"],
    version="{version}".format(version=version),
    description="Probe Python source code for language version.",
    author="Austin Bingham",
    author_email="austin@sixty-north.com",
    url="http://github.com/abingham/python-version-probe",
    # download_url="".format(version=version),
    keywords=["Python"],
    license="MIT License",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    install_requires=[
        'baker',
        'with_fixture',
    ],
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'python_version_probe = version_probe.app:main',
        ],
    },
)
