def Close_App_Script():
    #The beginning of the Close Application group
    #Delays the test execution for the specified time period.
    Delay(5000, "Pause to allow window to quiesce")
    #Closes the 'MainForm' window.
    Aliases.Orders.MainForm.Close()
    #The end of the Close Application group

def Delete_Record_Script():
    #Clicks the 0 subitem of the 'Bang Che' item of the 'OrdersView' list view.
    Aliases.Orders.MainForm.OrdersView.ClickItem("Bang Che")
    #Clicks the 6 item of the 'ToolBar' toolbar.
    Aliases.Orders.MainForm.ToolBar.ClickItem(6, False)
    #Clicks the 'btnYes' button.
    Aliases.Orders.dlgConfirmation.btnYes.ClickButton()

def Generate_Customer_List_Script():
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Report|Generate customer list...")
    if Aliases.Orders.dlgSaveAs.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.CustomerList_txt.Name.Exists == True:
        OCR.Recognize(Aliases.Orders.dlgSaveAs.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.CustomerList_txt.Name).BlockByText("CustomerList.txt").ClickR()
        #Moves the mouse cursor to the menu item specified and then simulates a single click.
        Aliases.Orders.dlgSaveAs.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.PopupMenu.Click("Delete")
        #Clicks the 'btnSave' button.
        Aliases.Orders.dlgSaveAs.btnSave.ClickButton()
        #Clicks the 'btnYes' button.
        Aliases.Orders.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()

def Update_Record_Script():
    #Clicks the 0 subitem of the 0 item of the 'OrdersView' list view.
    Aliases.Orders.MainForm.OrdersView.ClickItem(0)
    #Clicks the 5 item of the 'ToolBar' toolbar.
    Aliases.Orders.MainForm.ToolBar.ClickItem(5, False)
    #Enters the text 'Bang Che' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("Bang Che")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
