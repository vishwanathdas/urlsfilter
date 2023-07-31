from urllib.parse import urlparse

def extract_domain_and_link(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme != 'https':
        return None, None

    path_parts = parsed_url.path.split('/')
    if path_parts[-1].lower() in ('about-us', 'aboutus'):
        path_parts.pop()
    company_link = f"{parsed_url.scheme}://{parsed_url.netloc}/{'/'.join(path_parts)}/"
    domain_link = f"{parsed_url.scheme}://{parsed_url.netloc}/"
    return domain_link, company_link

# Test examples
input_urls = [
    "https://www.rncos.com/about-us.htm",
    "https://www.abcd.com/delhi/xyz/about-us"
]

for url in input_urls:
    domain, company_link = extract_domain_and_link(url)
    if domain and company_link:
        print(f"Input: {url}")
        print(f"Output - Domain: {domain}")
        print(f"Output - Company Link: {company_link}")
        print()
