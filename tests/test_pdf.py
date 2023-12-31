from pdf_structure_utilites import (files_to_one_pdf)
from pathlib import Path
import pytest
from pypdf import PdfReader

"""
What to test:
Wrong filename. 
Directory already exist
To only merge the pdfs
"""

def test_file_created_files_to_one_pdf(example_config) -> None:
    """Test functionality of files_to_one_pdf
    Parameters:
        example_config (pytest fixture): a preconfigured temporary directory containing an example configuration

    Returns:
    None
    """
    filename: str = "mymerge.pdf"

    directory_name: Path = Path(example_config) / Path("current_pdfs")
    files_to_one_pdf(directory_name,filename)
    new_file_name: Path = Path(example_config) / Path(filename)
    assert new_file_name.is_file()
    assert new_file_name.suffix == '.pdf'
    
    # We created 5 pdf files with one page each, therefore it should be 5 pages
    assert len(PdfReader(new_file_name).pages) == 5 

    # Assert that the order is correct. The pages should be in the order they were created
    reader = PdfReader(new_file_name)
    i = 0
    for page in reader.pages:
        assert page.mediabox.height - 297 == i
        i += 1

@pytest.mark.parametrize(
    "exception, directory_name, mergename",
    [
        (TypeError, 3, Path("merge.pdf")), # mergename correct, directory_name is a number
        (TypeError, Path("test"),5), # directory name correct, mergename is a number
        (ValueError, Path("test"), Path("merge")) # directory name correct, mergename without .pdf
    ],
)
def test_exception_filename_files_to_one_pdf(exception,directory_name,mergename) -> None:
    with pytest.raises(exception):
        files_to_one_pdf(directory_name,mergename)