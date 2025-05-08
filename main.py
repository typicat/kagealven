import pandas as pd


def main():
    df = pd.read_html(url)[0]
    df = df.fillna("")

    species_column = 2
    location_column = 10
    sum_art = df[species_column].value_counts()
    sum_loc = df[location_column].value_counts()

    print("Writing csv..")
    df.to_csv("output.csv", index=False, header=False)

    print(sum_art)
    print("-" * 35)
    print(sum_loc)
    print("Latest report:")

    latest_report = pd.DataFrame([df.iloc[0]])
    print(latest_report.to_string())


if __name__ == "__main__":
    url = "https://kagealven.com/fangstrapporter-aktuella"
    main()
