#Ordering Menu application for Backyard Cookin'

import tkinter
import tkinter.messagebox
from datetime import datetime

class BackyardCookin():

    def __init__(self):

        #CONSTANTS
        self.TAX_RATE = 0.10
        self.TAX_PERCENT = '10%'

        #float CONSTANTS containing item prices (example: CB1 = checkbox1, etc.)
        self.CB1 = 5.99
        self.CB2 = 4.99
        self.CB3 = 1.99
        self.CB4 = 0.99
        self.CB5 = 0.99
        self.CB6 = 0.00
        self.CB7 = 2.99

        #names of items for check boxes
        #names correspond with checkbox numbers above
        self.name1 = f'Cheese Burger - ${self.CB1}'
        self.name2 = f'Hotdog - ${self.CB2}'
        self.name3 = f'French Fries - ${self.CB3}'
        self.name4 = f'Assorted Chips - ${self.CB4}'
        self.name5 = f'Soft Drink - ${self.CB5}'
        self.name6 = 'Water - free'
        self.name7 = f'Ice Cream - ${self.CB7}'

        #set up main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Backyard Cookin\' - Main Menu')
        self.main_window.geometry('500x350')

        #set up main window's frames and pack
        self.frame_top = tkinter.Frame(self.main_window)
        self.frame_middle = tkinter.Frame(self.main_window)
        self.frame_bottom = tkinter.Frame(self.main_window)

        self.frame_top.pack(pady = (20,5))
        self.frame_middle.pack()
        self.frame_bottom.pack()

        #set up main window's title label and pack
        self.titleLabel = tkinter.Label(self.frame_top,
                                              text = 'Welcome to Backyard Cookin!',
                                              font = ('Arial', 18, 'bold'))
        self.instructionLabel = tkinter.Label(self.frame_top,
                                              text = 'Click \"Add an order\" to start ordering',
                                              font = ('Arial', 12))
        self.titleLabel.pack(side = 'top')
        self.instructionLabel.pack(side = 'top', pady = (10,20))

        #set up main window's buttons for ordering and quit, then pack
        self.order_button = tkinter.Button(self.frame_middle,
                                        text = 'Add an order',
                                        font = ('Arial', 12),
                                        relief = 'raised',
                                        command = self.open_menu)
        self.quit_button = tkinter.Button(self.frame_middle,
                                          text = 'Quit',
                                          font = ('Arial', 12),
                                          relief = 'raised',
                                          command = self.main_window.destroy)
        
        self.order_button.pack(side = 'left', padx = 5)
        self.quit_button.pack(side = 'left', padx = 5)

        #variable to hold the accumulated value for subTotal, later placed into string for display
        self.subTotalDouble = tkinter.DoubleVar()
        self.subTotalDouble.set(0.00)

        #to hold values for tax before displaying in another string
        self.taxDouble = tkinter.DoubleVar()
        self.taxDouble.set(0.00)
        
        #to hold values for grand total before desplaying in another string var
        self.grandTotalDouble = tkinter.DoubleVar()
        self.grandTotalDouble.set(0.00)

        #set up main window's display labels for menu output, then pack
        self.subTotalString = tkinter.StringVar() #string var to display subTotalDouble
        self.taxString = tkinter.StringVar() #string var to display taxDouble
        self.grandTotalString = tkinter.StringVar() #string var to display grandTotalDouble

        self.resultsSubTotal = tkinter.Label(self.frame_bottom,
                                        font = ('Arial', 13),
                                        textvariable = self.subTotalString)
        self.resultsTax = tkinter.Label(self.frame_bottom,
                                        font = ('Arial', 12),
                                        textvariable = self.taxString)
        self.resultsGrandTotal = tkinter.Label(self.frame_bottom,
                                         font = ('Arial', 14, 'bold'),
                                         textvariable = self.grandTotalString)
        
        self.resultsSubTotal.pack(padx = 20, pady = (20,5))
        self.resultsTax.pack(padx = 20, pady = (5,5))
        self.resultsGrandTotal.pack(padx = 20, pady = (5,20))

        #bool to display Sumbit Order button after adding an order
        self.didYouClick = tkinter.BooleanVar()
        self.didYouClick.set(False)

        #counter for order number for receipt
        self.orderNum = 0

        #make receipt
        with open('receipt.txt', 'w') as receipt:
            receipt.write('BACKYARD COOKIN\' receipt:\n\n')

        #all praise master loop
        tkinter.mainloop()
        
    def open_menu(self):

        #set up menu window
        self.menu_window = tkinter.Toplevel()
        self.menu_window.title('Backyard Cookin\' - Place Order')
        self.menu_window.geometry('500x600')

        #set up menu frames and pack
        self.frame_top = tkinter.Frame(self.menu_window)
        self.frame_middle1 = tkinter.Frame(self.menu_window)
        self.frame_middle2 = tkinter.Frame(self.menu_window)
        self.frame_middle3 = tkinter.Frame(self.menu_window)
        self.frame_middle4 = tkinter.Frame(self.menu_window)
        self.frame_bottom = tkinter.Frame(self.menu_window)

        self.frame_top.pack(pady = (20,10))
        self.frame_middle1.pack()
        self.frame_middle2.pack()
        self.frame_middle3.pack()
        self.frame_middle4.pack()
        self.frame_bottom.pack(pady = (20,5))

        #create integer variable objects for all Checkbuttons, then set them to off (0)
        self.checkbox1_var = tkinter.IntVar()
        self.checkbox2_var = tkinter.IntVar()
        self.checkbox3_var = tkinter.IntVar()
        self.checkbox4_var = tkinter.IntVar()
        self.checkbox5_var = tkinter.IntVar()
        self.checkbox6_var = tkinter.IntVar()
        self.checkbox7_var = tkinter.IntVar()

        #set values to off (0) for all checkboxes
        self.checkbox1_var.set(0)
        self.checkbox2_var.set(0)
        self.checkbox3_var.set(0)
        self.checkbox4_var.set(0)
        self.checkbox5_var.set(0)
        self.checkbox6_var.set(0)
        self.checkbox7_var.set(0)

        #set up menu window's title label and pack
        self.titleLabel = tkinter.Label(self.frame_top,
                                              text = 'Order Menu',
                                              font = ('Arial', 18, 'bold'))
        self.titleLabel.pack(side = 'top')

        #set up Entrée label and checkboxes in middle frame 1, then pack
        self.entrees_label = tkinter.Label(self.frame_middle1,
                                          text = 'Entrées',
                                          font = ('Arial', 14, 'underline'))
        self.checkbox1 = tkinter.Checkbutton(self.frame_middle1,
                                       text = f'{self.name1}',
                                       font = ('Arial', 12),
                                       variable = self.checkbox1_var)
        self.checkbox2 = tkinter.Checkbutton(self.frame_middle1,
                                       text = f'{self.name2}',
                                       font = ('Arial', 12),
                                       variable = self.checkbox2_var)
        
        self.entrees_label.pack(side = 'top', pady = (5,5))
        self.checkbox1.pack(anchor = 'w', side = 'top')
        self.checkbox2.pack(anchor = 'w', side = 'top')

        #set up Sides label and checkboxes in middle frame 2, then pack
        self.sides_label = tkinter.Label(self.frame_middle2,
                                          text = 'Sides',
                                          font = ('Arial', 14, 'underline'))
        self.checkbox3 = tkinter.Checkbutton(self.frame_middle2,
                                       text = f'{self.name3}',
                                       font = ('Arial', 12),
                                       variable = self.checkbox3_var)
        self.checkbox4 = tkinter.Checkbutton(self.frame_middle2,
                                       text = f'{self.name4}',
                                       font = ('Arial', 12),
                                       variable = self.checkbox4_var)
        
        self.sides_label.pack(side = 'top', pady = (10,5))
        self.checkbox3.pack(anchor = 'w', side = 'top')
        self.checkbox4.pack(anchor = 'w', side = 'top')

        #set up Beverages label and checkboxes in middle frame 3, then pack
        self.beverages_label = tkinter.Label(self.frame_middle3,
                                          text = 'Beverages',
                                          font = ('Arial', 14, 'underline'))
        self.checkbox5 = tkinter.Checkbutton(self.frame_middle3,
                                       text = f'{self.name5}',
                                       font = ('Arial', 12),
                                       variable = self.checkbox5_var)
        self.checkbox6 = tkinter.Checkbutton(self.frame_middle3,
                                       text = f'{self.name6}',
                                       font = ('Arial', 12),
                                       variable = self.checkbox6_var)
        
        self.beverages_label.pack(side = 'top', pady = (10,5))
        self.checkbox5.pack(anchor = 'w', side = 'top')
        self.checkbox6.pack(anchor = 'w', side = 'top')

        #set up Desserts label and checkboxes in middle frame 3, then pack
        self.desserts_label = tkinter.Label(self.frame_middle4,
                                            text = 'Desserts',
                                            font = ('Arial', 14, 'underline'))
        self.checkbox7 = tkinter.Checkbutton(self.frame_middle4,
                                             text = f'{self.name7}',
                                             font = ('Arial', 12),
                                             variable = self.checkbox7_var)
        
        self.desserts_label.pack(side = 'top', pady = (10,5))
        self.checkbox7.pack(anchor = 'w', side = 'top')

        #create Add-to-order and Back buttons,then pack
        self.addToOrder_button = tkinter.Button(self.frame_bottom,
                                          text = 'Add to order',
                                          font = ('Arial', 12),
                                          relief = 'raised',
                                          command = self.get_calculation)
                                                                            
        self.back_button = tkinter.Button(self.frame_bottom,
                                          text = 'Back',
                                          font = ('Arial', 12),
                                          relief = 'raised',
                                          command = self.menu_window.destroy)
        
        self.addToOrder_button.pack(side = 'left', padx = 5)
        self.back_button.pack(side = 'left', padx = 5)

    def get_calculation(self):

        #set accumulator for currentTotal
        self.currentTotal = 0.00
        self.currentDisplayPrice = tkinter.DoubleVar()
        self.currentDisplayPrice.set(0.00)

        #create list variable for adding items to receipt
        self.itemList = []

        #get currentTotal and item name/prices to itemList for receipt
        if self.checkbox1_var.get() == 1:
            self.currentTotal += self.CB1
            self.itemList.append(self.name1)
        if self.checkbox2_var.get() == 1:
            self.currentTotal += self.CB2
            self.itemList.append(self.name2)
        if self.checkbox3_var.get() == 1:
            self.currentTotal += self.CB3
            self.itemList.append(self.name3)
        if self.checkbox4_var.get() == 1:
            self.currentTotal += self.CB4
            self.itemList.append(self.name4)
        if self.checkbox5_var.get() == 1:
            self.currentTotal += self.CB5
            self.itemList.append(self.name5)
        if self.checkbox6_var.get() == 1:
            self.currentTotal += self.CB6
            self.itemList.append(self.name6)
        if self.checkbox7_var.get() == 1:
            self.currentTotal += self.CB7
            self.itemList.append(self.name7)
            
        #makes a placeholder to add the newest order's total to placeholder
        #then assign the old value and newest value to the displaying subTotal in main window
        self.place_holder = self.subTotalDouble.get()
        self.subTotalDouble.set(self.place_holder + self.currentTotal)

        #get value for taxes
        self.taxDouble.set(self.subTotalDouble.get() * self.TAX_RATE)

        #get value for grandTotal
        self.grandTotalDouble.set(self.taxDouble.get() + self.subTotalDouble.get())

        #place output into a formatted string for display to main window
        self.subTotalString.set(f'Subtotal: ${self.subTotalDouble.get():.2f}')
        self.taxString.set(f'Sales Tax ({self.TAX_PERCENT}): ${self.taxDouble.get():.2f}')
        self.grandTotalString.set(f'Grand Total: ${self.grandTotalDouble.get():.2f}')

        #sets bool to true for display sumbit button in main window
        self.didYouClick.set(True)

        #function call to check bool status and display sumbit order button in main window if true
        self.checkBool_displaySubmit()

        #increment order number for receipt
        #modify into integer because var changes to str after 1st order for receipt
        self.orderNum = int(self.orderNum)
        self.orderNum += 1

        #call funtion to add ordered items to reciept
        self.receipt_add_order()

        #closes menu window
        self.menu_window.destroy()

    def checkBool_displaySubmit(self):

        #if true, add and pack submit order button
        if self.didYouClick.get() == True:
            self.submit_order_button = tkinter.Button(self.main_window,
                                          text = 'Submit Order',
                                          font = ('Arial', 14, 'bold'),
                                          relief = 'raised',
                                          command = self.final)
            
            self.submit_order_button.pack(padx = 20, pady = 10)

    def receipt_add_order(self):

        #convert from int to string for output to receipt
        self.orderNum = str(self.orderNum)
        
        #open file and add items that were placed in listItems
        with open('receipt.txt', 'a') as receipt:
            receipt.write('Order #' + self.orderNum + '\n')
            for items in self.itemList:
                receipt.write(items + '\n')
            receipt.write('\n')

    def receipt_finalize(self):
        
        #write subTotalString, taxString, grandTotalString to receipt
        with open('MenuAppReceipt.txt', 'a') as receipt:
            receipt.write(self.subTotalString.get() + '\n' + self.taxString.get() + '\n' + self.grandTotalString.get() + '\n\n')
            receipt.write('Time stamp: ' + self.date + ' at ' +self.time + '\n')

    def final(self):

        #get date/time
        self.now = datetime.now()
        self.time = self.now.strftime('%H:%M')
        self.date = self.now.strftime('%m/%d/%Y')

        #sent grand totals to receipt
        self.receipt_finalize()
        
        #displays message
        tkinter.messagebox.showinfo('Backyard Cookin\' message', f'Thanks for dining with Backyard Cookin\'!\nYour order was submitted at {self.time} on {self.date}. A receipt has been generated.')

        #close app
        self.main_window.destroy()

if __name__ == '__main__':
    order_backYardCookin = BackyardCookin()
