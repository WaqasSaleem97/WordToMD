***Cloud Computing (Lab 4)***

***Name : Sarosh Majeed***

***Reg no : 2023-BSE-059***

***<span class="mark">Task 1 – Verify VM resources in VMware</span>***

***Confirm the VM resources that were allocated in Lab 1.***

***Open VMware
Workstation and locate the Ubuntu Server VM you used in Lab 1. Inspect
VM settings and note the following (no commands required for GUI): VM
name, RAM, CPU, disk, and network adapter type. Take a screenshot of the
VM settings window showing RAM, CPU, disk and networking.***

<img src="CC-Lab4-Sarosh059_media/media/image1.png" style="width:5.95556in;height:2.42361in" alt="1.png" />

***<span class="mark">Task
2 – Start VM and log in (use your preferred host terminal method
only)</span>***

<img src="CC-Lab4-Sarosh059_media/media/image2.png" style="width:3.69167in;height:2.78194in" alt="vm-login.png" />

***Use a single preferred host-terminal method to connect to the VM. Do
not switch between methods during the task. Start (or resume) the VM in
VMware Workstation on your host.***

***From your host, open your preferred terminal (for example: Windows
Command Prompt, PowerShell, macOS Terminal, or Linux Terminal) and
connect to the VM using SSH. Example:***

***ssh
student@\<vm-ip-address\>***

<img src="CC-Lab4-Sarosh059_media/media/image3.png" style="width:5.56111in;height:3.58542in" alt="3.whoami_pwd.png" />

***<span class="mark">Task 3 – Filesystem exploration — root tree and
dotfiles</span>***

***Explore Linux filesystem layout and hidden files. Capture outputs
using screenshots only (do not create text files). For the short
explanation required in this task, write the paragraph in an editor and
capture it as a screenshot (answers_md.png) — do not supply the .md
file.***

***Steps (run inside VM terminal)***

***List root directory contents:***

