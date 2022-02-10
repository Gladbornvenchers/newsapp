from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def index(request):
    newsApi = NewsApiClient(api_key = 'd1f4f1e59ddf44738428df7d8b584d22')
    headlines = newsApi.get_top_headlines(sources= 'bbc-news, cnn, the-next-web')
    articles = headlines['articles']
    desc = []
    news = []
    img = []


    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])

    mylist = zip(news, desc, img)


    return render(request, "main/index.html", context={"mylist": mylist})

