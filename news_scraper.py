from newsapi import NewsApiClient
from operator import itemgetter

newsapi = NewsApiClient(api_key="ee1bf85ed47f48dd8f89da2c29c7b02b")

sources = newsapi.get_sources(country='us')
source_list = list(map(itemgetter('name'), sources['sources']))

headlines = newsapi.get_top_headlines(q='covid',
                                      language='en',
                                      country='us')

article_list, content_list = ([], ) * 2
for source in source_list:
    try:
        all = newsapi.get_everything(q='covid',
                                        sources=source,
                                         language='en',
                                         from_param='2020-04-01',
                                         to='2020-04-10',
                                         sort_by='relevancy')
        article_list.append(str(map(itemgetter('title'), all['articles'])))
        content_list.append(str(map(itemgetter('content'), all['articles'])))
    except:
        print(source+' unavailable in selected range')

article_dict = {article_list[i]: content_list[i] for i in range(len(article_list))}

print(article_dict)
