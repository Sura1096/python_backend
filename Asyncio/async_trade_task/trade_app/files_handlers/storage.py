import asyncio
import os
from typing import Any

import aiofiles


class FilesSaver:
    def __init__(self, **kwargs: Any) -> None:
        """Класс для сохранения XLS-файлов."""
        self.xls_files_dict = kwargs
        self.files_name = []

    async def save_files(self) -> None:
        tasks = []
        for file_name, content in self.xls_files_dict.items():
            self.files_name.append(file_name)
            dir_path = os.path.join('bulletins', file_name)
            tasks.append(self.__save_file(dir_path, content))
        await asyncio.gather(*tasks)

    @staticmethod
    async def __save_file(dir_path: str, content: bytes) -> None:
        async with aiofiles.open(dir_path, 'wb') as file:
            await file.write(content)
