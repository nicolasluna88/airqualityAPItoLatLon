import requests

def updateAttributes(fid, values, config):
    propertiesXml = ""

    for name, value in values.items():
        propertiesXml += f"""
        <wfs:Property>
            <wfs:Name>{name}</wfs:Name>
            <wfs:Value>{value}</wfs:Value>
        </wfs:Property>
        """

    xml = f"""
    <wfs:Transaction service="WFS" version="1.1.0"
        xmlns:wfs="http://www.opengis.net/wfs"
        xmlns:ogc="http://www.opengis.net/ogc"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="
            http://www.opengis.net/wfs
            http://schemas.opengis.net/wfs/1.1.0/wfs.xsd">

        <wfs:Update typeName="{config["geoserver"]["layer"]}">
            {propertiesXml}
            <ogc:Filter>
                <ogc:FeatureId fid="{fid}"/>
            </ogc:Filter>
        </wfs:Update>
    </wfs:Transaction>
    """

    r = requests.post(
        config["geoserver"]["url"],
        data=xml.encode("utf-8"),
        headers={"Content-Type": "text/xml"},
        auth=(config["geoserver"]["user"], config["geoserver"]["password"])
    )

    return r.status_code == 200