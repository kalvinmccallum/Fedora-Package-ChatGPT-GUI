# Fedora-Package-ChatGPT-GUI
Fedora package created using https://github.com/Cubicpath/ChatGPT-GUI.

The following steps can be used to created the ChatGPT GUI package:

1. Install the necessary tools:
Install the rpmbuild tool, which is used to build RPM packages:
"sudo dnf install rpm-build"
Install the python3-devel and python3-setuptools packages, which are required for building Python packages:
"sudo dnf install python3-devel python3-setuptools"
Install the python3-pip package, which is required to install packages from PyPI:
"sudo dnf install python3-pip"

2. Create a new directory for the RPM build files:
"mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}"
Copy the source code for ChatGPT GUI 0.4.1 from PyPI into the ~/rpmbuild/SOURCES/ directory:
"cd ~/rpmbuild/SOURCES/"
"wget https://files.pythonhosted.org/packages/source/c/chatgpt-gui/chatgpt-gui-0.4.1.tar.gz"

3. Create a new spec file called chatgpt-gui.spec in the ~/rpmbuild/SPECS/ directory:
"cd ~/rpmbuild/SPECS/"
"gedit chatgpt-gui.spec"
Copy and paste the provided spec file contents into the chatgpt-gui.spec file and click save.
Be sure to update the changelog accordingly at the bottom of the spec file.

4. Build the RPM package:
"rpmbuild -bb chatgpt-gui.spec"

5. If the build is successful, the RPM package will be located in the rpmbuild/RPMS/noarch/ directory:
"ls rpmbuild/RPMS/noarch/"

6.Install the package using dnf:
"sudo dnf install rpmbuild/RPMS/noarch/chatgpt-gui-0.4.1-1.fc34.noarch.rpm"

7. Verify that the package is installed correctly by running
