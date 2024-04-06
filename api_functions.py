import requests

def rhyme(string):
    url = "http://ping.skarj.pl/rhyme"
    payload = {"string": string}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        return response.json()["output"]
    else:
        return (f"Error: {response.status_code}")
    

def define(word):
    url = "http://ping.skarj.pl/define"
    payload = {"string": word}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        definition = response.json()["output"]
        return(definition)
    else:
        return(f"Error: {response.status_code}")


def antonym(word):
    url = "http://ping.skarj.pl/antonym"
    payload = {"string": word}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        antonym = response.json()["output"]
        return (antonym)
    else:
        return (f"Error: {response.status_code}")


def synonym(word):
    url = "http://ping.skarj.pl/synonym"
    payload = {"string": word}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        synonym = response.json()["output"]
        print(synonym)
    else:
        print(f"Error: {response.status_code}")



def joke(topic):
    url = "http://ping.skarj.pl/joke"
    payload = {"string": topic}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        joke = response.json()["output"]
        return(joke)
    else:
        return(f"Error: {response.status_code}")
    
def owo(text):
    text = "Hello, how are you?"
    url = "http://ping.skarj.pl/owo"
    payload = {"string": text}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        owo_text = response.json()["output"]
        return(owo_text)
    else:
        return(f"Error: {response.status_code}")

def celebrity(celebrity_name):
    url = "http://ping.skarj.pl/celebrity"
    payload = {"string": celebrity_name}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        celebrity_info = response.json()["output"]
        return(celebrity_info)
    else:
        return(f"Error: {response.status_code}")


def anime(genres):
    url = "http://ping.skarj.pl/anime_suggestion"
    payload = {"string": genres}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        anime_suggestion = response.json()["output"]
        return(anime_suggestion)
    else:
        return(f"Error: {response.status_code}")

def adjective(subject):
    url = "http://ping.skarj.pl/adjective"
    payload = {"string": subject}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        adjective = response.json()["output"]
        return(adjective)
    else:
        return(f"Error: {response.status_code}")

def pickup_line(topic):
    url = "http://ping.skarj.pl/pickupLine"
    payload = {"string": topic}

    response = requests.get(url, params=payload)
    if response.status_code == 200:
        pickup_line = response.json()["output"]
        return(pickup_line)
    else:
        return(f"Error: {response.status_code}")


def astrologer(name,age,sign):
    person_info = name+' '+age+' '+sign
    print(person_info)
    url = "http://ping.skarj.pl/astrologer"
    payload = {"string": person_info}

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        prediction = response.json()["output"]
        return(prediction)
    else:
        return(f"Error: {response.status_code}")
    
# print(pickup_line("global variable"))