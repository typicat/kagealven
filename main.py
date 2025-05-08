import pandas as pd


def main():
    df = pd.read_html(url)[0]
    df = df.fillna('')

    species_column = 2
    location_column = 10
    sum_art = df[species_column].value_counts()
    sum_loc = df[location_column].value_counts()

    print("Writing csv..")
    df.to_csv('output.csv', index=False, header=False)

    print(sum_art)
    print("-" * 35)
    print(sum_loc)
    print("Latest report:")

    latest_report = pd.DataFrame([df.iloc[0]])  # Convert the top row to a dataframe
    print(latest_report.to_string())

    # You can now access specific values from the top row like this:
    #print("\nSpecific values from latest report:")
    #for column in latest_report.columns:
    #    print(f"{column}: {latest_report.iloc[0][column]}")


if __name__ == "__main__":
    url = "https://kagealven.com/fangstrapporter-aktuella"
    main()
