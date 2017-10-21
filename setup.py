"""StoryTeller python package configuration."""

from setuptools import setup

setup(
    name='storyteller',
    version='0.1.0',
    packages=['storyteller'],
    include_package_data=True,
    install_requires=[
        'flask',
        'arrow',
        'sh',
    ],
)
