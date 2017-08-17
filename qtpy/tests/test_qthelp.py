"""Test for QtHelp namespace."""

from __future__ import absolute_import

import pytest
from qtpy import PYSIDE2, QtHelp


@pytest.mark.skipif(PYSIDE2, reason="QtHelp bind is missing in PySide2")
def test_qthelp():
    """Test the qtpy.QtHelp namespace."""
    assert QtHelp.QHelpContentItem is not None
    assert QtHelp.QHelpContentModel is not None
    assert QtHelp.QHelpContentWidget is not None
    assert QtHelp.QHelpEngine is not None
    assert QtHelp.QHelpEngineCore is not None
    assert QtHelp.QHelpIndexModel is not None
    assert QtHelp.QHelpIndexWidget is not None
    assert QtHelp.QHelpSearchEngine is not None
    assert QtHelp.QHelpSearchQuery is not None
    assert QtHelp.QHelpSearchQueryWidget is not None
    assert QtHelp.QHelpSearchResultWidget is not None
