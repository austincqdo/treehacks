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
    response = requests.get("https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators?address=" + address + "&level=STATE_EXEC", headers=headers)
    #response = requests.get("https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators?address=450+Serra+Mall,+Stanford,+CA+94305&level=NATIONAL_UPPER", headers=headers)

    # Print the status code of the response.
    #print(response.status_code)
    parsed = json.loads(response.content.decode())
    #print(json.dumps(parsed, indent=4, sort_keys=True))
    num = 0;
    for items in parsed['officials']:
        key = "Candidate" + str(num)
        data.update({key: {}})
        #print(items[])
        data[key].update({"First Name" : items["first_name"]})
        data[key].update({"Last Name" : items["last_name"]})
        data[key].update({"Party" : items["party"]})
        print(items["emails"])
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
        #print(items["bio"])
        if not items["bio"]: #if empty
            #print("Bio: None", file=text_file)
            data[key].update({"Bio" : "None"})

        else:

            data[key].update({"Bio" : items["bio"][0]})
        num += 1
        #print("First Name: " +  items["first_name"], file=text_file)
        #print("Last Name: " + items["last_name"], file=text_file)
        #print("Party: " + items["party"], file=text_file)
        #if not items["emails"]:
        #    print("Emails: None", file=text_file)
        #else:
        #    for elem in items["emails"]:
        #        print("Emails" + elem, file=text_file)
        # print("Office: " + items["office_details"]["position"], file=text_file)
        # print("Addresses: " + "\n" + items["office_location"]["address_1"], file=text_file)
        # print(items["office_location"]["address_2"], file=text_file)
        # print(items["office_location"]["address_3"], file=text_file)
        # print(items["office_location"]["city"], file=text_file)
        # print(items["office_location"]["state"], file=text_file)
        # for social in items["socials"]:
        #     if social["identifier_type"] == "TWITTER":
        #         print("Twitter Handle: " + social["identifier_value"], file=text_file)
        # print("\n", file=text_file)
        # if not items["bio"]:
        #     print("Bio: None", file=text_file)
        # else:
        #     for elem in items["emails"]:
        #         print("Bio" + elem, file=text_file)
        # print("\n", file=text_file)
        # print("\n", file=text_file)

    return data






# with open("Output.txt", "w") as text_file:
#     #print(f"Purchase Amount: {TotalAmount}", file=text_file)
#     for items in parsed['officials']:
#         #print(items[])
#         print("First Name: " +  items["first_name"], file=text_file)
#         print("Last Name: " + items["last_name"], file=text_file)
#         print("Party: " + items["party"], file=text_file)
#         if not items["emails"]:
#             print("Emails: None", file=text_file)
#         else:
#             for elem in items["emails"]:
#                 print("Emails" + elem, file=text_file)
#         print("Office: " + items["office_details"]["position"], file=text_file)
#         print("Addresses: " + "\n" + items["office_location"]["address_1"], file=text_file)
#         print(items["office_location"]["address_2"], file=text_file)
#         print(items["office_location"]["address_3"], file=text_file)
#         print(items["office_location"]["city"], file=text_file)
#         print(items["office_location"]["state"], file=text_file)
#         for social in items["socials"]:
#             if social["identifier_type"] == "TWITTER":
#                 print("Twitter Handle: " + social["identifier_value"], file=text_file)
#         print("\n", file=text_file)
#         if not items["bio"]:
#             print("Bio: None", file=text_file)
#         else:
#             for elem in items["emails"]:
#                 print("Bio" + elem, file=text_file)
#         print("\n", file=text_file)
#         print("\n", file=text_file)







# for items in parsed['officials']:
#     #print(items[])
#     print("First Name: " + items["first_name"])
#     print("Last Name: " + items["last_name"])
#     print("Party: " + items["party"])
#     print("Emails: ")
#     for elem in items["emails"]:
#         print(elem)
#     print("Office: " + items["office_details"]["position"])
#     print("Addresses: " + "\n" + items["office_location"]["address_1"])
#     print(items["office_location"]["address_2"])
#     print(items["office_location"]["address_3"])
#     print(items["office_location"]["city"])
#     print(items["office_location"]["state"])
#     for social in items["socials"]:
#         if social["identifier_type"] == "TWITTER":
#             print("Twitter Handle: " + social["identifier_value"])
#     print("\n")
#     print("Bio: ")
#     for elem in items["bio"]:
#         print(elem)
#     print("\n")
#     print("\n")
