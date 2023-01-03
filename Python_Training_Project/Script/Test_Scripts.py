def Test_Check_Blog():
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Test_Web_App_Login_Fail")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Test_Web_App_Login_Fail", "All tests should follow this formatting in order to provide consistency to the look and feel of output logs", pmNormal, Project.Variables.LogAtrribTestTitle)
    #Runs a keyword test.
    KeywordTests.Mod_Open_Webstore_Edge.Run()
    #Runs a keyword test.
    KeywordTests.Mod_Open_Blog.Run()
    #Runs a keyword test.
    KeywordTests.Mod_Return_WebStore_Home.Run()
    #Runs a keyword test.
    KeywordTests.Mod_Close_Browser.Run()
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()

#@Debug
def Test_New_Function():
    #**** Consider duplicating this text as comment inside of the keyword test
    #**** This can serve as a flowerbox description when converted to a script
    #**** KMJ 09122022
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Test_Template")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Test_Template", "All tests should follow this formatting in order to provide consistency to the look and feel of output logs", pmNormal, Project.Variables.LogAtrribTestTitle)
    #Posts an error to the test log.
    Log.Error("This is in place to fail, so this test can be debugged", "For Demo purposes", pmNormal)
    #The beginning of the Test_Template_Module_Group group
    #Posts an information message to the test log.
    Log.Message("Test Template Information Message", "Log entry in the Test Template Keyword Test", pmNormal, Project.Variables.LogAtrribInformation)
    #Runs a keyword test.
    KeywordTests.Mod_Template.Run()
    #The end of the Test_Template_Module_Group group
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()

def Test_Sample_Web_App_Open():
    import Module_Scripts
    #**** Consider duplicating this text as comment inside of the keyword test
    #**** This can serve as a flowerbox description when converted to a script
    #**** KMJ 09122022
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Test_Template")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Sample", "", pmNormal, Project.Variables.LogAtrribModTitle)
    #The beginning of the Test_Template_Module_Group group
    #Runs a keyword test.
    KeywordTests.Mod_Template.Run()
    #Runs a script routine.
    Module_Scripts.Script_Mod_Template()
    #The end of the Test_Template_Module_Group group
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()

#@Smoke
def Test_Web_App_Login_Fail():
    #**** Login with invalid credentials KMJ 12/4/2022
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Test_Web_App_Login_Fail")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Test_Web_App_Login_Fail", "All tests should follow this formatting in order to provide consistency to the look and feel of output logs", pmNormal, Project.Variables.LogAtrribTestTitle)
    #The beginning of the Test_Web_App_Login_Fail group
    #Posts an information message to the test log.
    Log.Message("Test_Web_App_Login_Fail", "Log entry in the Test Template Keyword Test", pmNormal, Project.Variables.LogAtrribInformation)
    #Runs a keyword test.
    KeywordTests.Mod_Loop_Browsers.Run()
    #The beginning of the Edge group
    #Runs a keyword test.
    KeywordTests.Mod_Open_Webstore_Chrome.Run()
    #Runs a keyword test.
    KeywordTests.Mod_Open_Login.Run()
    #Runs a keyword test.
    KeywordTests.Mod_Close_Browser.Run()
    #The end of the Edge group
    #The beginning of the Chrome group
    #Runs a keyword test.
    KeywordTests.Mod_Open_Webstore_Chrome.Run()
    #Runs a keyword test.
    KeywordTests.Mod_Open_Login.Run()
    #Runs a keyword test.
    KeywordTests.Mod_Close_Browser.Run()
    #The end of the Chrome group
    #The beginning of the Firefox group
    #Runs a keyword test.
    #KeywordTests.Mod_Open_Webstore_FireFox.Run()
    #Runs a keyword test.
    #KeywordTests.Mod_Open_Login.Run()
    #Runs a keyword test.
    #KeywordTests.Mod_Close_Browser.Run()
    #The end of the Firefox group
    #The end of the Test_Web_App_Login_Fail group
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()

def Script_Test_Web_App_Login_Fail():
    import Module_Scripts
    #**** Login with invalid credentials KMJ 12/4/2022
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Test_Web_App_Login_Fail")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Test_Web_App_Login_Fail", "All tests should follow this formatting in order to provide consistency to the look and feel of output logs", pmNormal, Project.Variables.LogAtrribTestTitle)
    #The beginning of the Test_Web_App_Login_Fail group
    #Posts an information message to the test log.
    Log.Message("Test_Web_App_Login_Fail", "Log entry in the Test Template Keyword Test", pmNormal, Project.Variables.LogAtrribInformation)
    #Runs a script routine.
    Module_Scripts.Mod_Loop_Browsers()
    #The beginning of the Edge group
    #Runs a script routine.
    Module_Scripts.Mod_Open_Webstore_Edge()
    #Runs a script routine.
    Module_Scripts.Mod_Open_Login()
    #Runs a script routine.
    Module_Scripts.Mod_Close_Browser()
    #The end of the Edge group
    #The beginning of the Chrome group
    #Runs a script routine.
    Module_Scripts.Mod_Open_Webstore_Chrome()
    #Runs a script routine.
    Module_Scripts.Mod_Open_Login()
    #Runs a script routine.
    Module_Scripts.Mod_Close_Browser()
    #The end of the Chrome group
    #The end of the Test_Web_App_Login_Fail group
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()

def Script_Test_Check_Blog():
    import Module_Scripts
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Test_Web_App_Login_Fail")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Test_Web_App_Login_Fail", "All tests should follow this formatting in order to provide consistency to the look and feel of output logs", pmNormal, Project.Variables.LogAtrribTestTitle)
    #The beginning of the Test_Module_Group group
    #Runs a script routine.
    Module_Scripts.Mod_Open_Webstore_Edge()
    #Runs a script routine.
    Module_Scripts.Mod_Open_Blog()
    #Runs a script routine.
    Module_Scripts.Mod_Return_WebStore_Home()
    #Runs a keyword test.
    KeywordTests.Mod_Close_Browser.Run()
    #The end of the Test_Module_Group group
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()

def Junk_Script():
    #Posts an information message to the test log.
    Log.Message("Hello World", "")
