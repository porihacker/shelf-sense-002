DATABASE_FILE = "./database/books.txt"
title="To Kill a Mockingbird"
books={}
with open(DATABASE_FILE, "r") as f:
    book = f.readlines()
    for i in book:
       newbook= i.strip('\n').split(',')
       if title in newbook[0]:
           print("yes it is here")
           books['title']=newbook[0]
           books["author"]=newbook[1]

print(book)
              
           
        

