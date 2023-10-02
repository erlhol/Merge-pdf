import os
import shutil
from pypdf import PdfMerger
from pathlib import Path
import sys
from tkinter import filedialog
from tkinter import *

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

def move_files_from_downloads_to_directory(dest_path: str | Path):
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

def files_to_one_pdf_dialog():
    root = Tk()
    root.withdraw()
    content_folder = filedialog.askdirectory()
    save_as_folder = filedialog.asksaveasfilename()
    files_to_one_pdf(content_folder,save_as_folder)

def files_to_directory_dialog():
    root = Tk()
    root.withdraw()
    content_folder = filedialog.askdirectory()
    save_as_folder = filedialog.asksaveasfilename()
    files_to_directory(content_folder,save_as_folder)

def move_files_from_downloads_to_directory_dialog():
    root = Tk()
    root.withdraw()
    save_as_folder = filedialog.asksaveasfilename()
    move_files_from_downloads_to_directory(save_as_folder)

def files_from_downloads_to_merge_dialog():
    root = Tk()
    root.withdraw()
    save_as_folder = filedialog.asksaveasfilename()
    files_from_downloads_to_merge(save_as_folder)