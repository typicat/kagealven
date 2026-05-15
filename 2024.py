import pandas as pd
from io import StringIO
from urllib.request import Request, urlopen


FIREFOX_USER_AGENT = (
	"Mozilla/5.0 (X11; Linux x86_64; rv:138.0) "
	"Gecko/20100101 Firefox/138.0"
)


def fetch_html_with_firefox_ua(url: str) -> str:
	request = Request(url, headers={"User-Agent": FIREFOX_USER_AGENT})
	with urlopen(request, timeout=30) as response:
		return response.read().decode("utf-8", errors="replace")


url = "https://kagealven.com/2025/02/2024/"
html = fetch_html_with_firefox_ua(url)
df = pd.read_html(StringIO(html))[0]
df.to_csv("output_2024.csv", index=False, header=False, na_rep="")
