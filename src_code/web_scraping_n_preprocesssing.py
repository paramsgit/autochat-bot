#!/usr/bin/env python
# coding: utf-8

# In[1]:



# In[2]:


import wikipediaapi
import random
import time
import concurrent.futures
import requests
import re
import json
import os


# In[3]:


topic_dict2 = {
    "Health": ["Common diseases", "Global health statistics", "COVID-19", "Cancer", "Heart disease", "Diabetes", "Obesity"],
    "Environment": ["Global warming", "Endangered species", "Climate change", "Rainforests", "Pollution", "Biodiversity", "Natural disasters"],
    "Technology": ["Emerging technologies", "AI advancements", "Artificial intelligence", "Machine learning", "Space exploration", "Cybersecurity threats", "Blockchain technology"],
    "Economy": ["Wall Street Crash of 1929", "Stock market performance", "Job Markets", "2007–2008 financial crisis", "Unemployment rates", "Global trade agreements", "Cryptocurrencies", "Economic recession"],
    "Entertainment": ["Music Industry", "Popular cultural events", "Hollywood movies", "Music festivals", "Video streaming platforms", "Celebrities", "Award shows"],
    "Sports": ["Badminton", "Basketball", "Motorsport", "Football", "Cricket", "Olympic records"],
    "Politics": ["Presidential elections", "Foreign policy", "Democracy vs. Authoritarianism", "Political parties", "Human rights issues"],
    "Education": ["Online learning platforms", "STEM education", "School funding", "Educational reforms", "Digital classrooms"],
    "Travel": ["Tourism hotspots", "Airline industry challenges", "Adventure travel destinations", "Hotel chains", "Travel tips"],
    "Food": ["Food Power", "Famine", "Food Security", "Healthy eating", "Farm-to-table movement", "Fast food industry", "Global food distribution", "Veganism"]
}

