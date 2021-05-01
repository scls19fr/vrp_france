import click
import pandas as pd
from aerofiles.seeyou.writer import Writer
from aerofiles.seeyou.converter import WaypointStyle


@click.command()
@click.option(
    "--input", default="vrp_france_jprnavmaster.csv", help="CSV filename input"
)
@click.option("--output", default="vrp_france.cup", help="CUP filename output")
def main(input, output):
    # ToDo: manually add a ; at end of first line
    encoding = "utf8"  # "latin1"
    df = pd.read_csv(input, encoding=encoding, sep=";")

    print(df)

    with open(output, "wb") as fd:
        w = Writer(fd)
        for (_, wpt) in df.iterrows():
            code = wpt.CODE
            # splited_code = code.split("/")
            # if len(splited_code) == 2:
            #    ad, shortname = splited_code
            #    code = shortname + "@" + ad
            # else:
            #    shortname = wpt.CODE
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


if __name__ == "__main__":
    main()
