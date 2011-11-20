from nose.tools import assert_equals
from trashcli.cli.list import List

from StringIO import StringIO
import unittest
class DontTestList(unittest.TestCase):
    def test_help_option(self):
        out=StringIO()
        cmd=List(out)
        cmd.main('trash-list', '--help')
        assert_equals(out.getvalue(), """\
Usage: trash-list

List trashed files

Options:
  --version   show program's version number and exit
  -h, --help  show this help message and exit

Report bugs to http://code.google.com/p/trash-cli/issues
""")

