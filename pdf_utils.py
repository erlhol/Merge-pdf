import os
import shutil
from pypdf import PdfMerger
from pathlib import Path
import sys
from tkinter import filedialog
from tkinter import *
from datetime import datetime

def files_to_one_pdf(directory_name: str | Path, mergename: str | Path) -> None:
    """ Procedure to convert pdf files in the directory directory_name to a file named
    mergename. The files are ordered by download time, from oldest to most recent
    
    Parameters:
        - directory_name (str or pathlib.Path) : The absolute path to the pdfs directory
        - mergename (str or pathlib.Path) : The filename for the merged pdf file. Must end with .pdf
    
    Returns:
    None
    """
    merge_p = Path(mergename)
    if merge_p.suffix != '.pdf':
        raise ValueError("Filename does not contain .pdf suffix")
    p = Path(directory_name)
    merger = PdfMerger()
    for pdf in sorted(p.rglob("*.pdf"),key=os.path.getmtime):
        merger.append(pdf)     

    merger.write(mergename)
    merger.close()

def files_to_directory(directory_name: str | Path, dest_path: str | Path) -> None:
    """ Procedure to convert pdf files in the directory directory_name to a new directory dest_path
    with the n files named from 0 to n-1. The files are ordered by download time, from oldest to most recent
    
    Parameters:
        - directory_name (str or pathlib.Path) : The absolute path to the pdfs directory
        - dest_path (str or pathlib.Path) : The destination directory path
    
    Returns:
    None
    """
    dest_path: Path = Path(dest_path)
    dest_path.mkdir()
    p = Path(directory_name)
    i = 0
    for pdf in sorted(p.rglob("*.pdf"),key=os.path.getmtime):
        filename = str(i) + '.pdf'
        new_dest_path = dest_path / Path(filename)
        shutil.copy(pdf,new_dest_path)
        i += 1

def move_files_from_downloads_to_directory(dest_path: str | Path) -> None:
    """ Procedure to move all pdf files found in downloads directory to dest_path directory.
    The dest_path directory will include all the same files, but orderer by download time. 
    From oldest to most recent. The n files will be renamed from 0 to n-1
    
    Parameters:
        - dest_path (str or pathlib.Path) : The destination directory path
    
    Returns:
    None
    """
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
        # How to: https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder

def files_from_downloads_to_merge(mergename: str | Path) -> None:
    """ Procedure to merge all pdf files found in downloads directory to one merged pdf file named mergename.
    The merged file will be ordered by download time, from oldest to most recent.
    
    Parameters:
        - mergename (str or pathlib.Path) : The destination directory path
    
    Returns:
    None
    """
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

def files_to_one_pdf_dialog() -> None:
    """ A GUI procedure to merge all pdf files found in the chosen directory to one merged pdf file.
    The merged file will be ordered by download time, from oldest to most recent.
    The merged file will be placed in the chosen directory
    
    Returns:
    None
    """
    root = Tk()
    root.withdraw()
    content_folder = filedialog.askdirectory()
    save_as_folder = filedialog.asksaveasfilename()
    files_to_one_pdf(content_folder,save_as_folder)

def files_to_directory_dialog() -> None:
    """ A GUI procedure to copy all pdf files found in the chosen directory to a new chosen directory.
    The files will be ordered by download time, from oldest to most recent.
    The n files will be named from 0 to n-1
    
    Returns:
    None
    """
    root = Tk()
    root.withdraw()
    content_folder = filedialog.askdirectory()
    save_as_folder = filedialog.asksaveasfilename()
    files_to_directory(content_folder,save_as_folder)

def move_files_from_downloads_to_directory_dialog() -> None:
    """ A GUI procedure to move all pdf files found in the download directory to a chosen directory.
    The moved files will be ordered by download time, from oldest to most recent.
    The n moved files will be named from 0 to n-1
    
    Returns:
    None
    """
    root = Tk()
    root.withdraw()
    save_as_folder = filedialog.asksaveasfilename()
    move_files_from_downloads_to_directory(save_as_folder)

def files_from_downloads_to_merge_dialog() -> None:
    """ A GUI procedure to create a merged pdf from all pdf files found in the download directory.
    The merged file will be ordered by download time, from oldest to most recent.
    The merged file will be placed in the chosen directory
    
    Returns:
    None
    """
    root = Tk()
    root.withdraw()
    save_as_folder = filedialog.asksaveasfilename()
    files_from_downloads_to_merge(save_as_folder)
