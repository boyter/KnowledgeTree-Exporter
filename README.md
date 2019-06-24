# KnowledgeTree-Exporter

[![Scc Count Badge](https://sloc.xyz/github/boyter/KnowledgeTree-Exporter/)](https://github.com/boyter/KnowledgeTree-Exporter/)

Exporting Documents from KnowledgeTree 3.7.0.2

See https://boyter.org/2015/09/exporting-documents-knowledgetree-3-7-0-2/ for details

A short Python script which can be used to rebuild the folders and documents on disk. All that is required is to ensure that Python MySQLdb is installed and to set the database details. Depending on your KT install you may need to change the document location. Where  the script is run it will replicate the folder tree containing the documents preserving the structures, names and extensions.
