# INF601 - Advanced Programming in Python
# Antonio Hernandez
# Mini Project 3


# Proper import of packages used.
import requests

url = "https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup"  # Utelly API

'''
idlookup provides where you can watch the show
            source_id - mandatory parameter to search
            source - mandatory parameter that specifies the id value (IMDb, TMDb, etc)
            country - optional parameter that only shows services in given country
lookup provides where you can watch with partial name
            term - optional parameter to search
            country - optional parameter which returns services only in that country
'''



# Movie example given
querystring = {"term": "bojack", "country": "uk"}

headers = {
    "X-RapidAPI-Key": "4231ae9c48msh60f86763911ba59p12e3f8jsnba5b28340ad0",
    "X-RapidAPI-Host": "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
'''
what it provides:
url:"https://www.imdb.com/title/tt3398228"
id:"tt3398228"
id:"5d914028302b840050acbe62"
weight:5631
picture:"https://utellyassets9-4.imgix.net/api/Images/4e4d50a0040fd4500193202edbafce6a/Redirect?fit=crop&auto=compress&crop=faces,top"
name:"BoJack Horseman"
status_code:200
type:"imdb"
'''



# Need to connect it to base - model

# Search up feature


