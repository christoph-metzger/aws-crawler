import requests
from lxml import html


class SueddeutscheArticle(object):

    attributes = {
        'headline': '//section[@class="header"]/h2/strong/following-sibling::text()[1]',
        'sub_headline': '//section[@class="header"]/h2/strong/text()[1]',
	'body': '//section[@id="article-body"]/p//text()',
    }

    def __init__(self, sueddeutsche_url):
        html_code = requests.get(sueddeutsche_url).text
        self.dom = html.fromstring(html_code)

    def __getattr__(self, attr):
        xpath = self.attributes[attr]
        elements = self.dom.xpath(xpath)
        return self.clean(elements)

    def clean(self, elements):
        stripped = map(lambda x: x.strip(), elements)
        replaced = map(lambda x: x.replace(u"\xa0", " "), stripped)
        return "".join(replaced)
