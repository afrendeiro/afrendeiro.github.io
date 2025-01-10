---
layout: post
title: "Sanitizing ODT comments with Python"
description: "Sanitizing ODT comments with Python"
category: notebook
tags: [workflows, python]
---
{% include JB/setup %}


Ever found yourself needing to sanitize comments in an ODT file by updating their dates—perhaps to comply with data-sharing policies or for anonymization? Today, I’ll walk you through a Python script that does just that. It updates the dates of all comments in an ODT file (optionally filtering by author) and saves a sanitized version of the file.

## Why sanitize?

Comments in documents often contain metadata like dates and authorship information. When sharing or publishing these files, you might need to remove or modify this metadata for privacy or compliance reasons.

## Enter Python

Using Python’s robust ecosystem of libraries like lxml and zipfile, we can seamlessly extract, edit, and repackage ODT files. The script described here updates all comment dates to a specific value, such as 1900-01-01T00:00:00. It even allows filtering comments by author.

## How it works

The script:

1. Extracts the ODT file into a temporary directory.
2. Parses the content.xml file, which holds the comments.
3. Updates the date for all comments or only those by a specified author.
4. Repackages the modified content into a new ODT file with .sanitized.odt appended to the original filename.


## Running the script

Here’s how you can use it:

`python -m afire /path/to/odt/file.odt --date 2000-01-01T00:00:00 --author "John Doe"`

Replace `/path/to/odt/file.odt` with your file’s path. The `--date` argument specifies the new date for comments, and the `--author` argument filters comments by the given author. Both are optional.


## The code

```python
from pathlib import Path
import zipfile
from lxml import etree
import tempfile

def main(odt_file: Path, date: str = '1900-01-01T00:00:00', author: str = None) -> None:
    """
    Sanitize comments in an ODT file by updating their date to a specified value.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        with zipfile.ZipFile(odt_file, 'r') as odt_zip:
            odt_zip.extractall(temp_path)

        content_xml_path = temp_path / "content.xml"
        if not content_xml_path.exists():
            raise FileNotFoundError("content.xml not found in the ODT file.")

        tree = etree.parse(content_xml_path)
        root = tree.getroot()
        namespace = {"office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
                     "dc": "http://purl.org/dc/elements/1.1/"}

        annotations = root.findall(".//office:annotation", namespaces=namespace)
        if not annotations:
            raise ValueError("No comments found in the ODT file.")

        for annotation in annotations:
            author_element = annotation.find(".//dc:creator", namespaces=namespace)
            if author and (author_element is None or author_element.text != author):
                continue

            date_element = annotation.find(".//dc:date", namespaces=namespace)
            if date_element is not None:
                date_element.text = date
            else:
                new_date_element = etree.Element("{http://purl.org/dc/elements/1.1/}date")
                new_date_element.text = date
                annotation.append(new_date_element)

        tree.write(content_xml_path, xml_declaration=True, encoding="UTF-8")

        sanitized_odt_path = odt_file.with_suffix(odt_file.suffix + ".sanitized.odt")
        with zipfile.ZipFile(sanitized_odt_path, 'w', zipfile.ZIP_DEFLATED) as new_odt_zip:
            for file_path in temp_path.rglob("*"):
                arcname = file_path.relative_to(temp_path)
                new_odt_zip.write(file_path, arcname)

        print(f"Sanitized ODT file saved as {sanitized_odt_path}")
```

You can see that with absolutely no dependencies, just the standard library, a lot can be done.

## Final thoughts

This simple yet powerful script showcases Python’s utility in document processing.

Whether you’re anonymizing comments for publication or prepping files for archiving, this tool ensures your metadata is under control.

Try it out and let me know how it works for you! If you have suggestions or run into issues, feel free to reach out.
