**Task 1 — Print & filter environment variables**

Goal: Show environment variables and filter them using grep.

Commands and required screenshots (grouped as requested):

1.  Print all environment variables:

printenv

- Save screenshot as: task1_printenv_all.png

<img src="CC Lab 7_media/media/image1.png" style="width:6.5in;height:3.32292in" />

2.  Filter for SHELL, HOME and USER — run these greps together and
    capture one combined screenshot:

printenv \| grep SHELL

printenv \| grep HOME

printenv \| grep USER

- Save screenshot as: task1_grep_shell_home_user.png (single screenshot
  showing all three grep outputs together)

<img src="CC Lab 7_media/media/image2.png" style="width:5.15697in;height:1.33352in" />

**Task 2 — Export DB\_\* variables temporarily and observe scope**

Goal: Create env variables with export in the current shell, verify
them, then close shell and show variables are gone.

Per the requested grouping rule: capture all the variable-definition
(export) commands in a single screenshot; capture the echo/print checks
grouped logically.

Steps and required screenshots:

1.  Define all DB\_\* variables (run the three exports one after
    another). Capture them in one screenshot showing the three export
    commands and their execution:

export DB_URL="postgres://db.example.local:5432/mydb"

export DB_USER="labuser"

export DB_PASSWORD="labpass123"

- Save screenshot as: task2_exports_all.png (single screenshot showing
  all three export commands shown/executed)

<img src="CC Lab 7_media/media/image3.png" style="width:6.5in;height:0.77847in" />

2.  Echo the three variables (run the three echo commands together) and
    capture one screenshot showing their outputs:

echo "\$DB_URL"

echo "\$DB_USER"

echo "\$DB_PASSWORD"

- Save screenshot as: task2_echoes_all.png

<img src="CC Lab 7_media/media/image4.png" style="width:4.78192in;height:1.39603in" />

3.  Show all DB\_ variables with a single grep command (capture that
    output):

printenv \| grep '^DB\_'

- Save screenshot as: task2_printenv_grep_db.png

<img src="CC Lab 7_media/media/image5.png" style="width:5.31324in;height:1.04181in" />

4.  Close the bash session (e.g., exit) and reopen a new terminal.
    Verify the variables are gone by running the echo(s) and the grep
    together; capture both checks in one screenshot:

echo "\$DB_URL"

printenv \| grep '^DB\_'

- Save screenshot as: task2_after_restart_checks.png (single screenshot
  showing echo (empty) and printenv \| grep '^DB\_' with no results)

<img src="CC Lab 7_media/media/image6.png" style="width:5.08404in;height:1.2085in" />

**Task 3 — Make DB\_\* variables persistent in ~/.bashrc**

Goal: Add DB\_\* variables to ~/.bashrc, reload, and verify persistence.
Grouped captures: show the three export lines in ~/.bashrc together, and
group the post-source checks into one screenshot.

Steps and required screenshots:

1.  Open ~/.bashrc in an editor and append the three export lines.
    Capture the editor showing the three lines added (single
    screenshot):

vim ~/.bashrc

\# add at the end:

\# Lab 7 persistent DB variables

export DB_URL="postgres://db.example.local:5432/mydb"

export DB_USER="labuser"

export DB_PASSWORD="labpass123"

- Save screenshot as: task3_bashrc_added.png (single screenshot showing
  the three export lines in the editor)

<img src="CC Lab 7_media/media/image7.png" style="width:5.50077in;height:1.21892in" />

2.  Source ~/.bashrc and capture the source command in one screenshot
    together with the next verification commands (grouped): run source
    ~/.bashrc and then immediately run the three echoes and a single
    grep, capturing all of these in one screenshot:

source ~/.bashrc

echo "\$DB_URL"

echo "\$DB_USER"

echo "\$DB_PASSWORD"

printenv \| grep '^DB\_'

- Save screenshot as: task3_source_and_verification.png (single
  screenshot showing source, the three echoes, and the grep output)

> style="width:5.36533in;height:2.19822in" />

> <img src="CC Lab 7_media/media/image8.png" >

3.  Close and reopen terminal. Verify persistence by running one echo
    and the grep together — capture both in one screenshot:

echo "\$DB_URL"

printenv \| grep '^DB\_'

- Save screenshot as: task3_after_restart_persistent.png (single
  screenshot showing echo with value and grep output listing DB\_
  variables)

<img src="CC Lab 7_media/media/image9.png" style="width:5.44868in;height:1.57314in" />

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

sudo cat /etc/environment

- Save screenshot as: task4_etc_environment_before.png

<img src="CC Lab 7_media/media/image10.png" style="width:6.5in;height:0.72986in" />

2.  Show current PATH:

echo "\$PATH"

