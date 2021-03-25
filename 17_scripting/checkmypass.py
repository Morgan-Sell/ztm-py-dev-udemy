import requests
import hashlib
import sys


"""
NOTES:
-----
- "requests" module allows me to manually request something as if I was using a browser.
- Response 400 means something is wrong, e.g. unauthorized
- Want a response of 200
- Hasihing is a one-way algorithm
- K-anonymity allows somebody to receive information about me still not know who I am.
  ** It works by only provided the first 5 characters of the hash password

- Hash function is a function that generates a fixed-length value for each input that the function receives.
- A hash function is idempotent.
  ** Idempotent means the function will always return the same output for a given input.

- "haslib" module allows program to perform SHA hashing

"""




def request_api_data(query_char):
  url = "https://api.pwnedpasswords.com/range/" + query_char
  res = requests.get(url)
  
  if res.status_code != 200:
    raise RuntimeError(f"Error fetching: {res.status_code}. Check the API and try again.")
  return res


def get_password_leaks_count(hashes, hash_to_check):
  # ".text" returns all the hashes and their counts
  hashes = (line.split(":") for line in hashes.text.splitlines())
  # hashes is now a generator variable
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  # check if password exists in API response
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)


def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f"{password} was found {count} times... you should probably change your password.")
    else:
      print(f"{password} was NOT found. Carry on!")
    
  return "Done!"


if __name__ == "__main__":
  main(sys.argv[1:])