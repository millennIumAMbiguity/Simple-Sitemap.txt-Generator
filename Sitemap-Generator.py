import os
import glob
import sys

class SitemapGenFromURLs:
    def generate(self, urls):
        # Implement the logic for generating the sitemap XML from URLs.
        # This is a placeholder since the actual implementation depends on your requirements.
        xml_content = []
        for url in urls:
            xml_content.append(url)  # Example XML content
        return xml_content

if __name__ == "__main__":
    print("Simple Sitemap Generator")

    if len(sys.argv) != 3:
        print("Usage: python script.py folder-with-html-output website-url")
        sys.exit()

    path = sys.argv[1]
    base_url = sys.argv[2]

    # Ensure base URL ends with a slash
    if not base_url.endswith('/'):
        base_url += '/'

    urls = [base_url + "index.html"]

    count = 0

    for file_path in glob.glob(os.path.join(path, "html", "*.htm")):
        file = file_path.replace(os.path.join(path, "html"), "").replace(os.sep, "")
        urls.append(base_url + "html/" + file)
        count += 1

    gen = SitemapGenFromURLs()
    xml = gen.generate(urls)

    with open(os.path.join(path, "sitemap.txt"), "w") as file:
        for line in xml:
            file.write(line + "\n")

    print(f"Generated sitemap.txt with {count} URLs")