- Save screenshot as: task4_echo_path_before.png

<img src="CC Lab 7_media/media/image11.png" style="width:6.5in;height:0.56944in" />

3.  Edit /etc/environment and add Class:

sudo vim /etc/environment

\# add line: Class="CC-\<your_class_name\>"

- Save screenshot as: task4_etc_environment_edit_vim.png (editor with
  edit)

<img src="CC Lab 7_media/media/image12.png" style="width:6.5in;height:0.56597in" />

- Save screenshot as: task4_etc_environment_after.png (cat or editor
  view showing the new Class line)

<img src="CC Lab 7_media/media/image13.png" style="width:6.5in;height:0.61319in" />

4.  Re-login or open a new shell and show Class and PATH together
    (grouped prints): run echo \$Class and echo \$PATH together and
    capture in a single screenshot:

echo \$Class

echo "\$PATH"

- Save screenshot as: task4_echo_class_and_path.png (single screenshot
  showing both outputs)

<img src="CC Lab 7_media/media/image14.png" style="width:6.5in;height:4.84653in" />

5.  Create welcome script at your home directory (~/welcome) and make it
    executable (capture the heredoc creation and chmod together in one
    screenshot if possible):

cat \> ~/welcome \<\<'EOF'

\#!/bin/bash

echo "Welcome to Cloud Computing \$USER"

EOF

chmod +x ~/welcome

- Save screenshot as: task4_welcome_create_and_chmod.png (single
  screenshot showing heredoc creation command and chmod output/listing)

<img src="CC Lab 7_media/media/image15.png" style="width:6.5in;height:1.53611in" />

6.  Run the script from your home directory using ./welcome:

cd ~

./welcome

- Save screenshot as: task4_welcome_run_dot.png

<img src="CC Lab 7_media/media/image16.png" style="width:4.11516in;height:0.90638in" />

7.  Add your home directory to PATH in ~/.bashrc. NOTE: per your
    instruction we do not include an export PATH line here — only add
    the PATH modification line in the file. Capture the editor showing
    that PATH line in one screenshot:

vim ~/.bashrc

\# add at end:

PATH=\$PATH:~

- Save screenshot as: task4_bashrc_path_line.png (editor screenshot
  showing the PATH line only)

<img src="CC Lab 7_media/media/image17.png" style="width:2.16697in;height:0.55216in" />

8.  Apply the change and run welcome — capture these runtime commands in
    a separate screenshot (must be taken separately from the editor
    screenshot):

source ~/.bashrc

cd ~

welcome

- Save screenshot as: task4_bashrc_source_and_welcome.png (single
  screenshot showing the source command and the welcome output)

> style="width:4.57356in;height:1.01056in" />

> <img src="CC Lab 7_media/media/image18.png" >

**Task 5 — Block and allow SSH using ufw (firewall)**

Goal: Use ufw to deny and allow SSH then verify SSH connectivity changes
from host. Save screenshots after each logical command/step; group
related print checks when appropriate.

Steps and required screenshots:

1.  Enable ufw and show status (group both commands in one screenshot if
    you run them together):

sudo ufw enable

sudo ufw status verbose

- Save screenshot as: task5_ufw_enable_and_status.png

<img src="CC Lab 7_media/media/image19.png" style="width:5.5216in;height:1.59397in" />

2.  Deny TCP port 22 and show status (run deny and status
    numbered together and capture in one screenshot). Use short form as
    requested:

sudo ufw deny 22/tcp

sudo ufw status numbered

- Save screenshot as: task5_ufw_deny_22_and_status.png

<img src="CC Lab 7_media/media/image20.png" style="width:5.87582in;height:2.20864in" />

3.  From Windows host attempt to SSH (expected to fail) — capture the
    host-side SSH attempt in one screenshot:

ssh username@\<server_ip\>

- Save screenshot as: task5_ssh_attempt_blocked.png

<img src="CC Lab 7_media/media/image21.png" style="width:6.5in;height:2.03542in" />

4.  Allow SSH back and reload, then show status (group allow, reload,
    status in one screenshot if run together). Use short form as
    requested:

sudo ufw allow 22/tcp

sudo ufw reload

sudo ufw status

- Save screenshot as: task5_ufw_allow_reload_status.png

<img src="CC Lab 7_media/media/image22.png" style="width:5.98in;height:2.5316in" />

5.  From Windows host attempt SSH again (should succeed) — capture
    successful login in one screenshot:

ssh username@\<server_ip\>

- Save screenshot as: task5_ssh_success_after_allow.png

<img src="CC Lab 7_media/media/image23.png" style="width:5.16323in;height:4.72193in" />

**Task 6 — Configure SSH key-based login from Windows host**

