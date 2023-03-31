# URLSHORTENER
A curated list of URL Shortener Websites with responses for crawling

## Use Case

If you are writing a crawler or any kind of system that detecting a URL shortener is important,
then this list can help you!

## Description of the files

- names.txt

This file contains only the registered domain name for the URL shortener. The list **ONLY** contains the destination
URL not the website itself. For example, _bitly.com_ is the name of the Bitly website while the shortened URLs are 
in a form of bit.ly/blahblah. So we have only bit.ly domain in our list not bitly.com

I try to constantly update the list. If a domain name in the list has no "A" record or the website is down,
I will remove it from the list. However, if it's marked as malicious by Google safe browsing service, we still
keep it in the list.

Here is the link to automatically fetch the names list:
[https://raw.githubusercontent.com/dnsdbfr/urlshortener/master/names.txt](https://raw.githubusercontent.com/dnsdbfr/urlshortener/master/names.txt)

Here is an example in Python3 for getting the list of domain names: [fetch.py](./fetch.py)

- test/test.py

We run this file from time to time to filter out those domains in the list that already expired, or return NXDOMAIN.
Use the following command to run it.

```
cd test
python3 test.py ../names.txt | grep -v "NOERROR"
```

### No duplicate entry

Run this in bash
```bash
cat names.txt | sort | uniq -c | grep -E '\S*1.*' -v
```

