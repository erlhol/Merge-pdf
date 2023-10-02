import os
import shutil
from pypdf import PdfMerger
from pathlib import Path
import sys

def files_to_one_pdf(directory_name: str | Path, mergename: str | Path):
    merge_p = Path(mergename)
    assert merge_p.suffix == '.pdf'
    p = Path(directory_name)
    merger = PdfMerger()
    for pdf in sorted(p.rglob("*.pdf"),key=os.path.getmtime):
        merger.append(pdf)     

    merger.write(mergename)
    merger.close()

def files_to_directory(directory_name: str | Path, dest_path: str | Path):
    dest_path: Path = Path(dest_path)
    dest_path.mkdir()
    p = Path(directory_name)
    i = 0
    for pdf in sorted(p.rglob("*.pdf"),key=os.path.getmtime):
        filename = str(i) + '.pdf'
        new_dest_path = dest_path / Path(filename)
        shutil.copy(pdf,new_dest_path)
        i += 1

def files_from_downloads_to_directory(dest_path: str | Path):
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        downloads_path = Path(Path.home() / "Downloads")
        print(downloads_path)
        for content in downloads_path.rglob("*.pdf"):
            print(content)
    else:
        print("GTFO")

#files_to_one_pdf('myfiles','merged.pdf')
#files_to_directory('myfiles','my_dir')
files_from_downloads_to_directory("")