***ls -la /***

<img src="CC-Lab4-Sarosh059_media/media/image4.png" style="width:4.30903in;height:3.42431in" alt="4.ls_root.png" />

***View OS release information:***

***cat /etc/os-release***

<img src="CC-Lab4-Sarosh059_media/media/image5.png" style="width:6.04873in;height:1.92174in" alt="5.os-release.png" />

***Inspect these directories (run each command and screenshot the
output):***

***ls -la /bin***

<img src="CC-Lab4-Sarosh059_media/media/image6.png" style="width:3.9875in;height:0.60833in" alt="6.ls_bin.png" />

***ls -la /sbin***

***ls -la
/usr***

<img src="CC-Lab4-Sarosh059_media/media/image7.png" style="width:4.09167in;height:2.15625in" alt="7.ls_usr.png" />

***ls -la /opt***

<img src="CC-Lab4-Sarosh059_media/media/image8.png" style="width:2.97917in;height:0.69565in" alt="8.ls_opt.png" />

***ls -la /etc***

<img src="CC-Lab4-Sarosh059_media/media/image8.png" style="width:2.97917in;height:0.69565in" alt="8.ls_opt.png" />

***ls -la /dev***

<img src="CC-Lab4-Sarosh059_media/media/image9.png" style="width:4.37222in;height:3.72361in" alt="9.ls_dev.png" />

***ls -la /var***

<img src="CC-Lab4-Sarosh059_media/media/image10.png" style="width:4.34792in;height:2.26736in" alt="10.ls_var.png" />

***ls -la /tmp***

<img src="CC-Lab4-Sarosh059_media/media/image11.png" style="width:6.21172in;height:2.33721in" alt="11.ls_tmp.png" />

***List your home directory and show hidden (dot) files:***

***ls -la ~***

<img src="CC-Lab4-Sarosh059_media/media/image12.png" style="width:5.07219in;height:1.48837in" alt="12.home_ls.png" />

***Write a short paragraph (3–5 sentences) that explains the difference
between /bin, /usr/bin and /usr/local/bin. Open your editor:***

***nano ~/answers.md***

***Type the paragraph in the editor, save and exit.***

***After saving, open the editor display (or show the file) and capture
a screenshot of the paragraph.***

***Reminder:
Do not upload the .md file—submit the screenshot answers_md.png as proof
of your written answer.***

<img src="CC-Lab4-Sarosh059_media/media/image13.png" style="width:5.78403in;height:2.1625in" alt="13.answer_md.png" />

***<span class="mark">Task 4 – Essential CLI tasks — navigation and file
operations</span>***

***Steps (inside VM terminal)***

***Create a workspace and navigate:***

***mkdir
-p ~/lab4/workspace/python_project***

<img src="CC-Lab4-Sarosh059_media/media/image14.png" style="width:3.36111in;height:0.77361in" alt="15. cd_workspace.png" />

***cd ~/lab4/workspace/python_project***

***pwd***

<img src="CC-Lab4-Sarosh059_media/media/image15.png" style="width:2.94438in;height:0.35652in" alt="16.pwd_workspace.png" />

***Create files using an editor (open each editor session and save a
screenshot showing content):***

***nano README.md and Inside nano add: Lab 4 README and save.***

<img src="CC-Lab4-Sarosh059_media/media/image16.png" style="width:5.74878in;height:4.12069in" alt="17.nano_readme.png" />

***nano main.py and Inside nano add: print("hello lab4") and save.***

<img src="CC-Lab4-Sarosh059_media/media/image17.png" style="width:6.50224in;height:1.39231in" alt="18.nano_main.py.png" />

***nano
.env and Inside nano add: ENV=lab4 and save.***

<img src="CC-Lab4-Sarosh059_media/media/image18.png" style="width:5.36319in;height:1.90694in" alt="19.nano_env.png" />

***List files and capture:***

***ls
-la***

<img src="CC-Lab4-Sarosh059_media/media/image19.png" style="width:4.00208in;height:2.00347in" alt="20.workspace_ls.png" />

***Copy, move and remove: cp README.md README.copy.md and mv
README.copy.md and README.dev.md***

<img src="CC-Lab4-Sarosh059_media/media/image20.png" style="width:4.70972in;height:0.83819in" alt="21.cp-mv-rm.png" />

***mkdir -p ~/lab4/workspace/java_app***

<img src="CC-Lab4-Sarosh059_media/media/image21.png" style="width:4.84071in;height:0.27692in" alt="22.mkdir_java_app.png" />

***cp -r ~/lab4/workspace/python_project
~/lab4/workspace/java_app_copy***

<img src="CC-Lab4-Sarosh059_media/media/image22.png" style="width:5.75609in;height:0.35385in" alt="23.cp_recursive.png" />

***ls -la ~/lab4/workspace***

<img src="CC-Lab4-Sarosh059_media/media/image23.png" style="width:4.67147in;height:1.17692in" alt="24.copy_verify.png" />

***Use command history and tab completion:***

***history***

<img src="CC-Lab4-Sarosh059_media/media/image24.png" style="width:3.68681in;height:3.03056in" alt="25.history_png.png" />

***tab_completion***

<img src="CC-Lab4-Sarosh059_media/media/image25.png" style="width:4.08686in;height:0.25385in" alt="26.tab_completion.png" />

***<span class="mark">Task 5 – System info, resources &
processes</span>***

***Steps (inside VM terminal)***

***Kernel and OS: uname -a***

<img src="CC-Lab4-Sarosh059_media/media/image26.png" style="width:6.15609in;height:0.85385in" alt="27.uname.png" />

***CPU
(ensure model name visible): cat /proc/cpuinfo***

<img src="CC-Lab4-Sarosh059_media/media/image27.png" style="width:5.825in;height:3.16319in" alt="28.CPU-info.png" />

***Memory: free -h***

<img src="CC-Lab4-Sarosh059_media/media/image28.png" style="width:4.80224in;height:0.82308in" alt="29.mem-info.png" />

***Disk: df -h***

<img src="CC-Lab4-Sarosh059_media/media/image29.png" style="width:4.50994in;height:1.25385in" alt="30.disk-info.png" />

***Os Release: cat /etc/os-release***

<img src="CC-Lab4-Sarosh059_media/media/image30.png" style="width:5.33301in;height:1.88462in" alt="31.os-release.png" />

***Processes
(show top lines of ps output): ps aux***

<img src="CC-Lab4-Sarosh059_media/media/image31.png" style="width:5.01736in;height:3.59931in" alt="32.processes.png" />

***<span class="mark">Task 6 – Users and account verification (no sudo
group change)</span>***

***Create a non‑root user and verify the account exists. This task does
NOT add the created user to the sudo group.***

***Steps (inside VM terminal)***

***Create a new user named lab4user: sudo adduser lab4user***

<img src="CC-Lab4-Sarosh059_media/media/image32.png" style="width:4.36319in;height:0.96111in" alt="33.adduser_lab4user.png" />

***Verify the user entry: getent passwd lab4user***

<img src="CC-Lab4-Sarosh059_media/media/image33.png" style="width:4.50994in;height:2.96154in" alt="34.lab4user_pass.png" />

***Verification (Optional)***

<img src="CC-Lab4-Sarosh059_media/media/image34.png" style="width:4.24028in;height:0.52292in" alt="35.verification.png" />

***Switch
to the new user to verify login: su - lab4user***

<img src="CC-Lab4-Sarosh059_media/media/image35.png" style="width:3.60972in;height:0.33819in" alt="36.su_lab4user.png" />

***From the new user you may attempt a sudo command to show that sudo is
not available for this account (expected failure), e.g.: sudo whoami***

<img src="CC-Lab4-Sarosh059_media/media/image36.png" style="width:4.54792in;height:0.82292in" alt="37.sudo_whoami.png" />

***Return to the original user:***

***exit***

<img src="CC-Lab4-Sarosh059_media/media/image37.png" style="width:3.63301in;height:0.73846in" alt="38.exited_back.png" />