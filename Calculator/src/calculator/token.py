"""Token"""
#------------------------------------------------------------

# Standard library
from enum import Enum
from collections import namedtuple
# 3rd Party library


# Project library


#------------------------------------------------------------
TokenType = Enum(
                "TokenType", 
                [
                                "NUMBER", 
                                "ADD_OP", 
                                "MUL_OP", 
                                "POWER_OP", 
                                "FAC_OP", 
                                "LEFT_PAREN", 
                                "RIGHT_PAREN", 
                                "EMPTY", 
                                "ERROR",
                                "UNKNOWN",
                 ]
)

#------------------------------------------------------------
Token = namedtuple(
                "Token",
                [
                                "token_type",
                                "lexeme",
                ]
                
)
