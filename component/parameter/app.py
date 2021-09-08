from component.message import cm

__all__ = [
    "SATSOURCE",
    "CONFIDENCE",
    "TIME_SPAN",
    "BAR_FORMAT",
    "MAX_ALERTS",
    "METADATA_ROWS",
]

SATSOURCE = {
    "viirs": ("SUOMI_VIIRS_C2", "suomi-npp-viirs-c2"),
    "viirsnoa": ("J1_VIIRS_C2", "noaa-20-viirs-c2"),
    "modis": ("MODIS_C6", "c6"),
}

CONFIDENCE = {
    # Used for VIIRS (S-NPP & NOAA-20)
    "cat": {
        "high": ["high", "green"],
        "nominal": ["nominal", "orange"],
        "low": ["low", "red"],
    },
    "disc": {80: [">80", "green"], 50: [">50, <80", "orange"], 30: ["<50", "red"]},
}

# Time span for recent alerts
TIME_SPAN = {"24h": cm.alerts.hour24, "48h": cm.alerts.hour48, "7d": cm.alerts.day7}

# Specify format for the tqdm progress bar
BAR_FORMAT = "{l_bar}{bar}{n_fmt}/{total_fmt}"

# Maxiumum number of alerts to display on the map
MAX_ALERTS = 20000

# Columns to be retreived in the
METADATA_ROWS = {
    "index": cm.alerts.metadata.index,
    "latitude": cm.alerts.metadata.latitude,
    "longitude": cm.alerts.metadata.longitude,
    "acq_date": cm.alerts.metadata.acq_date,
    "acq_time": cm.alerts.metadata.acq_time,
    "confidence": cm.alerts.metadata.confidence,
    "validate": cm.alerts.metadata.validate,
    "observ": cm.alerts.metadata.observation,
}
