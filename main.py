import pandas as pd


def main():
    print("Fetching reports..")
    data = pd.read_html(url)
    df = data[0]
    df = df.fillna('')
    print("Writing csv..")
    df.to_csv('output.csv', index=False, header=False)
    sum_art = df[2].value_counts()
    sum_loc = df[10].value_counts()
    print(sum_art)
    print("-" * 35)
    print(sum_loc)


if __name__ == "__main__":
    url = "https://kagealven.com/fangstrapporter-aktuella"
    main()
