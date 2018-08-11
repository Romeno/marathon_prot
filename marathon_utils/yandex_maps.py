import json


def parse_geojson(geojson):
    if isinstance(geojson, str):
        d = json.loads(geojson)
    else:
        d = json.load(geojson)

    ret = {
        "route": None,
        "refresh_zones": {"points": []},
        "catering_zones": {"points": []},
        "toilets": {"points": []},
        "timing_points": {"points": []},
        "kilometers": {"points": []},
        "start": {"point": []},
        "finish": {"point": []},
        "sights": {"points": []},
        "fan_zones": {"points": []},
        "music": {"points": []},
        "relay_race_points": {"points": []},
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
                    }
                    desc = props.get("description")
                    if desc:
                        obj["desc"] = desc

                    if caption == "Зона освежения":
                        ret["refresh_zones"]["points"].append(obj)
                    if caption == "Зона питания":
                        ret["catering_zones"]["points"].append(obj)
                    if caption == "Туалет":
                        ret["toilets"]["points"].append(obj)
                    if caption == "Точка хронометража":
                        ret["timing_points"]["points"].append(obj)
                    if caption == "Километр":
                        num = props.get("iconContent")
                        if num:
                            obj["desc"] = num

                        ret["kilometers"]["points"].append(obj)
                    if caption == "Старт":
                        ret["start"]["point"] = obj
                    if caption == "Финиш":
                        ret["finish"]["point"] = obj
                    if caption == "Достопримечательность":
                        ret["sights"]["points"].append(obj)
                    if caption == "Фан-зона":
                        ret["fan_zones"]["points"].append(obj)
                    if caption == "Музыка":
                        ret["music"]["points"].append(obj)
                    if caption == "Точка передачи эстафеты":
                        ret["relay_race_points"]["points"].append(obj)

    return ret







