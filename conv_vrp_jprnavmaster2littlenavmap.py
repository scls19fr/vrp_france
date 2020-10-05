import pandas as pd

fname = "vrp_france_jprnavmaster.csv"

# ToDo: manually add a ; at end of first line
encoding = "utf8"  # "latin1"
df = pd.read_csv(fname, encoding=encoding, sep=";")

print(df)

df = df.rename(columns={
    "Cat": "Type",
    "Pays": "Region",
    "Nom": "Description",
    "CODE": "Name",
})

df["Type"] = df["Type"].map({"PtRep": "VRP"})
df["Ident"] = ""
df["MagneticDeclination"] = ""
df["Tags"] = ""

# df["Description"] = df["Description"].map(lambda s: '"' + s + '"')
df["VisibleFrom"] = 25 # NM
df["LastUpdateTimestamp"] = ""

df = df[["Type", "Name", "Ident", "Latitude", "Longitude", "Altitude", "MagneticDeclination", "Tags", "Description", "Region", "VisibleFrom", "LastUpdateTimestamp"]]
print(df)
df.to_csv("vrp_france_littlenavmap.csv", sep=",", index=False, header=False)
