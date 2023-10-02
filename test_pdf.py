from pypdf import PdfMerger
from pathlib import Path

def directory_to_one_pdf(directory_name: str | Path, mergename: str):
    merge_p = Path(mergename)
    assert merge_p.suffix == '.pdf'
    p = Path(directory_name)
    merger = PdfMerger()
    for pdf in p.rglob("*.pdf"):
        merger.append(pdf)     

    merger.write(mergename)
    merger.close()

def directory_to_multiple(directory_name: str | Path, new_dir_name: str):
    ...
    # TODO: sort the files by their download date.
    # Then give each lecture an index

directory_to_one_pdf('test_dir','merged')

