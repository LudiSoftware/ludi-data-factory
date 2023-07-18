

"""
document.querySelector("body > div > script:nth-child(5)")
/html/body/div/script[1]
    <script nonce> -> /html/body/div/script[1]

/html/body
/html/body

//*[@id="popupmodel"]/section[2]/div
/html/body/section[2]/div/div[2]
/html/body/section[2]/div/div[2]/p[2]


/html/body/section[2]/div/div[2]/p[2]/iframe

/html/body/div/script[1]
"""
from collections import namedtuple
from F import LIST, DICT
import dumper
import json

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
    # Remove last item if number of items is odd
    lst = LIST.flatten(lst)
    if len(lst) % 2 != 0:
        lst = lst[:-1]
    # Return the list as is if it contains only one pair
    if len(lst) == 2:
        return [lst]
    # Pair the coordinates
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

# -> 1. Parent Zones
# def extractParentZoneName(pz):
#     return pz[1]
def parseAllParentZones(allPZones):
    parents = {}
    for pz in allPZones:
        p_name = pz[1]
        all_sub_p_zones = pz[3][0][2][0]
        parents[p_name] = all_sub_p_zones
    return parents

# -> 2. Sub Zones
def extractSubZoneName(sz):
    # Parse Name
    try:
        return sz[2][0][1][0]
    except:
        return "No Name"
def parseAllSubZones(allSZones):
    all_sub_zones_dict = {}
    for parentName in allSZones:
        parentSubZones = allSZones[parentName]
        try:
            all_sub_zones_dict[parentName] = parseSingleSubZone(parentName, parentSubZones)
        except:
            continue
    return all_sub_zones_dict

def parseToRedZone(redzon_json:{}):
    from Models.RedZone import RedZone
    return RedZone(redzon_json)

def parseAllToRedZones(list_of_json:[]):
    redzones = []
    for j in list_of_json:
        redzones.append(parseToRedZone(j))
    return redzones

# -> PARSE SINGE SUBZONE
def _parse_single_zone_into_lat_lngs(raw_latlngs) -> {}:
    list_of_latLngs_dicts = []
    for item in raw_latlngs:
        list_of_latLngs_dicts.append(toLatLng(item[0], item[1]))
    return list_of_latLngs_dicts
def extractSubZoneLatLngs(sz) -> []:
    # Parse LatLngs
    raw_subZoneOne_latlngs = sz[1][0][0][0][0]
    newLatlngs = []
    for rawll in raw_subZoneOne_latlngs:
        f = LIST.flatten(rawll)
        coords = validate_coords(f)
        newLatlngs.append(coords)
    return _parse_single_zone_into_lat_lngs(newLatlngs)

def extractSubZoneLatLngs2(sz) -> []:
    # Parse LatLngs
    raw_subZoneOne_latlngs = sz[1][0]
    newLatlngs = []
    if type(raw_subZoneOne_latlngs) in [list, tuple]:
        try:
            raw_subZoneOne_latlngs = LIST.flatten(raw_subZoneOne_latlngs)
            coords = validate_coords(raw_subZoneOne_latlngs)
            newLatlngs.append(coords)
        except:
            pairs = pair_coordinates(raw_subZoneOne_latlngs)
            for pair in pairs:
                coords = validate_coords(pair)
                newLatlngs.append(coords)
    else:
        for rawll in raw_subZoneOne_latlngs:
            f = LIST.flatten(rawll)
            coords = validate_coords(f)
            newLatlngs.append(coords)
    return _parse_single_zone_into_lat_lngs(newLatlngs)


def extractSubZoneDescription(sz, default) -> str:
    try:
        return str(sz[2][0][1][1])
    except:
        return default

def intoJSON(name, description, parent_zone, latLngs):
    return {
        "name": name,
        "description": description,
        "governingBody": "BAA",
        "parentZone": parent_zone,
        "latLngs": latLngs
    }

def parseSingleSubZone(parentZoneName, sz) -> {}:
    temp = []
    for subZone in sz:
        try:
            subName = extractSubZoneName(subZone)
            for s in sz:
                try:
                    ltn = extractSubZoneLatLngs(s)
                    desc = extractSubZoneDescription(sz, subName)
                    temp.append(intoJSON(subName, desc, parentZoneName, ltn))
                except:
                    ltn = extractSubZoneLatLngs2(s)
                    desc = extractSubZoneDescription(sz, subName)
                    temp.append(intoJSON(subName, desc, parentZoneName, ltn))
        except:
            continue
    return temp


def initialParsing():
    data = json.loads(dumper.dump_string)
    no_empty = remove_empty_elements(data)
    raw_parent_zones = no_empty[1]
    all_parent_zones = raw_parent_zones[5]
    return all_parent_zones

def mergeSubZones(dict_list):
    # Create an empty dictionary to hold the merged dictionaries
    merged = {}
    # Iterate over the list of dictionaries
    for currentZone in dict_list:
        # Get the name and latLngs from the current dictionary
        name = currentZone.get('name')
        latLngs = currentZone.get('latLngs')
        if latLngs is None:
            continue
        if name in merged.keys():
            tempLatLngs = merged[name]['latLngs']
            if tempLatLngs is None:
                continue
            elif type(tempLatLngs) not in [list]:
                continue
            else:
                templl = tempLatLngs.append(latLngs)
                if templl:
                    merged[name]['latLngs'] = templl
        else:
            merged[name] = currentZone
    return merged


def cleanLatLngLists(dict_zone):
    latLngs = dict_zone['latLngs']
    latLngs = LIST.flatten(latLngs)
    latLngs = LIST.remove_duplicates(latLngs)
    dict_zone['latLngs'] = latLngs
    return dict_zone

rawPZ = initialParsing()
parentZones = parseAllParentZones(rawPZ)
all_red_zones = parseAllSubZones(parentZones)


temp = {}
for zoneName in all_red_zones:
    zones = all_red_zones[zoneName]
    raw = mergeSubZones(zones)
    z_list = []
    for z in raw:
        z_list.append(cleanLatLngLists(raw[z]))
    temp[zoneName] = z_list

print(temp)



















