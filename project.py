import requests
import json
import io
import sys
import re


def test():
    print("hello")
def output_data(location):
    data = {}
    headers = {
        'X-API-Key': '2e1uvo7yeX50ZGHvctPxi8ZWubhggyOydIWvOa5c'
    }
    input_words = re.compile('\w+').findall(location)

    address = ''
    for i in range(len(input_words)):
        if (i == len(input_words)-1):
            address += input_words[i]
        else:
            address += input_words[i] + "+"

#450+Serra+Mall,+Stanford,+CA+94305
    response = requests.get("https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators?address=" + address + "", headers=headers)
    #response = requests.get("https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators?address=450+Serra+Mall,+Stanford,+CA+94305&level=NATIONAL_UPPER", headers=headers)

    # Print the status code of the response.
    parsed = json.loads(response.content.decode())
    num = 0;
    for items in parsed['officials']:
        key = "Candidate" + str(num)
        data.update({key: {}})
        data[key].update({"First Name" : items["first_name"]})
        data[key].update({"Last Name" : items["last_name"]})
        data[key].update({"Party" : items["party"]})
        if not items["emails"]: #if empty
            data[key].update({"Emails" : "None"})

        else:
            for elem in items["emails"]:
                data[key].update({"Emails" + elem: "None"})
        data[key].update({"Office" : items["office_details"]["position"]})
        data[key].update({"Addresses" : [items["office_location"]["address_1"],items["office_location"]["address_2"],items["office_location"]["address_1"]]})
        data[key].update({"City" : items["office_location"]["city"]})
        data[key].update({"State" : items["office_location"]["state"]})
        for social in items["socials"]:
            if social["identifier_type"] == "TWITTER":
                data[key].update({"Twitter" : social["identifier_value"]})
        if not items["bio"]: #if empty
            data[key].update({"Bio" : "None"})

        else:

            data[key].update({"Bio" : items["bio"][0]})
        num += 1
    return data