import pytest

from cloudbot.util.formatting import munge, dict_format, pluralize, strip_colors, truncate_str, \
    capitalize_first, strip_html, multiword_replace

test_munge_input = "The quick brown fox jumps over the lazy dog"
test_munge_count = 3
test_munge_result_a = "Ţħë ʠüíċķ Бŗöωñ ƒöχ ĵüṁρš övëŗ ţħë ĺäźÿ đöġ"
test_munge_result_b = "Ţħë quick brown fox jumps over the lazy dog"

test_format_formats = ["{a} {b} {c}", "{a} {b}", "{a}"]
test_format_data = {"a": "First Thing", "b": "Second Thing"}
test_format_result = "First Thing Second Thing"

test_pluralize_num_a = 1
test_pluralize_num_b = 5
test_pluralize_result_a = "1 cake"
test_pluralize_result_b = "5 cakes"
test_pluralize_text = "cake"

test_strip_colors_input = "\x02I am bold\x02"
test_strip_colors_result = "I am bold"

test_truncate_str_input = "I am the example string for a unit test"
test_truncate_str_length_a = 10
test_truncate_str_length_b = 100
test_truncate_str_result_a = "I am the..."
test_truncate_str_result_b = "I am the example string for a unit test"

test_capitalize_first_input = "I really like the iPhone 3"
test_capitalize_first_result = "I Really Like The IPhone 3"

test_strip_html_input = "<strong>Cats &amp; Dogs: &#181;</strong>"
test_strip_html_result = "Cats & Dogs: µ"

test_multiword_replace_dict = {"<bit1>": "<replace1>", "[bit2]": "[replace2]"}
test_multiword_replace_text = "<bit1> likes [bit2]"
test_multiword_replace_result = "<replace1> likes [replace2]"


def test_munge():
    assert munge(test_munge_input) == test_munge_result_a
    assert munge(test_munge_input, test_munge_count) == test_munge_result_b


def test_dict_format():
    assert dict_format(test_format_data, test_format_formats) == test_format_result


def test_pluralize():
    assert pluralize(test_pluralize_num_a, test_pluralize_text) == test_pluralize_result_a
    assert pluralize(test_pluralize_num_b, test_pluralize_text) == test_pluralize_result_b


def test_strip_colors():
    assert strip_colors(test_strip_colors_input) == test_strip_colors_result


def test_truncate_str():
    assert truncate_str(test_truncate_str_input, length=test_truncate_str_length_a) == test_truncate_str_result_a
    assert truncate_str(test_truncate_str_input, length=test_truncate_str_length_b) == test_truncate_str_result_b


def test_capitalize_first():
    assert capitalize_first(test_capitalize_first_input) == test_capitalize_first_result


def test_strip_html():
    assert strip_html(test_strip_html_input) == test_strip_html_result


def test_multiword_replace():
    assert multiword_replace(test_multiword_replace_text, test_multiword_replace_dict) == test_multiword_replace_result