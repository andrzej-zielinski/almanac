from setuptools import setup, find_packages
from distutils.core import Extension

setup(
    name='perilous-wilds',
    url='https://gitlab.com/heroic-blades/perilous-wilds',
    author='Andrzej Zielinski',
    author_email='andrzejt.zielinski@gmail.com',
    # Needed to actually package something
    packages=["perilous"],
    # package_dir = {"":""},
    # ext_modules = [account_manager_module],
    # Needed for dependencies
    install_requires=['requests', 'pony', 'numpy'],
    # *strongly* suggested for sharing
    version='0.1.0.0',
    # The license can be anything you like
    license='Unspecified',
    description='An installable module emulating Perilous Wilds rules.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
