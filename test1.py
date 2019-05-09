import pandas as pd 
df=pd.read_csv("try.csv")
# print df["Name:"]
for i in range(970):
	print df["Name:"][i] 
	print "---"
	data = {"Name": df["Name:"][i]}
	db.child("users").push(data)