Goal: Copy your public key from the Windows host into the Ubuntu
server's ~/.ssh/authorized_keys to allow passwordless SSH. Save grouped
screenshots for the client-side actions and the server-side
edits/checks.

A. On Windows host (client) — group related client actions:

1.  Generate ed25519 key pair (if needed) and show the generated files
    in one screenshot (run ssh-keygen and then list ~/.ssh):

ssh-keygen -t ed25519 -f ~/.ssh/id_lab7 -C "lab_key"

ls -la ~/.ssh

- Save screenshot as: task6_windows_sshkey_and_list.png (single
  screenshot showing keygen result and ls of .ssh folder)

<img src="CC Lab 7_media/media/image24.png" style="width:5.89974in;height:5.13643in" />

<img src="CC Lab 7_media/media/image25.png" style="width:5.19615in;height:3.47243in" />

2.  Show the public key content (single screenshot):

type \$env:USERPROFILE\\ssh\id_lab7.pub

\# or on Git Bash: cat ~/.ssh/id_lab7.pub

- Save screenshot as: task6_windows_public_key.png

<img src="CC Lab 7_media/media/image26.png" style="width:6.5in;height:0.87153in" />

3.  Clear the known_hosts file content and verify it is empty (single
    screenshot):

\# Clear contents (PowerShell)

Clear-Content \$env:USERPROFILE\\ssh\known_hosts

\# View the file (should be empty)

type \$env:USERPROFILE\\ssh\known_hosts

- Save screenshot as: task6_windows_known_hosts_cleared_and_empty.png

<img src="CC Lab 7_media/media/image27.png" style="width:5.1995in;height:1.76872in" />

4.  Connect to the Ubuntu server using the standard SSH command (this
    will prompt to accept the server host key because known_hosts is
    empty). Capture the connection prompt/accept step in one screenshot:

ssh username@\<server_ip\>

\# Accept the host key prompt (yes) and complete the login (enter
password or key passphrase)

- Save screenshot as: task6_windows_ssh_accept_hostkey_and_login.png

<img src="CC Lab 7_media/media/image28.png" style="width:6.5in;height:4.86667in" />

<img src="CC Lab 7_media/media/image29.png" style="width:6.5in;height:2.31042in" />

5.  After the successful connection, view the known_hosts file to show
    the server host key was added (single screenshot):

type \$env:USERPROFILE\\ssh\known_hosts

- Save screenshot as: task6_windows_known_hosts_after_connect.png

<img src="CC Lab 7_media/media/image30.png" style="width:6.5in;height:1.51458in" />

B. On Ubuntu server — group related server-side commands:

1.  Prepare the ~/.ssh directory and clear authorized_keys (this will
    create the directory if missing, set the correct directory
    permissions, and truncate the authorized_keys file). Capture this
    command sequence and its output in one screenshot:

mkdir -p ~/.ssh

chmod 700 ~/.ssh

\> ~/.ssh/authorized_keys

- Save screenshot as: task6_server_clear_authorized_keys.png

<img src="CC Lab 7_media/media/image31.png" style="width:6.5in;height:1.54931in" />

2.  Append the public key, set file permissions, and show the
    resulting authorized_keys (capture commands and resulting file
    content in one screenshot):

\# paste public key name id_lab7.pub from Windows client into the echo
below

echo "ssh-ed25519 AAAA... yourpublickey ... comment" \>\>
~/.ssh/authorized_keys

chmod 600 ~/.ssh/authorized_keys

cat ~/.ssh/authorized_keys

- Save screenshot as: task6_server_add_key_and_show.png (single
  screenshot showing the commands and resulting authorized_keys content)

> style="width:6.5in;height:0.87569in" />

> <img src="CC Lab 7_media/media/image32.png" >

3.  From Windows host test passwordless login (capture successful login
    in one screenshot):

ssh username@\<server_ip\>

- Save screenshot as: task6_ssh_passwordless_login.png

<img src="CC Lab 7_media/media/image33.png" style="width:4.88663in;height:4.10404in" />

4.  Also demonstrate explicit identity usage (single screenshot):

ssh -i ~/.ssh/id_lab7 username@\<server_ip\>

- Save screenshot as: task6_ssh_with_identity_file.png

<img src="CC Lab 7_media/media/image34.png" style="width:4.11797in;height:3.61906in" />

<img src="CC Lab 7_media/media/image35.png" style="width:5.28336in;height:4.36328in" />

Important notes:

- Do NOT show or upload private key files.

- Ensure server-side permissions are
  strict: ~/.ssh 700, authorized_keys 600.

**Exam Evaluation Questions**

**Q1: Quick Environment Audit**

- Objective: Demonstrate you can inspect the current environment and
  extract a few key variables.

