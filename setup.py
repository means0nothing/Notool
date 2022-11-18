import os
import re
import functools
import itertools
import typing as t
from setuptools import setup, find_packages

project_name = 'notool'
description = 'Different handies'
url = 'https://github.com/means0nothing/Notool'


def readme():
    with open('README.md') as file:
        return file.read()


def version():
    result = ''
    with open(os.path.join(project_name, '__init__.py')) as file:
        for line in file.readlines():
            if line.startswith('__version__'):
                result = line[line.find('\'') + 1: line.rfind('\'')]
                break
    if not result:
        raise ValueError("Unable to determine version.")
    return result


@functools.cache
def _requirements() -> dict:
    with open('requirements.txt') as file:
        split = ((split[0], '' if len(split) == 1 else split[1]) for split
                 in (re.split(r'\s*#\s*', str.strip(line)) for line
                     in file.readlines()) if split[0])
        req_dict = {}
        for val, tag in split:
            if req_dict.get(tag) is None:
                req_dict[tag] = [val]
            else:
                req_dict[tag].append(val)
        return req_dict


def requirements(key: t.Optional[str] = ''):
    return _requirements()[key] if key is not None else \
        list(itertools.chain(*_requirements().values()))


setup(
    name=project_name,
    version=version(),
    description=description,
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='MIT',
    author='Pavel Shevcov',
    author_email='means0nothing@gmail.com',
    url=url,
    keywords=[],
    python_requires=">=3.9",
    classifiers=[
        'Development Status :: 3 - Alpha',  # '3 - Alpha', '4 - Beta', '5 - Production/Stable'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    ext_modules=[],
    setup_requires=['wheel'],
    install_requires=requirements(),
    extras_require={},
)
