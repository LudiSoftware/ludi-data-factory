from F import LIST
import BaseFunctions as bf

PARSED_SUB_ZONE_POLYGONS = {}
parsedPZs = []
TYPE = "polygon"

def parseParentZonePolygons(parentZone):
    name = parentZone[1]
    subZones = parentZone[3][0][2][0]
    return { "parent": name, "subZones": subZones, "type": TYPE }

def parseSubZonePolygons(subZone):
    latlngs = subZone[1][0][0][0][0]
    newLatLngs = []
    for ll in latlngs:
        flat = LIST.flatten(ll)
        parsedLatLngs = bf.toLatLng(flat[0], flat[1])
        newLatLngs.append(parsedLatLngs)
    name = LIST.flatten(subZone[2])[1]
    return { "name": name, "latlngs": newLatLngs, "type": TYPE }

rawPZ = bf.initialParsing()

""" 1. Parse out ParentZone Polygons """
for pz in rawPZ:
    parsedPZs.append(parseParentZonePolygons(pz))
""" 2. Parse out SubZones Polygons """
for pz in parsedPZs:
    temp = []
    for sz in pz["subZones"]:
        try:
            t = parseSubZonePolygons(sz)
            t["parentZone"] = pz["parent"]
            t["description"] = t["name"]
            redz = bf.parseToRedZone(t).toJson()
            temp.append(redz)
        except:
            continue
    PARSED_SUB_ZONE_POLYGONS[pz["parent"]] = temp

print(PARSED_SUB_ZONE_POLYGONS)

def save_to_firebase():
    from Firebase.YsrDB import FireDB
    db = FireDB("redzones")
    for parentName in PARSED_SUB_ZONE_POLYGONS:
        parentSubZones = PARSED_SUB_ZONE_POLYGONS[parentName]
        for zone in parentSubZones:
            print(zone)
            db.add_object(zone["id"], zone)

# from F import OS
# OS.save_dict_to_file("polys_backup", {"polys": PARSED_SUB_ZONE_POLYGONS}, "/Users/chazzromeo/Desktop/")

















