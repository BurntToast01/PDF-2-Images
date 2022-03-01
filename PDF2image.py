
from pdf2image import pdfinfo_from_path,convert_from_path



def conversion(x,y,z,g):
    pdf_file=x
    info = pdfinfo_from_path (pdf_file, userpw=None, poppler_path=None)
    last_check = int(y)-1
    maxPages = info["Pages"]
    for i in range (1,maxPages+1,1):
        print(type(i))
        if i <int(y):
            continue

        if i >=int(z)+1:
            print("page",i-1,"was converted")
            break

        #print(last_check)

        #print("converting page:",i)
        #last_check += int (1)
        if last_check >= 0:
            images = convert_from_path (pdf_file, dpi=200, first_page=int (y), last_page=maxPages, output_file=(g)
                                        , output_folder='/home/something/Downloads/document pdf conversion/tpm',
                                        fmt="jpg")
            last_check+=1
            print("All pages convereted over to images")
            break


        print ("Page", i - 1, "was converted")
        print ("converting page:", i)




conversion('/home/something/Downloads/document.pdf',input("from that page would you like to start?: "),input("from the starting page where do wanna stop?: "),input("And what should the file be called?: "))
