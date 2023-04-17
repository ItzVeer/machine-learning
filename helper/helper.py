import os
import urllib.request

def downloadData(url, path):
    """
    Downloads a file from the given URL to the specified path, if the file does not exist at the path.

    Args:
        url (str): URL of the file to be downloaded.
        path (str): Local file path where the downloaded file should be saved.
    """
    if os.path.isfile(path):
        print(f"File exists at location: {path}")
    else:
        try:
            urllib.request.urlretrieve(url, path)
            print(f"File downloaded to location: {path}")
        except urllib.error.URLError as e:
            print(f"Failed to download file from URL: {url}. Error: {e}")