topic_dict3 = {
                "Health": [
                    "Common diseases",
                    "Global health statistics",
                    "COVID-19",
                    "Cancer",
                    "Heart disease",
                    "Diabetes",
                    "Obesity",
                    "Mental health disorders",
                    "Vaccination controversies",
                    "Pandemics in history",
                    "Healthcare systems worldwide",
                    "Alternative medicine practices",
                    "Aging population challenges",
                    "Epidemiology",
                    "Nutrition and health",
                    "Antibiotic resistance",
                    "Health disparities",
                    "Genetic disorders",
                    "Public health policies",
                    "Maternal and child health",
                    "Healthcare innovations",
                    "Stress-related illnesses",
                    "Sleep disorders",
                    "Addiction and rehabilitation",
                    "Occupational health and safety",
                    "Rare diseases",
                    "Healthcare access and equity",
                    "Traditional medicine practices",
                    "Global mental health initiatives",
                    "Cultural influences on health"
                ],
                "Environment": [
                    "Global warming",
                    "Endangered species",
                    "Climate change",
                    "Rainforests",
                    "Pollution",
                    "Biodiversity",
                    "Natural disasters",
                    "Sustainable development goals",
                    "Renewable energy sources",
                    "Marine conservation",
                    "Environmental activism",
                    "Urbanization impacts on the environment",
                    "Waste management solutions",
                    "Deforestation",
                    "Water scarcity",
                    "Environmental policies worldwide",
                    "Conservation biology",
                    "Air quality monitoring",
                    "Green technology innovations",
                    "Ecological footprints",
                    "Ozone layer depletion",
                    "Wildlife trafficking",
                    "Land degradation",
                    "Carbon footprint reduction",
                    "Ocean acidification",
                    "Environmental justice movements",
                    "Ecosystem restoration",
                    "Greenhouse gas emissions",
                    "Ecotourism",
                    "Arctic melting"
                ],
                "Technology": [
                    "Emerging technologies",
                    "AI advancements",
                    "Artificial intelligence",
                    "Machine learning",
                    "Space exploration",
                    "Cybersecurity threats",
                    "Blockchain technology",
                    "Quantum computing",
                    "Internet of Things (IoT)",
                    "Augmented reality",
                    "Virtual reality",
                    "5G technology",
                    "Biotechnology",
                    "Robotics",
                    "Ethical implications of technology",
                    "Big data analytics",
                    "Autonomous vehicles",
                    "Smart cities",
                    "Digital privacy concerns",
                    "Technology in healthcare",
                    "Human-computer interaction",
                    "Tech startups and innovation hubs",
                    "Smart home devices",
                    "Tech in education",
                    "Nanotechnology",
                    "3D printing advancements",
                    "Future of work technologies",
                    "Telemedicine",
                    "Tech and environmental sustainability",
                    "Space tourism"
                ],
                "Economy": [
                    "Wall Street Crash of 1929",
                    "Stock market performance",
                    "Job Markets",
                    "2007–2008 financial crisis",
                    "Unemployment rates",
                    "Global trade agreements",
                    "Cryptocurrencies",
                    "Economic recession",
                    "Inflation and deflation",
                    "Global economic outlook",
                    "Consumer behavior trends",
                    "Monetary policies",
                    "Economic inequality",
                    "Fiscal policies",
                    "Labor market disruptions",
                    "Sustainable business practices",
                    "Debt crisis",
                    "Central banks and their roles",
                    "Corporate governance",
                    "Economic globalization",
                    "Entrepreneurship trends",
                    "Economic development strategies",
                    "Financial technology (FinTech)",
                    "Government stimulus packages",
                    "International monetary systems",
                    "Supply chain disruptions",
                    "Economic recovery plans",
                    "Microfinance initiatives",
                    "Economic forecasting",
                    "Economic sanctions"
                ],
                "Entertainment": [
                    "Music Industry",
                    "Popular cultural events",
                    "Hollywood movies",
                    "Music festivals",
                    "Video streaming platforms",
                    "Celebrities",
                    "Award shows",
                    "Television series",
                    "Gaming industry",
                    "Animation movies",
                    "Documentary filmmaking",
                    "Online content creation",
                    "Fan culture",
                    "Theatre productions",
                    "Entertainment marketing strategies",
                    "Cinematography techniques",
                    "Streaming wars",
                    "Film distribution methods",
                    "Reality TV trends",
                    "Music genres evolution",
                    "Influence of social media on entertainment",
                    "Film festivals",
                    "Art and entertainment collaborations",
                    "Entertainment law",
                    "Entertainment journalism",
                    "Live event experiences",
                    "Entertainment merchandising",
                    "Celebrity endorsements",
                    "Streaming platform algorithms"
                ],
                "Sports": [
                    "Badminton",
                    "Basketball",
                    "Motorsport",
                    "Football",
                    "Cricket",
                    "Olympic records",
                    "Baseball",
                    "Golf",
                    "Tennis",
                    "Athletics",
                    "Boxing",
                    "Rugby",
                    "Swimming",
                    "Wrestling",
                    "Equestrian sports",
                    "Martial arts",
                    "Winter sports",
                    "Extreme sports",
                    "Paralympic sports",
                    "Sports psychology",
                    "Sports medicine advancements",
                    "Youth sports development",
                    "Esports",
                    "Sports broadcasting",
                    "Athlete endorsements",
                    "Sports analytics",
                    "Sports sponsorships",
                    "Team management strategies",
                    "Sports facilities and infrastructure"
                ],
                "Politics": [
                    "Presidential elections",
                    "Foreign policy",
                    "Democracy vs. Authoritarianism",
                    "Political parties",
                    "Human rights issues",
                    "Geopolitical conflicts",
                    "Election interference",
                    "Political ideologies",
                    "Political campaign strategies",
                    "International relations",
                    "Political polarization",
                    "Government corruption",
                    "Civil liberties",
                    "Nationalism movements",
                    "Policy-making processes",
                    "Political activism",
                    "Civic engagement",
                    "Lobbying and interest groups",
                    "Voting systems",
                    "State sovereignty",
                    "Media's role in politics",
                    "Peacekeeping missions",
                    "War crimes",
                    "Political propaganda",
                    "Diplomatic negotiations",
                    "Political accountability",
                    "Youth involvement in politics",
                    "Freedom of speech debates",
                    "Political asylum policies",
                    "Political leadership styles"
                ],
              "Education": [
                    "Online learning platforms",
                    "STEM education",
                    "School funding",
                    "Educational reforms",
                    "Digital classrooms",
                    "Higher education trends",
                    "Education technology",
                    "Special education programs",
                    "Education policy analysis",
                    "Global learning disparities",
                    "Early childhood education",
                    "Education for sustainable development",
                    "Education equity initiatives",
                    "Teacher training programs",
                    "Innovative teaching methodologies",
                    "Education assessment methods",
                    "Adult education programs",
                    "Vocational training",
                    "Education for global citizenship",
                    "Learning analytics",
                    "Language learning technologies",
                    "Education and social mobility",
                    "Education and employment linkage",
                    "Education curriculum design",
                    "Education and mental health",
                    "Education data privacy",
                    "Educational leadership",
                    "Parental involvement in education",
                    "Education in marginalized communities",
                    "Lifelong learning initiatives"
                ],
                "Travel": [
                    "Tourism hotspots",
                    "Airline industry challenges",
                    "Adventure travel destinations",
                    "Hotel chains",
                    "Travel tips",
                    "Sustainable travel practices",
                    "Cultural immersion experiences",
                    "Solo travel adventures",
                    "Budget travel hacks",
                    "Ecotourism destinations",
                    "Travel technology innovations",
                    "Luxury travel trends",
                    "Backpacking trails",
                    "Responsible tourism initiatives",
                    "Volunteer travel opportunities",
                    "Family-friendly travel destinations",
                    "Heritage tourism sites",
                    "Off-the-beaten-path explorations",
                    "Food tourism experiences",
                    "Wellness retreats",
                    "Digital nomad lifestyle",
                    "Travel insurance insights",
                    "Airport innovations",
                    "Transportation advancements",
                    "Art and travel collaborations",
                    "Cruise industry trends",
                    "Local travel experiences",
                    "Tourist behavior analysis",
                    "Accessible travel options",
                    "Travel during global crises"
                ],
                "Food": [
                    "Food Power",
                    "Famine",
                    "Food Security",
                    "Healthy eating",
                    "Farm-to-table movement",
                    "Fast food industry",
                    "Global food distribution",
                    "Veganism",
                    "Organic food trends",
                    "Culinary tourism",
                    "Food cultures around the world",
                    "Slow food movement",
                    "Street food culture",
                    "Gastronomy and society",
                    "Food and identity",
                    "Food sovereignty",
                    "Sustainable agriculture",
                    "Food labeling and regulations",
                    "Food scarcity solutions",
                    "Functional foods",
                    "Food technology innovations",
                    "Food waste management",
                    "GMO debates",
                    "Urban farming initiatives",
                    "Food education programs",
                    "Traditional cuisines preservation",
                    "Food and health policies",
                    "Future of food production",
                    "Food and climate change",
                    "Food industry labor issues"
                ]
            }


