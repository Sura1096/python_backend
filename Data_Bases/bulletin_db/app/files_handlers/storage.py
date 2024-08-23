import os


class FilesSaver:
    def __init__(self, xls_files_dict: dict):
        """
        Класс для сохранения XLS-файлов.
        """
        self.xls_files_dict = xls_files_dict
        self.files_name = []

    def save_files(self) -> None:
        """
        Сохраняет XLS-файлы в папку "bulletins".

        Args:
            None

        Returns:
            None
        """
        for file_name, content in self.xls_files_dict.items():
            self.files_name.append(file_name)
            dir_path = os.path.join('bulletins', file_name)
            with open(dir_path, 'wb') as file:
                file.write(content)
