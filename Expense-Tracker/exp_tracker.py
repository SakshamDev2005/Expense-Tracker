import pandas as pd
from datetime import date as d
import sys

class Exp_Tracker:
    def __init__(self):
        self.df = pd.read_excel('exp_page.xlsx')

        self.li_page = ['Show Table','Make an Entry','Sum of Transactions','Exit System']
        self.li_func = ['self.show_table()','self.append_rows()','self.sum_rows()','sys.exit()']

    def show_table(self):
        print(self.df)
        self.page()

            
    def page(self):
        print('\n')
        for i in range(1,len(self.li_page)+1):
                print(f'{i} - ',self.li_page[i-1])

        try:
            ch = int(input('\nEnter the Choice ->'))
            if 0 < ch <= len(self.li_func):
                return eval(self.li_func[ch - 1])
            else:
                print('Invalid Entry')
                self.page()
        except Exception as e:
            print(e)
            print('Error, Try Again')
            self.page()
        
    def append_rows(self):
        x = len(self.df.index)
        dt = d.today()
        tr = input('Enter the Transcation Details ->')
        am = float(input('Enter the  Amount ->'))
        
        self.df.loc[x] = [x+1,tr,dt,am]
        try:
            self.df.to_excel('exp_page.xlsx',index=False)
            print('Entry is made in the File')
            self.page()
        except Exception as e:
            print(f'Error - {e}')
            print('Try Again')
            self.page()

    def sum_rows(self):
        print('format(yyyy-mm-dd)')
        try:
            start_date = str(input('Enter the Start Date ->'))
            end_date = str(input('Enter the End Date ->'))

            mask = (self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)
            filtered_data = self.df.loc[mask]
            print(filtered_data['Amount'].sum())

            self.page()
            
        except Exception as e:
            print(e)
            print('Error, Try Again')
                  

v = Exp_Tracker()
v.page()
