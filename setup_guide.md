# .NET Environment Setup Guide
This guide will take you through installing essential tools for .NET on Windows.

## List of Tools
We'll be installing the following
- [Git](#git)
- [.NET SDK](#net-software-development-kit-sdk)
- [Visual Studio Code](#visual-studio-code)
- [VS Code Extensions Configuration](#visual-studio-code-extensions)
## Git
1. Navigate to [Git for Windows Installation Page](https://git-scm.com/download/win) and download the latest release of git.
    ![git_installer_0](images/git_0.png)

2. Once the download finishes, locate the installer. It should be named something similar to the following file.

    ![git_installer_1](images/git_1.png)

3. Click Next through the following 2 screens
    ![git_installer_2](images/git_2.png)
    ![git_installer_3](images/git_3.png)

4.    Optionally, you can check the "Add a Git Bash profile to Windows Terminal" option.    
    ![git_installer_4](images/git_4.png)

5. You can leave this as is
    ![git_installer_5](images/git_5.png)

6. **This step is _VERY IMPORTANT_!**
    Unless you know how to use vim, I highly recommend you change this option to nano or any other text editor you may have.
    ![git_installer_6](images/git_6.png)
    ![git_installer_7](images/git_7.png)

7. You can keep the recommended options for the remainder of this installer
    ![git_installer_8](images/git_8.png)
    ![git_installer_9](images/git_9.png)
    ![git_installer_10](images/git_10.png)
    ![git_installer_11](images/git_11.png)
    ![git_installer_12](images/git_12.png)
    ![git_installer_13](images/git_13.png)
    ![git_installer_14](images/git_14.png)
    ![git_installer_15](images/git_15.png)
    ![git_installer_16](images/git_16.png)
    ![git_installer_17](images/git_17.png)
    ![git_installer_18](images/git_18.png)

8. Once the installation is finished, click the search button on your task bar and type "git bash". You should see the newly installed git bash software appear. Click on the icon to open it.
    ![git_installer_19](images/git_19.png)

9. In git bash, next to the $ (dollar) sign, type "git --version" and hit enter. If you get some version information, that means you have successfully installed git.
    ![git_installer_20](images/git_20.png)
    ![git_installer_21](images/git_21.png)

## .NET Software Development Kit (SDK)

1. Navigate to [.NET SDK website](https://dotnet.microsoft.com/en-us/download) and click the .NET 7.0 download link
![dotnet_sdk.0](images/dotnet_0.png)

2. Locate the installer and double click on the file to execute it
![dotnet_sdk.1](images/dotnet_1.png)

3. Click Install
![dotnet_sdk.2](images/dotnet_2.png)

4. If this appears, click Yes
![dotnet_sdk.3](images/dotnet_3.png)

5. Installation is finished
![dotnet_sdk.4](images/dotnet_4.png)

6. Now open git bash to verify that .NET SDK has been successfully installed
![git_bash_opening](images/git_19.png)

7. Type 'dotnet --version' and hit enter. You should see 7.x.x as the response
 ![dotnet_sdk.5](images/dotnet_5.png)

## Visual Studio Code
1. Navigate to [Visual Studio Code Installation Page](https://code.visualstudio.com/) and click on the "Download for Windows" button
    ![vscode_welcome_img](images/vscode_0.png)

2. Once the download finishes, locate the installer. It will be a file named VSCodeUserSetup-x64-{versionNumber}
    
    ![vscode_installer_1](images/vscode_1.png)
  
3. Accept the agreement and click next
    ![vscode_installer_2](images/vscode_2.png)

4. Make sure all the checkboxes under Other is checked, then click Next
    ![vscode_installer_3](images/vscode_3.png)

5. Click Install
    ![vscode_installer_4](images/vscode_4.png)

6. VS Code is Now installed on your machine!
    ![vscode_installer_5](images/vscode_5.png)

## Visual Studio Code Extensions
Prior to this section, please ensure that [Visual Studio Code (VSCode)](#visual-studio-code) is installed in your system. 

1. Search and Open VSCode
![vsc_opening](images/vsc_opening.png)

2. Click on the 5th icon from the left most column to navigate to extensions page. VS Code offers extensive extensions and they offer lots of useful functionalities. 
    ![vsc_ext_0](images/vscode_extension_0.png)
    We'll be installing the following
    - C# by Microsoft
    - C# XML Documentation Comments by Keisuke Kato
    - Live Share by Microsoft

3. C# by Microsoft offers the basic language support for C#
![vsc_ext_C#](images/vscode_extension_1.png)
4. C# XML Documentation Comments by Keisuke Kato: This extension enables a keyboard shortcut to quickly scaffold documentation in our code
![vsc_ext_C#_XML](images/vsc_ext_2.png)
5. Live Share by Microsoft: This extension allows you to share your code editor window with others and collaborate in real time.
![vsc_ext_live_share](images/vsc_ext_3.png)