import openpyxl

# Create new spreadsheet

book = openpyxl.Workbook()

# Select page

page_selected = book['Sheet']

# Add values to spreadsheet

page_selected.append(['Meses', 'Ganho R$'])
page_selected.append(['Janeiro', '750,20'])
page_selected.append(['Fevereiro', '600,00'])
page_selected.append(['Março', '580,40'])
page_selected.append(['Abril', '450,26'])
page_selected.append(['Maio', '660,90'])

# Save spreadsheet

book.save('PlanilhaPython.xlsx') 