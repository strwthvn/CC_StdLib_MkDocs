"""
MkDocs hooks for custom functionality
"""

import sys
import os

def on_startup(**kwargs):
    """
    Called when MkDocs starts up.
    Register custom Pygments lexers here.
    """
    # Add project root to Python path
    project_root = os.path.dirname(os.path.abspath(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    # Import and register IEC ST lexer
    try:
        from custom_lexers.iecst_lexer import IECSTLexer
        from pygments.lexers import _mapping

        # Register the lexer
        _mapping.LEXERS['IECSTLexer'] = (
            'custom_lexers.iecst_lexer',
            'IEC ST',
            ('iecst', 'st', 'iec', 'structured-text'),
            ('*.st', '*.ST'),
            ('text/x-iecst',)
        )

        print("✓ IEC ST lexer registered successfully")
    except Exception as e:
        print(f"✗ Failed to register IEC ST lexer: {e}")


def on_config(config, **kwargs):
    """
    Called after config is loaded.
    Can be used for additional configuration.
    """
    return config
