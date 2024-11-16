import urllib.request
import io

def get_robotext(url):
    try:
        path = url if url.endswith('/') else url + '/'
        req = urllib.request.urlopen(path + "robots.txt")
        data = io.TextIOWrapper(req, encoding='utf-8')
        return data.read()
    except urllib.error.HTTPError as e:
        return f"HTTP Error: {e.code}"
    except urllib.error.URLError as e:
        return f"URL Error: {e.reason}"
    except Exception as e:
        return f"An error occurred: {e}"



