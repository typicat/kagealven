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
    print("kagealven v0.1.1\n\nHämtar rapporter...")
    try:
        html = fetch_html_with_firefox_ua(url)
        df = pd.read_html(StringIO(html))[0]
    except Exception as e:
        print(f"Error fetching or parsing HTML: {e}")
        return

    if df.empty:
        print("No data found.")
        return

    df = df.fillna("")
    species_counts = df.iloc[:, SPECIES_COLUMN].value_counts()
    location_counts = df.iloc[:, LOCATION_COLUMN].value_counts()

    current_year = datetime.now().year
    output_filename = f"output_{current_year}.csv"
    df.to_csv(output_filename, index=False, header=False)
    print_counts("Arter", species_counts)
    print()
    print_counts("Platser", location_counts)
    print()
    print("\033[32mSenaste 3:\033[0m")
    # Print the latest 3 rows, newest first
    for i, row in enumerate(df.head(3).itertuples(index=False), 1):
        row_data = [str(x) for x in row]
        name = row_data[0] if len(row_data) > 0 else ""
        date = row_data[1] if len(row_data) > 1 else ""
        species = row_data[2] if len(row_data) > 2 else ""
        weight = row_data[8] if len(row_data) > 8 else ""
        location = row_data[10] if len(row_data) > 10 else ""

        print(f"{i}. {name:<15} {date:<12} {species:<8} {weight:<8} {location}")


if __name__ == "__main__":
    url = "https://kagealven.com/fangstrapporter-aktuella"
    main(url)
