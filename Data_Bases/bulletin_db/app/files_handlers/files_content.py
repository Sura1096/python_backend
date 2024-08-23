from .file_parser import FilesParser
from datetime import date


def get_date(filename: str) -> date:
    extract_bulletin_date = filename.split('_')[-1][:8]
    bulletin_date = (
        extract_bulletin_date[:4]
        + '-'
        + extract_bulletin_date[4:6]
        + '-'
        + extract_bulletin_date[6:8]
    )
    return date.fromisoformat(bulletin_date)


def files_parse():
    files_parser = FilesParser()
    info = files_parser.read_files()
    for file, content in info.items():
        bulletin_date = get_date(file)
        for cell in content:
            cell['date'] = bulletin_date
            cell['created_on'] = date.today()
            cell['updated_on'] = date.today()

    return info
