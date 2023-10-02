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
    dest_path: Path = Path(dest_path)
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        downloads_path = Path(Path.home() / "Downloads")
        dest_path.mkdir()
        i = 0
        for pdf in downloads_path.rglob("*.pdf"):
            filename = str(i) + '.pdf'
            new_dest_path = dest_path / Path(filename)
            shutil.move(pdf,new_dest_path)
            i += 1
    else:
        print("Your loss, get a real computer")

def files_from_downloads_to_merge(mergename: str | Path):
    merge_p = Path(mergename)
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        assert merge_p.suffix == '.pdf'
        downloads_path = Path(Path.home() / "Downloads")
        merger = PdfMerger()
        for pdf in sorted(downloads_path.rglob("*.pdf"),key=os.path.getmtime):
            merger.append(pdf)     

        merger.write(mergename)
        merger.close()
    else:
        print("Your loss, get a real computer")

#files_to_one_pdf('myfiles','merged.pdf')
#files_to_directory('myfiles','my_dir')
#files_from_downloads_to_directory("mine_filer")
files_from_downloads_to_merge("mymerge.pdf")