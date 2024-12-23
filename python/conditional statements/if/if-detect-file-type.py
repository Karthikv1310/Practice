'''
if condition
'''
'''Project-5-detect-file-type'''
i=input("Enter your file name with it's extension: ").lower()
if '.txt' in i:
    print("Text File Detected")
if '.pdf' in i:print("Pdf File Detected")
if 'jpg' in i:print("Jpg File Detected")
if 'png' in i:print("Png File Detected")
if 'excel' in i:print("Excel File Detected")