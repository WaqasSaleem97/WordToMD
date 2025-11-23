Fatima Jinnah Women University

> *Department of Software Engineering*
>
>   style="width:1.61597in;height:1.61597in" />
>
> *----------------------------------------------------------------------------------------------------------------------------------------*
>
> <u>LAB \#07</u>
>
> **SUBJECT: CLOUD COMPUTING**
>
> **SUBMITTED TO: SIR MUHAMMAD SHOAIB**
>
> **SUBMITTED BY: UMBER QASIM**
>
> **REGISTRATION NO: 2023-BSE-066**
>
> **CLASS: BSSE V-B**

> <img src="Umber_media/media/image1.jpeg" >

***<u>Environment Variables, PATH, UFW, and SSH Key
Authentication</u>***

**<u>Task#01:</u> Print & filter environment variables**

***Print all environment variables***

<img src="Umber_media/media/image2.png" style="width:6.5in;height:3.77431in" />

***Filter specific variables***

<img src="Umber_media/media/image3.png" style="width:4.08333in;height:1.02083in" />

**<u>Task#02:</u> Export DB\_\* variables temporarily and observe
scope**

***Define (export) variables***

<img src="Umber_media/media/image4.png" style="width:6.5in;height:0.49931in" />

***Echo the variables***

<img src="Umber_media/media/image5.png" style="width:4.03125in;height:1.03125in" />

***Filter only DB\_ variables using grep***

<img src="Umber_media/media/image6.png" style="width:4.15625in;height:0.70833in" />

***Close and reopen terminal***

<img src="Umber_media/media/image7.png" style="width:6.5in;height:5.67569in" />

**<u>Task#03:</u> Make DB\_\* variables persistent in ~/.bashrc**

***Open ~/.bashrc and variables***

<img src="Umber_media/media/image8.png" style="width:5.78125in;height:2.69792in" />

***Reload (source) and verify***

<img src="Umber_media/media/image9.png" style="width:4.17708in;height:2.04167in" />

***Close terminal and reopen***

<img src="Umber_media/media/image10.png" style="width:4.15625in;height:1.04167in" />

**<u>Task#04:</u> System-wide environment variable, welcome script, and
PATH**

***View /etc/environment (before editing)***

<img src="Umber_media/media/image11.png" style="width:6.5in;height:0.39931in" />

***Show current PATH***

<img src="Umber_media/media/image12.png" style="width:6.5in;height:0.29167in" />

***Edit /etc/environment and add Class variable***

<img src="Umber_media/media/image13.png" style="width:6.5in;height:0.52569in" />

<img src="Umber_media/media/image14.png" style="width:6.5in;height:0.37569in" />

<img src="Umber_media/media/image15.png" style="width:6.5in;height:0.55417in" />

***Create ~/welcome script and make it executable***

<img src="Umber_media/media/image16.png" style="width:4.40625in;height:0.84375in" />

***Run script with ./welcome***

<img src="Umber_media/media/image17.png" style="width:3.9375in;height:0.6875in" />

***Add PATH modification line to ~/.bashrc***

<img src="Umber_media/media/image18.png" style="width:6.5in;height:3.78125in" />

***Reload and verify you can run welcome directly***

<img src="Umber_media/media/image19.png" style="width:3.82292in;height:0.69792in" />

**<u>Task#05:</u> Block and allow SSH using ufw (firewall)**

***Enable UFW and show status***

<img src="Umber_media/media/image20.png" style="width:5.15625in;height:1.375in" />

***Deny SSH (port 22) and check status***

<img src="Umber_media/media/image21.png" style="width:5.23958in;height:1.80208in" />

***Attempt SSH from Windows host (should fail)***

<img src="Umber_media/media/image22.png" style="width:5.79167in;height:0.63542in" />

***Allow SSH back and reload firewall***

<img src="Umber_media/media/image23.png" style="width:3.94792in;height:1.84532in" />

***Attempt SSH again from Windows host (should succeed)***

<img src="Umber_media/media/image24.png" style="width:4.8087in;height:3.82292in" />

**<u>Task#06:</u> Configure SSH key-based login from Windows host**

***Generate SSH key pair (ed25519)***

<img src="Umber_media/media/image25.png" style="width:4.48958in;height:3.97026in" />

***Show the public key content***

<img src="Umber_media/media/image26.png" style="width:6.5in;height:0.59167in" />

***Clear known_hosts file***

<img src="Umber_media/media/image27.png" style="width:2.70833in;height:0.85417in" />

***First SSH connection to server***

<img src="Umber_media/media/image28.png" style="width:6.05208in;height:5.01495in" />

***Verify known_hosts updated***

<img src="Umber_media/media/image29.png" style="width:6.5in;height:0.58542in" />

***Prepare ~/.ssh directory & clear authorized_keys***

<img src="Umber_media/media/image30.png" style="width:4.55208in;height:0.70833in" />

***Add public key & set permissions***

<img src="Umber_media/media/image31.png" style="width:6.5in;height:0.37847in" />

***Test SSH Key-Based Login from Windows host (passwordless)***

<img src="Umber_media/media/image32.png" style="width:6.27083in;height:4.80208in" />

**<u>Exam Evaluation Questions</u>**

1.  **<u>Quick Environment Audit</u>**

***Display environment variables***

<img src="Umber_media/media/image33.png" style="width:6.5in;height:3.52847in" />

***Showing values for PATH, LANG, and PWD***

<img src="Umber_media/media/image34.png" style="width:6.5in;height:0.69514in" />

2.  **<u>Short-lived Student Info</u>**

***Set three variables (STUDENT_NAME, STUDENT_ROLL_NUMBER,
STUDENT_SEMESTER) using export***

<img src="Umber_media/media/image35.png" style="width:5.85417in;height:0.53125in" />

***Print the three values with echo (grouped)***

<img src="Umber_media/media/image36.png" style="width:5.34375in;height:1.01042in" />

***Single printenv\|grep command to list any STUDENT\_ variable***

<img src="Umber_media/media/image37.png" style="width:3.82142in;height:0.5913in" />

***Open a fresh terminal, and show that the STUDENT\_ variables are not
set (use echo and printenv\|grep together)***

<img src="Umber_media/media/image38.png" style="width:4.92708in;height:0.84375in" />

3.  **<u>Make It Sticky (Persistence Check for Student Info)</u>**

***Edit the ~/.bashrc file***

<img src="Umber_media/media/image39.png" style="width:3.52083in;height:0.57292in" />

***Reload Config and Verify***

<img src="Umber_media/media/image40.png" style="width:4.33333in;height:0.85417in" />

***Persistence*** ***Demonstration***

<img src="Umber_media/media/image41.png" style="width:3.96522in;height:1.13424in" />

4.  **<u>Firewall Rules: Block and Restore Ping (ICMP)</u>**

***UFW Enable and Status Check***

<img src="Umber_media/media/image42.png" style="width:3.49057in;height:1.40444in" />

***Ping (ICMP) Block:***

<img src="Umber_media/media/image43.png" style="width:6.5in;height:0.53889in" />

***Ping the server while the rule is active and capture the
blocked/failing:***

<img src="Umber_media/media/image44.png" style="width:3.82292in;height:1.53849in" />

***Re-allow ping (ICMP):***

<img src="Umber_media/media/image45.png" style="width:6.5in;height:0.3625in" />

***Capture the allow/reload:***

<img src="Umber_media/media/image46.png" style="width:4.40625in;height:2.65713in" />