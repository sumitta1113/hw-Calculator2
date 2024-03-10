"""Test case for lexical analysis."""

# Standard library

# 3rd Party library
import pytest

# Project library
from src.calculator.token import Token, TokenType
from src.calculator.lexer import Lexer

#----------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.NUMBER, "456"), 3),
        ("705", 1, Token(TokenType.NUMBER, "05"), 3),
        ("+", 0, Token(TokenType.ERROR, ""), 0),
        ("", 0, Token(TokenType.EMPTY, ""), 0),
        ("abc", 0, Token(TokenType.ERROR, ""), 0),
        ("123abc", 0, Token(TokenType.NUMBER, "123"), 3),
    ]
)
def test_get_number(text, pos, expected_token, expected_pos):
    #Arrange
    lexer = Lexer()
    #Act
    token, new_pos = lexer.get_number(text, pos)
    #Assert
    assert str(token) == str(expected_token)
    assert new_pos == expected_pos

                

#----------------------------------------------------------
@pytest.mark.parametrize(
                "text, pos, expected_token, expected_pos",
                [
                                ("123", 0, Token(TokenType.ERROR, ""), 0),
                                ("705", 1, Token(TokenType.ERROR, ""), 1),
                                ("+", 0, Token(TokenType.ADD_OP, "+"), 1),
                                ("+-", 1, Token(TokenType.ADD_OP, "-"), 2),
                ]
)
def test_get_add_op(text, pos, expected_token,  expected_pos):
                """Extract an addition operator from text starting at pos."""
                #Arrange
                lexer = Lexer()
                
                #Act
                token, new_pos = lexer.get_add_op(text, pos)
                
                #Assert
                assert str(token) == str(expected_token)
                assert new_pos == expected_pos

#------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("*", 0, Token(TokenType.MUL_OP, "*"), 1),
        ("/", 0, Token(TokenType.MUL_OP, "/"), 1),
        ("+", 0, Token(TokenType.ERROR, ""), 0),
        ("", 0, Token(TokenType.EMPTY, ""), 0),
        ("abc", 0, Token(TokenType.ERROR, ""), 0),
        ("*abc", 0, Token(TokenType.MUL_OP, "*"), 1),
        ("/abc", 0, Token(TokenType.MUL_OP, "/"), 1),
    ]
)
def test_get_mul_op(text, pos, expected_token, expected_pos):
    lexer = Lexer()
    token, new_pos = lexer.get_mul_op(text, pos)
    assert str(token) == str(expected_token)
    assert new_pos == expected_pos

#------------------------------------------------------ 
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("^", 0, Token(TokenType.POWER_OP, "^"), 1),
        ("+", 0, Token(TokenType.ERROR, ""), 0),
        ("", 0, Token(TokenType.EMPTY, ""), 0),
        ("abc", 0, Token(TokenType.ERROR, ""), 0),
        ("^abc", 0, Token(TokenType.POWER_OP, "^"), 1),
        ("^+", 0, Token(TokenType.POWER_OP, "^"), 1),
        ("^/^", 0, Token(TokenType.POWER_OP, "^"), 1),
    ]
)
def test_get_power_op(text, pos, expected_token, expected_pos):
    lexer = Lexer()
    token, new_pos = lexer.get_power_op(text, pos)
    assert str(token) == str(expected_token)
    assert new_pos == expected_pos
    
#------------------------------------------------------  
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("!", 0, Token(TokenType.FAC_OP, "!"), 1),
        ("+", 0, Token(TokenType.ERROR, ""), 0),
        ("", 0, Token(TokenType.EMPTY, ""), 0),
        ("abc", 0, Token(TokenType.ERROR, ""), 0),
        ("!abc", 0, Token(TokenType.FAC_OP, "!"), 1),
        ("!+", 0, Token(TokenType.FAC_OP, "!"), 1),
        ("!/", 0, Token(TokenType.FAC_OP, "!"), 1),
    ]
)
def test_get_fac_op(text, pos, expected_token, expected_pos):
    lexer = Lexer()
    token, new_pos = lexer.get_fac_op(text, pos)
    assert str(token) == str(expected_token)
    assert new_pos == expected_pos
    
#------------------------------------------------------ 
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("(", 0, Token(TokenType.LEFT_PAREN, "("), 1),
        ("+", 0, Token(TokenType.ERROR, ""), 0),
        ("", 0, Token(TokenType.EMPTY, ""), 0),
        ("abc", 0, Token(TokenType.ERROR, ""), 0),
        ("(abc", 0, Token(TokenType.LEFT_PAREN, "("), 1),
        ("(+", 0, Token(TokenType.LEFT_PAREN, "("), 1),
        ("(/", 0, Token(TokenType.LEFT_PAREN, "("), 1),
    ]
)
def test_get_left_paren(text, pos, expected_token, expected_pos):
    lexer = Lexer()
    token, new_pos = lexer.get_left_paren(text, pos)
    assert str(token) == str(expected_token)
    assert new_pos == expected_pos

#------------------------------------------------------ 
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        (")", 0, Token(TokenType.RIGHT_PAREN, ")"), 1),
        ("+", 0, Token(TokenType.ERROR, ""), 0),
        ("", 0, Token(TokenType.EMPTY, ""), 0),
        ("abc", 0, Token(TokenType.ERROR, ""), 0),
        (")abc", 0, Token(TokenType.RIGHT_PAREN, ")"), 1),
        (")+", 0, Token(TokenType.RIGHT_PAREN, ")"), 1),
        (")/", 0, Token(TokenType.RIGHT_PAREN, ")"), 1),
    ]
)
def test_get_right_paren(text, pos, expected_token, expected_pos):
    lexer = Lexer()
    token, new_pos = lexer.get_right_paren(text, pos)
    assert str(token) == str(expected_token)
    assert new_pos == expected_pos

#------------------------------------------------------ 
@pytest.mark.parametrize(
    "text, pos, expected_pos",
    [
        (" abc ", 0, 1),
        (" xyz ", 0, 1),
        (" xyz ", 1, 1),
        (" xyz ", 2, 2),
        (" xyz ", 3, 3),
        (" xyz ", 4, 5),
        (" xyz ", 5, 5),
        ("   pqr", 0, 3),
    ]
)
def test_skip_white_space(text, pos, expected_pos):
    lexer = Lexer()
    new_pos = lexer.skip_white_space(text, pos)
    assert new_pos == expected_pos
#------------------------------------------------------ 
