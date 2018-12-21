import github as g
import pandas as pd
import datetime


def filter_repo(repo, fields):
    output = {}
    for field in fields:
       if field in repo:
           output[field] = repo[field]
    return output

def convert_date(date):
    return datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')

def filter_repos(repos, fields):
    output = []
    for repo in repos:
        output.append(filter_repo(repo, fields))
    return output

def github_main():
    fields = ['html_url', 'description', 'name', 'created_at']
    repos = g.get_repos('sm5art')
    filtered = filter_repos(repos, fields)
    df = pd.DataFrame(filtered)
    df['created_at'] = df['created_at'].apply(convert_date)
    df = df.dropna()
    df['type'] = 0
    return df

def inputs(typ):
    print("THIS PROMPT IS FOR %s" % typ)
    data = []
    continue_on = True
    while continue_on:
        year = input("Year?")
        month = input("Month?")
        day = input("Day?")
        name = input("summary of this event")
        description = input("description of this event")
        date = datetime.datetime(year=int(year), month=int(month), day=int(day))
        data.append({'html_url': None, 'description': description, 'name': name, 'created_at': date})
        yes_no = input('more? n to leave')
        if yes_no[0] == 'n':
            continue_on = False
    return pd.DataFrame(data)

            


def work_main():
    df = inputs("WORK")
    df['type'] = 1
    return df

def education_main():
    df = inputs("EDUCATION")
    df['type'] = 2
    return df

def main():
    education = education_main()
    work = work_main()
    github = github_main()
    df = pd.concat([education, work, github])
    df.to_csv('output.csv')


    


if __name__ == "__main__":
    main()