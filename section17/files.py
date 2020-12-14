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
 '''
