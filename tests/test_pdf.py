from pdf_utils import (files_to_one_pdf)
from pathlib import Path

"""
What to test:
Wrong filename. 
Directory already exist
To only merge the pdfs
"""

def test_files_to_one_pdf(example_config) -> None:
    """Test functionality of files_to_one_pdf
    Parameters:
        example_config (pytest fixture): a preconfigured temporary directory containing an example configuration

    Returns:
    None
    """
    directory_name: Path = Path(example_config) / Path("current_pdfs")
    files_to_one_pdf(directory_name,"mymerge.pdf")
    new_file_name: Path = Path(example_config) / Path("mymerge.pdf")
    assert new_file_name.is_file()
    assert new_file_name.suffix == '.pdf'
