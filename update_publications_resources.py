#!/usr/bin/env python

import sys
from datetime import datetime
from pathlib import Path
import typing as tp

import pandas as pd


PUB_FORMAT = """<li>
                <p>
                    {authors}.
                    <br><strong>{title}</strong>.
                    <br>
                    {journal} ({year}).
                    <a rel="datacite:doi" href="http://dx.doi.org/{doi}">
                        doi:{doi}</a>
                    <a style="float:right">
                        <span
                            data-badge-type="2"
                            data-doi="{doi}"
                            data-hide-no-mentions="true"
                            class="altmetric-embed"></span>
                        <span
                            class="__dimensions_badge_embed__"
                            data-doi="{doi}"
                            data-legend="hover-right"
                            data-style="small_rectangle"
                            style='display: inline-block;'></span>
                    </a>
                    <br>{resources}
                </p>
            </li>"""
RESOURCE_FORMAT = """<a href="{resource_link}">
                        <button type="button" class="btn btn-default btn-sm">
                            <span
                                class="{resource_glypt}"
                                aria-hidden="true"></span> {resource_type} </button></a>"""
# columns: authors,title,journal,year,doi,publication_type
PUBS_CSV = Path("publications.csv")
# columns: doi,resource_type,resource_link
RESOURCES_CSV = Path("publication_resources.csv")
INPUT_DIR = Path(".")
input_file = "_index.md"
OUTPUT_DIR = Path(".")
output_file = "index.md"
DATE = datetime.now().isoformat().split("T")[0]
INDENT = "            "
AUTHOR_NAME = "André F. Rendeiro"


# A mapping between resource types and the HTML class with its glypt:
glypts = {
    "PDF": "glyphicon glyphicon-file",
    "Preprint": "glyphicon glyphicon-file",
    "Data": "glyphicon glyphicon-hdd",
    "Code": "fab fa-github",
    "Notebook": "fab book-open",
    "Press": "glyphicon glyphicon-text-color",
}


def main() -> int:
    pubs = pd.read_csv(PUBS_CSV)
    resources = pd.read_csv(RESOURCES_CSV, index_col=0)

    pub_list: tp.Dict[str, tp.List[str]] = dict()
    for pub_type in ["journal", "preprint"]:
        pub_list[pub_type] = list()
        extra = "| publication_type == 'review'" if pub_type == "journal" else ""
        for _, pub in pubs.query(
            f"publication_type == '{pub_type}' {extra}"
        ).iterrows():
            res = resources.loc[[pub["doi"]]]
            _res = list()
            for i, (_, r) in enumerate(res.iterrows()):
                if r.isnull().all():
                    continue
                r["resource_glypt"] = glypts[r["resource_type"]]
                _res.append(
                    ("\n" if i == 0 else "")
                    + "                    "
                    + RESOURCE_FORMAT.format(**r.to_dict())
                )
            pub["resources"] = "\n".join(_res)
            p = PUB_FORMAT.format(**pub.to_dict())
            pub_list[pub_type].append("            " + p)

    with open(INPUT_DIR / input_file, "r") as handle:
        content = (
            handle.read()
            .replace("{{publications_go_here}}", "\n".join(pub_list["journal"]))
            .replace("{{preprints_go_here}}", "\n".join(pub_list["preprint"]))
            .replace("{{current_date}}", DATE)
        )
    content = content.replace(AUTHOR_NAME, "<u>" + AUTHOR_NAME + "</u>").replace(
        r"$^\Omega$", "<sup>Ω</sup>"
    )
    with open(OUTPUT_DIR / output_file, "w") as handle:
        handle.write(content)

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(1)
