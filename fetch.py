import requests

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/dnsdbfr/urlshortener/master/names.txt"
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        lst = r.text
        lst = lst.split("\n")
        lst = [x.strip() for x in lst if x.strip() != "" and not x.startswith("#")]
        _ = [print(x) for x in lst]
        exit(0)
    else:
        print("ERROR: Can not fetch the list")
        exit(1)
    # end if
# end main
