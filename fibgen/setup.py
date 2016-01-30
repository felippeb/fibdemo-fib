try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'fibgen',
    'author': 'Felippe Burk',
    'url': 'https://github.com/rhohan/fibdemo-fib',
    'download_url': 'https://github.com/rhohan/fibdemo-fib/fibgen',
    'author_email': 'felippeburk@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['fibgen'],
    'scripts': [],
    'name': 'fibgen'
}

setup(**config)
