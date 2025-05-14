import pandas as pd

SPECIES_COLUMN = 2
LOCATION_COLUMN = 10

def main(url):
    print("kagealven v0.1.0 - fetching reports...")
    try:
        df = pd.read_html(url)[0]
    except Exception as e:
        print(f"Error fetching or parsing HTML: {e}")
        return

    df = df.fillna("")
    sum_art = df[SPECIES_COLUMN].value_counts()
    sum_loc = df[LOCATION_COLUMN].value_counts()

    df.to_csv("output.csv", index=False, header=False)
    print(sum_art)
    print("-" * 35)
    print(sum_loc)


if __name__ == "__main__":
    url = "https://kagealven.com/fangstrapporter-aktuella"
    main(url)
