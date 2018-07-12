"""
   @copyright: 2015 - 2018 SSH Communications Security Corporation.
   @author: Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""

from setuptools import setup
import should_check


README = "\n\n".join([
    "# python-should-check",
    should_check.Check.__doc__])

with open('README.md', 'wt') as readme_file:
    readme_file.write(README)


setup(
    name='python-should-check',
    version='0.0.2',
    description='Exception factory',
    long_description=README,
    license="MIT",
    author="Pauli Rikula",
    url='https://github.com/SSHcom/python-should-check',
    packages=['should_check'],
    python_requires='~=3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'],
    install_requires=[]
)

