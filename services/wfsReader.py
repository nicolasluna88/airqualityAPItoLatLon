import requests
from lxml import etree

def getCentroids(config):
    params = {
        "service": "WFS",
        "version": config["geoserver"]["wfsVersion"],
        "request": "GetFeature",
        "typeName": config["geoserver"]["layer"],
        "maxFeatures": config["maxFeatures"],
        "outputFormat": "text/xml; subtype=gml/2.1.2"
    }

    r = requests.get(config["geoserver"]["url"], params=params)
    r.raise_for_status()

    tree = etree.fromstring(r.content)

    ns = {
        "gml": "http://www.opengis.net/gml",
        "nextcity": "nextcity"
    }

    features = tree.findall(".//gml:featureMember", ns)
    centroids = []

    for f in features:
        feature = f[0]
        fid = feature.get("fid")

        lat = feature.findtext("nextcity:lat", namespaces=ns)
        lon = feature.findtext("nextcity:lon", namespaces=ns)

        if fid and lat and lon:
            centroids.append({
                "fid": fid,
                "lat": float(lat),
                "lon": float(lon)
            })

    return centroids
