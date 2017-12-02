# /var/folders/8b/8f0rkg496r9dgt_qltvwc4d80000gn/C/latexCreateTestingEnv
import os
import requests

def returnGist(link):
	# link = "https://gist.githubusercontent.com/louwjlabuschagne/c360ddcf0a098e0dd2b7d51e37fda204/raw/f6bd209edc3a08e2cefbe4634d8b1b1d96f1010c/Gist.tex"
	f = requests.get(link)
	return(f.text)

def mkdir(pwd, _dir=""):
	if dir == "":
		print("mkdir - specify directory")
	else:
		print(">>>pwd"+pwd)

		_dir = pwd+"/"+_dir

		if not os.path.exists(_dir):
		    os.makedirs(_dir)
		    print(_dir+" created")
		else:
			print(_dir+" already exists")
		return _dir

def touch(_file, _dir, gist_url):
	with open(_dir+"/"+_file, 'w') as f:
		print("retrieving"+_file+" from gist @"+gist_url+" and writing to "+_dir+"/"+_file)
		f.write(returnGist(gist_url))
		print("success")
#create directories
pwd = os.path.abspath(os.path.curdir)
assets = mkdir(pwd, "assets")
content = mkdir(pwd, "content")
figures = mkdir(pwd, "figures")

touch("preAmble.tex", content, "https://raw.githubusercontent.com/louwjlabuschagne/latexCreate/master/files/preAmble.tex")
touch("main.tex", pwd, "https://raw.githubusercontent.com/louwjlabuschagne/latexCreate/master/files/main.tex")
touch("compile.sh", pwd, "https://raw.githubusercontent.com/louwjlabuschagne/latexCreate/master/files/compile.sh")
touch("Bibliography.bib", pwd, "https://raw.githubusercontent.com/louwjlabuschagne/latexCreate/master/files/Bibliography.bib")
