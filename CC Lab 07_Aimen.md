**<u>Cloud Computing Lab</u>**

**<u>Lab 07 tasks</u>**

**<u>Environment Variables, PATH, UFW, and SSH Key Authentication</u>**

**Submitted To:** Muhammad Shoaib

**Submitted From:** Aimen Hafeez

**Registration Number:** 2023-BSE-002

**Task 1 — Print & filter environment variables (Ubuntu VM)**

Print all environment variables:

<img src="CC Lab 07_Aimen/images/image4.png" style="width:6.5in;height:2.66667in" />

Run three greps together (run the three commands consecutively in the
same terminal so one screenshot shows all three outputs).

<img src="CC Lab 07_Aimen/images/image9.png" style="width:4.27083in;height:1.20833in" />

**Task 2 — Export DB\_\* variables temporarily and observe scope**

Step A — Define variables (in one block; capture all three exports
together)

Run the three exports one after another:

<img src="CC Lab 07_Aimen/images/image2.png" style="width:6.5in;height:0.68056in" />

Step B — Echo them (three echoes together)

<img src="CC Lab 07_Aimen/images/image21.png" style="width:4.14583in;height:1.1875in" />

Step C — Show all DB\_ envs with grep

<img src="CC Lab 07_Aimen/images/image37.png" style="width:4.28125in;height:0.89583in" />

Step D — Close shell and reopen to show they disappear

Close the session:

<img src="CC Lab 07_Aimen/images/image43.png" style="width:3.77083in;height:0.98958in" />

Reconnect (from the Windows host or VM console). Then run these two
checks together

<img src="CC Lab 07_Aimen/images/image24.png" style="width:3.92708in;height:1.0625in" />

**Task 3 — Make DB\_\* variables persistent in ~/.bashrc**

Step A — Edit ~/.bashrc and add the three export lines (capture editor
showing the three lines)

<img src="CC Lab 07_Aimen/images/image22.png" style="width:5.00521in;height:4.09364in" />

Step B — Source ~/.bashrc and verify

<img src="CC Lab 07_Aimen/images/image34.png" style="width:4.21875in;height:2.02083in" />

Step C — Close and reopen terminal and verify persistence

Reconnect or open a new terminal and run:

<img src="CC Lab 07_Aimen/images/image25.png" style="width:5.84375in;height:2.17708in" />

**Task 4 — System-wide environment variable, welcome script, and PATH**

View /etc/environment (before)

<img src="CC Lab 07_Aimen/images/image35.png" style="width:6.5in;height:0.69444in" />

Show current PATH

<img src="CC Lab 07_Aimen/images/image20.png" style="width:6.5in;height:0.40278in" />

Edit /etc/environment and add Class="CC-\<your_class_name\>"

<img src="CC Lab 07_Aimen/images/image12.png" style="width:2.44792in;height:1.0625in" />

Then show the file after editing:

<img src="CC Lab 07_Aimen/images/image3.png" style="width:6.5in;height:0.84722in" />

Re-login or open a new shell and show Class and PATH together

<img src="CC Lab 07_Aimen/images/image46.png" style="width:5.28646in;height:1.72827in" />

Create ~/welcome script (capture heredoc creation and chmod together if
possible)

<img src="CC Lab 07_Aimen/images/image8.png" style="width:4.20313in;height:1.1214in" />

Run the script using ./welcome (from home directory)

<img src="CC Lab 07_Aimen/images/image51.png" style="width:3.41667in;height:0.6875in" />

Add home to PATH in ~/.bashrc

<img src="CC Lab 07_Aimen/images/image6.png" style="width:4.83854in;height:3.81689in" />

Source and run welcome

<img src="CC Lab 07_Aimen/images/image33.png" style="width:3.94792in;height:1.01042in" />

**Task 5 — Block and allow SSH using ufw (firewall)**

Enable ufw and show status

<img src="CC Lab 07_Aimen/images/image15.png" style="width:6.5in;height:3.02778in" />

Deny TCP port 22 and show numbered status

<img src="CC Lab 07_Aimen/images/image27.png" style="width:4.13542in;height:2.47917in" />

FROM WINDOWS HOST: attempt SSH (should fail) — capture client attempt

<img src="CC Lab 07_Aimen/images/image1.png" style="width:6.5in;height:0.59722in" />

Allow SSH back and reload & show status

<img src="CC Lab 07_Aimen/images/image17.png" style="width:3.72917in;height:1.39583in" />

