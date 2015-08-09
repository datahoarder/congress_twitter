# taken from here
# https://github.com/unitedstates/congress-legislators/blob/master/scripts/utils.py
import sys
def flags():
  _opts = {}
  for token in sys.argv[1:]:
    if token.startswith("--"):

      if "=" in token:
        key, value = token.split('=')
      else:
        key, value = token, True

      key = key.split("--")[1]
      if value == 'True': value = True
      elif value == 'False': value = False
      _opts[key.lower()] = value
  return _opts
