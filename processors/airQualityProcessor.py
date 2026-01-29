from services.openWeather import getAirPollution
from services.wfsReader import getCentroids
from services.wfsTransaction import updateAttributes
from utils.configLoader import loadConfig

def run():
    config = loadConfig()
    centroids = getCentroids(config)

    print(f"Centroides encontrados: {len(centroids)}")

    for c in centroids:
        components = getAirPollution(c["lat"], c["lon"], config)

        if not components:
            print(f"❌ Sin datos para {c['fid']}")
            continue

        valuesToUpdate = {
            k: components.get(k)
            for k in config["pollutants"]
            if k in components
        }

        ok = updateAttributes(c["fid"], valuesToUpdate, config)

        if ok:
            print(f"✅ {c['fid']} actualizado")
        else:
            print(f"⚠️ Error actualizando {c['fid']}")