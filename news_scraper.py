from newsapi import NewsApiClient
from operator import itemgetter
import csv

newsapi = NewsApiClient(api_key="ee1bf85ed47f48dd8f89da2c29c7b02b")

#populates source list, don't run unless needed
#sources = newsapi.get_sources(country='us')
#source_list = list(map(itemgetter('name'), sources['sources']))

#with open('data/source_list.csv','w') as result_file:
#    wr = csv.writer(result_file, dialect='excel')
#    wr.writerows(source_list)

#not needed - save some API calls
#headlines = newsapi.get_top_headlines(q='covid',
#                                      language='en',
#                                      country='us')

with open ('data/source_list.csv', newline='') as f:
    reader = csv.reader(f)
    read_list = list(reader)

source_list = []
for string in read_list:
    source_list.append(''.join(string))

article_list, content_list = ([], ) * 2
for source in source_list:
    try:
        all = newsapi.get_everything(q='covid',
                                        sources=source,
                                         language='en',
                                         from_param='2020-04-01',
                                         to='2020-04-10',
                                         sort_by='relevancy')
        #article_list.append(str(map(itemgetter('title'), all['articles'])))
        #content_list.append(str(map(itemgetter('content'), all['articles'])))
    except:
        print(source+' unavailable in selected range')

with open('data/article_data.csv','w') as data_file:
    wr = csv.writer(data_file)
    wr.writerows(all['articles'])
