#!/usr/bin/env python
import requests 
from pathlib import Path
from bs4 import BeautifulSoup, Tag
import sys 
import time
from urllib.error import HTTPError

def submit(token,problem,language,path_to_code):
    # print(problem,path_to_code)
    
    base_url = 'https://dmoj.ca'
    
    
    try:
        code = open(Path(path_to_code)).read()
    except Exception:
        raise 
    
    headers = {'Authorization':f'Bearer {token}'}
    doc = requests.get(base_url+'/user',headers=headers)
    try:
        doc.raise_for_status()
    except HTTPError:
        print('Invalid Authorization Token.')
        sys.exit()
    
    submit_url = f'{base_url}/problem/{problem}/submit'
    
    problem_get = requests.get(submit_url,headers=headers)
    try:
        problem_get.raise_for_status()
    except Exception:
        print('Invalid Problem Code.')
        sys.exit()
    
    soup = BeautifulSoup(problem_get.text,'html.parser')
    
    problem_id = soup.find(id='id_problem')['value']
    languages = {option['data-name'].lower().replace(' ',''):option['data-id'] for option in soup.find(id='id_language').find_all('option')}
    
    submission = requests.post(submit_url,headers=headers,data={'problem':problem_id,'source':code,'language':languages[language.lower()]},allow_redirects=True)
    
    #wew at least web uses forwardslash
    submission_num = submission.url.split('/')[-1]
    
    print('\nExecution Results:')
    
    while True:
        submission = requests.get(f'{base_url}/widgets/single_submission?id={submission_num}',headers=headers)
        
        soup1 = BeautifulSoup(submission.text,'html.parser')
        print(soup1.find(class_='status')['title'],end='')
        
        if all(x not in soup1.find(class_='status').text for x in ['G','P']):
            print(':\n')
            testcases = requests.get(f'{base_url}/widgets/submission_testcases?id={submission_num}',headers=headers)
            soup2 = BeautifulSoup(testcases.text,'html.parser')
            cases = soup2.find_all('table')
            for case in cases:
                if case.findPrevious('b'):
                    print(case.findPrevious('b').text)
                batch = list(case.find_all('tr')) 
                for row in batch:
                    print(' '.join([' '.join(x.text.split()) if type(x)==Tag else ''.join(x.split()) for x in row]))
                    
            print(f'{"-"*10}\nStatus: {soup1.find(class_="status")["title"]}')
            print(f'Memory: {soup1.find(class_="memory").text}')
            print(f'Time: {soup1.find(class_="sub-usage").find(class_="time").text.split()[-1]}')
            
            break
        print('...')
        
        time.sleep(1)
        
    
if __name__ == '__main__':
    if len(sys.argv)==1:
        # show the help
        print("helpful help message.")
        pass
    else:
        # submit to problem
        try:
            f = open('../token','r+')
        except FileNotFoundError:
            print("Token file does not exist! Please ensure that your token is configured with `configure` or `-c`")
            open('../token','w+')
            sys.exit(1)
        
        submit(f.read(),sys.argv[1],sys.argv[2],sys.argv[3])