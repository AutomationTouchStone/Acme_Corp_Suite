def Test_Open_Desktop_Script():
    #The beginning of the Open Application group
    #Runs the "Orders" tested application.
    TestedApps.Orders.Run(1, True)
    #The end of the Open Application group
    #The beginning of the Open File group
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("File|Open...")
    #Opens the 'C:\Users\Public\Documents\TestComplete 15 Samples\Desktop\Orders\C#\TCProjects\FirstTry.tbl' file via the 'dlgOpen' dialog.
    Aliases.Orders.dlgOpen.OpenFile("C:\\Users\\Public\\Documents\\TestComplete 15 Samples\\Desktop\\Orders\\C#\\TCProjects\\FirstTry.tbl", "Table (*.tbl)")
    #The end of the Open File group
    #The beginning of the New Order group
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|New order...")
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(50, 14)
    #Enters the text 'Josh Stilton' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("Josh Stilton")
    #Enters '[Tab]' in the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Keys("[Tab]")
    #Enters '![ReleaseLast]' in the 'Street' object.
    Aliases.Orders.OrderForm.Group.Street.Keys("![ReleaseLast]")
    #Enters the text '4125 Cumberland Court' in the 'Street' text editor.
    Aliases.Orders.OrderForm.Group.Street.SetText("4125 Cumberland Court")
    #Enters '[Tab]' in the 'Street' object.
    Aliases.Orders.OrderForm.Group.Street.Keys("[Tab]")
    #Enters the text 'Commerce' in the 'City' text editor.
    Aliases.Orders.OrderForm.Group.City.SetText("Commerce")
    #Enters '[Tab]' in the 'City' object.
    Aliases.Orders.OrderForm.Group.City.Keys("[Tab]")
    #Enters the text 'MI' in the 'State' text editor.
    Aliases.Orders.OrderForm.Group.State.SetText("MI")
    #Enters '[Tab]' in the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Keys("[Tab]")
    #Enters the text '48323' in the 'Zip' text editor.
    Aliases.Orders.OrderForm.Group.Zip.SetText("48323")
    #Clicks the 'MasterCard' button.
    Aliases.Orders.OrderForm.Group.MasterCard.ClickButton()
    #Clicks the 'CardNo' object.
    Aliases.Orders.OrderForm.Group.CardNo.Click(51, 13)
    #Enters the text '1234567890123456' in the 'CardNo' text editor.
    Aliases.Orders.OrderForm.Group.CardNo.SetText("1234567890123456")
    #Sets the date '6/6/2034' in the 'ExpDate' date/time picker.
    Aliases.Orders.OrderForm.Group.ExpDate.wDate = "6/6/2034"
    #Enters '[Tab]' in the 'ExpDate' object.
    Aliases.Orders.OrderForm.Group.ExpDate.Keys("[Tab]")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
    #The end of the New Order group
    #The beginning of the Save_As group
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("File|Save As...")
    #Enters the text 'FirstTry.tbl' in the 'ComboBox' text editor.
    Aliases.Orders.dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox.SetText("FirstTry.tbl")
    #Performs a single click on the specified button.
    Aliases.Orders.dlgSaveAs.btnSave.ClickButton()
    #Clicks the 'Confirm_Save_As' object.
    Aliases.Orders.dlgConfirmSaveAs.Confirm_Save_As.Click(207, 77)
    #Clicks the 'btnYes' button.
    Aliases.Orders.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()
    #The end of the Save_As group
    #The beginning of the Close Application group
    #Delays the test execution for the specified time period.
    Delay(5000, "Pause to allow window to quiesce")
    #Closes the 'MainForm' window.
    Aliases.Orders.MainForm.Close()
    #The end of the Close Application group
