import os
from setuptools import find_packages, setup


def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


package_name = 'pyindex'

setup(name=package_name,
      version=get_version("{package_name}\__init__.py".format(package_name=package_name)),
      description="Python package to create price indices",
      long_description=open('README.md').read(),
      classifiers=[
        'Development Status :: Development',
        'License :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Price Indices',
      ],
      author='Serge Goussev and Ross Beck-MacNeil',
      license='MIT',
      packages=[package_name],
      zip_safe=False)
