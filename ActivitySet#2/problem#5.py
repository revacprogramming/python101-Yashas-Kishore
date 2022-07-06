def get_cs():
	string=input("enter the string for the process:")
	return string
def cs_to_dict(cs):
	d=dict()
	split1=cs.split(';')
	for i in split1:
		split2=i.split('=')
		d[split2[0]]=split2[1]
	return d
def dict_to_cs(d):
	x=list()
	for i in d:
		join1=i+'='+d[i]
		x.append(join1)
	y=";".join(x)
	return y
def main():
	cs=get_cs()
	d=cs_to_dict(cs)
	print(d)
	cs=dict_to_cs(d)
	print(cs)
	
if _name_ == '_main_':
	main()
