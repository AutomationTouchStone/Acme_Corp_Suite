def Script_Mod_Template():
    #**** Consider duplicating this text as comment inside of the keyword test
    #**** This can serve as a flowerbox description when converted to a script
    #**** KMJ 09122022
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Script_Mod_Template")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Script_Mod_Template", "All test script modules should follow this formatting in order to provide consistency to the look and feel of output logs", pmNormal, Project.Variables.LogAtrribModTitle)
    #The beginning of the Mod_Template_Main_Operations_Group group
    #Posts an information message to the test log.
    Log.Message("Script Module Template Information Message", "Log entry in the Script_Mod_Template Keyword Test", pmNormal, Project.Variables.LogAtrribInformation)
    #The end of the Mod_Template_Main_Operations_Group group
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()

def Open_App_Script():
    #The beginning of the Open Application group
    #Runs the "Orders" tested application.
    TestedApps.Orders.Run(1, True)
    #The end of the Open Application group

def Dismiss_No_SCript():
    #Clicks the 'btnNo' button.
    Aliases.Orders.dlgConfirmation.btnNo.ClickButton()

def New_Order_Script():
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
