text = "This is the appended text\n New line again! "

saveFile = open('exampleFile.txt','a')
saveFile.write(text)
saveFile.close()
