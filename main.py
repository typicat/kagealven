import pandas as pd

SPECIES_COLUMN = 2
LOCATION_COLUMN = 10

def main(url):
    print("kagealven v0.1.1 - hämtar rapporter...")
    try:
        df = pd.read_html(url)[0]
    except Exception as e:
        print(f"Error fetching or parsing HTML: {e}")
        return

    df = df.fillna("")
    sum_art = df[SPECIES_COLUMN].value_counts()
    sum_loc = df[LOCATION_COLUMN].value_counts()

    df.to_csv("output.csv", index=False, header=False)
    print("Arter:")
    for species, count in sum_art.items():
        print(f"{species}: {count}")
    print("-" * 35)
    print("Platser:")
    for location, count in sum_loc.items():
        print(f"{location}: {count}")
    print("-" * 35)
    print("Senaste 3:")
    for i, row in df.head(3).iterrows():
        print(" ".join(str(x) for x in row))


if __name__ == "__main__":
    url = "https://kagealven.com/fangstrapporter-aktuella"
    main(url)
