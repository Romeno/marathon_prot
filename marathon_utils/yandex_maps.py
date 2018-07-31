import json


def parse_geojson(geojson):
    if isinstance(geojson, str):
        d = json.loads(geojson)
    else:
        d = json.load(geojson)

    ret = {
        "route": None,
        "refresh_zones": [],
        "catering_zones": [],
        "toilets": [],
        "timing_points": [],
        "kilometers": [],
        "start": None,
        "finish": None,
        "sights": [],
        "fan_zones": [],
        "music": [],
        "relay_race_points": [],
    }

    for feature in d["features"]:
        g = feature.get("geometry")
        props = feature.get("properties")
        if g:
            type = g["type"]
            if type == "LineString":
                ret["route"] = g["coordinates"]
            if type == "Point":
                if props:
                    caption = props["iconCaption"]
                    obj = {
                            "coords": g["coordinates"],
                            "desc": props["description"]
                    }
                    if caption == "Зона освежения":
                        ret["refresh_zones"].append(obj)
                    if caption == "Зона питания":
                        ret["catering_zones"].append(obj)
                    if caption == "Туалет":
                        ret["toilets"].append(obj)
                    if caption == "Точка хронометража":
                        ret["timing_points"].append(obj)
                    if caption == "Километр":
                        ret["kilometers"].append(obj)
                    if caption == "Старт":
                        ret["start"] = obj
                    if caption == "Финиш":
                        ret["finish"] = obj
                    if caption == "Достопримечательность":
                        ret["sights"].append(obj)
                    if caption == "Фан-зона":
                        ret["fan_zones"].append(obj)
                    if caption == "Музыка":
                        ret["music"].append(obj)
                    if caption == "Точка передачи эстафеты":
                        ret["relay_race_points"].append(obj)

    return ret







