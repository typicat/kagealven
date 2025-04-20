import pandas as pd


def stats():
    # TODO:
    # count species
    # summary catch of each specie
    print("Done! ")


def main():
    print("Fetching reports..")
    data = pd.read_html(url)
    df = data[0]
    df = df.fillna('')
    df.to_csv('output.csv', index=False, header=False)
    stats()


if __name__ == "__main__":
    url = "https://kagealven.com/fangstrapporter-aktuella"
    main()