<img src="CC Lab 07_Aimen/images/image26.png" style="width:4.85417in;height:2.23958in" />

FROM WINDOWS HOST: attempt SSH again

<img src="CC Lab 07_Aimen/images/image16.png" style="width:5.57292in;height:2.20833in" />

**Task 6 — Configure SSH key-based login from Windows host → Ubuntu
server**

Part A — On Windows host (client)

Generate ed25519 key pair (group the keygen and listing of ~/.ssh)’

<img src="CC Lab 07_Aimen/images/image50.png" style="width:6.45833in;height:2.95833in" />

<img src="CC Lab 07_Aimen/images/image38.png" style="width:4.90625in;height:2.59375in" />

Show the public key content

<img src="CC Lab 07_Aimen/images/image40.png" style="width:6.5in;height:0.63889in" />

Clear known_hosts and verify it's empty

<img src="CC Lab 07_Aimen/images/image7.png" style="width:5.02083in;height:0.65625in" />

Connect to Ubuntu server to accept host key

<img src="CC Lab 07_Aimen/images/image49.png" style="width:6.40625in;height:4.27083in" />

Show known_hosts after connect

<img src="CC Lab 07_Aimen/images/image30.png" style="width:6.5in;height:1.33333in" />

Part B — On Ubuntu server

Prepare ~/.ssh and clear authorized_keys

<img src="CC Lab 07_Aimen/images/image10.png" style="width:5.11458in;height:1.94792in" />

Append the public key from Windows into ~/.ssh/authorized_keys, set
permissions, and show file

Using SSH session paste

<img src="CC Lab 07_Aimen/images/image13.png" style="width:6.5in;height:1.13889in" />

From Windows host: test passwordless login

<img src="CC Lab 07_Aimen/images/image47.png" style="width:5.54167in;height:4.07292in" />

Demonstrate explicit identity usage

<img src="CC Lab 07_Aimen/images/image5.png" style="width:6.42708in;height:5.1875in" />

Server-side permission checks (optional verification):

<img src="CC Lab 07_Aimen/images/image41.png" style="width:6.36458in;height:1.21875in" />

## **Exam Evaluation Questions**

**Q1: Quick Environment Audit**

Display all environment variables

<img src="CC Lab 07_Aimen/images/image18.png" style="width:6.5in;height:5.08333in" />

Display PATH

<img src="CC Lab 07_Aimen/images/image29.png" style="width:6.5in;height:0.66667in" />

Display LANG

<img src="CC Lab 07_Aimen/images/image45.png" style="width:3.41667in;height:0.58333in" />

Display PWD

<img src="CC Lab 07_Aimen/images/image11.png" style="width:3.41667in;height:0.52083in" />

**Q2: Short-lived Student Info (Temporary Variables)**

Set three variables

<img src="CC Lab 07_Aimen/images/image42.png" style="width:4.83333in;height:0.77083in" />

Print the values

<img src="CC Lab 07_Aimen/images/image28.png" style="width:4.13542in;height:1.1875in" />

Show all STUDENT\_ variables

<img src="CC Lab 07_Aimen/images/image14.png" style="width:4.19792in;height:0.88542in" />

Close terminal

Open a NEW terminal

Check that variables are gone

<img src="CC Lab 07_Aimen/images/image23.png" style="width:4.78125in;height:1.35417in" />

**Q3: Make It Sticky (Persistent Variables)**

Open bashrc file

<img src="CC Lab 07_Aimen/images/image36.png" style="width:3.15625in;height:0.71875in" />

Verify variablesVerify variables

<img src="CC Lab 07_Aimen/images/image19.png" style="width:4.61458in;height:1.90625in" />

Close terminal and open a new one

Verify persistence

<img src="CC Lab 07_Aimen/images/image48.png" style="width:4.30208in;height:1.23958in" />

**Q4: Firewall: Block & Restore Ping (ICMP) Using UFW**

Enable UFW

<img src="CC Lab 07_Aimen/images/image31.png" style="width:6.5in;height:2.43056in" />

Block ping

<img src="CC Lab 07_Aimen/images/image32.png" style="width:5.16667in;height:1.85417in" />

From Windows machine, run:

<img src="CC Lab 07_Aimen/images/image44.png" style="width:5.26042in;height:1.77083in" />

Allow ping again

Remove deny OR allow icmp

<img src="CC Lab 07_Aimen/images/image39.png" style="width:5.42708in;height:2.54167in" />