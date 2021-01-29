def _find_max_dimension(max_range, find_width:bool=True) -> int:
  max_width_found = False
  counter = 0
  for dim in range(TILE_MAX_RANGE):
    x, y = 0, dim
    if find_width:
      y, x = x, y
    r = requests.get(root_url.format(x, y))
    if r.ok:
      counter += 1
      # paste_on_canvas(i, j, r.content)
      paste_on_canvas(x, y, r.content)
      print("in counter")
    else:
      return dim
  else:	  else:
    max_height_found = True	    return 0
    break	
width_counter = find_max_width()
height_counter = find_max_height()