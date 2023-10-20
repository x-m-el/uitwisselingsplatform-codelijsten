from rdflib import Graph
import os
import pprint

schemes_dir = './conceptschemes'
g = Graph()
for filename_codelist in os.listdir(schemes_dir):
  print("### Parsing file ", filename_codelist, "###")
  g.parse(os.path.join(schemes_dir, filename_codelist))

# for stmt in g:
#   pprint.pprint(stmt)

print("### All files parsed successfully ###")  