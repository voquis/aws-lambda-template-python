"""
Example integration tests
"""

from example import __version__

def test_version():
    """
    Test package version
    """
    assert __version__ == '0.1.0'
