from setuptools import setup

version = 0.1

with open('README.rst', 'r') as readme:
    long_description = readme.read()

setup(
    name="version_probe",
    packages=["version_probe"],
    version="{version}".format(version=version),
    description="Gathering metrics in codebases over time.",
    author="Austin Bingham",
    author_email="austin@sixty-north.com",
    # url="http://code.sixty-north.com/version_probe",
    # download_url="".format(version=version),
    keywords=["Python"],
    license="MIT License",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        # "Programming Language :: Python :: 3.4",
        # "Environment :: Other Environment",
        # "Intended Audience :: Developers",
        # "License :: OSI Approved :: MIT License",
        # "Operating System :: OS Independent",
        # "Topic :: Software Development :: Libraries :: Python Modules",
        # "Topic :: Experimentation",
        ],
    install_requires=[
    ],
    long_description=long_description,
    entry_points={
        # 'console_scripts': [
        #     'version_probe = version_probe.app:main',
        # ],
    },
)
