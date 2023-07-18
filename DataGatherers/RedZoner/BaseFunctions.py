from F import LIST, DICT
import json
import RedZonesHTML

def is_positive(num:float):
    if num > 0: return True
    return False

def validate_coords(coords):
    lat,lng = coords
    if not is_positive(lat) and is_positive(lng):
        return [lng, lat]
    return coords

def validate_coordinates(coords):
    new_cords = []
    for pair in coords:
        if len(pair) != 2 or not all(isinstance(i, (int, float)) for i in pair):
            continue
        lat, lng = pair
        if not is_positive(lat) and is_positive(lng):
            new_cords.append([lng, lat])
            continue
        new_cords.append(pair)
    return new_cords

def remove_empty_elements(lst):
    new_list = []
    for item in lst:
        if isinstance(item, list):
            item = remove_empty_elements(item)
            if item:
                new_list.append(item)
        elif isinstance(item, dict):
            item = {k: v for k, v in item.items() if v}
            if item:
                new_list.append(item)
        elif isinstance(item, str):
            if item.strip():
                new_list.append(item)
        elif isinstance(item, bool):
            continue
        elif isinstance(item, int):
            continue
        elif item is None:
            continue
        else:
            new_list.append(item)
    return new_list

def pair_coordinates(lst):
    lst = LIST.flatten(lst)
    if len(lst) % 2 != 0:
        lst = lst[:-1]
    if len(lst) == 2:
        return [lst]
    return [[lst[i], lst[i + 1]] for i in range(0, len(lst), 2)]

def extract_lat_lng(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            if all(isinstance(i, (int, float)) for i in item):
                result.append(item)
            else:
                result.extend(extract_lat_lng(item))
        elif isinstance(item, dict):
            result.extend(extract_lat_lng(list(item.values())))
    pairCoords = pair_coordinates(result)
    return validate_coordinates(pairCoords)

def toLatLng(lat, lng):
    return {"latitude":lat, "longitude":lng}

def parseToRedZone(redzone_json:{}):
    from Models.RedZone import RedZone
    return RedZone(redzone_json)

def parseAllToRedZones(list_of_json:[]):
    redzones = []
    for j in list_of_json:
        redzones.append(parseToRedZone(j))
    return redzones

def intoJSON(name, description, parent_zone, latLngs):
    return {
        "name": name,
        "description": description,
        "governingBody": "BAA",
        "parentZone": parent_zone,
        "latLngs": latLngs
    }

def extract_coords(lst):
    coords1 = LIST.flatten(LIST.get(0, lst, None))
    i = 1
    master = []
    temp1 = []
    for num in coords1:
        if i % 2 == 0:
            temp1.append(num)
            master.append(temp1)
            temp1 = []
        else:
            temp1.append(num)
        i += 1
    coords2 = LIST.get(3, lst, None)
    master.append(coords2)
    final = []
    for c in master:
        vc = validate_coords(c)
        final.append(toLatLng(vc[0], vc[1]))
    return final

def initialParsing():
    data = json.loads(RedZonesHTML.dump_string)
    no_empty = remove_empty_elements(data)
    raw_parent_zones = no_empty[1]
    all_parent_zones = raw_parent_zones[5]
    return all_parent_zones