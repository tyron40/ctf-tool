from setuptools import setup, find_packages

setup(
    name='ctf-tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ctf-tool=cli:start_tool',
        ],
    },
)
