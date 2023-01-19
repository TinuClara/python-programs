#Form a list of vowels selected from a given word
word=input("Enter a word")
vowel=["a","e","i","o","u"]
new_list=[]
list1=[i for i in word if i in vowel]
new_list.append(list1)
print(list1)