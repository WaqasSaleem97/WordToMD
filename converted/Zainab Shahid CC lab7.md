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
> **SUBMITTED BY: Zainab Shahid**
>
> **REGISTRATION NO: 2023-BSE-072**
>
> **CLASS: BSSE V-B**

<img src="Zainab Shahid CC lab7_media/media/image1.jpeg" >

**Task 1 — Print & filter environment variables**

Goal: Show environment variables and filter them using grep.

task1_printenv_all:

<img src="Zainab Shahid CC lab7_media/media/image2.png" style="width:6.5in;height:3.49653in" />

task1_grep_shell_home_user:

<img src="Zainab Shahid CC lab7_media/media/image3.png" style="width:5.52083in;height:2.08333in" />

**Task 2 — Export DB\_\* variables temporarily and observe scope**

<img src="Zainab Shahid CC lab7_media/media/image4.png" style="width:6.5in;height:1.19583in" />

2.  Echo the three variables (run the three echo commands together) and
    capture one screenshot showing their outputs:

<img src="Zainab Shahid CC lab7_media/media/image5.png" style="width:3.88542in;height:1.0625in" />

3.  Show all DB\_ variables with a single grep command (capture that
    output):

<img src="Zainab Shahid CC lab7_media/media/image6.png" style="width:4.6875in;height:1in" />

4.  Close the bash session (e.g., exit) and reopen a new terminal.
    Verify the variables are gone by running the echo(s) and the grep
    together; capture both checks in one screenshot:

<img src="Zainab Shahid CC lab7_media/media/image7.png" style="width:4.19792in;height:0.94792in" />

**Task 3 — Make DB\_\* variables persistent in ~/.bashrc**

Goal: Add DB\_\* variables to ~/.bashrc, reload, and verify persistence.
Grouped captures: show the three export lines in ~/.bashrc together, and
group the post-source checks into one screenshot.

1.  Open ~/.bashrc in an editor and append the three export lines.
    Capture the editor showing the three lines added (single
    screenshot):

<img src="Zainab Shahid CC lab7_media/media/image8.png" style="width:5.4375in;height:1.09375in" />

2.  Source ~/.bashrc and capture the source command in one screenshot
    together with the next verification commands (grouped): run source
    ~/.bashrc and then immediately run the three echoes and a single
    grep, capturing all of these in one screenshot:

<img src="Zainab Shahid CC lab7_media/media/image9.png" style="width:5.32292in;height:1.98958in" />

<img src="Zainab Shahid CC lab7_media/media/image10.png" style="width:4.15625in;height:2.28125in" />

<img src="Zainab Shahid CC lab7_media/media/image11.png" style="width:4.28125in;height:0.94792in" />

3.  Close and reopen terminal. Verify persistence by running one echo
    and the grep together — capture both in one screenshot:

<img src="Zainab Shahid CC lab7_media/media/image12.png" style="width:4.72917in;height:1.41667in" />

**Task 4 — System-wide environment variable, welcome script, and PATH**

Goal: Add Class variable to /etc/environment, view PATH, create
a welcome script at ~/welcome, make it executable, and add PATH entry in
~/.bashrc so welcome can be executed without ./. Capture grouped
screenshots as applicable.

Steps and required screenshots (grouping applies to "print with grep"
type commands and grouped variable definitions — in this task there is a
single system variable definition so a standard per-action capture is
used):

1.  View /etc/environment:

<img src="Zainab Shahid CC lab7_media/media/image13.png" style="width:6.5in;height:0.80625in" />

2.  Show current PATH:

<img src="Zainab Shahid CC lab7_media/media/image14.png" style="width:6.5in;height:0.43194in" />

3.  Edit /etc/environment and add Class:

<img src="Zainab Shahid CC lab7_media/media/image15.png" style="width:6.5in;height:1.58958in" />

<img src="Zainab Shahid CC lab7_media/media/image16.png" style="width:6.5in;height:0.775in" />

5.  Create welcome script at your home directory (~/welcome) and make it
    executable (capture the heredoc creation and chmod together in one
    screenshot if possible):

<img src="Zainab Shahid CC lab7_media/media/image17.png" style="width:6.5in;height:1.44375in" />

6.  Run the script from your home directory using ./welcome:

<img src="Zainab Shahid CC lab7_media/media/image18.png" style="width:4.375in;height:1in" />

7.  Add your home directory to PATH in ~/.bashrc. NOTE: per your
    instruction we do not include an export PATH line here — only add
    the PATH modification line in the file. Capture the editor showing
    that PATH line in one screenshot:

