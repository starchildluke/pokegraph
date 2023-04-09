try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pokegraph',
    packages=['pokegraph'],
    entry_points={'console_scripts': ['pokegraph=pokegraph.pokegraph:main']},
    version='0.1.1',
    author="starchildluke",
    author_email="luke@lukealexdavis.co.uk",
    url='https://github.com/starchildluke/pokegraph',
    download_url='https://pypi.python.org/pypi/pokegraph/',
    license='MIT',
    description='A command-line tool that draws Pokémon base stats graphs in the terminal.',
    platforms='any',
    keywords='python CLI tool drawing graphs shell terminal pokemon',
    python_requires='>=3.7',
    install_requires=['colorama'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