# In[4]:


# Function to perform an initial search using MediaWiki API
def search_wikipedia(query, num_results=10):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srprop": "",
        "srlimit": num_results
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    try: 
        search_results = data["query"]["search"]
    except e:
        print(f"Error: Unable to retrieve search results for query: {query}")
        print(f"Error: {e}")
        return []
    
    return search_results


# In[5]:


def get_revision_id(page_title):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": page_title,
        "prop": "revisions",
        "rvprop": "ids",
        "format": "json"
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Extract revision ID from the API response
    page_id = next(iter(data["query"]["pages"]))
    revision_id = data["query"]["pages"][page_id]["revisions"][0]["revid"]
    
    return revision_id


# In[6]:


headers = {
        "User-Agent": "wiki_scraper_9000/3.0 (Contact: aggvatsal26@gmail.com) - web scraping for final project"
    }


# ## Saving the obtained documents into a JSON file

# In[7]:


# Save the topic_documents dictionary to a JSON file
def save_json_file(title, topic_documents):
    filename = title + ".json"
    with open(filename, 'w') as json_file:
        json.dump(topic_documents, json_file)

    print(f"Scraped documents saved to: {filename}")


# In[8]:


def fetch_documents(topic, keywords, num_documents=6000, min_summary_length=200):
    documents = []
    wiki_wiki = wikipediaapi.Wikipedia("en", headers=headers)

    start_t = time.time()
    st_point = 0
    retry_attempts = 3  # Number of times to retry on timeout or error
    timeout_multiplier = 2  # Multiplier to increase timeout on each retry

    while len(documents) < num_documents:
        for i in range(st_point, len(keywords)):
            num_results = int((num_documents) / len(keywords)) + 1
            
            # Retry mechanism for fetching search results
            search_results = None
            retry_count = 0
            while retry_count < retry_attempts and not search_results:
                try:
                    search_results = search_wikipedia(keywords[i], num_results)
                except (wikipediaapi.exceptions.HTTPTimeoutError, wikipediaapi.exceptions.PageError):
                    retry_count += 1
                    print("Timeout (main): {} secs", 2 * retry_count)
                    time.sleep(2 * retry_count)  # Exponential backoff for retries

            if not search_results and st_point < len(keywords):
                continue
            elif not search_results and st_point >= len(keywords):
                break
            else:
                print(f"Querying documents for {topic} with {keywords[i]}....")

            for result in search_results:
                if len(unique_titles) >= num_documents:
                    break

                retry_count = 0
                while retry_count < retry_attempts:
                    try:
                        #timeout = random.uniform(0, 2)
                        #time.sleep(timeout)
                        page = wiki_wiki.page(result["title"])
                        break
                    except (wikipediaapi.exceptions.HTTPTimeoutError, wikipediaapi.exceptions.PageError):
                        retry_count += 1
                        print("Timeout (sub): {} secs", 2 * retry_count)
                        time.sleep(2 * retry_count)

                if retry_count == retry_attempts:
                    continue  # Skip to the next page in case of retries exhausted

                if len(page.summary) > min_summary_length and page.title not in unique_titles:
                    document_info = {
                        "revision_id": get_revision_id(page.title),
                        "title": page.title,
                        "summary": page.summary,
                        "url": page.fullurl,
                        "topic": topic
                    }
                    documents.append(document_info)
                    unique_titles.add(page.title)

            if len(documents) % 200 == 0:
                print(f"{len(documents)} scraped from Wikipedia in time {(time.time() - start_t):.2f} secs")
                
            if not os.path.exists("./script_jsons_2/" + topic):
                os.makedirs("./script_jsons_2/" + topic)
            save_json_file("./script_jsons_2/" + topic + "/" + keywords[i], documents)

        if len(documents) < num_documents:
            st_point = len(keywords)
            random.seed(1729)
            for link_name in random.sample(page.links.keys(), 5):
                if link_name not in keywords:
                    keywords.append(link_name)

    return documents


