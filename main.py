import pandas as pd

SPECIES_COLUMN = 2
LOCATION_COLUMN = 10


def print_counts(title: str, counts: pd.Series) -> None:
    print(f"\033[34m{title}:\033[0m")
    for item, count in counts.items():
        print(f"{item}: {count}")


def main(url: str) -> None:
    print("kagealven v0.1.1 - hämtar rapporter...")
    try:
        df = pd.read_html(url)[0]
    except Exception as e:
        print(f"Error fetching or parsing HTML: {e}")
        return

    if df.empty:
        print("No data found.")
        return

    df = df.fillna("")
    species_counts = df.iloc[:, SPECIES_COLUMN].value_counts()
    location_counts = df.iloc[:, LOCATION_COLUMN].value_counts()

    df.to_csv("output.csv", index=False, header=False)
    print_counts("Arter", species_counts)
    print_counts("Platser", location_counts)
    print("\033[32mSenaste 3:\033[0m")
    # Print the latest 3 rows, newest first
    for row in df.head(3).itertuples(index=False):
        print(" ".join(str(x) for x in row))


if __name__ == "__main__":
    url = "https://kagealven.com/fangstrapporter-aktuella"
    main(url)
