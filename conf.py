import sys
import os

sys.path.insert(0, os.path.abspath(''))

master_doc = 'index'

source_suffix = '.rst'

project = u'mcs'

extensions = [
    'pydata_sphinx_theme'
]

exclude_patterns = [
    '.git*',
    'crowdin.yaml',
    'theme',
    'output',
    'locale',
    'requirements.txt',
]

language = 'ru'
locale_dirs = ['./locale']
gettext_compact = False
gettext_location = True

html_theme = 'pydata_sphinx_theme'
