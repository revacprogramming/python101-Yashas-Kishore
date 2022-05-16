# Strings

text = "X-DSPAM-Confidence:    0.8475"
length=len(text)
pos=text.find(':')
num=text[pos+1:]
num.strip()
fnum=float(num)
print(fnum)
