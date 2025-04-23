import pandas as pd


def main():
    print("Fetching reports..")
    data = pd.read_html(url)
    df = data[0]
    df = df.fillna('')
    print("Writing csv..")
    df.to_csv('output.csv', index=False, header=False)
    sum = df[2].value_counts()
    print(sum)


if __name__ == "__main__":
    url = "https://kagealven.com/fangstrapporter-aktuella"
    main()
