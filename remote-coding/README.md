# Remotely code on your Pi with VS Code

[Visual Studio Code](https://code.visualstudio.com/?WT.mc_id=rpi_resources-github-jabenn) is a lightweight, cross-platform, open source code editor. You can install extensions to support a wide range of programming languages, connect to cloud services such as Azure, and even access other devices remotely.

One of these extensions is the [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack&WT.mc_id=rpi_resources-github-jabenn), which allows you to run Visual Studio Code (VS Code) to remotely connect to and program another device

This is a helpful extension for Pi users, as you can run VS Code on your main laptop or desktop and remotely code on the Pi, with full file system access, editing, and uploading, GPIO programming, and debugging.

> Only Pis using ARMv7 and v8 are supported, so only Pi 3 and 4s are supported. Earlier Pi devices and Pi Zeros are not supported. If you would like support for these devices, please up-vote [this issue on GitHub](https://github.com/microsoft/vscode-remote-release/issues/669)

## Connect to the Raspberry Pi from Visual Studio Code

First setup your Pi for headless access by following the [headless setup guide](../headless-setup/).

### Install the Remote Development extension in Visual Studio Code

To enable remote development in Visual Studio Code, install the [Remote Development Extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack&WT.mc_id=rpi_resources-github-jabenn).

1. Launch Visual Studio Code

1. Select the Extensions tab from the left hand menu, or select *View -> Extensions*

   ![The extensions tab in Visual Studio Code](./images/VSCodeMenuExtensions.png)

1. Search for `remote development` and install the *Remote Development* extension pack from Microsoft by selecting the **Install** button

   ![The remote development extension](./images/RemoteDevelopmentExtension.png)

### Connect to the Raspberry Pi

1. From Visual Studio Code, launch the command palette

   * On macOS, press command+shift+p
   * On Windows or Linux, press ctrl+shift+p

1. Search for `Remote-SSH: Connect to Host` and select it

   ![The connect to host option](./images/VSConnectToHost.png)

1. Select *+ Add new SSH Host*

   ![The add new host option](./images/AddNewSSHHost.png)

1. Enter `pi@raspberrypi.local` as the SSH connection command, changing the hostname from `raspberrypi` if you changed it when doing the headless setup.

   ![The SSH connection command](./images/EnterSSHHost.png)

1. Select the SSH configuration file to update. This will store the SSH connection details to make connection easier. There will be an option in your home folder, which will vary depending on your OS and user name, so select this.

1. Once the connection has been configured, a dialog will appear saying the host is configured. Select **Connect** from this dialog.

   ![The host added dialog](./images/HostAddedDialog.png)

1. A new VS Code window will open to host the connection. Enter your password (default is `raspberry`)

   ![The password entry dialog](./images/SSHPassword.png)

> Once the connection has been established, the next time *Remote-SSH: Connect to Host* is selected a new window will be opened and the password requested, there will be no need to configure it again.

Once you are connected, Visual Studio Code will be running as if it was installed on the Pi directly. If you open a folder, you will only be able to select folders on the Pi. The terminal will be a terminal session running on the Pi. If you want to copy files to the Pi, you can drag them from your file explorer/finder and drop them into the Visual Studio Code explorer window and they will be copied into the relevant folder, the same as if you were accessing a local folder.

## Using Visual Studio Code extensions on the remote device

If you want to use extensions on the Pi, such as the Python extension, these will need to be installed directly as the remote session does not include extensions that you may have installed on your laptop or desktop

### Installing Python Extension
For example - to install the Python extension, follow these steps:

1. Select the Extensions tab from the left hand menu, or select *View -> Extensions*

   ![The extensions tab in Visual Studio Code](./images/VSCodeMenuExtensions.png)

1. Search for `Python` and install the *Python* extension from Microsoft by selecting **Install in SSH: raspberrypi.local**.

   ![The python extension](./images/PythonExtension.png)

   > There are a number of Python extensions available, so ensure you install the one from Microsoft

1. A reload will be required, so select **Reload required**

   ![Reload required for the python extension](./images/PythonReloadRequired.png)

1. Visual Studio will reload the window, and you will be asked for your Raspberry Pi password again, so enter it.

Once this extension is installed you will be able to debug python applications on the remote device from your local Visual Studio Code instance.
