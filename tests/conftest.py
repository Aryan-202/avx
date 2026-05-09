import pytest
import os
import tempfile
from pathlib import Path

@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        original_dir = os.getcwd()
        os.chdir(tmpdirname)
        yield Path(tmpdirname)
        os.chdir(original_dir)

@pytest.fixture
def sample_files(temp_dir):
    """Create sample files for testing."""
    # Create test files
    (temp_dir / "test.txt").write_text("Hello World")
    (temp_dir / "test.docx").touch()
    (temp_dir / ".hidden").touch()
    (temp_dir / "subdir").mkdir()
    return temp_dir