"""Test export functions."""

from pywal import export, util

COLORS = util.read_file_json("tests/test_files/test_file.json")
COLORS["colors"].update(COLORS["special"])

TMP_DIR = "/tmp/wal"


def is_file_contents(tmp_path, pattern):
    """> Check for pattern in file."""
    content = util.read_file(tmp_path)
    return content[6] == pattern


def test_all_templates(tmp_path):
    """> Test substitutions in template file."""
    tmp_file = tmp_path / "colors.sh"
    export.every(COLORS, tmp_path)

    assert tmp_file.is_file()
    assert is_file_contents(tmp_file, "foreground='#F5F1F4'")


def test_css_template(tmp_path):
    """> Test substitutions in template file (css)."""
    tmp_file = tmp_path / "colors.css"
    export.color(COLORS, "css", tmp_file)

    assert tmp_file.is_file()
    assert is_file_contents(tmp_file, "    --background: #1F211E;")
