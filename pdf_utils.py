import os
import shutil
from pypdf import PdfMerger
from pathlib import Path

def files_to_one_pdf(directory_name: str | Path, mergename: str):
    merge_p = Path(mergename)
    assert merge_p.suffix == '.pdf'
    p = Path(directory_name)
    merger = PdfMerger()
    for pdf in sorted(p.rglob("*.pdf"),key=os.path.getmtime,reverse=True):
        merger.append(pdf)     

    merger.write(mergename)
    merger.close()

def files_to_directory(directory_name: str | Path, dest_path: str):
    dest_path: Path = Path(dest_path)
    dest_path.mkdir()
    p = Path(directory_name)
    i = 0
    for pdf in sorted(p.rglob("*.pdf"),key=os.path.getmtime,reverse=True):
        filename = str(i) + "_" + '.pdf'
        new_dest_path = dest_path / Path(filename)
        shutil.copy(pdf,new_dest_path)
        i += 1

files_to_one_pdf('test_dir','merged.pdf')
files_to_directory('test_dir','my_dir')