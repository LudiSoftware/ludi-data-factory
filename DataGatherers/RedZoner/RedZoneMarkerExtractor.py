import BaseFunctions as bf

PARSED_SUB_ZONE_MARKERS = {}
parsedPZs = []
temp_cords = []
TYPE = "marker"

def parseParentZoneMarkers(parentZone):
    name = parentZone[1]
    subZones = parentZone[2]
    return { "parent": name, "subZones": subZones, "type": TYPE }

def parseSubZoneMarkers(subZone):
    latlngs = subZone[1]
    name = subZone[2]
    return { "name": name, "latlngs": latlngs, "type": TYPE }

rawPZ = bf.initialParsing()

""" 1. Parse out ParentZone Markers """
for pz in rawPZ:
    parsedPZs.append(parseParentZoneMarkers(pz))
""" 2. Parse out SubZones Markers """
for pz in parsedPZs:
    temp = []
    for sz in pz["subZones"]:
        try:
            t = parseSubZoneMarkers(sz)
            temp.append(t)
        except:
            continue
    PARSED_SUB_ZONE_MARKERS[pz["parent"]] = temp
""" 3. Fix LatLngs """
for pz in PARSED_SUB_ZONE_MARKERS:
    for sz in PARSED_SUB_ZONE_MARKERS[pz]:
        raw = sz["latlngs"]
        paw = bf.extract_coords(raw)
        sz["latlngs"] = paw
        temp_cords.append(paw)

print(PARSED_SUB_ZONE_MARKERS)


















