# Code on your Pi remotely using VS Code

[Visual Studio Code](https://code.visualstudio.com/?WT.mc_id=rpi_resources-github-jabenn) is a lightweight, cross-platform, open source code editor. You can install extensions to support a wide range of programming languages, connect to cloud services such as Azure, an even access other devices remotely.

One of these extensions is the [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack&WT.mc_id=rpi_resources-github-jabenn), and this allows you to run Visual Studio Code on one device whilst connected to a remote device, accessing the remote file system and debugging applications as if you were running on that remote device directly.

This is great for users of Raspberry Pis. You can run Visual Studio code on your laptop or desktop and connect to a Pi, coding as if you were running on the Pi with full access to the file system, editing files on the device, drag and drop file upload, GPIO pins, and debugging on the device.

> Only Pis using ARMv7 and v8 are supported, so only Pi 3 and 4s are supported. Earlier Pi devices and Pi Zeros are not supported. If you would like support for these devices, please up-vote [this issue on GitHub](https://github.com/microsoft/vscode-remote-release/issues/669)

## Connect to the Raspberry Pi from Visual Studio Code

To connect to your Raspberry Pi, first set it up for headless access by following the [headless setup guide](../headless-setup/).

### Install the Remote Development extension in Visual Studio Code

To enable remote development in Visual Studio Code, you will need to install the [Remote Development Extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack&WT.mc_id=rpi_resources-github-jabenn).

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

1. Enter `pi@raspberrypi.local` as the SSH connection command, changing the device name from `raspberrypi` if you changed it when doing the headless setup.

   ![The SSH connection command](./images/EnterSSHHost.png)

1. Select the SSH configuration file to update. This will store the SSH connection details to make connection easier. There will be an option in your home folder, which will vary depending on your OS and user name, so select this.

1. Once the connection has been configured, a dialog will appear saying the host is configured. Select **Connect** from this dialog.

   ![The host added dialog](./images/HostAddedDialog.png)

1. A new Visual Studio Code window will open to host the connection. In the password prompt dialog, enter the password for your Raspberry Pi. The default password is `raspberry`, unless you changed it when doing the headless setup.

   ![The password entry dialog](./images/SSHPassword.png)

> Once the connection has been established, the next time *Remote-SSH: Connect to Host* is selected a new window will be opened and the password requested, there will be no need to configure it again.

Once you are connected, Visual Studio Code will be running as if it was installed on the Pi directly. If you open a folder, you will only be able to select folders on the Pi. The terminal will be a terminal session running on the Pi. If you want to copy files to the Pi, you can drag them from your file explorer/finder and drop them into the Visual Studio Code explorer window and they will be copied into the relevant folder, the same as if you were accessing a local folder.

## Using Visual Studio Code extensions on the remote device

If you want to use any extensions, these will need to be installed - the remote session doesn't automatically install the extensions that you have installed locally, you have to explicitly install extensions such as the Python extension on the remote device.

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
