#!usr/bin/env python
#assingment of finding serverside technolgies
import requests 
import sys#to take input in the command line
def main():
	try:
		if sys.argv !="":
			url="https://whatcms.org/APIEndpoint/Technology?key=2827e2da9581dd1b2eee3fd987936ad7f5e582a6408a0e2150c32abd7ac2c424bab8a9&url={}".format(sys.argv[1])
			print("given url :"+format(sys.argv[1]))
			obj_urldata=requests.get(url)#gets the url data
			obj_json=obj_urldata.json()#data which in json format into compatibiliy for python
			res=obj_json['results']#selecting a section of data
			
			res0=res[0]#selecting categories from the results data like name
			print("name: "+res0['name'])
			if res0['version']=="":#if version data of version is not given
				print("version :"+"not provided")
			else:#if given
				print("version: "+res0['version'])
			res1=res[1]#selecting categories onf the results data like programming
			print("programming technology: "+res1['name'])
			if res1['version']=="":
				print("version :"+"not provided")
			else:
				print("verion: "+ res1['version'])
			
			res2=res[2]#selecting categories onf the results data like server
			print("server: "+res2['name'])
			if res2['version']=="":
				print("version :"+"not provided")
			else:
				
				print("version: "+res2['version'])
		else:
			print ('please check url follow combination python file.py en.wikipedia.org')
			
	except:
		print ('please check url follow combination python filename.py en.wikipedia.org')
			
		


if __name__=='__main__':
	main()