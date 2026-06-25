import re
import requests

def extract_url_from_curl(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    url_match = re.search(r"curl\s+'([^']+)'", content)
    if url_match:
        return url_match.group(1)
    
    url_match = re.search(r'curl\s+"([^"]+)"', content)
    if url_match:
        return url_match.group(1)
        
    return None

url = extract_url_from_curl("/mnt/DATA/Proyek/menu_updater_GO/GO/session/curl/Foto menu curl.txt")
print("Extracted URL:", url)
