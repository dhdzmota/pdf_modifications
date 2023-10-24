import os
import webbrowser


from src.utils import get_pdf_files, merge_files_from_list


if __name__=='__main__':
    file_path = os.path.dirname(os.path.abspath(__file__))
    general_path = os.path.join(file_path, '..')
    data_path = os.path.join(general_path, 'data')

    path_to_files = os.path.join(data_path, 'modification_files')
    path_to_result = os.path.join(data_path, 'results')

    sorted_pdf_files = get_pdf_files(path_to_files)
    merge_files_from_list(sorted_pdf_files, path_to_result)
