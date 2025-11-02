"""
Pygments lexer for IEC 61131-3 Structured Text (ST)
Supports syntax highlighting with GitHub Dark color scheme
"""

from pygments.lexer import RegexLexer, bygroups, words, include
from pygments.token import (
    Comment, Keyword, Name, Number, Operator, Punctuation,
    String, Text, Whitespace
)

__all__ = ['IECSTLexer']


class IECSTLexer(RegexLexer):
    """
    Lexer for IEC 61131-3 Structured Text (ST) programming language.
    Used in industrial automation with CODESYS and similar platforms.
    """

    name = 'IEC ST'
    aliases = ['iecst', 'st', 'iec', 'structured-text']
    filenames = ['*.st', '*.ST']
    mimetypes = ['text/x-iecst']

    # Case-insensitive flags
    flags = 0

    # Control flow keywords
    CONTROL_KEYWORDS = [
        'IF', 'THEN', 'ELSIF', 'ELSE', 'END_IF',
        'CASE', 'OF', 'END_CASE',
        'FOR', 'TO', 'BY', 'DO', 'END_FOR',
        'WHILE', 'END_WHILE',
        'REPEAT', 'UNTIL', 'END_REPEAT',
        'EXIT', 'RETURN', 'CONTINUE'
    ]

    # Declaration keywords
    DECLARATION_KEYWORDS = [
        'VAR', 'VAR_INPUT', 'VAR_OUTPUT', 'VAR_IN_OUT',
        'VAR_GLOBAL', 'VAR_TEMP', 'VAR_EXTERNAL', 'VAR_ACCESS',
        'END_VAR', 'CONSTANT', 'RETAIN', 'NON_RETAIN',
        'AT', 'PERSISTENT', 'REFERENCE', 'REF_TO'
    ]

    # Program unit keywords
    PROGRAM_UNIT_KEYWORDS = [
        'PROGRAM', 'END_PROGRAM',
        'FUNCTION', 'END_FUNCTION',
        'FUNCTION_BLOCK', 'END_FUNCTION_BLOCK',
        'METHOD', 'END_METHOD',
        'ACTION', 'END_ACTION',
        'STRUCT', 'END_STRUCT',
        'TYPE', 'END_TYPE',
        'CLASS', 'END_CLASS',
        'INTERFACE', 'END_INTERFACE',
        'NAMESPACE', 'END_NAMESPACE',
        'PROPERTY', 'END_PROPERTY'
    ]

    # Logical and special keywords
    LOGICAL_KEYWORDS = [
        'TRUE', 'FALSE',
        'AND', 'OR', 'XOR', 'NOT',
        'MOD', 'ABS',
        'THIS', 'SUPER', 'NULL'
    ]

    # Data types
    DATA_TYPES = [
        # Boolean
        'BOOL',
        # Integer types
        'BYTE', 'WORD', 'DWORD', 'LWORD',
        'SINT', 'INT', 'DINT', 'LINT',
        'USINT', 'UINT', 'UDINT', 'ULINT',
        # Real types
        'REAL', 'LREAL',
        # Time types
        'TIME', 'DATE', 'TIME_OF_DAY', 'TOD',
        'DATE_AND_TIME', 'DT',
        # String types
        'STRING', 'WSTRING', 'CHAR', 'WCHAR',
        # Pointer types
        'POINTER', 'REFERENCE',
        # Special
        'ANY', 'ANY_INT', 'ANY_REAL', 'ANY_NUM',
        'ANY_BIT', 'ANY_STRING', 'ANY_DATE'
    ]

    # OOP and access modifiers
    MODIFIERS = [
        'PUBLIC', 'PRIVATE', 'PROTECTED', 'INTERNAL',
        'ABSTRACT', 'FINAL', 'EXTENDS', 'IMPLEMENTS'
    ]

    tokens = {
        'root': [
            include('whitespace'),
            include('comments'),
            include('strings'),
            include('numbers'),
            include('keywords'),
            include('types'),
            include('operators'),
            include('identifiers'),
        ],

        'whitespace': [
            (r'\s+', Whitespace),
        ],

        'comments': [
            # Multi-line comments with nesting support
            (r'\(\*', Comment.Multiline, 'comment'),
            # Single-line comments
            (r'//.*?$', Comment.Single),
        ],

        'comment': [
            (r'\(\*', Comment.Multiline, '#push'),
            (r'\*\)', Comment.Multiline, '#pop'),
            (r'[^(*]+', Comment.Multiline),
            (r'[(*]', Comment.Multiline),
        ],

        'strings': [
            # Single-quoted strings
            (r"'([^'\\]|\\.)*'", String),
            # Double-quoted strings (less common in ST)
            (r'"([^"\\\\]|\\.)*"', String),
        ],

        'numbers': [
            # Time literals: T#10s, TIME#1d2h3m4s
            (r'(T|TIME|D|DATE|TOD|TIME_OF_DAY|DT|DATE_AND_TIME)#[\w:\.]+', Number),
            # Typed literals with base prefix: INT#16#FF, DINT#2#1010
            (r'\w+#\d+#[\dA-Fa-f_]+', Number),
            # Hexadecimal: 16#FF
            (r'16#[\dA-Fa-f_]+', Number.Hex),
            # Binary: 2#1010
            (r'2#[01_]+', Number.Bin),
            # Octal: 8#777
            (r'8#[0-7_]+', Number.Oct),
            # Float with exponent: 1.23E-4
            (r'\d+\.\d*([eE][+-]?\d+)?', Number.Float),
            (r'\.\d+([eE][+-]?\d+)?', Number.Float),
            # Integer
            (r'\d+', Number.Integer),
        ],

        'keywords': [
            # Control flow
            (words(CONTROL_KEYWORDS, prefix=r'(?i)\b', suffix=r'\b'), Keyword),
            # Declarations
            (words(DECLARATION_KEYWORDS, prefix=r'(?i)\b', suffix=r'\b'), Keyword.Declaration),
            # Program units
            (words(PROGRAM_UNIT_KEYWORDS, prefix=r'(?i)\b', suffix=r'\b'), Keyword.Namespace),
            # Logical
            (words(LOGICAL_KEYWORDS, prefix=r'(?i)\b', suffix=r'\b'), Keyword.Constant),
            # Modifiers
            (words(MODIFIERS, prefix=r'(?i)\b', suffix=r'\b'), Keyword.Reserved),
        ],

        'types': [
            (words(DATA_TYPES, prefix=r'(?i)\b', suffix=r'\b'), Keyword.Type),
        ],

        'operators': [
            # Assignment
            (r':=', Operator),
            # Comparison
            (r'(<>|<=|>=|<|>|=)', Operator),
            # Arithmetic
            (r'(\*\*|\+|-|\*|/)', Operator),
            # Pointer and reference
            (r'(\^|\.)', Operator),
            # Brackets
            (r'[\[\]()]', Punctuation),
            # Delimiters
            (r'[;:,]', Punctuation),
        ],

        'identifiers': [
            # System variables with %
            (r'%[A-Za-z_]\w*', Name.Builtin),
            # Function/FB calls (identifier followed by parenthesis)
            (r'([A-Za-z_]\w*)(\s*)(\()', bygroups(Name.Function, Whitespace, Punctuation)),
            # Type identifiers (after colon in declarations)
            (r':\s*([A-Za-z_]\w*)', bygroups(Name.Class)),
            # Regular identifiers
            (r'[A-Za-z_]\w*', Name),
        ],
    }


def setup_lexer():
    """Register the IEC ST lexer with Pygments."""
    try:
        from pygments.lexers import get_lexer_by_name
        # Try to get lexer - if it fails, it's not registered
        try:
            get_lexer_by_name('iecst')
        except:
            # Register our lexer
            from pygments.lexers import _mapping
            _mapping.LEXERS['IECSTLexer'] = (
                'custom_lexers.iecst_lexer',
                'IEC ST',
                ('iecst', 'st', 'iec', 'structured-text'),
                ('*.st', '*.ST'),
                ('text/x-iecst',)
            )
    except ImportError:
        pass
