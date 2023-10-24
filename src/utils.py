import os

from pypdf import PdfMerger


def get_pdf_files(path_to_files):
    """This function gets a list of the pdf files in a given path.

    :param path_to_files: str
        String that indicates the relative path to the files.

    :return:
    sorted_pdf_files: list
        List of the pdf files in the path, in numerical-alphabetical order.

    """
    sorted_files = sorted(os.listdir(path_to_files))
    sorted_pdf_files = [
        os.path.join(path_to_files, file)
        for file in sorted_files if file.endswith('.pdf')
    ]
    return sorted_pdf_files


def merge_files_from_list(file_list, result_path):
    """ This function merges the pdf files that are found in a list into a
    result path.

    :param file_list:
    :param result_path:
    :return:
        None
    """
    merger = PdfMerger()
    for pdf_filepath in file_list:
        merger.append(pdf_filepath)

    desired_name = input('Title for document without `.pdf` extension: ')
    final_path = os.path.join(result_path, f"{desired_name}.pdf")
    merger.write(final_path)
    merger.close()
