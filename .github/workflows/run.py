# This script will GET the Microsoft's repo for Ubuntu and finds the latest Edge file in the directory
import requests
import re
from datetime import datetime

def main():
    url = "https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-dev/"
    r = requests.get(url)
    if r.status_code == 200:
        pattern = r'<a href="([^"]+)">[^<]+</a>\s+(\d{2}-\w{3}-\d{4}\s+\d{2}:\d{2})'
        matches = re.findall(pattern, r.text)
        # create a datetime object from the date of matches
        # and sort the list by the datetime object
        matches.sort(key=lambda x: datetime.strptime(x[1], "%d-%b-%Y %H:%M"), reverse=True)
        # get the version of the latest file
        latest_version = matches[0][0].split("_")[1].split("-")[0]
        # change the pkgver in the PKGBUILD in ./microsoft-edge-dev-bin
        with open("./microsoft-edge-dev-bin/PKGBUILD", "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line.startswith("pkgver="):
                    lines[i] = f"pkgver={latest_version}\n"
        # write lines to the file
        with open("./microsoft-edge-dev-bin/PKGBUILD", "w") as f:
            f.writelines(lines)

if __name__ == "__main__":
    main()