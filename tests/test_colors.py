"""Test imagemagick functions."""

from pywal import colors


def test_gen_colors():
    """> Generate a colorscheme."""
    result = colors.get("tests/test_files/test.jpg")
    assert len(result["colors"]["color0"]) == 7


def test_color_import():
    """> Read colors from a file."""
    result = colors.file("tests/test_files/test_file.json")
    assert result["colors"]["color0"] == "#1F211E"


def test_color_import_no_wallpaper():
    """> Read colors from a file without a wallpaper."""
    result = colors.file("tests/test_files/test_file2.json")
    assert result["wallpaper"] == "None"


def test_color_import_no_alpha():
    """> Read colors from a file without an alpha."""
    result = colors.file("tests/test_files/test_file2.json")
    assert result["alpha"] == "100"
