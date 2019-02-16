from bs4 import BeautifulSoup
import requests
import sys

#page_link = "http://www.ontheissues.org/CA/Dana_Rohrabacher_Abortion.htm"
def get_votes():
	page_link = "http://www.ontheissues.org/CA/" + sys.argv[1] + "_" + sys.argv[2] + "_" + sys.argv[3] + ".htm"
	page_response = requests.get(page_link, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")
	page_string_list = page_content.get_text().split()
	voted_list = []
	for i in range(len(page_string_list)):
		if page_string_list[i] == "Voted":
			voted = ""
			while page_string_list[i].endswith(".") == False:
				voted += page_string_list[i] + " "
				if i == len(page_string_list) - 1:
					break
				i += 1
			voted += page_string_list[i]
			voted_list.append(voted)
	for statement in voted_list:
		print(statement + "\n")


if __name__ == '__main__':
  get_votes()