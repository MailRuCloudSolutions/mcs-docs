import sys
import os

sys.path.insert(0, os.path.abspath(''))

master_doc = 'index'

source_suffix = '.rst'

project = u'mcs'

exclude_patterns = [
    'locale',
    'cleanup.py',
]

language = 'en'
locale_dirs = ['./doc/locale']
gettext_compact = False
gettext_location = True
