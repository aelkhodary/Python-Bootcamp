'''
* Working with PDFs and spreadsheet CSV Files

* CSV stands for comma separated variables

* Its possible to export excel files and Google Spreedsheets to .CSV files
   it only exports the information .

* Things like formulas ,images ,and macros can not be within a.csv file.

* Simply put, a.csv file only contains the raw data from the spreadsheet .

* built in csv module for python ,which will  allow us to grab columns,
   rows ,and values from a.csv file as well as write to a.csv file .
* Other libraries to consider :
  - Pandas (visualization and analysis)
  - Openpyxl (For Excel files)
  - Google Sheets Python API
'''
print('\n******************* CSV ***************\n')
import csv
# Open the file
data = open('example.csv',encoding='utf-8')
# csv.reader
csv_data =csv.reader(data)
# reformat it into a python object list of lists
data_lines = list(csv_data)

print(data_lines)
print(data_lines[0])
print(len(data_lines))
print('\n******************* lines*******\n')
for line in data_lines[:5]:
    print(line)
print('\n******************* Print Emails*******\n')
print(data_lines[10][3])
all_emails = []
for line in data_lines[:len(data_lines)]:
    print(line[3])
    all_emails.append(line[3])
print(all_emails)

print('\n*********** Read then write to csv *******\n')
data = open('example.csv',encoding='utf-8')
csv_data =csv.reader(data)
data_lines = list(csv_data)
# a -> append
#file_to_output = open('to_save_file.csv',mode='a',encoding='utf-8',newline='')
file_to_output = open('to_save_file.csv',mode='w',encoding='utf-8',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
for line in data_lines[:len(data_lines)]:
    csv_writer.writerow(line)
file_to_output.close()


print('\n******************* PDF ***************\n')
'''
 * PDF stands for Portable Document Format
 * We will use the open-source and free PyPDF2 library
 >> pip install PyPDF2
 '''


'''
import PyPDF2
# rb -> read binary
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(f'number of pages {pdf_reader.numPages}')
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
#print(f'Page one text is {page_one_text}')
f.close()
'''
import PyPDF2
# rb -> read binary
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
pages_list = [x for x in range(0,pdf_reader.numPages)]
pdf_text = []
for n in pages_list:
    print(f'******************number of page {n}*************')
    page_n= pdf_reader.getPage(n)
    page_n_text = page_n.extractText()
    pdf_text.append(page_n_text)
    #print(f'Page  text is {page_n_text}')
f.close()

'''
Add pages to new pdf file

'''

f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
page_one = pdf_reader.getPage(0)
print(type(page_one))#<class 'PyPDF2.pdf.PageObject'>
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_one)
pdf_output = open('Some_BrandNew_Doc.pdf','wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()


'''
Puzzle Exercise - Solutions
'''
import csv
data = open('find_the_link.csv', encoding='utf-8')
data_lines = list(csv.reader(data))
print(enumerate(data_lines))
link_str = ''
for row_num,data in enumerate(data_lines):
    #print(row_num)
    #print(data)
    link_str += data[row_num]
    print(link_str)

import PyPDF2
import re
f = open('Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfFileReader(f)
pattern = r'\d{3}.\d{3}.\d{4}' #505-503-445
all_text = ''
for n in range(pdf.numPages):
    page = pdf.getPage(n)
    page_text = page.extractText()
    all_text = all_text +' '+ page_text
print(re.findall(pattern,all_text))
for match in re.finditer(pattern,all_text):
    print(match)
print(type(all_text))
print(all_text[41790:41808+20])
