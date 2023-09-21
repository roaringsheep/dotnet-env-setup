# .NET Environment Setup Guide
This guide will take you through installing essential tools for .NET on Windows.

## List of Tools
We'll be installing the following
- [Git](#git)
- [.NET SDK](#net-software-development-kit-sdk)
- [Visual Studio Code](#visual-studio-code)
- [VS Code Extensions Configuration](#visual-studio-code-extensions)
## Git
1. Navigate to [Git for Windows Installation Page]($git) and download the latest release of git.
    ![git_installer_0](@git.0)

2. Once the download finishes, locate the installer. It should be named something similar to the following file.

    ![git_installer_1](@git.1)

3. Click Next through the following 2 screens
    ![git_installer_2](@git.2)
    ![git_installer_3](@git.3)

4.    Optionally, you can check the "Add a Git Bash profile to Windows Terminal" option.    
    ![git_installer_4](@git.4)

5. You can leave this as is
    ![git_installer_5](@git.5)

6. **This step is _VERY IMPORTANT_!**
    Unless you know how to use vim, I highly recommend you change this option to nano or any other text editor you may have.
    ![git_installer_6](@git.6)
    ![git_installer_7](@git.7)

7. You can keep the recommended options for the remainder of this installer
    ![git_installer_8](@git.8)
    ![git_installer_9](@git.9)
    ![git_installer_10](@git.10)
    ![git_installer_11](@git.11)
    ![git_installer_12](@git.12)
    ![git_installer_13](@git.13)
    ![git_installer_14](@git.14)
    ![git_installer_15](@git.15)
    ![git_installer_16](@git.16)
    ![git_installer_17](@git.17)
    ![git_installer_18](@git.18)

8. Once the installation is finished, click the search button on your task bar and type "git bash". You should see the newly installed git bash software appear. Click on the icon to open it.
    ![git_installer_19](@git.19)

9. In git bash, next to the $ (dollar) sign, type "git --version" and hit enter. If you get some version information, that means you have successfully installed git.
    ![git_installer_20](@git.20)
    ![git_installer_21](@git.21)

## .NET Software Development Kit (SDK)

1. Navigate to [.NET SDK website]($dotnetsdk) and click the .NET 7.0 download link
![dotnet_sdk.0](@dotnet.0)

2. Locate the installer and double click on the file to execute it
![dotnet_sdk.1](@dotnet.1)

3. Click Install
![dotnet_sdk.2](@dotnet.2)

4. If this appears, click Yes
![dotnet_sdk.3](@dotnet.3)

5. Installation is finished
![dotnet_sdk.4](@dotnet.4)

6. Now open git bash to verify that .NET SDK has been successfully installed
![git_bash_opening]($gitbash_opening)

7. Type 'dotnet --version' and hit enter. You should see 7.x.x as the response
 ![dotnet_sdk.5](@dotnet.5)

## Visual Studio Code
1. Navigate to [Visual Studio Code Installation Page]($vscode) and click on the "Download for Windows" button
    ![vscode_welcome_img](@vscode.0)

2. Once the download finishes, locate the installer. It will be a file named VSCodeUserSetup-x64-{versionNumber}
    
    ![vscode_installer_1](@vscode.1)
  
3. Accept the agreement and click next
    ![vscode_installer_2](@vscode.2)

4. Make sure all the checkboxes under Other is checked, then click Next
    ![vscode_installer_3](@vscode.3)

5. Click Install
    ![vscode_installer_4](@vscode.4)

6. VS Code is Now installed on your machine!
    ![vscode_installer_5](@vscode.5)

## Visual Studio Code Extensions
Prior to this section, please ensure that [Visual Studio Code (VSCode)](#visual-studio-code) is installed in your system. 

1. Search and Open VSCode
![vsc_opening]($vsc_opening)

2. Click on the 5th icon from the left most column to navigate to extensions page. VS Code offers extensive extensions and they offer lots of useful functionalities. 
    ![vsc_ext_0](@vscode_ext.0)
    We'll be installing the following
    - C# by Microsoft
    - C# XML Documentation Comments by Keisuke Kato
    - Live Share by Microsoft

3. C# by Microsoft offers the basic language support for C#
![vsc_ext_C#](@vscode_ext.1)
4. C# XML Documentation Comments by Keisuke Kato: This extension enables a keyboard shortcut to quickly scaffold documentation in our code
![vsc_ext_C#_XML](@vscode_ext.2)
5. Live Share by Microsoft: This extension allows you to share your code editor window with others and collaborate in real time.
![vsc_ext_live_share](@vscode_ext.3)