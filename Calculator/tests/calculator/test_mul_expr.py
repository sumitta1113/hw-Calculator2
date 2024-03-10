"""Test cases for Multiplication expression."""

# Standard library

# 3rd Party library
import pytest

# Project library
from src.calculator.data_type import FactExpr, Number
from src.calculator.data_type import PowerExpr
from src.calculator.data_type import UnaryExpr
from src.calculator.data_type import MulExpr


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "op, left, right, expected",
    [
        ("*", Number(1), Number(0), 0),
        ("*", Number(5), Number(0), 0),
        ("/", Number(0), Number(7), 0),
        ("%", Number(22), Number(6), 4),
        ("*", Number(2), FactExpr(Number(3)), 12),
        (
                        "*", 
                        FactExpr(Number(3)), 
                        UnaryExpr("-", Number(5)), 
                        -30
         ),
         (
                        "*", 
                        PowerExpr(FactExpr(Number(3)), Number(2)), 
                        UnaryExpr("+", Number(1)), 
                        36                               
         ),
    ]
)
def test_mult_expr(op, left, right, expected):
    """Calculate the value of the multiplication expression."""
    # Arrange
    expr = MulExpr(op, left, right)

    # Act
    result = expr.eval()

    # Assert
    assert result == expected
