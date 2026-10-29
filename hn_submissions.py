import requests
from operator import itemgetter
import plotly.express as px

# Make an API call and check the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:5]:

    # Make a new API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    try:
        # Build a dictionary for each article
        submission_dict = {
            "title": response_dict["title"],
            "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
            "comments": response_dict["descendants"],
        }
        submission_dicts.append(submission_dict)

    except KeyError:
        continue

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

submission_link, submission_comments = [], []

for submission_dict in submission_dicts:
    submission_link.append(
        f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    )
    submission_comments.append(submission_dict["comments"])

    # print(f"\nTitle: {submission_dict['title']}")
    # print(f"Discussion link:{submission_dict['hn_link']}")
    # print(f"Comments:{submission_dict['comments']}")

labels = {"x": "Submission", "y": "Comments"}
fig = px.bar(x=submission_link, y=submission_comments, labels=labels)
fig.show()
