import os
import urllib.request

UD_RELEASE = "2.3"

def check_fce():
    try:
        code = os.stat("fce-released-dataset/license").st_size
        return code
    except OSError:
        print('''Error: FCE folder 'fce-released-dataset' not in the current directory.
Please download the dataset from https://www.ilexir.co.uk/datasets/index.html
and unzip the file in the current directory.''')
        return 0


def obtain_data(code):
    url = f"https://people.csail.mit.edu/berzak/tle-{UD_RELEASE}-{code}/data.zip"
    try:
        urllib.request.urlretrieve(url, "data.zip")
        print("Done, annotations with data are in data.zip")
    except Exception as e:
        print(f"Error: Failed obtaining annotations with data from {url}\n{e}")


def main():
    code = check_fce()
    if code:
        obtain_data(code)


if __name__ == "__main__":
    main()
