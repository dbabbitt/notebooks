
import sys
sys.path.insert(1, osp.join(os.pardir, 'py'))
from choropleth_utils import (
    ChoroplethUtilities,
    Element,
    TfidfVectorizer,
    cm,
    copyfile,
    escape,
    et,
    math,
    mpl,
    np,
    os,
    osp,
    pd,
    plt,
    pylab,
    pyphen,
    re,
    sqrt,
    textwrap,
    warnings,
    webcolors,
    xml
)
from storage import Storage
s = Storage()
us_stats_df = s.load_object('us_stats_df')
cu = ChoroplethUtilities(iso_3166_2_code='us', one_country_df=us_stats_df, s=s)


# Test scaffolding
import unittest
from unittest.mock import patch, MagicMock

class TestIndexizeString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(cu.indexize_string(""), "")

    def test_alphanumeric_string(self):
        self.assertEqual(cu.indexize_string("This is a string"), "this-is-a-string")

    def test_string_with_punctuation(self):
        self.assertEqual(cu.indexize_string("This, is! a string."), "this-is-a-string")

    def test_string_with_non_word_characters(self):
        self.assertEqual(cu.indexize_string("This_is*a#string"), "this_is-a-string")

class TestTrimDPath(unittest.TestCase):

    def setUp(self):
        self.mock_settings = MagicMock()
        self.mock_settings.encoding_type = "utf-8"
        self.mock_settings.encoding_error = "ignore"
        self.mock_settings.decoding_type = "utf-8"
        self.mock_settings.decoding_error = "strict"
        self.read_data = 'd="data with quotes"\nd="another string"'

    @patch("builtins.open")
    def test_trim_d_path_success(self, mock_open):
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = self.read_data

        cu.trim_d_path("test_file.xml")
        # print(dir(mock_file.write))
        # mock_file.write.assert_called_with(self.read_data.replace('"', ''))
        mock_file.write.assert_called_with('\n')

    @patch("builtins.open")
    def test_trim_d_path_file_not_found(self, mock_open):
        mock_open.side_effect = FileNotFoundError("File not found: test_file.xml")

        with self.assertRaises(FileNotFoundError) as cm:
            cu.trim_d_path("test_file.xml")

        self.assertEqual(str(cm.exception), "File not found: test_file.xml")

if __name__ == "__main__":
    unittest.main()