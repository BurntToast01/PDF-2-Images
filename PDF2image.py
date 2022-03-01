
from pdf2image import pdfinfo_from_path,convert_from_path



def conversion():
    x=input("I need the full directory path to the PDF file please: ")
    a= input ("Where would you like to save convereted file/s?: ")
    y=input("from that page would you like to start?: ")
    z=input("from the starting page where do wanna stop?: ")
    g=input("And what should the file be called?: ")
    pdf_file=x
    info = pdfinfo_from_path (pdf_file, userpw=None, poppler_path=None)
    last_check = int(y)-1
    maxPages = info["Pages"]
    for i in range (1,int(z)+1,1):
        #print(type(i))
        if i <int(y):
            continue

        if i >=int(z)+1:
            print("page",i-1,"was converted")
            break

        #print(last_check)

        #print("converting page:",i)
        #last_check += int (1)
        if last_check >= 0:
            images = convert_from_path (pdf_file, dpi=200, first_page=int (y), last_page=int(z), output_file=(g)
                                        , output_folder=a,
                                        fmt="jpg")
            last_check+=1
            print("All pages convereted over to images")
            break


        print ("Page", i - 1, "was converted")
        print ("converting page:", i)

conversion()
