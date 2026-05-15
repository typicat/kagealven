import pandas as pd
from io import StringIO
from datetime import datetime
from urllib.request import Request, urlopen

SPECIES_COLUMN = 2
LOCATION_COLUMN = 10
FIREFOX_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64; rv:138.0) "
    "Gecko/20100101 Firefox/138.0"
)


def fetch_html_with_firefox_ua(url: str) -> str:
    request = Request(url, headers={"User-Agent": FIREFOX_USER_AGENT})
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def print_counts(title: str, counts: pd.Series) -> None:
    print(f"\033[34m{title}\033[0m")
    for item, count in counts.items():
        print(f"{item:<15} {count}")


def main(url: str) -> None:
    ver = "0.1.2"
    print(f"kagealven v{ver}\n\nHämtar rapporter...")
    try:
        html = fetch_html_with_firefox_ua(url)
        df = pd.read_html(StringIO(html))[0]
    except Exception as e:
        print(f"Error fetching or parsing HTML: {e}")
        return

    if df.empty:
        print("No data found.")
        return

    species_counts = df.iloc[:, SPECIES_COLUMN].dropna().astype(str).value_counts()
    location_counts = df.iloc[:, LOCATION_COLUMN].dropna().astype(str).value_counts()

    current_year = datetime.now().year
    output_filename = f"output_{current_year}.csv"
    # Avoid creating a full copied DataFrame just to replace NaN when writing CSV.
    df.to_csv(output_filename, index=False, header=False, na_rep="")
    print_counts("Arter", species_counts)
    print()
    print_counts("Platser", location_counts)
    print()
    print("\033[32mSenaste 3:\033[0m")
    # Print the latest 3 rows, newest first
    for i, row in enumerate(df.head(3).itertuples(index=False, name=None), 1):
        name = "" if len(row) <= 0 or pd.isna(row[0]) else str(row[0])
        date = "" if len(row) <= 1 or pd.isna(row[1]) else str(row[1])
        species = "" if len(row) <= 2 or pd.isna(row[2]) else str(row[2])
        weight = "" if len(row) <= 8 or pd.isna(row[8]) else str(row[8])
        location = "" if len(row) <= 10 or pd.isna(row[10]) else str(row[10])

        print(f"{i}. {name:<15} {date:<12} {species:<8} {weight:<8} {location}")


if __name__ == "__main__":
    url = "https://kagealven.com/fangstrapporter-aktuella"
    main(url)
