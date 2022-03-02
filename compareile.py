import filecmp
file1=input("Enter the first file to be compared:")
file2=input("Enter the second file to be compared:")
b=filecmp.cmp(file1,file2)
if b: print("Files are equal")
else: print("Files are not equal")
