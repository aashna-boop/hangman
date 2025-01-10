# --------------------------------------------------------------#
# List-Program No 	: L3-P13
# Developed By	  	: aashna suman
# Date        	  	: 3 december 2022
# --------------------------------------------------------------#

s=input('Enter string: ')
while len(s)>10 or not s.isalpha():
  s=input('enter a string of less than 10 alphabets: ')
s=s.upper()
l=s
h=''

for i in range(20):
  print()

for i in s:
  if i in 'BCDFGHJKLMNPQRSTVWXYZ':
    l=l.replace(i,'_')

a=1
d=0
while a<10:
  print('Hint:',l)
  print('Enter guess ',a,':',sep='',end=' ')
  g=(input()).upper()
  if len(g)>1:
    print('Enter only one letter')
  elif g in 'AEIOU':
    print('Vowels already present')
  elif g in h:
    d+=2
    print('Penalty of 2 for re-input')
  elif g in s:
    l=l[:s.find(g):]+g+l[s.find(g)+1::]
    print('Match')
  else:
    print('No match')
  if l==s:
    print('u done it',s)
    print('final score is',20-d-a)
    break
  a+=1
  h+=g
else:
  print('what is a loser? u. u is a loser')
