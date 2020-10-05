import pandas as pd
from aerofiles.seeyou.writer import Writer
from aerofiles.seeyou.converter import WaypointStyle


fname = "vrp_france_jprnavmaster.csv"

# ToDo: manually add a ; at end of first line
encoding = "utf8"  # "latin1"
df = pd.read_csv(fname, encoding=encoding, sep=";")

print(df)

fname_out = "vrp_france.cup"
with open(fname_out, "wb") as fd:
    w = Writer(fd)
    for (_, wpt) in df.iterrows():
        code = wpt.CODE
        splited_code = code.split("/")
        if len(splited_code) == 2:
            ad, shortname = splited_code
            code = shortname + "@" + ad
        else:
            shortname = wpt.CODE
        w.write_waypoint(
            code,
            shortname,
            wpt.Pays,
            wpt.Latitude,
            wpt.Longitude,
            elevation=wpt.Altitude,
            style=WaypointStyle.NORMAL,
            runway_direction=u"",
            runway_length=u"",
            frequency=u"",
            description=wpt.Nom,
        )
