import os
import sys
from pathlib import Path
from pypdf import PdfWriter

from pytest import fixture

# Add merge-pdf to path
sys.path.insert(0, str(Path(__file__).parents[1].resolve()))

@fixture
def example_config(tmp_path):
    """Custom pytest fixture that contains an example configuration with some files.
    Parameters:
    tmp_path (pathlib.Path): fixture which will provide a temporary directory unique
                             to the test invocation, created in the base temporary directory.
    """
    def create_pdf(pdf_path: str | Path):
        pdf_writer = PdfWriter()
        pdf_writer.add_blank_page(219, 297)
        pdf_writer.write(pdf_path)

    pdf_dir: Path = tmp_path / "current_pdfs"
    pdf_dir.mkdir(parents=True, exist_ok=True)

    not_only_pdfs_dir: Path = tmp_path / "not_only_pdfs"
    not_only_pdfs_dir.mkdir(parents=True, exist_ok=True)

    # Add pdf files to the current_pdfs directory
    create_pdf(pdf_dir / "lecture1.pdf")
    create_pdf(pdf_dir / "lecture2.pdf")
    create_pdf(pdf_dir / "lecture3.pdf")
    create_pdf(pdf_dir / "lecture5.pdf")
    create_pdf(pdf_dir / "lecture4.pdf")
    
    # Add arbitrary files to not_only_pdfs directory
    create_pdf(not_only_pdfs_dir / "lecture1.pdf")
    (not_only_pdfs_dir / "lecture2.docx").touch()
    (not_only_pdfs_dir / "lecture3.png").touch()
    (not_only_pdfs_dir / "lecture5").touch()
    create_pdf(not_only_pdfs_dir / "lecture5.pdf")

    save_cwd = os.getcwd()
    os.chdir(tmp_path)
    yield tmp_path
    os.chdir(save_cwd)