<img src="Zainab Shahid CC lab7_media/media/image19.png" style="width:5.29167in;height:1.0625in" />

<img src="Zainab Shahid CC lab7_media/media/image20.png" style="width:3.875in;height:0.82292in" />

<img src="Zainab Shahid CC lab7_media/media/image21.png" style="width:3.40625in;height:0.54167in" />

**Task 5 — Block and allow SSH using ufw (firewall)**

Goal: Use ufw to deny and allow SSH then verify SSH connectivity changes
from host. Save screenshots after each logical command/step; group
related print checks when appropriate.

<img src="Zainab Shahid CC lab7_media/media/image22.png" style="width:4.98958in;height:1.4375in" />

2.  Deny TCP port 22 and show status (run deny and status
    numbered together and capture in one screenshot). Use short form as
    requested:

<img src="Zainab Shahid CC lab7_media/media/image23.png" style="width:5.64583in;height:2.98958in" />

3.  From Windows host attempt to SSH (expected to fail) — capture the
    host-side SSH attempt in one screenshot:

<img src="Zainab Shahid CC lab7_media/media/image24.png" style="width:6.125in;height:2.01042in" />

4.  Allow SSH back and reload, then show status (group allow, reload,
    status in one screenshot if run together). Use short form as
    requested:

<img src="Zainab Shahid CC lab7_media/media/image25.png" style="width:6.3125in;height:2.19792in" />

5.  From Windows host attempt SSH again (should succeed) — capture
    successful login in one screenshot:

<img src="Zainab Shahid CC lab7_media/media/image26.png" style="width:6.5in;height:4.64167in" />

**Task 6 — Configure SSH key-based login from Windows host**

Goal: Copy your public key from the Windows host into the Ubuntu
server's ~/.ssh/authorized_keys to allow passwordless SSH. Save grouped
screenshots for the client-side actions and the server-side
edits/checks.

<img src="Zainab Shahid CC lab7_media/media/image27.png" style="width:6.5in;height:3.0375in" />

<img src="Zainab Shahid CC lab7_media/media/image28.png" style="width:6.5in;height:1.71806in" />

2.  Show the public key content (single screenshot):

<img src="Zainab Shahid CC lab7_media/media/image29.png" style="width:6.5in;height:0.56458in" />

3.  Clear the known_hosts file content and verify it is empty (single
    screenshot):

<img src="Zainab Shahid CC lab7_media/media/image30.png" style="width:4.92708in;height:0.98958in" />

4.  Connect to the Ubuntu server using the standard SSH command (this
    will prompt to accept the server host key because known_hosts is
    empty). Capture the connection prompt/accept step in one screenshot:

<img src="Zainab Shahid CC lab7_media/media/image31.png" style="width:6.5in;height:3.89653in" />

5.  After the successful connection, view the known_hosts file to show
    the server host key was added (single screenshot):

<img src="Zainab Shahid CC lab7_media/media/image32.png" style="width:4.625in;height:0.80208in" />

6.Append the public key, set file permissions, and show the
resulting authorized_keys (capture commands and resulting file content
in one screenshot):

<img src="Zainab Shahid CC lab7_media/media/image33.png" style="width:6.5in;height:0.68333in" />

7.Append the public key, set file permissions, and show the
resulting authorized_keys (capture commands and resulting file content
in one screenshot)

<img src="Zainab Shahid CC lab7_media/media/image34.png" style="width:6.5in;height:0.77847in" />

3.  From Windows host test passwordless login (capture successful login
    in one screenshot):

<img src="Zainab Shahid CC lab7_media/media/image35.png" style="width:6.5in;height:4.63611in" />

**Exam Evaluation Questions**

**Q1: Quick Environment Audit**

- Objective: Demonstrate you can inspect the current environment and
  extract a few key variables.

- Actions & evidence:

  1.  Run a single command to display environment variables and capture
      its output.

      - Save screenshot: EE_q1_env_all.png

<img src="Zainab Shahid CC lab7_media/media/image36.png" style="width:6.5in;height:3.31458in" />

2.  In the same terminal session, run three filters (one per line) to
    show values for PATH, LANG, and PWD, then capture a single
    screenshot showing the three outputs together.

    - Save screenshot: EE_q1_env_filters.png

<img src="Zainab Shahid CC lab7_media/media/image37.png" style="width:6.5in;height:0.98194in" />

**Q2: Short-lived Student Info**

- Objective: Show how temporary environment variables behave
  (session-scoped).

