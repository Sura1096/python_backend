from urllib.request import urlopen
import urllib.error


class WebParser:
    def __init__(self):
        self.url = 'https://spimex.com/upload/reports/oil_xls/oil_xls_202312'

    def _get_all_url(self) -> dict:
        xls_files = {}
        for date in range(1, 32):
            full_url = (
                f'{self.url}0{date}162000.xls'
                if len(str(date)) < 2
                else f'{self.url}{date}162000.xls'
            )
            try:
                url = urlopen(full_url)
                file_name = full_url.split('/')[-1]
                xls_files[file_name] = url.read()
            except urllib.error.HTTPError:
                continue

        return xls_files
