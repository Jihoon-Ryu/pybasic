"""/////import & def/////"""

import requests 
from bs4 import BeautifulSoup

"""max job elements in one page"""   
LIMIT = 50  

INDEED_URL = f"https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch"


"""/////return max_page/////"""

def max_indeed_pages():

 result = requests.get(INDEED_URL)

 soup = BeautifulSoup(result.text, "html.parser")

 pagination = soup.find("div", {"class":"pagination"})

 links = pagination.find_all('a')

 pages = []

 for link in links[:-1]:
  pages.append(int(link.string))

 max_page = pages[-1]  

 return max_page

"""/////extract jobs/////"""

def extract_indeed_jobs(max_page):
    jobs= []

    """set URL of each page in requests, soup way 리겟텍뷰파""" 
    for page in range(max_page):
       result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")

       soup = BeautifulSoup(result.text, "html.parser")
    
       """get title"""
       results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
       
       
       for result in results:
        title=result.find("h2", {"class":"title"}).find("a")["title"]
        
        """get company"""
        company= result.find("span", {"class":"company"})
           
        company_anchor = company.find("a") 
         
        if company_anchor is not None:
         company= (str(company.find("a").string))
        else:
         company= (str(company.string))  
         
        company=company.strip()       

        job ={"title": title, "company": company}
        print(job)