- Actions & evidence:

  1.  In one terminal, set three variables (STUDENT_NAME,
      STUDENT_ROLL_NUMBER, STUDENT_SEMESTER) using export — execute all
      three consecutively and capture them in one screenshot (show the
      commands executed).

      - Save screenshot: EE_q2_exports.png

<img src="Zainab Shahid CC lab7_media/media/image38.png" style="width:6.46875in;height:0.76042in" />

2.  Still in the same session, print the three values with echo
    (grouped) and capture the outputs in one screenshot.

    - Save screenshot: EE_q2_echoes.png

<img src="Zainab Shahid CC lab7_media/media/image39.png" style="width:4.53125in;height:1.07292in" />

3.  Use a single printenv\|grep command to list any STUDENT\_ variables
    and capture the result.

    - Save screenshot: EE_q2_printenv_grep.png

<img src="Zainab Shahid CC lab7_media/media/image40.png" style="width:4.1875in;height:0.83333in" />

4.  Exit that shell, open a fresh terminal, and show that the STUDENT\_
    variables are not set (use echo and printenv\|grep together) —
    capture in one screenshot.

    - Save screenshot: EE_q2_after_restart.png

<img src="Zainab Shahid CC lab7_media/media/image41.png" style="width:4.89583in;height:1.44792in" />

**Q3: Make It Sticky (Persistence Check for Student Info)**

- Objective: Demonstrate persistence of environment variables across
  sessions via shell configuration.

- Actions & evidence:

  1.  Edit ~/.bashrc and append the three STUDENT\_\* exports. Capture a
      screenshot of the editor showing the new lines.

      - Save screenshot: EE_q3_bashrc_editor.png

<img src="Zainab Shahid CC lab7_media/media/image42.png" style="width:5.22917in;height:1.04167in" />

2.  Reload your shell config with a single command and then verify the
    three variables and show printenv \| grep '^STUDENT\_' — capture
    these verification outputs together in one screenshot.

    - Save screenshot: EE_q3_after_source.png

<img src="Zainab Shahid CC lab7_media/media/image43.png" style="width:4.82292in;height:2.04167in" />

3.  Close and re-open a terminal and demonstrate the STUDENT_NAME
    variable is available (echo and printenv grep together) — capture in
    one screenshot.

    - Save screenshot: EE_q3_after_restart.png

<img src="Zainab Shahid CC lab7_media/media/image44.png" style="width:4.80208in;height:1.41667in" />

**Q4: Firewall Rules: Block and Restore Ping (ICMP)**

- **Objective: Demonstrate you can block ping (ICMP echo) traffic using
  ufw and then re-allow it; show effect from a client.**

- **Actions & evidence:**

  1.  **Enable ufw and capture the enable command and status together in
      one screenshot.**

      - **Save screenshot: EE_q5_ufw_enable_status.png**

<img src="Zainab Shahid CC lab7_media/media/image45.png" style="width:5.17708in;height:1.09375in" />

<img src="Zainab Shahid CC lab7_media/media/image46.png" style="width:6.5in;height:4.72083in" />

2.  **Add a rule to block ping (ICMP echo) and show ufw status
    numbered in the same screenshot.**

    - **Suggested command example:**

    - **sudo ufw deny proto icmp from any to any**

**sudo ufw status numbered**

- **Save screenshot: EE_q5_ufw_deny_ping_status.png**

<img src="Zainab Shahid CC lab7_media/media/image47.png" style="width:6.5in;height:0.62153in" />

3.  **From your Windows host (or another client), attempt to ping the
    server while the rule is active and capture the blocked/failing ping
    in one screenshot.**

    - **Save screenshot: EE_q5_ping_blocked.png**

<img src="Zainab Shahid CC lab7_media/media/image48.png" style="width:5.07292in;height:2.82292in" />

4.  **Re-allow ping (ICMP) (or remove the deny rule) and capture the
    allow/reload/status sequence in one screenshot.**

    - **Suggested command example:**

    - **sudo ufw allow proto icmp from any to any**

    - **sudo ufw reload**

**sudo ufw status**

- **Save screenshot: EE_q5_ufw_allow_ping_status.png**

<img src="Zainab Shahid CC lab7_media/media/image49.png" style="width:6.5in;height:3.00069in" />

5.  **From the client, ping the server again and capture successful
    replies in one screenshot.**

    - **Save screenshot: EE_q5_ping_success.png**

<img src="Zainab Shahid CC lab7_media/media/image50.png" style="width:5.42708in;height:3.14583in" />