- Actions & evidence:

  1.  Run a single command to display environment variables and capture
      its output.

      - Save screenshot: EE_q1_env_all.png

<img src="CC Lab 7_media/media/image36.png" style="width:6.5in;height:3.64583in" />

2.  In the same terminal session, run three filters (one per line) to
    show values for PATH, LANG, and PWD, then capture a single
    screenshot showing the three outputs together.

    - Save screenshot: EE_q1_env_filters.png

<img src="CC Lab 7_media/media/image37.png" style="width:6.5in;height:0.86389in" />

**Q2: Short-lived Student Info**

- Objective: Show how temporary environment variables behave
  (session-scoped).

- Actions & evidence:

  1.  In one terminal, set three variables (STUDENT_NAME,
      STUDENT_ROLL_NUMBER, STUDENT_SEMESTER) using export — execute all
      three consecutively and capture them in one screenshot (show the
      commands executed).

      - Save screenshot: EE_q2_exports.png

<img src="CC Lab 7_media/media/image38.png" style="width:6.5in;height:0.8875in" />

2.  Still in the same session, print the three values with echo
    (grouped) and capture the outputs in one screenshot.

    - Save screenshot: EE_q2_echoes.png

> style="width:6.12586in;height:1.41686in" />

> <img src="CC Lab 7_media/media/image39.png" >

3.  Use a single printenv\|grep command to list any STUDENT\_ variables
    and capture the result.

    - Save screenshot: EE_q2_printenv_grep.png

<img src="CC Lab 7_media/media/image40.png" style="width:5.05279in;height:1.00014in" />

4.  Exit that shell, open a fresh terminal, and show that the STUDENT\_
    variables are not set (use echo and printenv\|grep together) —
    capture in one screenshot.

    - Save screenshot: EE_q2_after_restart.png

<img src="CC Lab 7_media/media/image41.png" style="width:6.20614in;height:6.23332in" />

**Q3: Make It Sticky (Persistence Check for Student Info)**

- Objective: Demonstrate persistence of environment variables across
  sessions via shell configuration.

- Actions & evidence:

  1.  Edit ~/.bashrc and append the three STUDENT\_\* exports. Capture a
      screenshot of the editor showing the new lines.

      - Save screenshot: EE_q3_bashrc_editor.png

<img src="CC Lab 7_media/media/image42.png" style="width:6.06335in;height:2.6462in" />

2.  Reload your shell config with a single command and then verify the
    three variables and show printenv \| grep '^STUDENT\_' — capture
    these verification outputs together in one screenshot.

    - Save screenshot: EE_q3_after_source.png

<img src="CC Lab 7_media/media/image43.png" style="width:5.64662in;height:2.34408in" />

3.  Close and re-open a terminal and demonstrate the STUDENT_NAME
    variable is available (echo and printenv grep together) — capture in
    one screenshot.

    - Save screenshot: EE_q3_after_restart.png

<img src="CC Lab 7_media/media/image44.png" style="width:6.5in;height:6.06319in" />

**Q4: Firewall Rules: Block and Restore Ping (ICMP)**

- Objective: Demonstrate you can block ping (ICMP echo) traffic using
  ufw and then re-allow it; show effect from a client.

- Actions & evidence:

  1.  Enable ufw and capture the enable command and status together in
      one screenshot.

      - Save screenshot: EE_q5_ufw_enable_status.png

<img src="CC Lab 7_media/media/image45.png" style="width:5.66746in;height:2.65662in" />

2.  Add a rule to block ping (ICMP echo) and show ufw status numbered in
    the same screenshot.

    - Suggested command example:

sudo ufw deny proto icmp from any to any

sudo ufw status numbered

- Save screenshot: EE_q5_ufw_deny_ping_status.png

<img src="CC Lab 7_media/media/image46.png" style="width:6.49049in;height:1.86484in" />

3.  From your Windows host (or another client), attempt to ping the
    server while the rule is active and capture the blocked/failing ping
    in one screenshot.

    - Save screenshot: EE_q5_ping_blocked.png

<img src="CC Lab 7_media/media/image47.png" style="width:6.5in;height:3.00972in" />

4.  Re-allow ping (ICMP) (or remove the deny rule) and capture the
    allow/reload/status sequence in one screenshot.

    - Suggested command example:

    - sudo ufw allow proto icmp from any to any

    - sudo ufw reload

sudo ufw status

- Save screenshot: EE_q5_ufw_allow_ping_status.png

<img src="CC Lab 7_media/media/image48.png" style="width:6.5in;height:7.34375in" />

5.  From the client, ping the server again and capture successful
    replies in one screenshot.

    - Save screenshot: EE_q5_ping_success.png

<img src="CC Lab 7_media/media/image49.png" style="width:6.5in;height:3.75694in" />

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
