from typing import List
from sys import argv
import os
import PyPDF2


def join_pdfs(args: List[str], output_dir: str = "") -> int:
    """Join n pdfs together into a single pdf."""
    if len(args) < 3:
        print("Usage: pdf.py <file1.pdf> <file2.pdf> (optional)<output_dir>")
        return 1

    merger = PyPDF2.PdfMerger()
    for file in args:
        if file.endswith(".pdf"):
            # absolute_path = os.path.abspath(file)
            merger.append(file)
        merger.write(output_dir + "combined_doc.pdf")

    merger.close()
    return 0


def resolve_file(file: str) -> str:
    """Resolve the filepath if not in the same directory."""
    pass


if __name__ == '__main__':
    join_pdfs(argv, argv[-1])