# In[ ]:


# Create a dictionary to store documents for each topic
topic_documents = {}
unique_titles = set()

start_time = time.time()

# Create a dictionary to store documents for each topic
topic_documents = {}

random.seed(1729)

start_time = time.time()
i = 0
# Fetch documents for each topic
for topic, keywords in topic_dict3.items():
    if i >= 0: 
        documents = fetch_documents(topic, keywords)
        topic_documents[topic] = documents
        save_json_file("./script_jsons_2/" + topic, topic_documents)
    i += 1

print(f"Time taken to scrape all documents: {(time.time() - start_time):.2f} secs")


# In[ ]:


def is_alphanumeric(text):
    # Remove any whitespace from the text
    cleaned_text = text.replace(" ", "")
    
    # Check if the cleaned text is alphanumeric
    return cleaned_text.isalnum()


# In[ ]:


def preprocess_text(text):
    # Define a regular expression pattern to match non-alphanumeric characters
    # The pattern [^\w\s] matches any character that is not a word character (alphanumeric) or whitespace
    pattern = r'[^\w]'
    
    # Use the re.sub() function to replace matched characters with an empty string
    cleaned_text = re.sub(pattern, ' ', text)
    
    return cleaned_text


# ### Checking count of alphanumeric document

# In[ ]:


# Iterate through the list of dictionaries and check each summary
alphanumeric_doc_count = 0
count = 0
for key in topic_documents.keys():
    for document_info in topic_documents[key]:
        #print(document_info)
        document_info["summary"] = preprocess_text(document_info["summary"])
        #print(summary)
        
        if is_alphanumeric(document_info["summary"]):
            alphanumeric_doc_count += 1
        else:
            count += 1
            if count % 10 == 0:
                print("******* BREAKING PREMPTIVELY ********")

# Print the count of alphanumeric summaries
print(f"Number, Percentage of alphanumeric summaries: {alphanumeric_doc_count, (alphanumeric_doc_count/6000)*100}")


# In[ ]:


topic_documents


# ### Saving the JSON after preprocessing and replacing non-alphanumeric with whitespace using regex

# In[ ]:


filename = "wiki_documents_scraped_preprocessed.json"

with open(filename, 'w') as json_file:
    json.dump(topic_documents, json_file)

print(f"Scraped documents saved to: {filename}")


# In[ ]:




