import click
import pandas as pd


@click.command()
@click.option(
    "--input", default="vrp_france_jprnavmaster.csv", help="CSV filename input"
)
@click.option(
    "--output",
    default="vrp_france_littlenavmap.csv",
    help="LittleNavMap filename output",
)
def main(input, output):
    # ToDo: manually add a ; at end of first line
    encoding = "utf8"  # "latin1"
    df = pd.read_csv(input, encoding=encoding, sep=";")

    print(df)

    df = df.rename(
        columns={"Cat": "Type", "Pays": "Region", "Nom": "Description", "CODE": "Name",}
    )

    df["Type"] = df["Type"].map({"PtRep": "VRP"})
    df["Ident"] = ""
    df["MagneticDeclination"] = ""
    df["Tags"] = ""

    # df["Description"] = df["Description"].map(lambda s: '"' + s + '"')
    df["VisibleFrom"] = 25  # NM
    df["LastUpdateTimestamp"] = ""

    df = df[
        [
            "Type",
            "Name",
            "Ident",
            "Latitude",
            "Longitude",
            "Altitude",
            "MagneticDeclination",
            "Tags",
            "Description",
            "Region",
            "VisibleFrom",
            "LastUpdateTimestamp",
        ]
    ]
    print(df)
    df.to_csv(output, sep=",", index=False, header=False)


if __name__ == "__main__":
    main()
