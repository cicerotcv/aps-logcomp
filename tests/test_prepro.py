import pytest
from compiler.errors import SyntaxError
from compiler.prepro import PrePro


@pytest.fixture
def hash_comment():
    return "# hash comment\n"


@pytest.fixture
def multiple_hash_comment(hash_comment):
    return hash_comment*3


@pytest.fixture
def alternate_hash_comments(hash_comment):
    return f"{hash_comment}not comment\n{hash_comment}"


class TestHashComment:
    @staticmethod
    def test_comment(hash_comment):
        expected = ""
        output = PrePro.remove_hash_comment(hash_comment)
        assert expected == output

    @staticmethod
    def test_multiple_comment(multiple_hash_comment):
        expected = ""
        output = PrePro.remove_hash_comment(multiple_hash_comment)
        assert expected == output

    @staticmethod
    def test_alternate_comments(alternate_hash_comments):
        expected = "not comment\n"
        output = PrePro.remove_hash_comment(alternate_hash_comments)
        assert expected == output


class TestBlockComment:
    @staticmethod
    def test_valid_comment():
        valid_comment = "this is /* */a valid string"
        expected = "this is a valid string"
        output = PrePro.remove_block_comment(valid_comment)
        assert output == expected

    @staticmethod
    def test_valid_multiple_comments():
        valid_comment = "this is /* this is a comment */a valid/*another comment */ string"
        expected = "this is a valid string"
        output = PrePro.remove_block_comment(valid_comment)
        assert output == expected

    @staticmethod
    def test_unclosing_comment():
        valid_comment = "this is /* this is a comment a valid another comment string"
        with pytest.raises(SyntaxError):
            PrePro.remove_block_comment(valid_comment)
