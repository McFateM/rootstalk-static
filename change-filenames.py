import os

"""
Renames the files within and below the current directory to be Unix friendly.
(0) Removes "Volume V, Issue 1, "
(1) Makes lowercase (not a Unix requirement, just looks better ;)
(2) Changes spaces, colons, apostrophes, underscores and exclaimation points to hyphens
(3) Removes commas and semi-colons
(4) Replaces doubled hyphens and doubled periods with singles
(5) Replaces ".-" with "-" and "-." with "."


Usage:
python3 change-filenames.py
"""

def change(name):    
  new_name = name.replace("Volume V, Issue 1, ", "").replace(" ", "-").replace(",", "").replace(";", "").replace(":", "-").replace("'", "-").replace("!", "-").replace("_", "-").replace("--", "-").replace("..", ".").replace("--", "-").replace("..", ".").replace(".-", "-").replace("-.", ".").lower()
  if (new_name != name):
    print( "changing: ", name, " --> ", new_name)
    os.rename(name, new_name)

# First, do the dirs...
for root, dirs, files in os.walk("."):
  dirs[:] = [d for d in dirs if not d[0] == '.']
  for d in dirs:
    change(d)

# Now, do the files in those dirs...
for root, dirs, files in os.walk("."):
  files = [f for f in files if not f[0] == '.']
  dirs[:] = [d for d in dirs if not d[0] == '.']
  for f in files:
    change(root + "/" + f)
