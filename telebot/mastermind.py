import urllib.request, json


def get_response(user_input):
    url = "https://api.covid19api.com/summary"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    for i in range(len(data['Countries'])):
        key,value = list(data['Countries'][i].items())[0]
        if value==user_input:
            x=data['Countries'][i]
            tmpstring = ""
            for key, value in x.items():
                tmpstring = tmpstring + "{0:<20} {1}".format(key, value) + "\n"
            return tmpstring

