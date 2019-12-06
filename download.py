#!/usr/bin/env python

from pathlib import Path
import re
import urllib.request

OUTPUT_DIRECTORY = Path("downloaded")
DOC_REGEX = re.compile(r"Doc:\s+\[(.*)\]\((.*)\)")

if not OUTPUT_DIRECTORY.is_dir():
    OUTPUT_DIRECTORY.mkdir(parents=True)

for path in Path(".").glob("*.md"):
    for match in DOC_REGEX.finditer(path.read_text()):
        output_path = OUTPUT_DIRECTORY / (match.group(1) + ".pdf")
        url = match.group(2)
        if output_path.is_file():
            print(f"Already downloaded {url} to {output_path}")
        else:
            print(f"Downloading {url} to {output_path}")
            urllib.request.urlretrieve(url, output_path)


