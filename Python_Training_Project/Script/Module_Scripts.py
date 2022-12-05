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

def Mod_Close_Browser():
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Mod_Close_Browser", "", pmNormal, Project.Variables.LogAtrribModTitle)
    #Closes the 'BrowserWindow' window.
    Aliases.browser.BrowserWindow.Close()
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()

def Mod_Login_Fail():
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Mod_Login_Fail", "", pmNormal, Project.Variables.LogAtrribModTitle)
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()

def Mod_Loop_Browsers():
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Mod_Loop_Browsers", "", pmNormal, Project.Variables.LogAtrribModTitle)
    #The beginning of the Mod_Loop_Browsers group
    #The beginning of the Browser_Loop group
    #Iterates through the specified browsers.
    BrowserItems = []
    BrowserItems.append(Browsers.Item["chrome"])
    BrowserItems.append(Browsers.Item["edge"])
    i = 0
    while i < len(BrowserItems):
        BrowserItems[i].Run("https://bearstore-testsite.smartbear.com/")
        #Checks whether the 'contentText' property of the Aliases.browser.pageShop.sectionContent.textnodeWelcomeToOurStore object equals 'Welcome to our store.'.
        aqObject.CheckProperty(Aliases.browser.pageShop.sectionContent.textnodeWelcomeToOurStore, "contentText", cmpEqual, "Welcome to our store.")
        #Runs a keyword test.
        KeywordTests.Mod_Open_Login.Run()
        #Runs a keyword test.
        KeywordTests.Mod_Close_Browser.Run()
        i = i + 1
    #The end of the Browser_Loop group
    #The end of the Mod_Loop_Browsers group
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()

def Mod_Open_Blog():
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Mod_Open_Blog", "", pmNormal, Project.Variables.LogAtrribModTitle)
    #Clicks the 'linkBlog' link.
    Aliases.browser.pageShop.header.navUsd.navNews.linkBlog.Click()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageBlog.Wait()
    #Checks whether the 'contentText' property of the Aliases.browser.pageBlog.sectionContent.textnodeBlog object equals 'Blog'.
    aqObject.CheckProperty(Aliases.browser.pageBlog.sectionContent.textnodeBlog, "contentText", cmpEqual, "Blog")
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()

def Mod_Open_Login():
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Mod_Open_Login", "", pmNormal, Project.Variables.LogAtrribModTitle)
    #Clicks the 'textnodeLogIn' control.
    Aliases.browser.pageShop.header.navUsd.linkLogIn.textnodeLogIn.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageLogin.sectionContent.textnodeSignIn object equals 'Sign In'.
    aqObject.CheckProperty(Aliases.browser.pageLogin.sectionContent.textnodeSignIn, "contentText", cmpEqual, "Sign In")
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()

def Mod_Open_Webstore_Chrome():
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Mod_Open_Webstore_Chrome", "", pmNormal, Project.Variables.LogAtrribModTitle)
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("https://bearstore-testsite.smartbear.com/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Checks whether the 'contentText' property of the Aliases.browser.pageShop.sectionContent.textnodeWelcomeToOurStore object equals 'Welcome to our store.'.
    aqObject.CheckProperty(Aliases.browser.pageShop.sectionContent.textnodeWelcomeToOurStore, "contentText", cmpEqual, "Welcome to our store.")
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()

def Mod_Open_Webstore_Edge():
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Mod_Open_Webstore_Edge", "", pmNormal, Project.Variables.LogAtrribModTitle)
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("https://bearstore-testsite.smartbear.com/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Checks whether the 'contentText' property of the Aliases.browser.pageShop.sectionContent.textnodeWelcomeToOurStore object equals 'Welcome to our store.'.
    aqObject.CheckProperty(Aliases.browser.pageShop.sectionContent.textnodeWelcomeToOurStore, "contentText", cmpEqual, "Welcome to our store.")
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()

def Mod_Open_Webstore_FireFox():
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Mod_Open_Webstore_FireFox", "", pmNormal, Project.Variables.LogAtrribModTitle)
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btFirefox].Run("about:blank")
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.CurrentBrowser.Navigate("https://bearstore-testsite.smartbear.com/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Checks whether the 'contentText' property of the Aliases.browser.pageShop.sectionContent.textnodeWelcomeToOurStore object equals 'Welcome to our store.'.
    aqObject.CheckProperty(Aliases.browser.pageShop.sectionContent.textnodeWelcomeToOurStore, "contentText", cmpEqual, "Welcome to our store.")
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()

def Mod_Return_WebStore_Home():
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Mod_Return_WebStore_Home", "", pmNormal, Project.Variables.LogAtrribModTitle)
    #Clicks the 'imageSmartstore' control.
    Aliases.browser.pageBlog.header.link.imageSmartstore.Click()
    #Checks whether the 'contentText' property of the Aliases.browser.pageShop.sectionContent.textnodeWelcomeToOurStore object equals 'Welcome to our store.'.
    aqObject.CheckProperty(Aliases.browser.pageShop.sectionContent.textnodeWelcomeToOurStore, "contentText", cmpEqual, "Welcome to our store.")
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
