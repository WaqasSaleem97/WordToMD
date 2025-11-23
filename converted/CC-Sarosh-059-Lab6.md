                              Cloud Computing (Lab 6
                                                   6)

Name : Sarosh Majeed

Reg no : 2023-BSE-059

Task 1 – Switch to root with su - and back to a normal user Goal:
Demonstrate switching to the root account using su - and exiting back to
your normal user.

Set a root password (Ubuntu root is disabled by default; this enables
su - temporarily for the lab):

sudo passwd root

# Enter a temporary root password for the lab

Switch to root and verify:

su - whoami id

Switch back to your normal user: exit whoami

Task 2 – Create user tom and verify in passwd/group/shadow Goal: Create
a user named tom, then verify the account in system files files.

Create user tom (interactive, sets password and home directory): sudo
adduser tom Verify tom in system files (view and visually confirm
presence): cat /etc/passwd

cat /etc/group

sudo cat /etc/shadow

Notes: /etc/shadow stores password hashes (not plaintext). You must use
sudo to read it.

Task 3 – Create groups; change tom’s primary and secondary groups Goal:
Create groups developer, devops, and designer. Change tom’s primary
group and manage secondary groups.

Create groups and verify by viewing /etc/group (visually confirm entries
exist):

sudo groupadd developer

sudo groupadd devops

sudo groupadd designer

cat /etc/group

Change tom’s primary group to designer and verify:

sudo usermod -g designer tom

id tom

Add secondary groups developer and devops to tom and verify:

sudo usermod -aG aG developer,devops tom

id tom

groups tom

Replace all secondary groups so only tom (user’s own group) remains and
verify:

sudo usermod -G tom tom

id tom

groups tom Task 4 – Create/delete users (Jerry, Scooby) and groups
(jolly, anime) Goal: Create users using both adduser and useradd,
demonstrate login/password/home directory differences, then delete
users/groups.

Create users: sudo adduser Jerry sudo useradd Scooby

Try to log in as Scooby immediately (expected authentication failure
because there is no password yet): su – Scooby

Set a password for Scooby: sudo passwd Scooby

Try logging in as Scooby again (home directory still missing; expect a
message such as “No directory, direc logging in with HOME=/”): su -
Scooby

Show that Scooby’s home directory does not exist yet and what
/etc/passwd says:

exit

cat /etc/passwd ls -ld /home/Scooby

Manually create Scooby’s home directory and set proper ownership and
permissions:

sudo mkdir -p /home/Scooby

sudo chown Scooby:Scooby /home/Scooby

sudo chmod 750 /home/Scooby

ls -ld /home/Scooby

Log in as Scooby again and verify you land in the correct home
directory:

su - Scooby

pwd

ls -la

Verify users in system files and observe shell of Scooby: exit cat
/etc/passwd Change the shell from /bin/sh to /bin/bash

sudo usermod -ss /bin/bash Scooby

su - Scooby

Create groups:

sudo addgroup jolly

sudo groupadd anime

Verify groups: cat /etc/group Delete groups and users:

sudo delgroup jolly

sudo groupdel anime

cat /etc/group

sudo deluser –remove-home home Jerry

sudo userdel -r Scooby

cat /etc/passwd

Task 5 – Create user Student; create files; set owner/group; identify
file types Create Student: sudo adduser Student

Switch to Student and create files:

su - Student

touch file1

mkdir -p dir1

touch dir1/file2

ls –l

Change owner then group for file1 (separate commands):

sudo chown tom file1

ls -l file1

sudo chgrp devops file1

ls -l file1 Identify files/directories and show /dev/null:

ls -l

ls -l dir1

ls -l /dev/null

file file1 dir1 /dev/null

Exit Student: exit

Task 6 – Change permissions using symbolic mode Target file: ~/file1
(run these as the Student user)

Ensure Student and file present:

su - Student

cd ~

ls -l file1

Remove all permissions:

chmod -rwx file1 ls -l file1

Add read to all:

chmod +r file1

ls -l file1

Add execute to user:

chmod u+x file1

ls -l file1

Add write to user and group:

chmod ug+w file1

ls -l file1

Remove all permissions (explicit):

chmod ugo-rwx file1

ls -l file1

Task 7 – Change permissions using “set” symbolic form (u= g= o=) Ensure
you are Student: su - Student

cd ~

ls -l file1

Set all to rwx:

chmod u=rwx,g=rwx,o=rwx file1

ls -l file1

Remove execute from group and others:

chmod g=rw,o=rw file1

ls -l file1

Remove all permissions:

chmod u=,g=,o= file1

ls -l file1

Task 8 – Change permissions using numeric (octal) mode Ensure you are
Student: su - Student

cd ~

ls -l file1

Run each command and capture pture screenshot after each ls:

chmod 777 file1

ls -l file1

chmod 700 file1

ls -l file1

chmod 744 file1

ls -l file1

chmod 640 file1

ls -l file1

chmod 664 file1

ls -l file1 chmod 775 file1

ls -l file1

chmod 750 file1

ls -l file1

Task 9 – Practice pipes, pagers, grep, and redirects with
/var/log/syslog less:

sudo cat /var/log/syslog \| less

# quit q \#arrow keys to move

more: sudo cat /var/log/syslog \| more

# quit q \#spacebar to move

grep failures/errors: sudo grep -EE ‘fail\|error’ /var/log/syslog \|
head

# E enables extended regex \# head shows only the first 10 result

redirect: sudo grep -ii systemd /var/log/syslog \> ~/syslog_systemd.txt

# \> creates or overwrites the file.

append: sudo grep -ii network /var/log/syslog \>\> ~/syslog_systemd.txt

cat ~/syslog_systemd.txt

# \>\> appends (adds at the end without deleting old

Alternative (journalctl) if needed:

sudo journalctl \| less

sudo journalctl -u systemd \| grep –i error \> ~/journal_errors.txt

Task 10 – Script setup.sh – variables, command substitution, file/dir
checks, permissions (use vim) Goal: Using vim, write a script named
setup.sh that implements each numbered step below. After writing the
code for each step, run the script and capture screenshots showing the
vim editor (script content) and the script output for that step.
Students must add the code for each step into the same file setup.sh
step-by-step step (i.e., write 1., save, run and screenshot; then append
2., save, run and screenshot; and so on).

For each step you MUST:

Open vim and edit setup.sh

Insert only the code shown for that ste step (append to the existing
file)

Save and quit vim (:wq)

Make the file executable if not already: chmod +x setup.sh

Run the script: ./setup.sh

Capture two screenshots: One showing the vim editor with the script
content after you added the step (use the vim screen before :wq)

One showing the terminal output after running the script (show the
command and the output)

Start in your Student home directory (recommended).

------------------------------------------------------------------------

Include bash shebang

Code to add (enter in vim as the first line of the file):

\#!/bin/bash

Steps:

vim setup.sh → add the shebang line → save and quit

chmod +x setup.sh

./setup.sh

script run output (likely no output but show ./setup.sh run)

Define variable var1 and echo it

Code to append: # Define and show var1

var1=“Hello from Lab 6”

echo “var1: \$var1”

Steps:

vim setup.sh → append the code above → save and quit

./setup.sh

Save output of ls -ll into variable allFiles and echo it

Code to append:

# Save ls -l to variable and display

allFiles=“\$(ls -l)”

echo “allFiles (ls -l):”

echo “\$allFiles”

Steps:

vim setup.sh → append the code above → save and quit ./setup.sh

If directory dir1 exists echo a message; else create it

Code to append:

# Directory check

if \[ -d “dir1” \]; then

echo “Directory dir1 exists.”

else

echo “Directory dir1 does not exist. Creating…”

mkdir -p “dir1”

echo “Directory dir1 created.”

fi

Steps:

vim setup.sh → append the code above → save and quit

./setup.sh script run output showing directory message or creation If
file dir1/file2 does not exist, create it

Code to append:

# File check

if \[ -f “dir1/file2” \]; then

echo “file2 already exists.”

else

echo “file2 does not exist. Creating…”

touch “dir1/file2”

chmod a-rwx “dir1/file2”

echo “file2 created.”

fi

Steps:

vim setup.sh → append the code above → save and quit

./setup.sh script run output showing file creation message or existence
Check read, write, execute permissions on dir1/file2; grant missing user
perms and show final ls

Code to append:

# Permission checks for dir1/file2 (user permissions)

f=“dir1/file2”

if \[ ! -r “\$f” \]; then

echo “Read permission missing; granting to user…”

chmod u+r “\$f”

fi

if \[ ! -w “\$f” \]; then

echo “Write permission missing; granting to user…”

chmod u+w “\$f”

fi

if \[ ! -x “\$f” \]; then

echo “Execute permission missing; granting to user…”

chmod u+x “\$f”

fi

echo “Final permissions for \$f:”

ls -l “\$f”

Steps:

vim setup.sh → append the code above → save and quit

./setup.sh script run output showing the permission grants and final ls
-l dir1/file2 Important notes for Task 10:

Students MUST add the code incrementally exactly as described above (do
not replace the file each time — append).

Capture the vim editor screen (showing your code in the buffer) before
you save and quit for each step (these are the task10_b\*\_vim.png
files).

After saving, aving, run the script and capture the terminal output for
that run (these are the task10_b\*\_run.png files).

If a step reports that a directory/file already exists, that is
acceptable — still capture the output screenshot showing the script’s
message.

Task 11 – Script setup.sh – argument comparisons (eq, ne, gt, lt, ge,
le) and string checks Updated: replace the previous single single-script
approach with an incremental exercise. Students will overwrite setup.sh
and then add each individual if if-test one-by-one. one. After adding
each if-test if they must run the script with example arguments and
capture screenshots. This teaches the individual comparison operators
and makes each if sstatement a separate step.

Important overall instructions

Start by overwriting setup.sh (vim setup.sh) and add only what the step
asks (do not add all tests at once).

After editing in vim, save (:wq), make executable (chmod +x setup.sh) if
needed, then run the script sc with the example commands shown for each
step. For each step capture two screenshots:

A vim screenshot showing the current file buffer with the newly added
lines (before :wq) — name as specified for the step.

A terminal screenshot showing the commands you ran (chmod +x setup.sh if
necessary) and the script outputs for the example invocations — name as
specified for the step.

For the numeric comparisons, set a variable num=\$1 at the top of the
file before adding the individual if-tests (this will be the initial
step). For string checks, set str=\$2 before adding the string if-tests.
if

create file with shebang and set num and str variables

In vim create/overwrite setup.sh and insert:

\#!/bin/bash

num=\$1

str=\$2

Save and quit (:wq)

Make executable and run with examples:

chmod +x setup.sh

./setup.sh 10 Student

add the -eq test (equal)

Append to setup.sh:

if \[ “\$num” -eq 10 \]; then

echo “\$num is equal to 10 (-eq).”

else

echo “\$num is NOT equal to 10 (-eq).” eq).”

fi Save and quit; then run these commands (capture both in one terminal
screenshot):

./setup.sh 10 Student

./setup.sh 7 Student

add the -ne test (not equal)

Append to setup.sh:

if \[ “\$num” -ne 10 \]; then

echo “\$num is not equal to 10 (-ne).” ne).”

else

echo “\$num is equal to 10 (-ne ne false).”

fi

Save and quit; run:

./setup.sh 7 Student

./setup.sh 10 Student add the -gt test (greater than)

Append:

if \[ “\$num” -gt 10 \]; then

echo “\$num is greater than 10 (-gt).” gt).”

else

echo “\$num is NOT greater than 10 ((-gt).”

fi

Run:

./setup.sh 12 Student

./setup.sh 9 Student

add the -lt test (less than)

Append:

if \[ “\$num” -lt 10 \]; then

echo “\$num is less than 10 (-lt).” else

echo “\$num is NOT less than 10 (–lt).”

fi

Run:

./setup.sh 5 Student

./setup.sh 11 Student

add the -ge ge test (greater than or equal)

Append:

if \[ “\$num” -ge 10 \]; then

echo “\$num is greater than or equal to 10 ((-ge).”

else

echo “\$num is NOT greater than or equal to 10 ((-ge).”

fi

Run:

./setup.sh 10 Student ./setup.sh 8 Student

add the -le le test (less than or equal)

Append:

if \[ “\$num” -le 10 \]; then

echo “\$num is less than or equal to 10 ((-le).”

else

echo “\$num is NOT less than or equal to 10 ((-le).”

fi

Run:

./setup.sh 10 Student

./setup.sh 12 Student string equality test ( = )

Ensure str=\$2 exists at top (1.). Append:

if \[ “\$str” = “Student” \]; then

echo “Second argument equals ‘Student’ ( = ).”

else

echo “Second argument does NOT equal ‘Student’ ( = ).”

fi

Run:

./setup.sh 10 Student

./setup.sh 10 Test

string inequality test ( != )

Append:

if \[ “\$str” != “Student” \]; then

echo “Second argument is not equal to ‘Student’ ( != ).”

else

echo “Second argument equals ‘Student’ ( != false).”

fi

Run:

./setup.sh 10 Test

./setup.sh 10 Student check if second argument rgument is empty (zero
(zero-length)

Append:

if \[ -z “\$str” \]; then

echo “Second argument is empty (zero (zero-length).”

else

echo “Second argument is not empty.”

fi

Run:

./setup.sh 10

./setup.sh 10 Student Important Note Task 11 :

Students MUST follow the incremental approach: add one test at a time
and capture the vim buffer and run output screenshots for each step.

Using the two example runs per step in a single terminal screenshot
helps demonstrate both true and false results for the operator being
ttaught.

If a non-numeric numeric value is used for \$1 during integer
comparisons the shell may print an error; that is expected here because
we are demonstrating the operator behavior step step-by-step. step. (If
you want to avoid runtime errors, you can add integer validatio
validation before the comparisons — but for this exercise we are
isolating each if-test test into its own step.)

Task 12 – Script setup.sh – print all arguments with a for loop Create
the script with shebang and basic structure

Open vim and overwrite setup.sh:

vim setup.sh

Insert these lines (first step — shebang and a short comment):

\#!/bin/bash

# Script to demonstrate printing all user

                                     user-entered arguments using $*

Save and quit (:wq)

Append the for loop using \$\* and print each argument

Re-open setup.sh in vim and append the following lines:

# Print all arguments using \$\*

echo “Printing all arguments using \$\*:”

for arg in \$\*; do

echo “Argument: \$arg” done

Save and quit (:wq)

Make the script executable and run it with example arguments:

chmod +x setup.sh

./setup.sh one “two words” three

Task 13 – Script setup.sh – while loop summation and functions Clear the
previous code of setup.sh and write a new script, step-by-step, that:

Starts with a shebang line

Implements an interactive while loop that prompts tthe he user to enter
numbers and keeps a running total until the user types q to quit; after
each input the script echoes “Total Score: <current_total>”

Implements a function sum_two() that runs its own interactive while loop
doing the same accumulation and echoes the running totals

Adds a second function that takes two numeric arguments, sums them, and
returns the result via echo (demonstrated in the script)

Important: if you move the while-loop loop logic into the sum_two()
function, delete the standalone while- while loop code to avoid running
the same loop twice

Add the shebang line

Open vim and overwrite setup.sh with the shebang line: #!/bin/bash

Save and quit (:wq)

Make executable and run (no output expected):

chmod +x setup.sh

./setup.sh

Add the while-loop summation (interactive)

Re-open open setup.sh in vim and append the while while-loop:

# While-loop

        loop summation (interactive)

sum=0

while true; do

read -p p “Enter a number (or ‘q’ to quit):” input

if \[ “\$input” = “q” \]; then

break

fi

sum=\$((sum + input))

echo “Total Score: \$sum”

done

echo “Final total: \$sum”

Save and quit (:wq)

Run the script and demonstrate a short session (example): enter 5, then
7, then q ./setup.sh

# interactively enter:

\#5

\#7

\#q

Add the interactive summation function and demonstrate it

Re-open open setup.sh in vim and append the function sum_two() which
contains its own interactive while- while loop:

# Function to accumulate scores interactively

sum_two() {

sum=0

while true; do

read -p p “Enter a number (or ‘q’ to quit):” input

if \[ “\$input” = “q” \]; then

     break

fi

sum=\$((sum + input))  echo “Total Score: \$sum”

    done

    echo "Function final total: $sum"

}

# Demonstrate the function

echo “Now calling sum_two function:”

sum_two

Save and quit (:wq)

Important: If you have the standalone while while-loop loop from step 2
and you place this function into the script, delete the standalone loop
to avoid executing the same interactive logic twice when running the
script.

Run the script and demonstrate a short session (example): enter 3, 4, q
when prompted by the function:

./setup.sh

# when prompted by the function enter:

\#3

\#4

\#q Add a function that takes two numeric arguments, sums them, and
returns the result (echo)

Re-open open setup.sh in vim and append the following function and
demonstration. This function accepts two numeric arguments, adds them,
and return the sum. The script then captures that output and displays
it.

# Function that sums two arguments and returns th

                                               the result

sum_args() {

    a=$1

    b=$2

    return $((a + b))

}

# Demonstrate sum_args function

echo “Now demonstrating sum_args function:”

sum_args 3 4

result=\$?

echo “sum_args(3,4) returned: \$result”

Save and quit (:wq)

Run the script and capture the demonstration output:

chmod +x setup.sh

./setup.sh

# Observe the output that shows “sum_args(3,4) returned: 7”

Notes for Task 13:

Overwrite previous contents of setup.sh at the start of Task 13 (step
1).

Add code incrementally, save, run, and capture both the vim buffer and
the run output screenshots for each numbered step.

The while-loop and the functions are interactive; include the user
inputs in the run screenshots to demonstrate the behavior.

If you decide to use the function-based approach for interactive
summation, remove the earlier standalone while-loop to avoid duplicate
interaction.

Task 14 – Codespaces GUI — fork repo, run start-desktop.sh, open VNC,
stop GUI Goal: Fork the specified repository to your GitHub account,
open it in GitHub Codespaces, run the provided script to start a desktop
GUI, connect to the GUI via the Codespaces forwarded port (6080) -\>
vnc.html, and then stop the GUI using the provided stop script.

Important notes before starting:

GitHub Codespaces must be enabled for your account/org. Codespaces
availability and billing may apply.

The instructions below assume you have permission and capacity to create
a Codespace for your fork.

If Codespaces is not available, you may perform this step on another
cloud environment that exposes the same port and scripts, but the
screenshot filenames below assume Codespaces.

Steps:

Fork the repository to your GitHub account

Open the repo URL in your browser:

Ubuntu Machine

Click “Fork” (top-right) and fork it to your account. Open a Codespace
on your fork

In your forked repository on GitHub, click the green “Code” button →
“Open with Codespaces” → “Create codespace on main”” (or appropriate
branch).

Wait for the Codespace to initialize.

Verify the start script is present and executable (capture evidence)

In the Codespace terminal list files in the repo root and show the start
sscript cript and stop script exist:

ls -l start-desktop.sh stop-desktop.sh desktop.sh If not executable,
make it executable:

chmod +x start-desktop.sh stop-desktop.sh desktop.sh

Save a screenshot showing the ls -ll output (file listing) and the chmod
command if applied:

Run the start script inside the Codespace terminal

In the Codespace terminal run:

# Ensure the start script is executable

chmod +x start-desktop.sh

# Start the desktop GUI

./start-desktop.sh

Capture the terminal output showing successful start messages.

Verify forwarded ports in Codespaces (Ports view)

Open the Codespaces “Ports” panel / view and confirm port 6080 is
forwarded and visible. Save a screenshot shot of the Ports view showing
port 6080 and its status:

Open forwarded port 6080 and connect to VNC HTML page

In the Codespaces UI, open the forwarded port’s preview URL or copy the
forwarded URL and open it in your browser.

Visit thee port 6080 address and click the vnc.html link.

When prompted for a password enter:

codespace

Capture screenshots of:

The browser showing the forwarded port URL in the address bar / Codesp
Codespacess preview

The VNC password prompt (showing p password assword field; do NOT
include typed password in a screenshot): task14_vnc_password_prompt.png

The VNC session after successful connection showing the GUI/desktop:
task14_vnc_desktop.png

(Optional) A focused screenshot of vnc.html UI showing the “Connect” b
button utton before/after connecting: task14_vnc_connect.png Stop the
GUI

When finished, return to the Codespace terminal and run:

./stop-desktop.sh

Capture the terminal output that shows the GUI stopping and any cleanup
messages.

Troubleshooting tips:

If port 6080 is not visible, check Codespaces “Ports” view and forward
it manually.

If the VNC page fails to connect, verify the start start-desktop.sh
desktop.sh completed without errors and that the VNC server is listening
on the expected port insi inside the Codespace.

If Codespaces is unavailable for your account, consider forking and
running the same scripts on another cloud VM that forwards port 6080 and
adapt screenshots/file names accordingly.

------------------------------------------------------------------------




---

### Extracted images

![](CC-Sarosh-059-Lab6_media/image-000.jpg)
![](CC-Sarosh-059-Lab6_media/image-001.jpg)
![](CC-Sarosh-059-Lab6_media/image-002.jpg)
![](CC-Sarosh-059-Lab6_media/image-003.png)
![](CC-Sarosh-059-Lab6_media/image-004.png)
![](CC-Sarosh-059-Lab6_media/image-005.png)
![](CC-Sarosh-059-Lab6_media/image-006.png)
![](CC-Sarosh-059-Lab6_media/image-007.png)
![](CC-Sarosh-059-Lab6_media/image-008.png)
![](CC-Sarosh-059-Lab6_media/image-009.png)
![](CC-Sarosh-059-Lab6_media/image-010.png)
![](CC-Sarosh-059-Lab6_media/image-011.png)
![](CC-Sarosh-059-Lab6_media/image-012.png)
![](CC-Sarosh-059-Lab6_media/image-013.png)
![](CC-Sarosh-059-Lab6_media/image-014.png)
![](CC-Sarosh-059-Lab6_media/image-015.png)
![](CC-Sarosh-059-Lab6_media/image-016.png)
![](CC-Sarosh-059-Lab6_media/image-017.png)
![](CC-Sarosh-059-Lab6_media/image-018.png)
![](CC-Sarosh-059-Lab6_media/image-019.png)
![](CC-Sarosh-059-Lab6_media/image-020.png)
![](CC-Sarosh-059-Lab6_media/image-021.png)
![](CC-Sarosh-059-Lab6_media/image-022.png)
![](CC-Sarosh-059-Lab6_media/image-023.png)
![](CC-Sarosh-059-Lab6_media/image-024.png)
![](CC-Sarosh-059-Lab6_media/image-025.png)
![](CC-Sarosh-059-Lab6_media/image-026.png)
![](CC-Sarosh-059-Lab6_media/image-027.png)
![](CC-Sarosh-059-Lab6_media/image-028.png)
![](CC-Sarosh-059-Lab6_media/image-029.png)
![](CC-Sarosh-059-Lab6_media/image-030.png)
![](CC-Sarosh-059-Lab6_media/image-031.png)
![](CC-Sarosh-059-Lab6_media/image-032.png)
![](CC-Sarosh-059-Lab6_media/image-033.png)
![](CC-Sarosh-059-Lab6_media/image-034.png)
![](CC-Sarosh-059-Lab6_media/image-035.jpg)
![](CC-Sarosh-059-Lab6_media/image-036.jpg)
![](CC-Sarosh-059-Lab6_media/image-037.png)
![](CC-Sarosh-059-Lab6_media/image-038.png)
![](CC-Sarosh-059-Lab6_media/image-039.png)
![](CC-Sarosh-059-Lab6_media/image-040.png)
![](CC-Sarosh-059-Lab6_media/image-041.png)
![](CC-Sarosh-059-Lab6_media/image-042.png)
![](CC-Sarosh-059-Lab6_media/image-043.png)
![](CC-Sarosh-059-Lab6_media/image-044.png)
![](CC-Sarosh-059-Lab6_media/image-045.png)
![](CC-Sarosh-059-Lab6_media/image-046.png)
![](CC-Sarosh-059-Lab6_media/image-047.png)
![](CC-Sarosh-059-Lab6_media/image-048.png)
![](CC-Sarosh-059-Lab6_media/image-049.png)
![](CC-Sarosh-059-Lab6_media/image-050.png)
![](CC-Sarosh-059-Lab6_media/image-051.png)
![](CC-Sarosh-059-Lab6_media/image-052.png)
![](CC-Sarosh-059-Lab6_media/image-053.png)
![](CC-Sarosh-059-Lab6_media/image-054.png)
![](CC-Sarosh-059-Lab6_media/image-055.png)
![](CC-Sarosh-059-Lab6_media/image-056.png)
![](CC-Sarosh-059-Lab6_media/image-057.png)
![](CC-Sarosh-059-Lab6_media/image-058.png)
![](CC-Sarosh-059-Lab6_media/image-059.png)
![](CC-Sarosh-059-Lab6_media/image-060.png)
![](CC-Sarosh-059-Lab6_media/image-061.png)
![](CC-Sarosh-059-Lab6_media/image-062.png)
![](CC-Sarosh-059-Lab6_media/image-063.png)
![](CC-Sarosh-059-Lab6_media/image-064.png)
![](CC-Sarosh-059-Lab6_media/image-065.png)
![](CC-Sarosh-059-Lab6_media/image-066.png)
![](CC-Sarosh-059-Lab6_media/image-067.png)
![](CC-Sarosh-059-Lab6_media/image-068.png)
![](CC-Sarosh-059-Lab6_media/image-069.png)
![](CC-Sarosh-059-Lab6_media/image-070.png)
![](CC-Sarosh-059-Lab6_media/image-071.png)
![](CC-Sarosh-059-Lab6_media/image-072.png)
![](CC-Sarosh-059-Lab6_media/image-073.jpg)
![](CC-Sarosh-059-Lab6_media/image-074.jpg)
![](CC-Sarosh-059-Lab6_media/image-075.jpg)
![](CC-Sarosh-059-Lab6_media/image-076.png)
![](CC-Sarosh-059-Lab6_media/image-077.png)
![](CC-Sarosh-059-Lab6_media/image-078.png)
![](CC-Sarosh-059-Lab6_media/image-079.png)
![](CC-Sarosh-059-Lab6_media/image-080.png)
![](CC-Sarosh-059-Lab6_media/image-081.png)
![](CC-Sarosh-059-Lab6_media/image-082.png)
![](CC-Sarosh-059-Lab6_media/image-083.png)
![](CC-Sarosh-059-Lab6_media/image-084.png)
![](CC-Sarosh-059-Lab6_media/image-085.png)
![](CC-Sarosh-059-Lab6_media/image-086.png)
![](CC-Sarosh-059-Lab6_media/image-087.png)
![](CC-Sarosh-059-Lab6_media/image-088.png)
![](CC-Sarosh-059-Lab6_media/image-089.png)
![](CC-Sarosh-059-Lab6_media/image-090.png)
![](CC-Sarosh-059-Lab6_media/image-091.png)
![](CC-Sarosh-059-Lab6_media/image-092.png)
![](CC-Sarosh-059-Lab6_media/image-093.png)
![](CC-Sarosh-059-Lab6_media/image-094.png)
![](CC-Sarosh-059-Lab6_media/image-095.png)
![](CC-Sarosh-059-Lab6_media/image-096.png)
![](CC-Sarosh-059-Lab6_media/image-097.png)
![](CC-Sarosh-059-Lab6_media/image-098.png)
![](CC-Sarosh-059-Lab6_media/image-099.png)
![](CC-Sarosh-059-Lab6_media/image-100.png)
![](CC-Sarosh-059-Lab6_media/image-1000.png)
![](CC-Sarosh-059-Lab6_media/image-1001.png)
![](CC-Sarosh-059-Lab6_media/image-1002.png)
![](CC-Sarosh-059-Lab6_media/image-1003.png)
![](CC-Sarosh-059-Lab6_media/image-1004.png)
![](CC-Sarosh-059-Lab6_media/image-1005.png)
![](CC-Sarosh-059-Lab6_media/image-1006.png)
![](CC-Sarosh-059-Lab6_media/image-1007.png)
![](CC-Sarosh-059-Lab6_media/image-1008.png)
![](CC-Sarosh-059-Lab6_media/image-1009.png)
![](CC-Sarosh-059-Lab6_media/image-101.png)
![](CC-Sarosh-059-Lab6_media/image-1010.png)
![](CC-Sarosh-059-Lab6_media/image-1011.jpg)
![](CC-Sarosh-059-Lab6_media/image-1012.jpg)
![](CC-Sarosh-059-Lab6_media/image-1013.png)
![](CC-Sarosh-059-Lab6_media/image-1014.png)
![](CC-Sarosh-059-Lab6_media/image-1015.png)
![](CC-Sarosh-059-Lab6_media/image-1016.png)
![](CC-Sarosh-059-Lab6_media/image-1017.png)
![](CC-Sarosh-059-Lab6_media/image-1018.png)
![](CC-Sarosh-059-Lab6_media/image-1019.png)
![](CC-Sarosh-059-Lab6_media/image-102.png)
![](CC-Sarosh-059-Lab6_media/image-1020.png)
![](CC-Sarosh-059-Lab6_media/image-1021.png)
![](CC-Sarosh-059-Lab6_media/image-1022.png)
![](CC-Sarosh-059-Lab6_media/image-1023.png)
![](CC-Sarosh-059-Lab6_media/image-1024.png)
![](CC-Sarosh-059-Lab6_media/image-1025.png)
![](CC-Sarosh-059-Lab6_media/image-1026.png)
![](CC-Sarosh-059-Lab6_media/image-1027.png)
![](CC-Sarosh-059-Lab6_media/image-1028.png)
![](CC-Sarosh-059-Lab6_media/image-1029.png)
![](CC-Sarosh-059-Lab6_media/image-103.png)
![](CC-Sarosh-059-Lab6_media/image-1030.png)
![](CC-Sarosh-059-Lab6_media/image-1031.png)
![](CC-Sarosh-059-Lab6_media/image-1032.png)
![](CC-Sarosh-059-Lab6_media/image-1033.png)
![](CC-Sarosh-059-Lab6_media/image-1034.png)
![](CC-Sarosh-059-Lab6_media/image-1035.png)
![](CC-Sarosh-059-Lab6_media/image-1036.png)
![](CC-Sarosh-059-Lab6_media/image-1037.png)
![](CC-Sarosh-059-Lab6_media/image-1038.png)
![](CC-Sarosh-059-Lab6_media/image-1039.png)
![](CC-Sarosh-059-Lab6_media/image-104.png)
![](CC-Sarosh-059-Lab6_media/image-1040.png)
![](CC-Sarosh-059-Lab6_media/image-1041.png)
![](CC-Sarosh-059-Lab6_media/image-1042.png)
![](CC-Sarosh-059-Lab6_media/image-1043.png)
![](CC-Sarosh-059-Lab6_media/image-1044.png)
![](CC-Sarosh-059-Lab6_media/image-1045.png)
![](CC-Sarosh-059-Lab6_media/image-1046.png)
![](CC-Sarosh-059-Lab6_media/image-1047.png)
![](CC-Sarosh-059-Lab6_media/image-1048.png)
![](CC-Sarosh-059-Lab6_media/image-1049.jpg)
![](CC-Sarosh-059-Lab6_media/image-105.png)
![](CC-Sarosh-059-Lab6_media/image-1050.jpg)
![](CC-Sarosh-059-Lab6_media/image-1051.png)
![](CC-Sarosh-059-Lab6_media/image-1052.png)
![](CC-Sarosh-059-Lab6_media/image-1053.png)
![](CC-Sarosh-059-Lab6_media/image-1054.png)
![](CC-Sarosh-059-Lab6_media/image-1055.png)
![](CC-Sarosh-059-Lab6_media/image-1056.png)
![](CC-Sarosh-059-Lab6_media/image-1057.png)
![](CC-Sarosh-059-Lab6_media/image-1058.png)
![](CC-Sarosh-059-Lab6_media/image-1059.png)
![](CC-Sarosh-059-Lab6_media/image-106.png)
![](CC-Sarosh-059-Lab6_media/image-1060.png)
![](CC-Sarosh-059-Lab6_media/image-1061.png)
![](CC-Sarosh-059-Lab6_media/image-1062.png)
![](CC-Sarosh-059-Lab6_media/image-1063.png)
![](CC-Sarosh-059-Lab6_media/image-1064.png)
![](CC-Sarosh-059-Lab6_media/image-1065.png)
![](CC-Sarosh-059-Lab6_media/image-1066.png)
![](CC-Sarosh-059-Lab6_media/image-1067.png)
![](CC-Sarosh-059-Lab6_media/image-1068.png)
![](CC-Sarosh-059-Lab6_media/image-1069.png)
![](CC-Sarosh-059-Lab6_media/image-107.png)
![](CC-Sarosh-059-Lab6_media/image-1070.png)
![](CC-Sarosh-059-Lab6_media/image-1071.png)
![](CC-Sarosh-059-Lab6_media/image-1072.png)
![](CC-Sarosh-059-Lab6_media/image-1073.png)
![](CC-Sarosh-059-Lab6_media/image-1074.png)
![](CC-Sarosh-059-Lab6_media/image-1075.png)
![](CC-Sarosh-059-Lab6_media/image-1076.png)
![](CC-Sarosh-059-Lab6_media/image-1077.png)
![](CC-Sarosh-059-Lab6_media/image-1078.png)
![](CC-Sarosh-059-Lab6_media/image-1079.png)
![](CC-Sarosh-059-Lab6_media/image-108.jpg)
![](CC-Sarosh-059-Lab6_media/image-1080.png)
![](CC-Sarosh-059-Lab6_media/image-1081.png)
![](CC-Sarosh-059-Lab6_media/image-1082.png)
![](CC-Sarosh-059-Lab6_media/image-1083.jpg)
![](CC-Sarosh-059-Lab6_media/image-1084.jpg)
![](CC-Sarosh-059-Lab6_media/image-1085.png)
![](CC-Sarosh-059-Lab6_media/image-1086.png)
![](CC-Sarosh-059-Lab6_media/image-1087.png)
![](CC-Sarosh-059-Lab6_media/image-1088.png)
![](CC-Sarosh-059-Lab6_media/image-1089.png)
![](CC-Sarosh-059-Lab6_media/image-109.jpg)
![](CC-Sarosh-059-Lab6_media/image-1090.png)
![](CC-Sarosh-059-Lab6_media/image-1091.png)
![](CC-Sarosh-059-Lab6_media/image-1092.png)
![](CC-Sarosh-059-Lab6_media/image-1093.png)
![](CC-Sarosh-059-Lab6_media/image-1094.png)
![](CC-Sarosh-059-Lab6_media/image-1095.png)
![](CC-Sarosh-059-Lab6_media/image-1096.png)
![](CC-Sarosh-059-Lab6_media/image-1097.png)
![](CC-Sarosh-059-Lab6_media/image-1098.png)
![](CC-Sarosh-059-Lab6_media/image-1099.png)
![](CC-Sarosh-059-Lab6_media/image-110.jpg)
![](CC-Sarosh-059-Lab6_media/image-1100.png)
![](CC-Sarosh-059-Lab6_media/image-1101.png)
![](CC-Sarosh-059-Lab6_media/image-1102.png)
![](CC-Sarosh-059-Lab6_media/image-1103.png)
![](CC-Sarosh-059-Lab6_media/image-1104.png)
![](CC-Sarosh-059-Lab6_media/image-1105.png)
![](CC-Sarosh-059-Lab6_media/image-1106.png)
![](CC-Sarosh-059-Lab6_media/image-1107.png)
![](CC-Sarosh-059-Lab6_media/image-1108.png)
![](CC-Sarosh-059-Lab6_media/image-1109.png)
![](CC-Sarosh-059-Lab6_media/image-111.png)
![](CC-Sarosh-059-Lab6_media/image-1110.png)
![](CC-Sarosh-059-Lab6_media/image-1111.png)
![](CC-Sarosh-059-Lab6_media/image-1112.png)
![](CC-Sarosh-059-Lab6_media/image-1113.png)
![](CC-Sarosh-059-Lab6_media/image-1114.png)
![](CC-Sarosh-059-Lab6_media/image-1115.png)
![](CC-Sarosh-059-Lab6_media/image-1116.png)
![](CC-Sarosh-059-Lab6_media/image-1117.png)
![](CC-Sarosh-059-Lab6_media/image-1118.png)
![](CC-Sarosh-059-Lab6_media/image-1119.png)
![](CC-Sarosh-059-Lab6_media/image-112.png)
![](CC-Sarosh-059-Lab6_media/image-1120.png)
![](CC-Sarosh-059-Lab6_media/image-1121.jpg)
![](CC-Sarosh-059-Lab6_media/image-1122.png)
![](CC-Sarosh-059-Lab6_media/image-1123.png)
![](CC-Sarosh-059-Lab6_media/image-1124.png)
![](CC-Sarosh-059-Lab6_media/image-1125.png)
![](CC-Sarosh-059-Lab6_media/image-1126.png)
![](CC-Sarosh-059-Lab6_media/image-1127.png)
![](CC-Sarosh-059-Lab6_media/image-1128.png)
![](CC-Sarosh-059-Lab6_media/image-1129.png)
![](CC-Sarosh-059-Lab6_media/image-113.png)
![](CC-Sarosh-059-Lab6_media/image-1130.png)
![](CC-Sarosh-059-Lab6_media/image-1131.png)
![](CC-Sarosh-059-Lab6_media/image-1132.png)
![](CC-Sarosh-059-Lab6_media/image-1133.png)
![](CC-Sarosh-059-Lab6_media/image-1134.png)
![](CC-Sarosh-059-Lab6_media/image-1135.png)
![](CC-Sarosh-059-Lab6_media/image-1136.png)
![](CC-Sarosh-059-Lab6_media/image-1137.png)
![](CC-Sarosh-059-Lab6_media/image-1138.png)
![](CC-Sarosh-059-Lab6_media/image-1139.png)
![](CC-Sarosh-059-Lab6_media/image-114.png)
![](CC-Sarosh-059-Lab6_media/image-1140.png)
![](CC-Sarosh-059-Lab6_media/image-1141.png)
![](CC-Sarosh-059-Lab6_media/image-1142.png)
![](CC-Sarosh-059-Lab6_media/image-1143.png)
![](CC-Sarosh-059-Lab6_media/image-1144.png)
![](CC-Sarosh-059-Lab6_media/image-1145.png)
![](CC-Sarosh-059-Lab6_media/image-1146.png)
![](CC-Sarosh-059-Lab6_media/image-1147.png)
![](CC-Sarosh-059-Lab6_media/image-1148.png)
![](CC-Sarosh-059-Lab6_media/image-1149.png)
![](CC-Sarosh-059-Lab6_media/image-115.png)
![](CC-Sarosh-059-Lab6_media/image-1150.png)
![](CC-Sarosh-059-Lab6_media/image-1151.png)
![](CC-Sarosh-059-Lab6_media/image-1152.png)
![](CC-Sarosh-059-Lab6_media/image-1153.png)
![](CC-Sarosh-059-Lab6_media/image-1154.jpg)
![](CC-Sarosh-059-Lab6_media/image-1155.png)
![](CC-Sarosh-059-Lab6_media/image-1156.png)
![](CC-Sarosh-059-Lab6_media/image-1157.png)
![](CC-Sarosh-059-Lab6_media/image-1158.png)
![](CC-Sarosh-059-Lab6_media/image-1159.png)
![](CC-Sarosh-059-Lab6_media/image-116.png)
![](CC-Sarosh-059-Lab6_media/image-1160.png)
![](CC-Sarosh-059-Lab6_media/image-1161.png)
![](CC-Sarosh-059-Lab6_media/image-1162.png)
![](CC-Sarosh-059-Lab6_media/image-1163.png)
![](CC-Sarosh-059-Lab6_media/image-1164.png)
![](CC-Sarosh-059-Lab6_media/image-1165.png)
![](CC-Sarosh-059-Lab6_media/image-1166.png)
![](CC-Sarosh-059-Lab6_media/image-1167.png)
![](CC-Sarosh-059-Lab6_media/image-1168.png)
![](CC-Sarosh-059-Lab6_media/image-1169.png)
![](CC-Sarosh-059-Lab6_media/image-117.png)
![](CC-Sarosh-059-Lab6_media/image-1170.png)
![](CC-Sarosh-059-Lab6_media/image-1171.png)
![](CC-Sarosh-059-Lab6_media/image-1172.png)
![](CC-Sarosh-059-Lab6_media/image-1173.png)
![](CC-Sarosh-059-Lab6_media/image-1174.png)
![](CC-Sarosh-059-Lab6_media/image-1175.png)
![](CC-Sarosh-059-Lab6_media/image-1176.png)
![](CC-Sarosh-059-Lab6_media/image-1177.png)
![](CC-Sarosh-059-Lab6_media/image-1178.png)
![](CC-Sarosh-059-Lab6_media/image-1179.png)
![](CC-Sarosh-059-Lab6_media/image-118.png)
![](CC-Sarosh-059-Lab6_media/image-1180.png)
![](CC-Sarosh-059-Lab6_media/image-1181.png)
![](CC-Sarosh-059-Lab6_media/image-1182.png)
![](CC-Sarosh-059-Lab6_media/image-1183.png)
![](CC-Sarosh-059-Lab6_media/image-1184.png)
![](CC-Sarosh-059-Lab6_media/image-1185.png)
![](CC-Sarosh-059-Lab6_media/image-1186.png)
![](CC-Sarosh-059-Lab6_media/image-1187.png)
![](CC-Sarosh-059-Lab6_media/image-1188.png)
![](CC-Sarosh-059-Lab6_media/image-1189.png)
![](CC-Sarosh-059-Lab6_media/image-119.png)
![](CC-Sarosh-059-Lab6_media/image-1190.png)
![](CC-Sarosh-059-Lab6_media/image-1191.jpg)
![](CC-Sarosh-059-Lab6_media/image-1192.jpg)
![](CC-Sarosh-059-Lab6_media/image-1193.png)
![](CC-Sarosh-059-Lab6_media/image-1194.png)
![](CC-Sarosh-059-Lab6_media/image-1195.png)
![](CC-Sarosh-059-Lab6_media/image-1196.png)
![](CC-Sarosh-059-Lab6_media/image-1197.png)
![](CC-Sarosh-059-Lab6_media/image-1198.png)
![](CC-Sarosh-059-Lab6_media/image-1199.png)
![](CC-Sarosh-059-Lab6_media/image-120.png)
![](CC-Sarosh-059-Lab6_media/image-1200.png)
![](CC-Sarosh-059-Lab6_media/image-1201.png)
![](CC-Sarosh-059-Lab6_media/image-1202.png)
![](CC-Sarosh-059-Lab6_media/image-1203.png)
![](CC-Sarosh-059-Lab6_media/image-1204.png)
![](CC-Sarosh-059-Lab6_media/image-1205.png)
![](CC-Sarosh-059-Lab6_media/image-1206.png)
![](CC-Sarosh-059-Lab6_media/image-1207.png)
![](CC-Sarosh-059-Lab6_media/image-1208.png)
![](CC-Sarosh-059-Lab6_media/image-1209.png)
![](CC-Sarosh-059-Lab6_media/image-121.png)
![](CC-Sarosh-059-Lab6_media/image-1210.png)
![](CC-Sarosh-059-Lab6_media/image-1211.png)
![](CC-Sarosh-059-Lab6_media/image-1212.png)
![](CC-Sarosh-059-Lab6_media/image-1213.png)
![](CC-Sarosh-059-Lab6_media/image-1214.png)
![](CC-Sarosh-059-Lab6_media/image-1215.png)
![](CC-Sarosh-059-Lab6_media/image-1216.png)
![](CC-Sarosh-059-Lab6_media/image-1217.png)
![](CC-Sarosh-059-Lab6_media/image-1218.png)
![](CC-Sarosh-059-Lab6_media/image-1219.png)
![](CC-Sarosh-059-Lab6_media/image-122.png)
![](CC-Sarosh-059-Lab6_media/image-1220.png)
![](CC-Sarosh-059-Lab6_media/image-1221.png)
![](CC-Sarosh-059-Lab6_media/image-1222.png)
![](CC-Sarosh-059-Lab6_media/image-1223.png)
![](CC-Sarosh-059-Lab6_media/image-1224.png)
![](CC-Sarosh-059-Lab6_media/image-1225.jpg)
![](CC-Sarosh-059-Lab6_media/image-1226.png)
![](CC-Sarosh-059-Lab6_media/image-1227.png)
![](CC-Sarosh-059-Lab6_media/image-1228.png)
![](CC-Sarosh-059-Lab6_media/image-1229.png)
![](CC-Sarosh-059-Lab6_media/image-123.jpg)
![](CC-Sarosh-059-Lab6_media/image-1230.png)
![](CC-Sarosh-059-Lab6_media/image-1231.png)
![](CC-Sarosh-059-Lab6_media/image-1232.png)
![](CC-Sarosh-059-Lab6_media/image-1233.png)
![](CC-Sarosh-059-Lab6_media/image-1234.png)
![](CC-Sarosh-059-Lab6_media/image-1235.png)
![](CC-Sarosh-059-Lab6_media/image-1236.png)
![](CC-Sarosh-059-Lab6_media/image-1237.png)
![](CC-Sarosh-059-Lab6_media/image-1238.png)
![](CC-Sarosh-059-Lab6_media/image-1239.png)
![](CC-Sarosh-059-Lab6_media/image-124.png)
![](CC-Sarosh-059-Lab6_media/image-1240.png)
![](CC-Sarosh-059-Lab6_media/image-1241.png)
![](CC-Sarosh-059-Lab6_media/image-1242.png)
![](CC-Sarosh-059-Lab6_media/image-1243.png)
![](CC-Sarosh-059-Lab6_media/image-1244.png)
![](CC-Sarosh-059-Lab6_media/image-1245.png)
![](CC-Sarosh-059-Lab6_media/image-1246.png)
![](CC-Sarosh-059-Lab6_media/image-1247.png)
![](CC-Sarosh-059-Lab6_media/image-1248.png)
![](CC-Sarosh-059-Lab6_media/image-1249.png)
![](CC-Sarosh-059-Lab6_media/image-125.png)
![](CC-Sarosh-059-Lab6_media/image-1250.png)
![](CC-Sarosh-059-Lab6_media/image-1251.png)
![](CC-Sarosh-059-Lab6_media/image-1252.png)
![](CC-Sarosh-059-Lab6_media/image-1253.png)
![](CC-Sarosh-059-Lab6_media/image-1254.png)
![](CC-Sarosh-059-Lab6_media/image-1255.png)
![](CC-Sarosh-059-Lab6_media/image-1256.png)
![](CC-Sarosh-059-Lab6_media/image-1257.png)
![](CC-Sarosh-059-Lab6_media/image-1258.png)
![](CC-Sarosh-059-Lab6_media/image-1259.png)
![](CC-Sarosh-059-Lab6_media/image-126.png)
![](CC-Sarosh-059-Lab6_media/image-1260.png)
![](CC-Sarosh-059-Lab6_media/image-1261.png)
![](CC-Sarosh-059-Lab6_media/image-1262.jpg)
![](CC-Sarosh-059-Lab6_media/image-1263.png)
![](CC-Sarosh-059-Lab6_media/image-1264.png)
![](CC-Sarosh-059-Lab6_media/image-1265.png)
![](CC-Sarosh-059-Lab6_media/image-1266.png)
![](CC-Sarosh-059-Lab6_media/image-1267.png)
![](CC-Sarosh-059-Lab6_media/image-1268.png)
![](CC-Sarosh-059-Lab6_media/image-1269.png)
![](CC-Sarosh-059-Lab6_media/image-127.png)
![](CC-Sarosh-059-Lab6_media/image-1270.png)
![](CC-Sarosh-059-Lab6_media/image-1271.png)
![](CC-Sarosh-059-Lab6_media/image-1272.png)
![](CC-Sarosh-059-Lab6_media/image-1273.png)
![](CC-Sarosh-059-Lab6_media/image-1274.png)
![](CC-Sarosh-059-Lab6_media/image-1275.png)
![](CC-Sarosh-059-Lab6_media/image-1276.png)
![](CC-Sarosh-059-Lab6_media/image-1277.png)
![](CC-Sarosh-059-Lab6_media/image-1278.png)
![](CC-Sarosh-059-Lab6_media/image-1279.png)
![](CC-Sarosh-059-Lab6_media/image-128.png)
![](CC-Sarosh-059-Lab6_media/image-1280.png)
![](CC-Sarosh-059-Lab6_media/image-1281.png)
![](CC-Sarosh-059-Lab6_media/image-1282.png)
![](CC-Sarosh-059-Lab6_media/image-1283.png)
![](CC-Sarosh-059-Lab6_media/image-1284.png)
![](CC-Sarosh-059-Lab6_media/image-1285.png)
![](CC-Sarosh-059-Lab6_media/image-1286.png)
![](CC-Sarosh-059-Lab6_media/image-1287.png)
![](CC-Sarosh-059-Lab6_media/image-1288.png)
![](CC-Sarosh-059-Lab6_media/image-1289.png)
![](CC-Sarosh-059-Lab6_media/image-129.png)
![](CC-Sarosh-059-Lab6_media/image-1290.png)
![](CC-Sarosh-059-Lab6_media/image-1291.png)
![](CC-Sarosh-059-Lab6_media/image-1292.png)
![](CC-Sarosh-059-Lab6_media/image-1293.png)
![](CC-Sarosh-059-Lab6_media/image-1294.png)
![](CC-Sarosh-059-Lab6_media/image-1295.png)
![](CC-Sarosh-059-Lab6_media/image-1296.png)
![](CC-Sarosh-059-Lab6_media/image-1297.png)
![](CC-Sarosh-059-Lab6_media/image-1298.png)
![](CC-Sarosh-059-Lab6_media/image-1299.jpg)
![](CC-Sarosh-059-Lab6_media/image-130.png)
![](CC-Sarosh-059-Lab6_media/image-1300.png)
![](CC-Sarosh-059-Lab6_media/image-1301.png)
![](CC-Sarosh-059-Lab6_media/image-1302.png)
![](CC-Sarosh-059-Lab6_media/image-1303.png)
![](CC-Sarosh-059-Lab6_media/image-1304.png)
![](CC-Sarosh-059-Lab6_media/image-1305.png)
![](CC-Sarosh-059-Lab6_media/image-1306.png)
![](CC-Sarosh-059-Lab6_media/image-1307.png)
![](CC-Sarosh-059-Lab6_media/image-1308.png)
![](CC-Sarosh-059-Lab6_media/image-1309.png)
![](CC-Sarosh-059-Lab6_media/image-131.png)
![](CC-Sarosh-059-Lab6_media/image-1310.png)
![](CC-Sarosh-059-Lab6_media/image-1311.png)
![](CC-Sarosh-059-Lab6_media/image-1312.png)
![](CC-Sarosh-059-Lab6_media/image-1313.png)
![](CC-Sarosh-059-Lab6_media/image-1314.png)
![](CC-Sarosh-059-Lab6_media/image-1315.png)
![](CC-Sarosh-059-Lab6_media/image-1316.png)
![](CC-Sarosh-059-Lab6_media/image-1317.png)
![](CC-Sarosh-059-Lab6_media/image-1318.png)
![](CC-Sarosh-059-Lab6_media/image-1319.png)
![](CC-Sarosh-059-Lab6_media/image-132.png)
![](CC-Sarosh-059-Lab6_media/image-1320.png)
![](CC-Sarosh-059-Lab6_media/image-1321.png)
![](CC-Sarosh-059-Lab6_media/image-1322.png)
![](CC-Sarosh-059-Lab6_media/image-1323.png)
![](CC-Sarosh-059-Lab6_media/image-1324.png)
![](CC-Sarosh-059-Lab6_media/image-1325.png)
![](CC-Sarosh-059-Lab6_media/image-1326.png)
![](CC-Sarosh-059-Lab6_media/image-1327.png)
![](CC-Sarosh-059-Lab6_media/image-1328.png)
![](CC-Sarosh-059-Lab6_media/image-1329.png)
![](CC-Sarosh-059-Lab6_media/image-133.png)
![](CC-Sarosh-059-Lab6_media/image-1330.png)
![](CC-Sarosh-059-Lab6_media/image-1331.png)
![](CC-Sarosh-059-Lab6_media/image-1332.png)
![](CC-Sarosh-059-Lab6_media/image-1333.png)
![](CC-Sarosh-059-Lab6_media/image-1334.png)
![](CC-Sarosh-059-Lab6_media/image-1335.png)
![](CC-Sarosh-059-Lab6_media/image-1336.png)
![](CC-Sarosh-059-Lab6_media/image-1337.png)
![](CC-Sarosh-059-Lab6_media/image-1338.png)
![](CC-Sarosh-059-Lab6_media/image-1339.png)
![](CC-Sarosh-059-Lab6_media/image-134.png)
![](CC-Sarosh-059-Lab6_media/image-1340.jpg)
![](CC-Sarosh-059-Lab6_media/image-1341.jpg)
![](CC-Sarosh-059-Lab6_media/image-1342.jpg)
![](CC-Sarosh-059-Lab6_media/image-1343.png)
![](CC-Sarosh-059-Lab6_media/image-1344.png)
![](CC-Sarosh-059-Lab6_media/image-1345.png)
![](CC-Sarosh-059-Lab6_media/image-1346.png)
![](CC-Sarosh-059-Lab6_media/image-1347.png)
![](CC-Sarosh-059-Lab6_media/image-1348.png)
![](CC-Sarosh-059-Lab6_media/image-1349.png)
![](CC-Sarosh-059-Lab6_media/image-135.png)
![](CC-Sarosh-059-Lab6_media/image-1350.png)
![](CC-Sarosh-059-Lab6_media/image-1351.png)
![](CC-Sarosh-059-Lab6_media/image-1352.png)
![](CC-Sarosh-059-Lab6_media/image-1353.png)
![](CC-Sarosh-059-Lab6_media/image-1354.png)
![](CC-Sarosh-059-Lab6_media/image-1355.png)
![](CC-Sarosh-059-Lab6_media/image-1356.png)
![](CC-Sarosh-059-Lab6_media/image-1357.png)
![](CC-Sarosh-059-Lab6_media/image-1358.png)
![](CC-Sarosh-059-Lab6_media/image-1359.png)
![](CC-Sarosh-059-Lab6_media/image-136.png)
![](CC-Sarosh-059-Lab6_media/image-1360.png)
![](CC-Sarosh-059-Lab6_media/image-1361.png)
![](CC-Sarosh-059-Lab6_media/image-1362.png)
![](CC-Sarosh-059-Lab6_media/image-1363.png)
![](CC-Sarosh-059-Lab6_media/image-1364.png)
![](CC-Sarosh-059-Lab6_media/image-1365.png)
![](CC-Sarosh-059-Lab6_media/image-1366.png)
![](CC-Sarosh-059-Lab6_media/image-1367.png)
![](CC-Sarosh-059-Lab6_media/image-1368.png)
![](CC-Sarosh-059-Lab6_media/image-1369.png)
![](CC-Sarosh-059-Lab6_media/image-137.png)
![](CC-Sarosh-059-Lab6_media/image-1370.png)
![](CC-Sarosh-059-Lab6_media/image-1371.png)
![](CC-Sarosh-059-Lab6_media/image-1372.png)
![](CC-Sarosh-059-Lab6_media/image-1373.png)
![](CC-Sarosh-059-Lab6_media/image-1374.png)
![](CC-Sarosh-059-Lab6_media/image-1375.jpg)
![](CC-Sarosh-059-Lab6_media/image-1376.jpg)
![](CC-Sarosh-059-Lab6_media/image-1377.jpg)
![](CC-Sarosh-059-Lab6_media/image-1378.png)
![](CC-Sarosh-059-Lab6_media/image-1379.png)
![](CC-Sarosh-059-Lab6_media/image-138.png)
![](CC-Sarosh-059-Lab6_media/image-1380.png)
![](CC-Sarosh-059-Lab6_media/image-1381.png)
![](CC-Sarosh-059-Lab6_media/image-1382.png)
![](CC-Sarosh-059-Lab6_media/image-1383.png)
![](CC-Sarosh-059-Lab6_media/image-1384.png)
![](CC-Sarosh-059-Lab6_media/image-1385.png)
![](CC-Sarosh-059-Lab6_media/image-1386.png)
![](CC-Sarosh-059-Lab6_media/image-1387.png)
![](CC-Sarosh-059-Lab6_media/image-1388.png)
![](CC-Sarosh-059-Lab6_media/image-1389.png)
![](CC-Sarosh-059-Lab6_media/image-139.png)
![](CC-Sarosh-059-Lab6_media/image-1390.jpg)
![](CC-Sarosh-059-Lab6_media/image-1391.png)
![](CC-Sarosh-059-Lab6_media/image-1392.png)
![](CC-Sarosh-059-Lab6_media/image-1393.png)
![](CC-Sarosh-059-Lab6_media/image-1394.png)
![](CC-Sarosh-059-Lab6_media/image-1395.png)
![](CC-Sarosh-059-Lab6_media/image-1396.png)
![](CC-Sarosh-059-Lab6_media/image-1397.png)
![](CC-Sarosh-059-Lab6_media/image-1398.png)
![](CC-Sarosh-059-Lab6_media/image-1399.png)
![](CC-Sarosh-059-Lab6_media/image-140.png)
![](CC-Sarosh-059-Lab6_media/image-1400.png)
![](CC-Sarosh-059-Lab6_media/image-1401.png)
![](CC-Sarosh-059-Lab6_media/image-1402.png)
![](CC-Sarosh-059-Lab6_media/image-1403.png)
![](CC-Sarosh-059-Lab6_media/image-1404.png)
![](CC-Sarosh-059-Lab6_media/image-1405.png)
![](CC-Sarosh-059-Lab6_media/image-1406.png)
![](CC-Sarosh-059-Lab6_media/image-1407.png)
![](CC-Sarosh-059-Lab6_media/image-1408.png)
![](CC-Sarosh-059-Lab6_media/image-1409.png)
![](CC-Sarosh-059-Lab6_media/image-141.png)
![](CC-Sarosh-059-Lab6_media/image-1410.png)
![](CC-Sarosh-059-Lab6_media/image-1411.png)
![](CC-Sarosh-059-Lab6_media/image-1412.png)
![](CC-Sarosh-059-Lab6_media/image-1413.png)
![](CC-Sarosh-059-Lab6_media/image-1414.png)
![](CC-Sarosh-059-Lab6_media/image-1415.jpg)
![](CC-Sarosh-059-Lab6_media/image-1416.png)
![](CC-Sarosh-059-Lab6_media/image-1417.png)
![](CC-Sarosh-059-Lab6_media/image-1418.png)
![](CC-Sarosh-059-Lab6_media/image-1419.png)
![](CC-Sarosh-059-Lab6_media/image-142.png)
![](CC-Sarosh-059-Lab6_media/image-1420.png)
![](CC-Sarosh-059-Lab6_media/image-1421.png)
![](CC-Sarosh-059-Lab6_media/image-1422.png)
![](CC-Sarosh-059-Lab6_media/image-1423.png)
![](CC-Sarosh-059-Lab6_media/image-1424.png)
![](CC-Sarosh-059-Lab6_media/image-1425.png)
![](CC-Sarosh-059-Lab6_media/image-1426.png)
![](CC-Sarosh-059-Lab6_media/image-1427.png)
![](CC-Sarosh-059-Lab6_media/image-1428.png)
![](CC-Sarosh-059-Lab6_media/image-1429.png)
![](CC-Sarosh-059-Lab6_media/image-143.png)
![](CC-Sarosh-059-Lab6_media/image-1430.png)
![](CC-Sarosh-059-Lab6_media/image-1431.png)
![](CC-Sarosh-059-Lab6_media/image-1432.png)
![](CC-Sarosh-059-Lab6_media/image-1433.png)
![](CC-Sarosh-059-Lab6_media/image-1434.png)
![](CC-Sarosh-059-Lab6_media/image-1435.png)
![](CC-Sarosh-059-Lab6_media/image-1436.png)
![](CC-Sarosh-059-Lab6_media/image-1437.png)
![](CC-Sarosh-059-Lab6_media/image-1438.png)
![](CC-Sarosh-059-Lab6_media/image-1439.png)
![](CC-Sarosh-059-Lab6_media/image-144.png)
![](CC-Sarosh-059-Lab6_media/image-1440.png)
![](CC-Sarosh-059-Lab6_media/image-1441.png)
![](CC-Sarosh-059-Lab6_media/image-1442.png)
![](CC-Sarosh-059-Lab6_media/image-1443.png)
![](CC-Sarosh-059-Lab6_media/image-1444.png)
![](CC-Sarosh-059-Lab6_media/image-1445.png)
![](CC-Sarosh-059-Lab6_media/image-1446.png)
![](CC-Sarosh-059-Lab6_media/image-1447.png)
![](CC-Sarosh-059-Lab6_media/image-1448.jpg)
![](CC-Sarosh-059-Lab6_media/image-1449.jpg)
![](CC-Sarosh-059-Lab6_media/image-145.png)
![](CC-Sarosh-059-Lab6_media/image-1450.png)
![](CC-Sarosh-059-Lab6_media/image-1451.png)
![](CC-Sarosh-059-Lab6_media/image-1452.png)
![](CC-Sarosh-059-Lab6_media/image-1453.png)
![](CC-Sarosh-059-Lab6_media/image-1454.png)
![](CC-Sarosh-059-Lab6_media/image-1455.png)
![](CC-Sarosh-059-Lab6_media/image-1456.png)
![](CC-Sarosh-059-Lab6_media/image-1457.png)
![](CC-Sarosh-059-Lab6_media/image-1458.png)
![](CC-Sarosh-059-Lab6_media/image-1459.png)
![](CC-Sarosh-059-Lab6_media/image-146.png)
![](CC-Sarosh-059-Lab6_media/image-1460.png)
![](CC-Sarosh-059-Lab6_media/image-1461.png)
![](CC-Sarosh-059-Lab6_media/image-1462.jpg)
![](CC-Sarosh-059-Lab6_media/image-1463.png)
![](CC-Sarosh-059-Lab6_media/image-1464.png)
![](CC-Sarosh-059-Lab6_media/image-1465.png)
![](CC-Sarosh-059-Lab6_media/image-1466.png)
![](CC-Sarosh-059-Lab6_media/image-1467.png)
![](CC-Sarosh-059-Lab6_media/image-1468.png)
![](CC-Sarosh-059-Lab6_media/image-1469.png)
![](CC-Sarosh-059-Lab6_media/image-147.png)
![](CC-Sarosh-059-Lab6_media/image-1470.png)
![](CC-Sarosh-059-Lab6_media/image-1471.png)
![](CC-Sarosh-059-Lab6_media/image-1472.png)
![](CC-Sarosh-059-Lab6_media/image-1473.png)
![](CC-Sarosh-059-Lab6_media/image-1474.png)
![](CC-Sarosh-059-Lab6_media/image-1475.png)
![](CC-Sarosh-059-Lab6_media/image-1476.png)
![](CC-Sarosh-059-Lab6_media/image-1477.png)
![](CC-Sarosh-059-Lab6_media/image-1478.png)
![](CC-Sarosh-059-Lab6_media/image-1479.png)
![](CC-Sarosh-059-Lab6_media/image-148.jpg)
![](CC-Sarosh-059-Lab6_media/image-1480.png)
![](CC-Sarosh-059-Lab6_media/image-1481.png)
![](CC-Sarosh-059-Lab6_media/image-1482.png)
![](CC-Sarosh-059-Lab6_media/image-1483.png)
![](CC-Sarosh-059-Lab6_media/image-1484.png)
![](CC-Sarosh-059-Lab6_media/image-1485.png)
![](CC-Sarosh-059-Lab6_media/image-1486.png)
![](CC-Sarosh-059-Lab6_media/image-1487.png)
![](CC-Sarosh-059-Lab6_media/image-1488.png)
![](CC-Sarosh-059-Lab6_media/image-1489.png)
![](CC-Sarosh-059-Lab6_media/image-149.jpg)
![](CC-Sarosh-059-Lab6_media/image-1490.png)
![](CC-Sarosh-059-Lab6_media/image-1491.png)
![](CC-Sarosh-059-Lab6_media/image-1492.png)
![](CC-Sarosh-059-Lab6_media/image-1493.png)
![](CC-Sarosh-059-Lab6_media/image-1494.png)
![](CC-Sarosh-059-Lab6_media/image-1495.png)
![](CC-Sarosh-059-Lab6_media/image-1496.png)
![](CC-Sarosh-059-Lab6_media/image-1497.png)
![](CC-Sarosh-059-Lab6_media/image-1498.png)
![](CC-Sarosh-059-Lab6_media/image-1499.png)
![](CC-Sarosh-059-Lab6_media/image-150.jpg)
![](CC-Sarosh-059-Lab6_media/image-1500.png)
![](CC-Sarosh-059-Lab6_media/image-1501.png)
![](CC-Sarosh-059-Lab6_media/image-1502.png)
![](CC-Sarosh-059-Lab6_media/image-1503.png)
![](CC-Sarosh-059-Lab6_media/image-1504.png)
![](CC-Sarosh-059-Lab6_media/image-1505.png)
![](CC-Sarosh-059-Lab6_media/image-1506.png)
![](CC-Sarosh-059-Lab6_media/image-1507.png)
![](CC-Sarosh-059-Lab6_media/image-1508.png)
![](CC-Sarosh-059-Lab6_media/image-1509.png)
![](CC-Sarosh-059-Lab6_media/image-151.png)
![](CC-Sarosh-059-Lab6_media/image-1510.png)
![](CC-Sarosh-059-Lab6_media/image-1511.png)
![](CC-Sarosh-059-Lab6_media/image-1512.png)
![](CC-Sarosh-059-Lab6_media/image-1513.png)
![](CC-Sarosh-059-Lab6_media/image-1514.png)
![](CC-Sarosh-059-Lab6_media/image-1515.png)
![](CC-Sarosh-059-Lab6_media/image-1516.png)
![](CC-Sarosh-059-Lab6_media/image-1517.png)
![](CC-Sarosh-059-Lab6_media/image-1518.png)
![](CC-Sarosh-059-Lab6_media/image-1519.png)
![](CC-Sarosh-059-Lab6_media/image-152.png)
![](CC-Sarosh-059-Lab6_media/image-1520.png)
![](CC-Sarosh-059-Lab6_media/image-1521.png)
![](CC-Sarosh-059-Lab6_media/image-1522.png)
![](CC-Sarosh-059-Lab6_media/image-1523.png)
![](CC-Sarosh-059-Lab6_media/image-1524.png)
![](CC-Sarosh-059-Lab6_media/image-1525.png)
![](CC-Sarosh-059-Lab6_media/image-1526.png)
![](CC-Sarosh-059-Lab6_media/image-1527.png)
![](CC-Sarosh-059-Lab6_media/image-1528.png)
![](CC-Sarosh-059-Lab6_media/image-1529.png)
![](CC-Sarosh-059-Lab6_media/image-153.png)
![](CC-Sarosh-059-Lab6_media/image-1530.png)
![](CC-Sarosh-059-Lab6_media/image-1531.png)
![](CC-Sarosh-059-Lab6_media/image-1532.png)
![](CC-Sarosh-059-Lab6_media/image-1533.png)
![](CC-Sarosh-059-Lab6_media/image-1534.png)
![](CC-Sarosh-059-Lab6_media/image-1535.png)
![](CC-Sarosh-059-Lab6_media/image-1536.png)
![](CC-Sarosh-059-Lab6_media/image-1537.png)
![](CC-Sarosh-059-Lab6_media/image-1538.png)
![](CC-Sarosh-059-Lab6_media/image-1539.png)
![](CC-Sarosh-059-Lab6_media/image-154.png)
![](CC-Sarosh-059-Lab6_media/image-1540.png)
![](CC-Sarosh-059-Lab6_media/image-1541.png)
![](CC-Sarosh-059-Lab6_media/image-1542.png)
![](CC-Sarosh-059-Lab6_media/image-1543.png)
![](CC-Sarosh-059-Lab6_media/image-1544.png)
![](CC-Sarosh-059-Lab6_media/image-1545.png)
![](CC-Sarosh-059-Lab6_media/image-1546.png)
![](CC-Sarosh-059-Lab6_media/image-1547.png)
![](CC-Sarosh-059-Lab6_media/image-1548.png)
![](CC-Sarosh-059-Lab6_media/image-1549.png)
![](CC-Sarosh-059-Lab6_media/image-155.png)
![](CC-Sarosh-059-Lab6_media/image-1550.png)
![](CC-Sarosh-059-Lab6_media/image-1551.png)
![](CC-Sarosh-059-Lab6_media/image-1552.png)
![](CC-Sarosh-059-Lab6_media/image-1553.png)
![](CC-Sarosh-059-Lab6_media/image-1554.png)
![](CC-Sarosh-059-Lab6_media/image-1555.png)
![](CC-Sarosh-059-Lab6_media/image-1556.png)
![](CC-Sarosh-059-Lab6_media/image-1557.png)
![](CC-Sarosh-059-Lab6_media/image-1558.png)
![](CC-Sarosh-059-Lab6_media/image-1559.jpg)
![](CC-Sarosh-059-Lab6_media/image-156.png)
![](CC-Sarosh-059-Lab6_media/image-1560.png)
![](CC-Sarosh-059-Lab6_media/image-1561.png)
![](CC-Sarosh-059-Lab6_media/image-1562.png)
![](CC-Sarosh-059-Lab6_media/image-1563.png)
![](CC-Sarosh-059-Lab6_media/image-1564.png)
![](CC-Sarosh-059-Lab6_media/image-1565.png)
![](CC-Sarosh-059-Lab6_media/image-1566.png)
![](CC-Sarosh-059-Lab6_media/image-1567.png)
![](CC-Sarosh-059-Lab6_media/image-1568.png)
![](CC-Sarosh-059-Lab6_media/image-1569.png)
![](CC-Sarosh-059-Lab6_media/image-157.png)
![](CC-Sarosh-059-Lab6_media/image-1570.png)
![](CC-Sarosh-059-Lab6_media/image-1571.png)
![](CC-Sarosh-059-Lab6_media/image-1572.png)
![](CC-Sarosh-059-Lab6_media/image-1573.png)
![](CC-Sarosh-059-Lab6_media/image-1574.png)
![](CC-Sarosh-059-Lab6_media/image-1575.png)
![](CC-Sarosh-059-Lab6_media/image-1576.png)
![](CC-Sarosh-059-Lab6_media/image-1577.png)
![](CC-Sarosh-059-Lab6_media/image-1578.png)
![](CC-Sarosh-059-Lab6_media/image-1579.png)
![](CC-Sarosh-059-Lab6_media/image-158.png)
![](CC-Sarosh-059-Lab6_media/image-1580.png)
![](CC-Sarosh-059-Lab6_media/image-1581.png)
![](CC-Sarosh-059-Lab6_media/image-1582.png)
![](CC-Sarosh-059-Lab6_media/image-1583.png)
![](CC-Sarosh-059-Lab6_media/image-1584.png)
![](CC-Sarosh-059-Lab6_media/image-1585.png)
![](CC-Sarosh-059-Lab6_media/image-1586.png)
![](CC-Sarosh-059-Lab6_media/image-1587.png)
![](CC-Sarosh-059-Lab6_media/image-1588.png)
![](CC-Sarosh-059-Lab6_media/image-1589.png)
![](CC-Sarosh-059-Lab6_media/image-159.png)
![](CC-Sarosh-059-Lab6_media/image-1590.png)
![](CC-Sarosh-059-Lab6_media/image-1591.png)
![](CC-Sarosh-059-Lab6_media/image-1592.jpg)
![](CC-Sarosh-059-Lab6_media/image-1593.jpg)
![](CC-Sarosh-059-Lab6_media/image-1594.png)
![](CC-Sarosh-059-Lab6_media/image-1595.png)
![](CC-Sarosh-059-Lab6_media/image-1596.png)
![](CC-Sarosh-059-Lab6_media/image-1597.png)
![](CC-Sarosh-059-Lab6_media/image-1598.png)
![](CC-Sarosh-059-Lab6_media/image-1599.png)
![](CC-Sarosh-059-Lab6_media/image-160.png)
![](CC-Sarosh-059-Lab6_media/image-1600.png)
![](CC-Sarosh-059-Lab6_media/image-1601.png)
![](CC-Sarosh-059-Lab6_media/image-1602.png)
![](CC-Sarosh-059-Lab6_media/image-1603.png)
![](CC-Sarosh-059-Lab6_media/image-1604.png)
![](CC-Sarosh-059-Lab6_media/image-1605.png)
![](CC-Sarosh-059-Lab6_media/image-1606.jpg)
![](CC-Sarosh-059-Lab6_media/image-1607.png)
![](CC-Sarosh-059-Lab6_media/image-1608.png)
![](CC-Sarosh-059-Lab6_media/image-1609.png)
![](CC-Sarosh-059-Lab6_media/image-161.png)
![](CC-Sarosh-059-Lab6_media/image-1610.png)
![](CC-Sarosh-059-Lab6_media/image-1611.png)
![](CC-Sarosh-059-Lab6_media/image-1612.png)
![](CC-Sarosh-059-Lab6_media/image-1613.png)
![](CC-Sarosh-059-Lab6_media/image-1614.png)
![](CC-Sarosh-059-Lab6_media/image-1615.png)
![](CC-Sarosh-059-Lab6_media/image-1616.png)
![](CC-Sarosh-059-Lab6_media/image-1617.png)
![](CC-Sarosh-059-Lab6_media/image-1618.png)
![](CC-Sarosh-059-Lab6_media/image-1619.png)
![](CC-Sarosh-059-Lab6_media/image-162.png)
![](CC-Sarosh-059-Lab6_media/image-1620.png)
![](CC-Sarosh-059-Lab6_media/image-1621.png)
![](CC-Sarosh-059-Lab6_media/image-1622.png)
![](CC-Sarosh-059-Lab6_media/image-1623.png)
![](CC-Sarosh-059-Lab6_media/image-1624.png)
![](CC-Sarosh-059-Lab6_media/image-1625.png)
![](CC-Sarosh-059-Lab6_media/image-1626.png)
![](CC-Sarosh-059-Lab6_media/image-1627.png)
![](CC-Sarosh-059-Lab6_media/image-1628.png)
![](CC-Sarosh-059-Lab6_media/image-1629.png)
![](CC-Sarosh-059-Lab6_media/image-163.png)
![](CC-Sarosh-059-Lab6_media/image-1630.png)
![](CC-Sarosh-059-Lab6_media/image-1631.jpg)
![](CC-Sarosh-059-Lab6_media/image-1632.jpg)
![](CC-Sarosh-059-Lab6_media/image-1633.png)
![](CC-Sarosh-059-Lab6_media/image-1634.png)
![](CC-Sarosh-059-Lab6_media/image-1635.png)
![](CC-Sarosh-059-Lab6_media/image-1636.png)
![](CC-Sarosh-059-Lab6_media/image-1637.png)
![](CC-Sarosh-059-Lab6_media/image-1638.png)
![](CC-Sarosh-059-Lab6_media/image-1639.png)
![](CC-Sarosh-059-Lab6_media/image-164.png)
![](CC-Sarosh-059-Lab6_media/image-1640.png)
![](CC-Sarosh-059-Lab6_media/image-1641.png)
![](CC-Sarosh-059-Lab6_media/image-1642.png)
![](CC-Sarosh-059-Lab6_media/image-1643.png)
![](CC-Sarosh-059-Lab6_media/image-1644.png)
![](CC-Sarosh-059-Lab6_media/image-1645.png)
![](CC-Sarosh-059-Lab6_media/image-1646.png)
![](CC-Sarosh-059-Lab6_media/image-1647.png)
![](CC-Sarosh-059-Lab6_media/image-1648.png)
![](CC-Sarosh-059-Lab6_media/image-1649.png)
![](CC-Sarosh-059-Lab6_media/image-165.png)
![](CC-Sarosh-059-Lab6_media/image-1650.png)
![](CC-Sarosh-059-Lab6_media/image-1651.png)
![](CC-Sarosh-059-Lab6_media/image-1652.png)
![](CC-Sarosh-059-Lab6_media/image-1653.png)
![](CC-Sarosh-059-Lab6_media/image-1654.png)
![](CC-Sarosh-059-Lab6_media/image-1655.png)
![](CC-Sarosh-059-Lab6_media/image-1656.png)
![](CC-Sarosh-059-Lab6_media/image-1657.png)
![](CC-Sarosh-059-Lab6_media/image-1658.png)
![](CC-Sarosh-059-Lab6_media/image-1659.png)
![](CC-Sarosh-059-Lab6_media/image-166.png)
![](CC-Sarosh-059-Lab6_media/image-1660.png)
![](CC-Sarosh-059-Lab6_media/image-1661.png)
![](CC-Sarosh-059-Lab6_media/image-1662.png)
![](CC-Sarosh-059-Lab6_media/image-1663.png)
![](CC-Sarosh-059-Lab6_media/image-1664.png)
![](CC-Sarosh-059-Lab6_media/image-1665.jpg)
![](CC-Sarosh-059-Lab6_media/image-1666.png)
![](CC-Sarosh-059-Lab6_media/image-1667.png)
![](CC-Sarosh-059-Lab6_media/image-1668.png)
![](CC-Sarosh-059-Lab6_media/image-1669.png)
![](CC-Sarosh-059-Lab6_media/image-167.png)
![](CC-Sarosh-059-Lab6_media/image-1670.png)
![](CC-Sarosh-059-Lab6_media/image-1671.png)
![](CC-Sarosh-059-Lab6_media/image-1672.png)
![](CC-Sarosh-059-Lab6_media/image-1673.png)
![](CC-Sarosh-059-Lab6_media/image-1674.png)
![](CC-Sarosh-059-Lab6_media/image-1675.png)
![](CC-Sarosh-059-Lab6_media/image-1676.png)
![](CC-Sarosh-059-Lab6_media/image-1677.png)
![](CC-Sarosh-059-Lab6_media/image-1678.png)
![](CC-Sarosh-059-Lab6_media/image-1679.png)
![](CC-Sarosh-059-Lab6_media/image-168.png)
![](CC-Sarosh-059-Lab6_media/image-1680.png)
![](CC-Sarosh-059-Lab6_media/image-1681.png)
![](CC-Sarosh-059-Lab6_media/image-1682.png)
![](CC-Sarosh-059-Lab6_media/image-1683.png)
![](CC-Sarosh-059-Lab6_media/image-1684.png)
![](CC-Sarosh-059-Lab6_media/image-1685.png)
![](CC-Sarosh-059-Lab6_media/image-1686.png)
![](CC-Sarosh-059-Lab6_media/image-1687.png)
![](CC-Sarosh-059-Lab6_media/image-1688.png)
![](CC-Sarosh-059-Lab6_media/image-1689.png)
![](CC-Sarosh-059-Lab6_media/image-169.png)
![](CC-Sarosh-059-Lab6_media/image-1690.png)
![](CC-Sarosh-059-Lab6_media/image-1691.png)
![](CC-Sarosh-059-Lab6_media/image-1692.png)
![](CC-Sarosh-059-Lab6_media/image-1693.png)
![](CC-Sarosh-059-Lab6_media/image-1694.png)
![](CC-Sarosh-059-Lab6_media/image-1695.png)
![](CC-Sarosh-059-Lab6_media/image-1696.png)
![](CC-Sarosh-059-Lab6_media/image-1697.png)
![](CC-Sarosh-059-Lab6_media/image-1698.png)
![](CC-Sarosh-059-Lab6_media/image-1699.png)
![](CC-Sarosh-059-Lab6_media/image-170.png)
![](CC-Sarosh-059-Lab6_media/image-1700.png)
![](CC-Sarosh-059-Lab6_media/image-1701.png)
![](CC-Sarosh-059-Lab6_media/image-1702.jpg)
![](CC-Sarosh-059-Lab6_media/image-1703.jpg)
![](CC-Sarosh-059-Lab6_media/image-1704.png)
![](CC-Sarosh-059-Lab6_media/image-1705.png)
![](CC-Sarosh-059-Lab6_media/image-1706.png)
![](CC-Sarosh-059-Lab6_media/image-1707.png)
![](CC-Sarosh-059-Lab6_media/image-1708.png)
![](CC-Sarosh-059-Lab6_media/image-1709.png)
![](CC-Sarosh-059-Lab6_media/image-171.png)
![](CC-Sarosh-059-Lab6_media/image-1710.png)
![](CC-Sarosh-059-Lab6_media/image-1711.png)
![](CC-Sarosh-059-Lab6_media/image-1712.png)
![](CC-Sarosh-059-Lab6_media/image-1713.png)
![](CC-Sarosh-059-Lab6_media/image-1714.png)
![](CC-Sarosh-059-Lab6_media/image-1715.png)
![](CC-Sarosh-059-Lab6_media/image-1716.png)
![](CC-Sarosh-059-Lab6_media/image-1717.png)
![](CC-Sarosh-059-Lab6_media/image-1718.png)
![](CC-Sarosh-059-Lab6_media/image-1719.png)
![](CC-Sarosh-059-Lab6_media/image-172.png)
![](CC-Sarosh-059-Lab6_media/image-1720.png)
![](CC-Sarosh-059-Lab6_media/image-1721.png)
![](CC-Sarosh-059-Lab6_media/image-1722.png)
![](CC-Sarosh-059-Lab6_media/image-1723.png)
![](CC-Sarosh-059-Lab6_media/image-1724.png)
![](CC-Sarosh-059-Lab6_media/image-1725.png)
![](CC-Sarosh-059-Lab6_media/image-1726.png)
![](CC-Sarosh-059-Lab6_media/image-1727.png)
![](CC-Sarosh-059-Lab6_media/image-1728.png)
![](CC-Sarosh-059-Lab6_media/image-1729.png)
![](CC-Sarosh-059-Lab6_media/image-173.png)
![](CC-Sarosh-059-Lab6_media/image-1730.png)
![](CC-Sarosh-059-Lab6_media/image-1731.png)
![](CC-Sarosh-059-Lab6_media/image-1732.png)
![](CC-Sarosh-059-Lab6_media/image-1733.png)
![](CC-Sarosh-059-Lab6_media/image-1734.png)
![](CC-Sarosh-059-Lab6_media/image-1735.png)
![](CC-Sarosh-059-Lab6_media/image-1736.jpg)
![](CC-Sarosh-059-Lab6_media/image-1737.jpg)
![](CC-Sarosh-059-Lab6_media/image-1738.jpg)
![](CC-Sarosh-059-Lab6_media/image-1739.png)
![](CC-Sarosh-059-Lab6_media/image-174.png)
![](CC-Sarosh-059-Lab6_media/image-1740.png)
![](CC-Sarosh-059-Lab6_media/image-1741.png)
![](CC-Sarosh-059-Lab6_media/image-1742.png)
![](CC-Sarosh-059-Lab6_media/image-1743.png)
![](CC-Sarosh-059-Lab6_media/image-1744.png)
![](CC-Sarosh-059-Lab6_media/image-1745.png)
![](CC-Sarosh-059-Lab6_media/image-1746.png)
![](CC-Sarosh-059-Lab6_media/image-1747.png)
![](CC-Sarosh-059-Lab6_media/image-1748.png)
![](CC-Sarosh-059-Lab6_media/image-1749.png)
![](CC-Sarosh-059-Lab6_media/image-175.png)
![](CC-Sarosh-059-Lab6_media/image-1750.png)
![](CC-Sarosh-059-Lab6_media/image-1751.jpg)
![](CC-Sarosh-059-Lab6_media/image-1752.png)
![](CC-Sarosh-059-Lab6_media/image-1753.png)
![](CC-Sarosh-059-Lab6_media/image-1754.png)
![](CC-Sarosh-059-Lab6_media/image-1755.png)
![](CC-Sarosh-059-Lab6_media/image-1756.png)
![](CC-Sarosh-059-Lab6_media/image-1757.png)
![](CC-Sarosh-059-Lab6_media/image-1758.png)
![](CC-Sarosh-059-Lab6_media/image-1759.png)
![](CC-Sarosh-059-Lab6_media/image-176.png)
![](CC-Sarosh-059-Lab6_media/image-1760.png)
![](CC-Sarosh-059-Lab6_media/image-1761.png)
![](CC-Sarosh-059-Lab6_media/image-1762.png)
![](CC-Sarosh-059-Lab6_media/image-1763.png)
![](CC-Sarosh-059-Lab6_media/image-1764.png)
![](CC-Sarosh-059-Lab6_media/image-1765.png)
![](CC-Sarosh-059-Lab6_media/image-1766.png)
![](CC-Sarosh-059-Lab6_media/image-1767.png)
![](CC-Sarosh-059-Lab6_media/image-1768.png)
![](CC-Sarosh-059-Lab6_media/image-1769.png)
![](CC-Sarosh-059-Lab6_media/image-177.png)
![](CC-Sarosh-059-Lab6_media/image-1770.png)
![](CC-Sarosh-059-Lab6_media/image-1771.png)
![](CC-Sarosh-059-Lab6_media/image-1772.png)
![](CC-Sarosh-059-Lab6_media/image-1773.png)
![](CC-Sarosh-059-Lab6_media/image-1774.png)
![](CC-Sarosh-059-Lab6_media/image-1775.png)
![](CC-Sarosh-059-Lab6_media/image-1776.jpg)
![](CC-Sarosh-059-Lab6_media/image-1777.png)
![](CC-Sarosh-059-Lab6_media/image-1778.png)
![](CC-Sarosh-059-Lab6_media/image-1779.png)
![](CC-Sarosh-059-Lab6_media/image-178.png)
![](CC-Sarosh-059-Lab6_media/image-1780.png)
![](CC-Sarosh-059-Lab6_media/image-1781.png)
![](CC-Sarosh-059-Lab6_media/image-1782.png)
![](CC-Sarosh-059-Lab6_media/image-1783.png)
![](CC-Sarosh-059-Lab6_media/image-1784.png)
![](CC-Sarosh-059-Lab6_media/image-1785.png)
![](CC-Sarosh-059-Lab6_media/image-1786.png)
![](CC-Sarosh-059-Lab6_media/image-1787.png)
![](CC-Sarosh-059-Lab6_media/image-1788.png)
![](CC-Sarosh-059-Lab6_media/image-1789.png)
![](CC-Sarosh-059-Lab6_media/image-179.png)
![](CC-Sarosh-059-Lab6_media/image-1790.png)
![](CC-Sarosh-059-Lab6_media/image-1791.png)
![](CC-Sarosh-059-Lab6_media/image-1792.png)
![](CC-Sarosh-059-Lab6_media/image-1793.png)
![](CC-Sarosh-059-Lab6_media/image-1794.png)
![](CC-Sarosh-059-Lab6_media/image-1795.png)
![](CC-Sarosh-059-Lab6_media/image-1796.png)
![](CC-Sarosh-059-Lab6_media/image-1797.png)
![](CC-Sarosh-059-Lab6_media/image-1798.png)
![](CC-Sarosh-059-Lab6_media/image-1799.png)
![](CC-Sarosh-059-Lab6_media/image-180.png)
![](CC-Sarosh-059-Lab6_media/image-1800.png)
![](CC-Sarosh-059-Lab6_media/image-1801.png)
![](CC-Sarosh-059-Lab6_media/image-1802.png)
![](CC-Sarosh-059-Lab6_media/image-1803.png)
![](CC-Sarosh-059-Lab6_media/image-1804.png)
![](CC-Sarosh-059-Lab6_media/image-1805.png)
![](CC-Sarosh-059-Lab6_media/image-1806.png)
![](CC-Sarosh-059-Lab6_media/image-1807.png)
![](CC-Sarosh-059-Lab6_media/image-1808.png)
![](CC-Sarosh-059-Lab6_media/image-1809.jpg)
![](CC-Sarosh-059-Lab6_media/image-181.png)
![](CC-Sarosh-059-Lab6_media/image-1810.jpg)
![](CC-Sarosh-059-Lab6_media/image-1811.png)
![](CC-Sarosh-059-Lab6_media/image-1812.png)
![](CC-Sarosh-059-Lab6_media/image-1813.png)
![](CC-Sarosh-059-Lab6_media/image-1814.png)
![](CC-Sarosh-059-Lab6_media/image-1815.png)
![](CC-Sarosh-059-Lab6_media/image-1816.png)
![](CC-Sarosh-059-Lab6_media/image-1817.png)
![](CC-Sarosh-059-Lab6_media/image-1818.png)
![](CC-Sarosh-059-Lab6_media/image-1819.png)
![](CC-Sarosh-059-Lab6_media/image-182.png)
![](CC-Sarosh-059-Lab6_media/image-1820.png)
![](CC-Sarosh-059-Lab6_media/image-1821.png)
![](CC-Sarosh-059-Lab6_media/image-1822.png)
![](CC-Sarosh-059-Lab6_media/image-1823.jpg)
![](CC-Sarosh-059-Lab6_media/image-1824.png)
![](CC-Sarosh-059-Lab6_media/image-1825.png)
![](CC-Sarosh-059-Lab6_media/image-1826.png)
![](CC-Sarosh-059-Lab6_media/image-1827.png)
![](CC-Sarosh-059-Lab6_media/image-1828.png)
![](CC-Sarosh-059-Lab6_media/image-1829.png)
![](CC-Sarosh-059-Lab6_media/image-183.jpg)
![](CC-Sarosh-059-Lab6_media/image-1830.png)
![](CC-Sarosh-059-Lab6_media/image-1831.png)
![](CC-Sarosh-059-Lab6_media/image-1832.png)
![](CC-Sarosh-059-Lab6_media/image-1833.png)
![](CC-Sarosh-059-Lab6_media/image-1834.png)
![](CC-Sarosh-059-Lab6_media/image-1835.png)
![](CC-Sarosh-059-Lab6_media/image-1836.png)
![](CC-Sarosh-059-Lab6_media/image-1837.png)
![](CC-Sarosh-059-Lab6_media/image-1838.png)
![](CC-Sarosh-059-Lab6_media/image-1839.png)
![](CC-Sarosh-059-Lab6_media/image-184.jpg)
![](CC-Sarosh-059-Lab6_media/image-1840.png)
![](CC-Sarosh-059-Lab6_media/image-1841.png)
![](CC-Sarosh-059-Lab6_media/image-1842.png)
![](CC-Sarosh-059-Lab6_media/image-1843.png)
![](CC-Sarosh-059-Lab6_media/image-1844.png)
![](CC-Sarosh-059-Lab6_media/image-1845.png)
![](CC-Sarosh-059-Lab6_media/image-1846.png)
![](CC-Sarosh-059-Lab6_media/image-1847.png)
![](CC-Sarosh-059-Lab6_media/image-1848.jpg)
![](CC-Sarosh-059-Lab6_media/image-1849.png)
![](CC-Sarosh-059-Lab6_media/image-185.jpg)
![](CC-Sarosh-059-Lab6_media/image-1850.png)
![](CC-Sarosh-059-Lab6_media/image-1851.png)
![](CC-Sarosh-059-Lab6_media/image-1852.png)
![](CC-Sarosh-059-Lab6_media/image-1853.png)
![](CC-Sarosh-059-Lab6_media/image-1854.png)
![](CC-Sarosh-059-Lab6_media/image-1855.png)
![](CC-Sarosh-059-Lab6_media/image-1856.png)
![](CC-Sarosh-059-Lab6_media/image-1857.png)
![](CC-Sarosh-059-Lab6_media/image-1858.png)
![](CC-Sarosh-059-Lab6_media/image-1859.png)
![](CC-Sarosh-059-Lab6_media/image-186.png)
![](CC-Sarosh-059-Lab6_media/image-1860.png)
![](CC-Sarosh-059-Lab6_media/image-1861.png)
![](CC-Sarosh-059-Lab6_media/image-1862.png)
![](CC-Sarosh-059-Lab6_media/image-1863.png)
![](CC-Sarosh-059-Lab6_media/image-1864.png)
![](CC-Sarosh-059-Lab6_media/image-1865.png)
![](CC-Sarosh-059-Lab6_media/image-1866.png)
![](CC-Sarosh-059-Lab6_media/image-1867.png)
![](CC-Sarosh-059-Lab6_media/image-1868.png)
![](CC-Sarosh-059-Lab6_media/image-1869.png)
![](CC-Sarosh-059-Lab6_media/image-187.png)
![](CC-Sarosh-059-Lab6_media/image-1870.png)
![](CC-Sarosh-059-Lab6_media/image-1871.png)
![](CC-Sarosh-059-Lab6_media/image-1872.png)
![](CC-Sarosh-059-Lab6_media/image-1873.png)
![](CC-Sarosh-059-Lab6_media/image-1874.png)
![](CC-Sarosh-059-Lab6_media/image-1875.png)
![](CC-Sarosh-059-Lab6_media/image-1876.png)
![](CC-Sarosh-059-Lab6_media/image-1877.png)
![](CC-Sarosh-059-Lab6_media/image-1878.png)
![](CC-Sarosh-059-Lab6_media/image-1879.png)
![](CC-Sarosh-059-Lab6_media/image-188.png)
![](CC-Sarosh-059-Lab6_media/image-1880.png)
![](CC-Sarosh-059-Lab6_media/image-1881.jpg)
![](CC-Sarosh-059-Lab6_media/image-1882.jpg)
![](CC-Sarosh-059-Lab6_media/image-1883.png)
![](CC-Sarosh-059-Lab6_media/image-1884.png)
![](CC-Sarosh-059-Lab6_media/image-1885.png)
![](CC-Sarosh-059-Lab6_media/image-1886.png)
![](CC-Sarosh-059-Lab6_media/image-1887.png)
![](CC-Sarosh-059-Lab6_media/image-1888.png)
![](CC-Sarosh-059-Lab6_media/image-1889.png)
![](CC-Sarosh-059-Lab6_media/image-189.png)
![](CC-Sarosh-059-Lab6_media/image-1890.png)
![](CC-Sarosh-059-Lab6_media/image-1891.png)
![](CC-Sarosh-059-Lab6_media/image-1892.png)
![](CC-Sarosh-059-Lab6_media/image-1893.png)
![](CC-Sarosh-059-Lab6_media/image-1894.png)
![](CC-Sarosh-059-Lab6_media/image-1895.jpg)
![](CC-Sarosh-059-Lab6_media/image-1896.png)
![](CC-Sarosh-059-Lab6_media/image-1897.png)
![](CC-Sarosh-059-Lab6_media/image-1898.png)
![](CC-Sarosh-059-Lab6_media/image-1899.png)
![](CC-Sarosh-059-Lab6_media/image-190.png)
![](CC-Sarosh-059-Lab6_media/image-1900.png)
![](CC-Sarosh-059-Lab6_media/image-1901.png)
![](CC-Sarosh-059-Lab6_media/image-1902.png)
![](CC-Sarosh-059-Lab6_media/image-1903.png)
![](CC-Sarosh-059-Lab6_media/image-1904.png)
![](CC-Sarosh-059-Lab6_media/image-1905.png)
![](CC-Sarosh-059-Lab6_media/image-1906.png)
![](CC-Sarosh-059-Lab6_media/image-1907.png)
![](CC-Sarosh-059-Lab6_media/image-1908.png)
![](CC-Sarosh-059-Lab6_media/image-1909.png)
![](CC-Sarosh-059-Lab6_media/image-191.png)
![](CC-Sarosh-059-Lab6_media/image-1910.png)
![](CC-Sarosh-059-Lab6_media/image-1911.png)
![](CC-Sarosh-059-Lab6_media/image-1912.png)
![](CC-Sarosh-059-Lab6_media/image-1913.png)
![](CC-Sarosh-059-Lab6_media/image-1914.png)
![](CC-Sarosh-059-Lab6_media/image-1915.png)
![](CC-Sarosh-059-Lab6_media/image-1916.png)
![](CC-Sarosh-059-Lab6_media/image-1917.png)
![](CC-Sarosh-059-Lab6_media/image-1918.png)
![](CC-Sarosh-059-Lab6_media/image-1919.png)
![](CC-Sarosh-059-Lab6_media/image-192.png)
![](CC-Sarosh-059-Lab6_media/image-1920.jpg)
![](CC-Sarosh-059-Lab6_media/image-1921.jpg)
![](CC-Sarosh-059-Lab6_media/image-1922.png)
![](CC-Sarosh-059-Lab6_media/image-1923.png)
![](CC-Sarosh-059-Lab6_media/image-1924.png)
![](CC-Sarosh-059-Lab6_media/image-1925.png)
![](CC-Sarosh-059-Lab6_media/image-1926.png)
![](CC-Sarosh-059-Lab6_media/image-1927.png)
![](CC-Sarosh-059-Lab6_media/image-1928.png)
![](CC-Sarosh-059-Lab6_media/image-1929.png)
![](CC-Sarosh-059-Lab6_media/image-193.png)
![](CC-Sarosh-059-Lab6_media/image-1930.png)
![](CC-Sarosh-059-Lab6_media/image-1931.png)
![](CC-Sarosh-059-Lab6_media/image-1932.png)
![](CC-Sarosh-059-Lab6_media/image-1933.png)
![](CC-Sarosh-059-Lab6_media/image-1934.png)
![](CC-Sarosh-059-Lab6_media/image-1935.png)
![](CC-Sarosh-059-Lab6_media/image-1936.png)
![](CC-Sarosh-059-Lab6_media/image-1937.png)
![](CC-Sarosh-059-Lab6_media/image-1938.png)
![](CC-Sarosh-059-Lab6_media/image-1939.png)
![](CC-Sarosh-059-Lab6_media/image-194.png)
![](CC-Sarosh-059-Lab6_media/image-1940.png)
![](CC-Sarosh-059-Lab6_media/image-1941.png)
![](CC-Sarosh-059-Lab6_media/image-1942.png)
![](CC-Sarosh-059-Lab6_media/image-1943.png)
![](CC-Sarosh-059-Lab6_media/image-1944.png)
![](CC-Sarosh-059-Lab6_media/image-1945.png)
![](CC-Sarosh-059-Lab6_media/image-1946.png)
![](CC-Sarosh-059-Lab6_media/image-1947.png)
![](CC-Sarosh-059-Lab6_media/image-1948.png)
![](CC-Sarosh-059-Lab6_media/image-1949.png)
![](CC-Sarosh-059-Lab6_media/image-195.png)
![](CC-Sarosh-059-Lab6_media/image-1950.png)
![](CC-Sarosh-059-Lab6_media/image-1951.png)
![](CC-Sarosh-059-Lab6_media/image-1952.png)
![](CC-Sarosh-059-Lab6_media/image-1953.png)
![](CC-Sarosh-059-Lab6_media/image-1954.jpg)
![](CC-Sarosh-059-Lab6_media/image-1955.jpg)
![](CC-Sarosh-059-Lab6_media/image-1956.jpg)
![](CC-Sarosh-059-Lab6_media/image-1957.jpg)
![](CC-Sarosh-059-Lab6_media/image-1958.png)
![](CC-Sarosh-059-Lab6_media/image-1959.png)
![](CC-Sarosh-059-Lab6_media/image-196.png)
![](CC-Sarosh-059-Lab6_media/image-1960.png)
![](CC-Sarosh-059-Lab6_media/image-1961.png)
![](CC-Sarosh-059-Lab6_media/image-1962.png)
![](CC-Sarosh-059-Lab6_media/image-1963.png)
![](CC-Sarosh-059-Lab6_media/image-1964.png)
![](CC-Sarosh-059-Lab6_media/image-1965.png)
![](CC-Sarosh-059-Lab6_media/image-1966.png)
![](CC-Sarosh-059-Lab6_media/image-1967.png)
![](CC-Sarosh-059-Lab6_media/image-1968.png)
![](CC-Sarosh-059-Lab6_media/image-1969.png)
![](CC-Sarosh-059-Lab6_media/image-197.png)
![](CC-Sarosh-059-Lab6_media/image-1970.jpg)
![](CC-Sarosh-059-Lab6_media/image-1971.jpg)
![](CC-Sarosh-059-Lab6_media/image-1972.png)
![](CC-Sarosh-059-Lab6_media/image-1973.png)
![](CC-Sarosh-059-Lab6_media/image-1974.png)
![](CC-Sarosh-059-Lab6_media/image-1975.png)
![](CC-Sarosh-059-Lab6_media/image-1976.png)
![](CC-Sarosh-059-Lab6_media/image-1977.png)
![](CC-Sarosh-059-Lab6_media/image-1978.png)
![](CC-Sarosh-059-Lab6_media/image-1979.png)
![](CC-Sarosh-059-Lab6_media/image-198.jpg)
![](CC-Sarosh-059-Lab6_media/image-1980.png)
![](CC-Sarosh-059-Lab6_media/image-1981.png)
![](CC-Sarosh-059-Lab6_media/image-1982.png)
![](CC-Sarosh-059-Lab6_media/image-1983.png)
![](CC-Sarosh-059-Lab6_media/image-1984.png)
![](CC-Sarosh-059-Lab6_media/image-1985.png)
![](CC-Sarosh-059-Lab6_media/image-1986.png)
![](CC-Sarosh-059-Lab6_media/image-1987.png)
![](CC-Sarosh-059-Lab6_media/image-1988.png)
![](CC-Sarosh-059-Lab6_media/image-1989.png)
![](CC-Sarosh-059-Lab6_media/image-199.png)
![](CC-Sarosh-059-Lab6_media/image-1990.png)
![](CC-Sarosh-059-Lab6_media/image-1991.png)
![](CC-Sarosh-059-Lab6_media/image-1992.png)
![](CC-Sarosh-059-Lab6_media/image-1993.png)
![](CC-Sarosh-059-Lab6_media/image-1994.png)
![](CC-Sarosh-059-Lab6_media/image-1995.png)
![](CC-Sarosh-059-Lab6_media/image-1996.jpg)
![](CC-Sarosh-059-Lab6_media/image-1997.png)
![](CC-Sarosh-059-Lab6_media/image-1998.png)
![](CC-Sarosh-059-Lab6_media/image-1999.png)
![](CC-Sarosh-059-Lab6_media/image-200.png)
![](CC-Sarosh-059-Lab6_media/image-2000.png)
![](CC-Sarosh-059-Lab6_media/image-2001.png)
![](CC-Sarosh-059-Lab6_media/image-2002.png)
![](CC-Sarosh-059-Lab6_media/image-2003.png)
![](CC-Sarosh-059-Lab6_media/image-2004.png)
![](CC-Sarosh-059-Lab6_media/image-2005.png)
![](CC-Sarosh-059-Lab6_media/image-2006.png)
![](CC-Sarosh-059-Lab6_media/image-2007.png)
![](CC-Sarosh-059-Lab6_media/image-2008.png)
![](CC-Sarosh-059-Lab6_media/image-2009.png)
![](CC-Sarosh-059-Lab6_media/image-201.png)
![](CC-Sarosh-059-Lab6_media/image-2010.png)
![](CC-Sarosh-059-Lab6_media/image-2011.png)
![](CC-Sarosh-059-Lab6_media/image-2012.png)
![](CC-Sarosh-059-Lab6_media/image-2013.png)
![](CC-Sarosh-059-Lab6_media/image-2014.png)
![](CC-Sarosh-059-Lab6_media/image-2015.png)
![](CC-Sarosh-059-Lab6_media/image-2016.png)
![](CC-Sarosh-059-Lab6_media/image-2017.png)
![](CC-Sarosh-059-Lab6_media/image-2018.png)
![](CC-Sarosh-059-Lab6_media/image-2019.png)
![](CC-Sarosh-059-Lab6_media/image-202.png)
![](CC-Sarosh-059-Lab6_media/image-2020.png)
![](CC-Sarosh-059-Lab6_media/image-2021.png)
![](CC-Sarosh-059-Lab6_media/image-2022.png)
![](CC-Sarosh-059-Lab6_media/image-2023.png)
![](CC-Sarosh-059-Lab6_media/image-2024.png)
![](CC-Sarosh-059-Lab6_media/image-2025.png)
![](CC-Sarosh-059-Lab6_media/image-2026.png)
![](CC-Sarosh-059-Lab6_media/image-2027.png)
![](CC-Sarosh-059-Lab6_media/image-2028.png)
![](CC-Sarosh-059-Lab6_media/image-2029.jpg)
![](CC-Sarosh-059-Lab6_media/image-203.png)
![](CC-Sarosh-059-Lab6_media/image-2030.jpg)
![](CC-Sarosh-059-Lab6_media/image-2031.png)
![](CC-Sarosh-059-Lab6_media/image-2032.png)
![](CC-Sarosh-059-Lab6_media/image-2033.png)
![](CC-Sarosh-059-Lab6_media/image-2034.png)
![](CC-Sarosh-059-Lab6_media/image-2035.png)
![](CC-Sarosh-059-Lab6_media/image-2036.png)
![](CC-Sarosh-059-Lab6_media/image-2037.png)
![](CC-Sarosh-059-Lab6_media/image-2038.png)
![](CC-Sarosh-059-Lab6_media/image-2039.png)
![](CC-Sarosh-059-Lab6_media/image-204.png)
![](CC-Sarosh-059-Lab6_media/image-2040.png)
![](CC-Sarosh-059-Lab6_media/image-2041.png)
![](CC-Sarosh-059-Lab6_media/image-2042.png)
![](CC-Sarosh-059-Lab6_media/image-2043.jpg)
![](CC-Sarosh-059-Lab6_media/image-2044.png)
![](CC-Sarosh-059-Lab6_media/image-2045.png)
![](CC-Sarosh-059-Lab6_media/image-2046.png)
![](CC-Sarosh-059-Lab6_media/image-2047.png)
![](CC-Sarosh-059-Lab6_media/image-2048.png)
![](CC-Sarosh-059-Lab6_media/image-2049.png)
![](CC-Sarosh-059-Lab6_media/image-205.png)
![](CC-Sarosh-059-Lab6_media/image-2050.png)
![](CC-Sarosh-059-Lab6_media/image-2051.png)
![](CC-Sarosh-059-Lab6_media/image-2052.png)
![](CC-Sarosh-059-Lab6_media/image-2053.png)
![](CC-Sarosh-059-Lab6_media/image-2054.png)
![](CC-Sarosh-059-Lab6_media/image-2055.png)
![](CC-Sarosh-059-Lab6_media/image-2056.png)
![](CC-Sarosh-059-Lab6_media/image-2057.png)
![](CC-Sarosh-059-Lab6_media/image-2058.png)
![](CC-Sarosh-059-Lab6_media/image-2059.png)
![](CC-Sarosh-059-Lab6_media/image-206.png)
![](CC-Sarosh-059-Lab6_media/image-2060.png)
![](CC-Sarosh-059-Lab6_media/image-2061.png)
![](CC-Sarosh-059-Lab6_media/image-2062.png)
![](CC-Sarosh-059-Lab6_media/image-2063.png)
![](CC-Sarosh-059-Lab6_media/image-2064.png)
![](CC-Sarosh-059-Lab6_media/image-2065.png)
![](CC-Sarosh-059-Lab6_media/image-2066.png)
![](CC-Sarosh-059-Lab6_media/image-2067.png)
![](CC-Sarosh-059-Lab6_media/image-2068.jpg)
![](CC-Sarosh-059-Lab6_media/image-2069.jpg)
![](CC-Sarosh-059-Lab6_media/image-207.png)
![](CC-Sarosh-059-Lab6_media/image-2070.png)
![](CC-Sarosh-059-Lab6_media/image-2071.png)
![](CC-Sarosh-059-Lab6_media/image-2072.png)
![](CC-Sarosh-059-Lab6_media/image-2073.png)
![](CC-Sarosh-059-Lab6_media/image-2074.png)
![](CC-Sarosh-059-Lab6_media/image-2075.png)
![](CC-Sarosh-059-Lab6_media/image-2076.png)
![](CC-Sarosh-059-Lab6_media/image-2077.png)
![](CC-Sarosh-059-Lab6_media/image-2078.png)
![](CC-Sarosh-059-Lab6_media/image-2079.png)
![](CC-Sarosh-059-Lab6_media/image-208.png)
![](CC-Sarosh-059-Lab6_media/image-2080.png)
![](CC-Sarosh-059-Lab6_media/image-2081.png)
![](CC-Sarosh-059-Lab6_media/image-2082.png)
![](CC-Sarosh-059-Lab6_media/image-2083.png)
![](CC-Sarosh-059-Lab6_media/image-2084.png)
![](CC-Sarosh-059-Lab6_media/image-2085.png)
![](CC-Sarosh-059-Lab6_media/image-2086.png)
![](CC-Sarosh-059-Lab6_media/image-2087.png)
![](CC-Sarosh-059-Lab6_media/image-2088.png)
![](CC-Sarosh-059-Lab6_media/image-2089.png)
![](CC-Sarosh-059-Lab6_media/image-209.png)
![](CC-Sarosh-059-Lab6_media/image-2090.png)
![](CC-Sarosh-059-Lab6_media/image-2091.png)
![](CC-Sarosh-059-Lab6_media/image-2092.png)
![](CC-Sarosh-059-Lab6_media/image-2093.png)
![](CC-Sarosh-059-Lab6_media/image-2094.png)
![](CC-Sarosh-059-Lab6_media/image-2095.png)
![](CC-Sarosh-059-Lab6_media/image-2096.png)
![](CC-Sarosh-059-Lab6_media/image-2097.png)
![](CC-Sarosh-059-Lab6_media/image-2098.png)
![](CC-Sarosh-059-Lab6_media/image-2099.png)
![](CC-Sarosh-059-Lab6_media/image-210.png)
![](CC-Sarosh-059-Lab6_media/image-2100.png)
![](CC-Sarosh-059-Lab6_media/image-2101.png)
![](CC-Sarosh-059-Lab6_media/image-2102.jpg)
![](CC-Sarosh-059-Lab6_media/image-2103.jpg)
![](CC-Sarosh-059-Lab6_media/image-2104.jpg)
![](CC-Sarosh-059-Lab6_media/image-2105.jpg)
![](CC-Sarosh-059-Lab6_media/image-2106.png)
![](CC-Sarosh-059-Lab6_media/image-2107.png)
![](CC-Sarosh-059-Lab6_media/image-2108.png)
![](CC-Sarosh-059-Lab6_media/image-2109.png)
![](CC-Sarosh-059-Lab6_media/image-211.png)
![](CC-Sarosh-059-Lab6_media/image-2110.png)
![](CC-Sarosh-059-Lab6_media/image-2111.png)
![](CC-Sarosh-059-Lab6_media/image-2112.png)
![](CC-Sarosh-059-Lab6_media/image-2113.png)
![](CC-Sarosh-059-Lab6_media/image-2114.png)
![](CC-Sarosh-059-Lab6_media/image-2115.png)
![](CC-Sarosh-059-Lab6_media/image-2116.png)
![](CC-Sarosh-059-Lab6_media/image-2117.png)
![](CC-Sarosh-059-Lab6_media/image-2118.jpg)
![](CC-Sarosh-059-Lab6_media/image-2119.jpg)
![](CC-Sarosh-059-Lab6_media/image-212.png)
![](CC-Sarosh-059-Lab6_media/image-2120.png)
![](CC-Sarosh-059-Lab6_media/image-2121.png)
![](CC-Sarosh-059-Lab6_media/image-2122.png)
![](CC-Sarosh-059-Lab6_media/image-2123.png)
![](CC-Sarosh-059-Lab6_media/image-2124.png)
![](CC-Sarosh-059-Lab6_media/image-2125.png)
![](CC-Sarosh-059-Lab6_media/image-2126.png)
![](CC-Sarosh-059-Lab6_media/image-2127.png)
![](CC-Sarosh-059-Lab6_media/image-2128.png)
![](CC-Sarosh-059-Lab6_media/image-2129.png)
![](CC-Sarosh-059-Lab6_media/image-213.png)
![](CC-Sarosh-059-Lab6_media/image-2130.png)
![](CC-Sarosh-059-Lab6_media/image-2131.png)
![](CC-Sarosh-059-Lab6_media/image-2132.png)
![](CC-Sarosh-059-Lab6_media/image-2133.png)
![](CC-Sarosh-059-Lab6_media/image-2134.png)
![](CC-Sarosh-059-Lab6_media/image-2135.png)
![](CC-Sarosh-059-Lab6_media/image-2136.png)
![](CC-Sarosh-059-Lab6_media/image-2137.png)
![](CC-Sarosh-059-Lab6_media/image-2138.png)
![](CC-Sarosh-059-Lab6_media/image-2139.png)
![](CC-Sarosh-059-Lab6_media/image-214.png)
![](CC-Sarosh-059-Lab6_media/image-2140.png)
![](CC-Sarosh-059-Lab6_media/image-2141.png)
![](CC-Sarosh-059-Lab6_media/image-2142.png)
![](CC-Sarosh-059-Lab6_media/image-2143.png)
![](CC-Sarosh-059-Lab6_media/image-2144.jpg)
![](CC-Sarosh-059-Lab6_media/image-2145.jpg)
![](CC-Sarosh-059-Lab6_media/image-2146.png)
![](CC-Sarosh-059-Lab6_media/image-2147.png)
![](CC-Sarosh-059-Lab6_media/image-2148.png)
![](CC-Sarosh-059-Lab6_media/image-2149.png)
![](CC-Sarosh-059-Lab6_media/image-215.png)
![](CC-Sarosh-059-Lab6_media/image-2150.png)
![](CC-Sarosh-059-Lab6_media/image-2151.png)
![](CC-Sarosh-059-Lab6_media/image-2152.png)
![](CC-Sarosh-059-Lab6_media/image-2153.png)
![](CC-Sarosh-059-Lab6_media/image-2154.png)
![](CC-Sarosh-059-Lab6_media/image-2155.png)
![](CC-Sarosh-059-Lab6_media/image-2156.png)
![](CC-Sarosh-059-Lab6_media/image-2157.png)
![](CC-Sarosh-059-Lab6_media/image-2158.png)
![](CC-Sarosh-059-Lab6_media/image-2159.png)
![](CC-Sarosh-059-Lab6_media/image-216.png)
![](CC-Sarosh-059-Lab6_media/image-2160.png)
![](CC-Sarosh-059-Lab6_media/image-2161.png)
![](CC-Sarosh-059-Lab6_media/image-2162.png)
![](CC-Sarosh-059-Lab6_media/image-2163.png)
![](CC-Sarosh-059-Lab6_media/image-2164.png)
![](CC-Sarosh-059-Lab6_media/image-2165.png)
![](CC-Sarosh-059-Lab6_media/image-2166.png)
![](CC-Sarosh-059-Lab6_media/image-2167.png)
![](CC-Sarosh-059-Lab6_media/image-2168.png)
![](CC-Sarosh-059-Lab6_media/image-2169.png)
![](CC-Sarosh-059-Lab6_media/image-217.png)
![](CC-Sarosh-059-Lab6_media/image-2170.png)
![](CC-Sarosh-059-Lab6_media/image-2171.png)
![](CC-Sarosh-059-Lab6_media/image-2172.png)
![](CC-Sarosh-059-Lab6_media/image-2173.png)
![](CC-Sarosh-059-Lab6_media/image-2174.png)
![](CC-Sarosh-059-Lab6_media/image-2175.png)
![](CC-Sarosh-059-Lab6_media/image-2176.png)
![](CC-Sarosh-059-Lab6_media/image-2177.png)
![](CC-Sarosh-059-Lab6_media/image-2178.jpg)
![](CC-Sarosh-059-Lab6_media/image-2179.jpg)
![](CC-Sarosh-059-Lab6_media/image-218.png)
![](CC-Sarosh-059-Lab6_media/image-2180.png)
![](CC-Sarosh-059-Lab6_media/image-2181.png)
![](CC-Sarosh-059-Lab6_media/image-2182.png)
![](CC-Sarosh-059-Lab6_media/image-2183.png)
![](CC-Sarosh-059-Lab6_media/image-2184.png)
![](CC-Sarosh-059-Lab6_media/image-2185.png)
![](CC-Sarosh-059-Lab6_media/image-2186.png)
![](CC-Sarosh-059-Lab6_media/image-2187.png)
![](CC-Sarosh-059-Lab6_media/image-2188.png)
![](CC-Sarosh-059-Lab6_media/image-2189.png)
![](CC-Sarosh-059-Lab6_media/image-219.png)
![](CC-Sarosh-059-Lab6_media/image-2190.png)
![](CC-Sarosh-059-Lab6_media/image-2191.png)
![](CC-Sarosh-059-Lab6_media/image-2192.png)
![](CC-Sarosh-059-Lab6_media/image-2193.png)
![](CC-Sarosh-059-Lab6_media/image-2194.png)
![](CC-Sarosh-059-Lab6_media/image-2195.png)
![](CC-Sarosh-059-Lab6_media/image-2196.png)
![](CC-Sarosh-059-Lab6_media/image-2197.png)
![](CC-Sarosh-059-Lab6_media/image-2198.png)
![](CC-Sarosh-059-Lab6_media/image-2199.png)
![](CC-Sarosh-059-Lab6_media/image-220.png)
![](CC-Sarosh-059-Lab6_media/image-2200.png)
![](CC-Sarosh-059-Lab6_media/image-2201.png)
![](CC-Sarosh-059-Lab6_media/image-2202.png)
![](CC-Sarosh-059-Lab6_media/image-2203.png)
![](CC-Sarosh-059-Lab6_media/image-2204.png)
![](CC-Sarosh-059-Lab6_media/image-2205.png)
![](CC-Sarosh-059-Lab6_media/image-2206.png)
![](CC-Sarosh-059-Lab6_media/image-2207.png)
![](CC-Sarosh-059-Lab6_media/image-2208.png)
![](CC-Sarosh-059-Lab6_media/image-2209.png)
![](CC-Sarosh-059-Lab6_media/image-221.png)
![](CC-Sarosh-059-Lab6_media/image-2210.png)
![](CC-Sarosh-059-Lab6_media/image-2211.png)
![](CC-Sarosh-059-Lab6_media/image-2212.png)
![](CC-Sarosh-059-Lab6_media/image-2213.png)
![](CC-Sarosh-059-Lab6_media/image-2214.png)
![](CC-Sarosh-059-Lab6_media/image-2215.png)
![](CC-Sarosh-059-Lab6_media/image-2216.jpg)
![](CC-Sarosh-059-Lab6_media/image-2217.jpg)
![](CC-Sarosh-059-Lab6_media/image-2218.png)
![](CC-Sarosh-059-Lab6_media/image-2219.png)
![](CC-Sarosh-059-Lab6_media/image-222.png)
![](CC-Sarosh-059-Lab6_media/image-2220.png)
![](CC-Sarosh-059-Lab6_media/image-2221.png)
![](CC-Sarosh-059-Lab6_media/image-2222.png)
![](CC-Sarosh-059-Lab6_media/image-2223.png)
![](CC-Sarosh-059-Lab6_media/image-2224.png)
![](CC-Sarosh-059-Lab6_media/image-2225.png)
![](CC-Sarosh-059-Lab6_media/image-2226.png)
![](CC-Sarosh-059-Lab6_media/image-2227.png)
![](CC-Sarosh-059-Lab6_media/image-2228.png)
![](CC-Sarosh-059-Lab6_media/image-2229.png)
![](CC-Sarosh-059-Lab6_media/image-223.jpg)
![](CC-Sarosh-059-Lab6_media/image-2230.png)
![](CC-Sarosh-059-Lab6_media/image-2231.png)
![](CC-Sarosh-059-Lab6_media/image-2232.png)
![](CC-Sarosh-059-Lab6_media/image-2233.png)
![](CC-Sarosh-059-Lab6_media/image-2234.png)
![](CC-Sarosh-059-Lab6_media/image-2235.png)
![](CC-Sarosh-059-Lab6_media/image-2236.png)
![](CC-Sarosh-059-Lab6_media/image-2237.png)
![](CC-Sarosh-059-Lab6_media/image-2238.png)
![](CC-Sarosh-059-Lab6_media/image-2239.png)
![](CC-Sarosh-059-Lab6_media/image-224.jpg)
![](CC-Sarosh-059-Lab6_media/image-2240.png)
![](CC-Sarosh-059-Lab6_media/image-2241.png)
![](CC-Sarosh-059-Lab6_media/image-2242.png)
![](CC-Sarosh-059-Lab6_media/image-2243.png)
![](CC-Sarosh-059-Lab6_media/image-2244.png)
![](CC-Sarosh-059-Lab6_media/image-2245.png)
![](CC-Sarosh-059-Lab6_media/image-2246.png)
![](CC-Sarosh-059-Lab6_media/image-2247.png)
![](CC-Sarosh-059-Lab6_media/image-2248.png)
![](CC-Sarosh-059-Lab6_media/image-2249.png)
![](CC-Sarosh-059-Lab6_media/image-225.jpg)
![](CC-Sarosh-059-Lab6_media/image-2250.jpg)
![](CC-Sarosh-059-Lab6_media/image-2251.jpg)
![](CC-Sarosh-059-Lab6_media/image-2252.png)
![](CC-Sarosh-059-Lab6_media/image-2253.png)
![](CC-Sarosh-059-Lab6_media/image-2254.png)
![](CC-Sarosh-059-Lab6_media/image-2255.png)
![](CC-Sarosh-059-Lab6_media/image-2256.png)
![](CC-Sarosh-059-Lab6_media/image-2257.png)
![](CC-Sarosh-059-Lab6_media/image-2258.png)
![](CC-Sarosh-059-Lab6_media/image-2259.png)
![](CC-Sarosh-059-Lab6_media/image-226.jpg)
![](CC-Sarosh-059-Lab6_media/image-2260.png)
![](CC-Sarosh-059-Lab6_media/image-2261.png)
![](CC-Sarosh-059-Lab6_media/image-2262.png)
![](CC-Sarosh-059-Lab6_media/image-2263.png)
![](CC-Sarosh-059-Lab6_media/image-2264.png)
![](CC-Sarosh-059-Lab6_media/image-2265.png)
![](CC-Sarosh-059-Lab6_media/image-2266.png)
![](CC-Sarosh-059-Lab6_media/image-2267.png)
![](CC-Sarosh-059-Lab6_media/image-2268.png)
![](CC-Sarosh-059-Lab6_media/image-2269.png)
![](CC-Sarosh-059-Lab6_media/image-227.png)
![](CC-Sarosh-059-Lab6_media/image-2270.png)
![](CC-Sarosh-059-Lab6_media/image-2271.png)
![](CC-Sarosh-059-Lab6_media/image-2272.png)
![](CC-Sarosh-059-Lab6_media/image-2273.png)
![](CC-Sarosh-059-Lab6_media/image-2274.png)
![](CC-Sarosh-059-Lab6_media/image-2275.png)
![](CC-Sarosh-059-Lab6_media/image-2276.png)
![](CC-Sarosh-059-Lab6_media/image-2277.png)
![](CC-Sarosh-059-Lab6_media/image-2278.png)
![](CC-Sarosh-059-Lab6_media/image-2279.png)
![](CC-Sarosh-059-Lab6_media/image-228.png)
![](CC-Sarosh-059-Lab6_media/image-2280.png)
![](CC-Sarosh-059-Lab6_media/image-2281.png)
![](CC-Sarosh-059-Lab6_media/image-2282.png)
![](CC-Sarosh-059-Lab6_media/image-2283.png)
![](CC-Sarosh-059-Lab6_media/image-2284.png)
![](CC-Sarosh-059-Lab6_media/image-2285.png)
![](CC-Sarosh-059-Lab6_media/image-2286.png)
![](CC-Sarosh-059-Lab6_media/image-2287.png)
![](CC-Sarosh-059-Lab6_media/image-2288.jpg)
![](CC-Sarosh-059-Lab6_media/image-2289.jpg)
![](CC-Sarosh-059-Lab6_media/image-229.png)
![](CC-Sarosh-059-Lab6_media/image-2290.png)
![](CC-Sarosh-059-Lab6_media/image-2291.png)
![](CC-Sarosh-059-Lab6_media/image-2292.png)
![](CC-Sarosh-059-Lab6_media/image-2293.png)
![](CC-Sarosh-059-Lab6_media/image-2294.png)
![](CC-Sarosh-059-Lab6_media/image-2295.png)
![](CC-Sarosh-059-Lab6_media/image-2296.png)
![](CC-Sarosh-059-Lab6_media/image-2297.png)
![](CC-Sarosh-059-Lab6_media/image-2298.png)
![](CC-Sarosh-059-Lab6_media/image-2299.png)
![](CC-Sarosh-059-Lab6_media/image-230.png)
![](CC-Sarosh-059-Lab6_media/image-2300.png)
![](CC-Sarosh-059-Lab6_media/image-2301.png)
![](CC-Sarosh-059-Lab6_media/image-2302.png)
![](CC-Sarosh-059-Lab6_media/image-2303.png)
![](CC-Sarosh-059-Lab6_media/image-2304.png)
![](CC-Sarosh-059-Lab6_media/image-2305.png)
![](CC-Sarosh-059-Lab6_media/image-2306.png)
![](CC-Sarosh-059-Lab6_media/image-2307.png)
![](CC-Sarosh-059-Lab6_media/image-2308.png)
![](CC-Sarosh-059-Lab6_media/image-2309.png)
![](CC-Sarosh-059-Lab6_media/image-231.png)
![](CC-Sarosh-059-Lab6_media/image-2310.png)
![](CC-Sarosh-059-Lab6_media/image-2311.png)
![](CC-Sarosh-059-Lab6_media/image-2312.png)
![](CC-Sarosh-059-Lab6_media/image-2313.png)
![](CC-Sarosh-059-Lab6_media/image-2314.png)
![](CC-Sarosh-059-Lab6_media/image-2315.png)
![](CC-Sarosh-059-Lab6_media/image-2316.png)
![](CC-Sarosh-059-Lab6_media/image-2317.png)
![](CC-Sarosh-059-Lab6_media/image-2318.png)
![](CC-Sarosh-059-Lab6_media/image-2319.png)
![](CC-Sarosh-059-Lab6_media/image-232.png)
![](CC-Sarosh-059-Lab6_media/image-2320.png)
![](CC-Sarosh-059-Lab6_media/image-2321.png)
![](CC-Sarosh-059-Lab6_media/image-2322.jpg)
![](CC-Sarosh-059-Lab6_media/image-2323.png)
![](CC-Sarosh-059-Lab6_media/image-2324.png)
![](CC-Sarosh-059-Lab6_media/image-2325.png)
![](CC-Sarosh-059-Lab6_media/image-2326.png)
![](CC-Sarosh-059-Lab6_media/image-2327.png)
![](CC-Sarosh-059-Lab6_media/image-2328.png)
![](CC-Sarosh-059-Lab6_media/image-2329.png)
![](CC-Sarosh-059-Lab6_media/image-233.png)
![](CC-Sarosh-059-Lab6_media/image-2330.png)
![](CC-Sarosh-059-Lab6_media/image-2331.png)
![](CC-Sarosh-059-Lab6_media/image-2332.png)
![](CC-Sarosh-059-Lab6_media/image-2333.png)
![](CC-Sarosh-059-Lab6_media/image-2334.png)
![](CC-Sarosh-059-Lab6_media/image-2335.png)
![](CC-Sarosh-059-Lab6_media/image-2336.png)
![](CC-Sarosh-059-Lab6_media/image-2337.png)
![](CC-Sarosh-059-Lab6_media/image-2338.png)
![](CC-Sarosh-059-Lab6_media/image-2339.png)
![](CC-Sarosh-059-Lab6_media/image-234.png)
![](CC-Sarosh-059-Lab6_media/image-2340.png)
![](CC-Sarosh-059-Lab6_media/image-2341.png)
![](CC-Sarosh-059-Lab6_media/image-2342.png)
![](CC-Sarosh-059-Lab6_media/image-2343.png)
![](CC-Sarosh-059-Lab6_media/image-2344.png)
![](CC-Sarosh-059-Lab6_media/image-2345.png)
![](CC-Sarosh-059-Lab6_media/image-2346.png)
![](CC-Sarosh-059-Lab6_media/image-2347.png)
![](CC-Sarosh-059-Lab6_media/image-2348.png)
![](CC-Sarosh-059-Lab6_media/image-2349.png)
![](CC-Sarosh-059-Lab6_media/image-235.png)
![](CC-Sarosh-059-Lab6_media/image-2350.png)
![](CC-Sarosh-059-Lab6_media/image-2351.png)
![](CC-Sarosh-059-Lab6_media/image-2352.png)
![](CC-Sarosh-059-Lab6_media/image-2353.png)
![](CC-Sarosh-059-Lab6_media/image-2354.png)
![](CC-Sarosh-059-Lab6_media/image-2355.png)
![](CC-Sarosh-059-Lab6_media/image-2356.png)
![](CC-Sarosh-059-Lab6_media/image-2357.png)
![](CC-Sarosh-059-Lab6_media/image-2358.png)
![](CC-Sarosh-059-Lab6_media/image-2359.jpg)
![](CC-Sarosh-059-Lab6_media/image-236.png)
![](CC-Sarosh-059-Lab6_media/image-2360.png)
![](CC-Sarosh-059-Lab6_media/image-2361.png)
![](CC-Sarosh-059-Lab6_media/image-2362.png)
![](CC-Sarosh-059-Lab6_media/image-2363.png)
![](CC-Sarosh-059-Lab6_media/image-2364.png)
![](CC-Sarosh-059-Lab6_media/image-2365.png)
![](CC-Sarosh-059-Lab6_media/image-2366.png)
![](CC-Sarosh-059-Lab6_media/image-2367.png)
![](CC-Sarosh-059-Lab6_media/image-2368.png)
![](CC-Sarosh-059-Lab6_media/image-2369.png)
![](CC-Sarosh-059-Lab6_media/image-237.png)
![](CC-Sarosh-059-Lab6_media/image-2370.png)
![](CC-Sarosh-059-Lab6_media/image-2371.png)
![](CC-Sarosh-059-Lab6_media/image-2372.png)
![](CC-Sarosh-059-Lab6_media/image-2373.png)
![](CC-Sarosh-059-Lab6_media/image-2374.png)
![](CC-Sarosh-059-Lab6_media/image-2375.png)
![](CC-Sarosh-059-Lab6_media/image-2376.png)
![](CC-Sarosh-059-Lab6_media/image-2377.png)
![](CC-Sarosh-059-Lab6_media/image-2378.png)
![](CC-Sarosh-059-Lab6_media/image-2379.png)
![](CC-Sarosh-059-Lab6_media/image-238.png)
![](CC-Sarosh-059-Lab6_media/image-2380.png)
![](CC-Sarosh-059-Lab6_media/image-2381.png)
![](CC-Sarosh-059-Lab6_media/image-2382.png)
![](CC-Sarosh-059-Lab6_media/image-2383.png)
![](CC-Sarosh-059-Lab6_media/image-2384.png)
![](CC-Sarosh-059-Lab6_media/image-2385.png)
![](CC-Sarosh-059-Lab6_media/image-2386.png)
![](CC-Sarosh-059-Lab6_media/image-2387.png)
![](CC-Sarosh-059-Lab6_media/image-2388.png)
![](CC-Sarosh-059-Lab6_media/image-2389.png)
![](CC-Sarosh-059-Lab6_media/image-239.png)
![](CC-Sarosh-059-Lab6_media/image-2390.png)
![](CC-Sarosh-059-Lab6_media/image-2391.png)
![](CC-Sarosh-059-Lab6_media/image-2392.jpg)
![](CC-Sarosh-059-Lab6_media/image-2393.jpg)
![](CC-Sarosh-059-Lab6_media/image-2394.png)
![](CC-Sarosh-059-Lab6_media/image-2395.png)
![](CC-Sarosh-059-Lab6_media/image-2396.png)
![](CC-Sarosh-059-Lab6_media/image-2397.png)
![](CC-Sarosh-059-Lab6_media/image-2398.png)
![](CC-Sarosh-059-Lab6_media/image-2399.png)
![](CC-Sarosh-059-Lab6_media/image-240.png)
![](CC-Sarosh-059-Lab6_media/image-2400.png)
![](CC-Sarosh-059-Lab6_media/image-2401.png)
![](CC-Sarosh-059-Lab6_media/image-2402.png)
![](CC-Sarosh-059-Lab6_media/image-2403.png)
![](CC-Sarosh-059-Lab6_media/image-2404.png)
![](CC-Sarosh-059-Lab6_media/image-2405.png)
![](CC-Sarosh-059-Lab6_media/image-2406.jpg)
![](CC-Sarosh-059-Lab6_media/image-2407.png)
![](CC-Sarosh-059-Lab6_media/image-2408.png)
![](CC-Sarosh-059-Lab6_media/image-2409.png)
![](CC-Sarosh-059-Lab6_media/image-241.png)
![](CC-Sarosh-059-Lab6_media/image-2410.png)
![](CC-Sarosh-059-Lab6_media/image-2411.png)
![](CC-Sarosh-059-Lab6_media/image-2412.png)
![](CC-Sarosh-059-Lab6_media/image-2413.png)
![](CC-Sarosh-059-Lab6_media/image-2414.png)
![](CC-Sarosh-059-Lab6_media/image-2415.png)
![](CC-Sarosh-059-Lab6_media/image-2416.png)
![](CC-Sarosh-059-Lab6_media/image-2417.png)
![](CC-Sarosh-059-Lab6_media/image-2418.png)
![](CC-Sarosh-059-Lab6_media/image-2419.png)
![](CC-Sarosh-059-Lab6_media/image-242.png)
![](CC-Sarosh-059-Lab6_media/image-2420.png)
![](CC-Sarosh-059-Lab6_media/image-2421.png)
![](CC-Sarosh-059-Lab6_media/image-2422.png)
![](CC-Sarosh-059-Lab6_media/image-2423.png)
![](CC-Sarosh-059-Lab6_media/image-2424.png)
![](CC-Sarosh-059-Lab6_media/image-2425.png)
![](CC-Sarosh-059-Lab6_media/image-2426.png)
![](CC-Sarosh-059-Lab6_media/image-2427.png)
![](CC-Sarosh-059-Lab6_media/image-2428.png)
![](CC-Sarosh-059-Lab6_media/image-2429.png)
![](CC-Sarosh-059-Lab6_media/image-243.png)
![](CC-Sarosh-059-Lab6_media/image-2430.png)
![](CC-Sarosh-059-Lab6_media/image-2431.jpg)
![](CC-Sarosh-059-Lab6_media/image-2432.png)
![](CC-Sarosh-059-Lab6_media/image-2433.png)
![](CC-Sarosh-059-Lab6_media/image-2434.png)
![](CC-Sarosh-059-Lab6_media/image-2435.png)
![](CC-Sarosh-059-Lab6_media/image-2436.png)
![](CC-Sarosh-059-Lab6_media/image-2437.png)
![](CC-Sarosh-059-Lab6_media/image-2438.png)
![](CC-Sarosh-059-Lab6_media/image-2439.png)
![](CC-Sarosh-059-Lab6_media/image-244.png)
![](CC-Sarosh-059-Lab6_media/image-2440.png)
![](CC-Sarosh-059-Lab6_media/image-2441.png)
![](CC-Sarosh-059-Lab6_media/image-2442.png)
![](CC-Sarosh-059-Lab6_media/image-2443.png)
![](CC-Sarosh-059-Lab6_media/image-2444.png)
![](CC-Sarosh-059-Lab6_media/image-2445.png)
![](CC-Sarosh-059-Lab6_media/image-2446.png)
![](CC-Sarosh-059-Lab6_media/image-2447.png)
![](CC-Sarosh-059-Lab6_media/image-2448.png)
![](CC-Sarosh-059-Lab6_media/image-2449.png)
![](CC-Sarosh-059-Lab6_media/image-245.png)
![](CC-Sarosh-059-Lab6_media/image-2450.png)
![](CC-Sarosh-059-Lab6_media/image-2451.png)
![](CC-Sarosh-059-Lab6_media/image-2452.png)
![](CC-Sarosh-059-Lab6_media/image-2453.png)
![](CC-Sarosh-059-Lab6_media/image-2454.png)
![](CC-Sarosh-059-Lab6_media/image-2455.png)
![](CC-Sarosh-059-Lab6_media/image-2456.png)
![](CC-Sarosh-059-Lab6_media/image-2457.png)
![](CC-Sarosh-059-Lab6_media/image-2458.png)
![](CC-Sarosh-059-Lab6_media/image-2459.png)
![](CC-Sarosh-059-Lab6_media/image-246.png)
![](CC-Sarosh-059-Lab6_media/image-2460.png)
![](CC-Sarosh-059-Lab6_media/image-2461.png)
![](CC-Sarosh-059-Lab6_media/image-2462.png)
![](CC-Sarosh-059-Lab6_media/image-2463.png)
![](CC-Sarosh-059-Lab6_media/image-2464.jpg)
![](CC-Sarosh-059-Lab6_media/image-2465.jpg)
![](CC-Sarosh-059-Lab6_media/image-2466.png)
![](CC-Sarosh-059-Lab6_media/image-2467.png)
![](CC-Sarosh-059-Lab6_media/image-2468.png)
![](CC-Sarosh-059-Lab6_media/image-2469.png)
![](CC-Sarosh-059-Lab6_media/image-247.png)
![](CC-Sarosh-059-Lab6_media/image-2470.png)
![](CC-Sarosh-059-Lab6_media/image-2471.png)
![](CC-Sarosh-059-Lab6_media/image-2472.png)
![](CC-Sarosh-059-Lab6_media/image-2473.png)
![](CC-Sarosh-059-Lab6_media/image-2474.png)
![](CC-Sarosh-059-Lab6_media/image-2475.png)
![](CC-Sarosh-059-Lab6_media/image-2476.png)
![](CC-Sarosh-059-Lab6_media/image-2477.png)
![](CC-Sarosh-059-Lab6_media/image-2478.jpg)
![](CC-Sarosh-059-Lab6_media/image-2479.png)
![](CC-Sarosh-059-Lab6_media/image-248.png)
![](CC-Sarosh-059-Lab6_media/image-2480.png)
![](CC-Sarosh-059-Lab6_media/image-2481.png)
![](CC-Sarosh-059-Lab6_media/image-2482.png)
![](CC-Sarosh-059-Lab6_media/image-2483.png)
![](CC-Sarosh-059-Lab6_media/image-2484.png)
![](CC-Sarosh-059-Lab6_media/image-2485.png)
![](CC-Sarosh-059-Lab6_media/image-2486.png)
![](CC-Sarosh-059-Lab6_media/image-2487.png)
![](CC-Sarosh-059-Lab6_media/image-2488.png)
![](CC-Sarosh-059-Lab6_media/image-2489.png)
![](CC-Sarosh-059-Lab6_media/image-249.png)
![](CC-Sarosh-059-Lab6_media/image-2490.png)
![](CC-Sarosh-059-Lab6_media/image-2491.png)
![](CC-Sarosh-059-Lab6_media/image-2492.png)
![](CC-Sarosh-059-Lab6_media/image-2493.png)
![](CC-Sarosh-059-Lab6_media/image-2494.png)
![](CC-Sarosh-059-Lab6_media/image-2495.png)
![](CC-Sarosh-059-Lab6_media/image-2496.png)
![](CC-Sarosh-059-Lab6_media/image-2497.png)
![](CC-Sarosh-059-Lab6_media/image-2498.png)
![](CC-Sarosh-059-Lab6_media/image-2499.png)
![](CC-Sarosh-059-Lab6_media/image-250.png)
![](CC-Sarosh-059-Lab6_media/image-2500.png)
![](CC-Sarosh-059-Lab6_media/image-2501.png)
![](CC-Sarosh-059-Lab6_media/image-2502.png)
![](CC-Sarosh-059-Lab6_media/image-2503.jpg)
![](CC-Sarosh-059-Lab6_media/image-2504.png)
![](CC-Sarosh-059-Lab6_media/image-2505.png)
![](CC-Sarosh-059-Lab6_media/image-2506.png)
![](CC-Sarosh-059-Lab6_media/image-2507.png)
![](CC-Sarosh-059-Lab6_media/image-2508.png)
![](CC-Sarosh-059-Lab6_media/image-2509.png)
![](CC-Sarosh-059-Lab6_media/image-251.png)
![](CC-Sarosh-059-Lab6_media/image-2510.png)
![](CC-Sarosh-059-Lab6_media/image-2511.png)
![](CC-Sarosh-059-Lab6_media/image-2512.png)
![](CC-Sarosh-059-Lab6_media/image-2513.png)
![](CC-Sarosh-059-Lab6_media/image-2514.png)
![](CC-Sarosh-059-Lab6_media/image-2515.png)
![](CC-Sarosh-059-Lab6_media/image-2516.png)
![](CC-Sarosh-059-Lab6_media/image-2517.png)
![](CC-Sarosh-059-Lab6_media/image-2518.png)
![](CC-Sarosh-059-Lab6_media/image-2519.png)
![](CC-Sarosh-059-Lab6_media/image-252.png)
![](CC-Sarosh-059-Lab6_media/image-2520.png)
![](CC-Sarosh-059-Lab6_media/image-2521.png)
![](CC-Sarosh-059-Lab6_media/image-2522.png)
![](CC-Sarosh-059-Lab6_media/image-2523.png)
![](CC-Sarosh-059-Lab6_media/image-2524.png)
![](CC-Sarosh-059-Lab6_media/image-2525.png)
![](CC-Sarosh-059-Lab6_media/image-2526.png)
![](CC-Sarosh-059-Lab6_media/image-2527.png)
![](CC-Sarosh-059-Lab6_media/image-2528.png)
![](CC-Sarosh-059-Lab6_media/image-2529.png)
![](CC-Sarosh-059-Lab6_media/image-253.png)
![](CC-Sarosh-059-Lab6_media/image-2530.png)
![](CC-Sarosh-059-Lab6_media/image-2531.png)
![](CC-Sarosh-059-Lab6_media/image-2532.png)
![](CC-Sarosh-059-Lab6_media/image-2533.png)
![](CC-Sarosh-059-Lab6_media/image-2534.png)
![](CC-Sarosh-059-Lab6_media/image-2535.png)
![](CC-Sarosh-059-Lab6_media/image-2536.jpg)
![](CC-Sarosh-059-Lab6_media/image-2537.jpg)
![](CC-Sarosh-059-Lab6_media/image-2538.png)
![](CC-Sarosh-059-Lab6_media/image-2539.png)
![](CC-Sarosh-059-Lab6_media/image-254.png)
![](CC-Sarosh-059-Lab6_media/image-2540.png)
![](CC-Sarosh-059-Lab6_media/image-2541.png)
![](CC-Sarosh-059-Lab6_media/image-2542.png)
![](CC-Sarosh-059-Lab6_media/image-2543.png)
![](CC-Sarosh-059-Lab6_media/image-2544.png)
![](CC-Sarosh-059-Lab6_media/image-2545.png)
![](CC-Sarosh-059-Lab6_media/image-2546.png)
![](CC-Sarosh-059-Lab6_media/image-2547.png)
![](CC-Sarosh-059-Lab6_media/image-2548.png)
![](CC-Sarosh-059-Lab6_media/image-2549.png)
![](CC-Sarosh-059-Lab6_media/image-255.png)
![](CC-Sarosh-059-Lab6_media/image-2550.jpg)
![](CC-Sarosh-059-Lab6_media/image-2551.png)
![](CC-Sarosh-059-Lab6_media/image-2552.png)
![](CC-Sarosh-059-Lab6_media/image-2553.png)
![](CC-Sarosh-059-Lab6_media/image-2554.png)
![](CC-Sarosh-059-Lab6_media/image-2555.png)
![](CC-Sarosh-059-Lab6_media/image-2556.png)
![](CC-Sarosh-059-Lab6_media/image-2557.png)
![](CC-Sarosh-059-Lab6_media/image-2558.png)
![](CC-Sarosh-059-Lab6_media/image-2559.png)
![](CC-Sarosh-059-Lab6_media/image-256.png)
![](CC-Sarosh-059-Lab6_media/image-2560.png)
![](CC-Sarosh-059-Lab6_media/image-2561.png)
![](CC-Sarosh-059-Lab6_media/image-2562.png)
![](CC-Sarosh-059-Lab6_media/image-2563.png)
![](CC-Sarosh-059-Lab6_media/image-2564.png)
![](CC-Sarosh-059-Lab6_media/image-2565.png)
![](CC-Sarosh-059-Lab6_media/image-2566.png)
![](CC-Sarosh-059-Lab6_media/image-2567.png)
![](CC-Sarosh-059-Lab6_media/image-2568.png)
![](CC-Sarosh-059-Lab6_media/image-2569.png)
![](CC-Sarosh-059-Lab6_media/image-257.png)
![](CC-Sarosh-059-Lab6_media/image-2570.png)
![](CC-Sarosh-059-Lab6_media/image-2571.png)
![](CC-Sarosh-059-Lab6_media/image-2572.png)
![](CC-Sarosh-059-Lab6_media/image-2573.png)
![](CC-Sarosh-059-Lab6_media/image-2574.png)
![](CC-Sarosh-059-Lab6_media/image-2575.png)
![](CC-Sarosh-059-Lab6_media/image-2576.png)
![](CC-Sarosh-059-Lab6_media/image-2577.png)
![](CC-Sarosh-059-Lab6_media/image-2578.png)
![](CC-Sarosh-059-Lab6_media/image-2579.png)
![](CC-Sarosh-059-Lab6_media/image-258.png)
![](CC-Sarosh-059-Lab6_media/image-2580.png)
![](CC-Sarosh-059-Lab6_media/image-2581.png)
![](CC-Sarosh-059-Lab6_media/image-2582.png)
![](CC-Sarosh-059-Lab6_media/image-2583.png)
![](CC-Sarosh-059-Lab6_media/image-2584.png)
![](CC-Sarosh-059-Lab6_media/image-2585.png)
![](CC-Sarosh-059-Lab6_media/image-2586.png)
![](CC-Sarosh-059-Lab6_media/image-2587.png)
![](CC-Sarosh-059-Lab6_media/image-2588.png)
![](CC-Sarosh-059-Lab6_media/image-2589.png)
![](CC-Sarosh-059-Lab6_media/image-259.jpg)
![](CC-Sarosh-059-Lab6_media/image-2590.png)
![](CC-Sarosh-059-Lab6_media/image-2591.png)
![](CC-Sarosh-059-Lab6_media/image-2592.png)
![](CC-Sarosh-059-Lab6_media/image-2593.png)
![](CC-Sarosh-059-Lab6_media/image-2594.png)
![](CC-Sarosh-059-Lab6_media/image-2595.png)
![](CC-Sarosh-059-Lab6_media/image-2596.png)
![](CC-Sarosh-059-Lab6_media/image-2597.png)
![](CC-Sarosh-059-Lab6_media/image-2598.png)
![](CC-Sarosh-059-Lab6_media/image-2599.png)
![](CC-Sarosh-059-Lab6_media/image-260.jpg)
![](CC-Sarosh-059-Lab6_media/image-2600.png)
![](CC-Sarosh-059-Lab6_media/image-2601.png)
![](CC-Sarosh-059-Lab6_media/image-2602.png)
![](CC-Sarosh-059-Lab6_media/image-2603.png)
![](CC-Sarosh-059-Lab6_media/image-2604.png)
![](CC-Sarosh-059-Lab6_media/image-2605.png)
![](CC-Sarosh-059-Lab6_media/image-2606.png)
![](CC-Sarosh-059-Lab6_media/image-2607.png)
![](CC-Sarosh-059-Lab6_media/image-2608.png)
![](CC-Sarosh-059-Lab6_media/image-2609.png)
![](CC-Sarosh-059-Lab6_media/image-261.jpg)
![](CC-Sarosh-059-Lab6_media/image-2610.png)
![](CC-Sarosh-059-Lab6_media/image-2611.png)
![](CC-Sarosh-059-Lab6_media/image-2612.png)
![](CC-Sarosh-059-Lab6_media/image-2613.png)
![](CC-Sarosh-059-Lab6_media/image-2614.png)
![](CC-Sarosh-059-Lab6_media/image-2615.png)
![](CC-Sarosh-059-Lab6_media/image-2616.png)
![](CC-Sarosh-059-Lab6_media/image-2617.png)
![](CC-Sarosh-059-Lab6_media/image-2618.png)
![](CC-Sarosh-059-Lab6_media/image-2619.png)
![](CC-Sarosh-059-Lab6_media/image-262.png)
![](CC-Sarosh-059-Lab6_media/image-2620.png)
![](CC-Sarosh-059-Lab6_media/image-2621.png)
![](CC-Sarosh-059-Lab6_media/image-2622.png)
![](CC-Sarosh-059-Lab6_media/image-2623.png)
![](CC-Sarosh-059-Lab6_media/image-2624.png)
![](CC-Sarosh-059-Lab6_media/image-2625.png)
![](CC-Sarosh-059-Lab6_media/image-2626.png)
![](CC-Sarosh-059-Lab6_media/image-2627.png)
![](CC-Sarosh-059-Lab6_media/image-2628.png)
![](CC-Sarosh-059-Lab6_media/image-2629.png)
![](CC-Sarosh-059-Lab6_media/image-263.png)
![](CC-Sarosh-059-Lab6_media/image-2630.png)
![](CC-Sarosh-059-Lab6_media/image-2631.png)
![](CC-Sarosh-059-Lab6_media/image-2632.png)
![](CC-Sarosh-059-Lab6_media/image-2633.png)
![](CC-Sarosh-059-Lab6_media/image-2634.png)
![](CC-Sarosh-059-Lab6_media/image-2635.png)
![](CC-Sarosh-059-Lab6_media/image-2636.png)
![](CC-Sarosh-059-Lab6_media/image-2637.png)
![](CC-Sarosh-059-Lab6_media/image-2638.png)
![](CC-Sarosh-059-Lab6_media/image-2639.png)
![](CC-Sarosh-059-Lab6_media/image-264.png)
![](CC-Sarosh-059-Lab6_media/image-2640.png)
![](CC-Sarosh-059-Lab6_media/image-2641.png)
![](CC-Sarosh-059-Lab6_media/image-2642.png)
![](CC-Sarosh-059-Lab6_media/image-2643.png)
![](CC-Sarosh-059-Lab6_media/image-2644.png)
![](CC-Sarosh-059-Lab6_media/image-2645.png)
![](CC-Sarosh-059-Lab6_media/image-2646.png)
![](CC-Sarosh-059-Lab6_media/image-2647.jpg)
![](CC-Sarosh-059-Lab6_media/image-2648.jpg)
![](CC-Sarosh-059-Lab6_media/image-2649.jpg)
![](CC-Sarosh-059-Lab6_media/image-265.png)
![](CC-Sarosh-059-Lab6_media/image-2650.png)
![](CC-Sarosh-059-Lab6_media/image-2651.png)
![](CC-Sarosh-059-Lab6_media/image-2652.png)
![](CC-Sarosh-059-Lab6_media/image-2653.png)
![](CC-Sarosh-059-Lab6_media/image-2654.png)
![](CC-Sarosh-059-Lab6_media/image-2655.png)
![](CC-Sarosh-059-Lab6_media/image-2656.png)
![](CC-Sarosh-059-Lab6_media/image-2657.png)
![](CC-Sarosh-059-Lab6_media/image-2658.png)
![](CC-Sarosh-059-Lab6_media/image-2659.png)
![](CC-Sarosh-059-Lab6_media/image-266.png)
![](CC-Sarosh-059-Lab6_media/image-2660.png)
![](CC-Sarosh-059-Lab6_media/image-2661.png)
![](CC-Sarosh-059-Lab6_media/image-2662.png)
![](CC-Sarosh-059-Lab6_media/image-2663.png)
![](CC-Sarosh-059-Lab6_media/image-2664.png)
![](CC-Sarosh-059-Lab6_media/image-2665.png)
![](CC-Sarosh-059-Lab6_media/image-2666.png)
![](CC-Sarosh-059-Lab6_media/image-2667.png)
![](CC-Sarosh-059-Lab6_media/image-2668.png)
![](CC-Sarosh-059-Lab6_media/image-2669.png)
![](CC-Sarosh-059-Lab6_media/image-267.png)
![](CC-Sarosh-059-Lab6_media/image-2670.png)
![](CC-Sarosh-059-Lab6_media/image-2671.png)
![](CC-Sarosh-059-Lab6_media/image-2672.png)
![](CC-Sarosh-059-Lab6_media/image-2673.png)
![](CC-Sarosh-059-Lab6_media/image-2674.png)
![](CC-Sarosh-059-Lab6_media/image-2675.png)
![](CC-Sarosh-059-Lab6_media/image-2676.png)
![](CC-Sarosh-059-Lab6_media/image-2677.png)
![](CC-Sarosh-059-Lab6_media/image-2678.png)
![](CC-Sarosh-059-Lab6_media/image-2679.png)
![](CC-Sarosh-059-Lab6_media/image-268.png)
![](CC-Sarosh-059-Lab6_media/image-2680.png)
![](CC-Sarosh-059-Lab6_media/image-2681.png)
![](CC-Sarosh-059-Lab6_media/image-2682.jpg)
![](CC-Sarosh-059-Lab6_media/image-2683.jpg)
![](CC-Sarosh-059-Lab6_media/image-2684.jpg)
![](CC-Sarosh-059-Lab6_media/image-2685.png)
![](CC-Sarosh-059-Lab6_media/image-2686.png)
![](CC-Sarosh-059-Lab6_media/image-2687.png)
![](CC-Sarosh-059-Lab6_media/image-2688.png)
![](CC-Sarosh-059-Lab6_media/image-2689.png)
![](CC-Sarosh-059-Lab6_media/image-269.png)
![](CC-Sarosh-059-Lab6_media/image-2690.png)
![](CC-Sarosh-059-Lab6_media/image-2691.png)
![](CC-Sarosh-059-Lab6_media/image-2692.png)
![](CC-Sarosh-059-Lab6_media/image-2693.png)
![](CC-Sarosh-059-Lab6_media/image-2694.png)
![](CC-Sarosh-059-Lab6_media/image-2695.png)
![](CC-Sarosh-059-Lab6_media/image-2696.png)
![](CC-Sarosh-059-Lab6_media/image-2697.jpg)
![](CC-Sarosh-059-Lab6_media/image-2698.jpg)
![](CC-Sarosh-059-Lab6_media/image-2699.png)
![](CC-Sarosh-059-Lab6_media/image-270.png)
![](CC-Sarosh-059-Lab6_media/image-2700.png)
![](CC-Sarosh-059-Lab6_media/image-2701.png)
![](CC-Sarosh-059-Lab6_media/image-2702.png)
![](CC-Sarosh-059-Lab6_media/image-2703.png)
![](CC-Sarosh-059-Lab6_media/image-2704.png)
![](CC-Sarosh-059-Lab6_media/image-2705.png)
![](CC-Sarosh-059-Lab6_media/image-2706.png)
![](CC-Sarosh-059-Lab6_media/image-2707.png)
![](CC-Sarosh-059-Lab6_media/image-2708.png)
![](CC-Sarosh-059-Lab6_media/image-2709.png)
![](CC-Sarosh-059-Lab6_media/image-271.png)
![](CC-Sarosh-059-Lab6_media/image-2710.png)
![](CC-Sarosh-059-Lab6_media/image-2711.png)
![](CC-Sarosh-059-Lab6_media/image-2712.png)
![](CC-Sarosh-059-Lab6_media/image-2713.png)
![](CC-Sarosh-059-Lab6_media/image-2714.png)
![](CC-Sarosh-059-Lab6_media/image-2715.png)
![](CC-Sarosh-059-Lab6_media/image-2716.png)
![](CC-Sarosh-059-Lab6_media/image-2717.png)
![](CC-Sarosh-059-Lab6_media/image-2718.png)
![](CC-Sarosh-059-Lab6_media/image-2719.png)
![](CC-Sarosh-059-Lab6_media/image-272.png)
![](CC-Sarosh-059-Lab6_media/image-2720.png)
![](CC-Sarosh-059-Lab6_media/image-2721.png)
![](CC-Sarosh-059-Lab6_media/image-2722.png)
![](CC-Sarosh-059-Lab6_media/image-2723.jpg)
![](CC-Sarosh-059-Lab6_media/image-2724.jpg)
![](CC-Sarosh-059-Lab6_media/image-2725.png)
![](CC-Sarosh-059-Lab6_media/image-2726.png)
![](CC-Sarosh-059-Lab6_media/image-2727.png)
![](CC-Sarosh-059-Lab6_media/image-2728.png)
![](CC-Sarosh-059-Lab6_media/image-2729.png)
![](CC-Sarosh-059-Lab6_media/image-273.png)
![](CC-Sarosh-059-Lab6_media/image-2730.png)
![](CC-Sarosh-059-Lab6_media/image-2731.png)
![](CC-Sarosh-059-Lab6_media/image-2732.png)
![](CC-Sarosh-059-Lab6_media/image-2733.png)
![](CC-Sarosh-059-Lab6_media/image-2734.png)
![](CC-Sarosh-059-Lab6_media/image-2735.png)
![](CC-Sarosh-059-Lab6_media/image-2736.png)
![](CC-Sarosh-059-Lab6_media/image-2737.png)
![](CC-Sarosh-059-Lab6_media/image-2738.png)
![](CC-Sarosh-059-Lab6_media/image-2739.png)
![](CC-Sarosh-059-Lab6_media/image-274.png)
![](CC-Sarosh-059-Lab6_media/image-2740.png)
![](CC-Sarosh-059-Lab6_media/image-2741.png)
![](CC-Sarosh-059-Lab6_media/image-2742.png)
![](CC-Sarosh-059-Lab6_media/image-2743.png)
![](CC-Sarosh-059-Lab6_media/image-2744.png)
![](CC-Sarosh-059-Lab6_media/image-2745.png)
![](CC-Sarosh-059-Lab6_media/image-2746.png)
![](CC-Sarosh-059-Lab6_media/image-2747.png)
![](CC-Sarosh-059-Lab6_media/image-2748.png)
![](CC-Sarosh-059-Lab6_media/image-2749.png)
![](CC-Sarosh-059-Lab6_media/image-275.png)
![](CC-Sarosh-059-Lab6_media/image-2750.png)
![](CC-Sarosh-059-Lab6_media/image-2751.png)
![](CC-Sarosh-059-Lab6_media/image-2752.png)
![](CC-Sarosh-059-Lab6_media/image-2753.png)
![](CC-Sarosh-059-Lab6_media/image-2754.png)
![](CC-Sarosh-059-Lab6_media/image-2755.png)
![](CC-Sarosh-059-Lab6_media/image-2756.png)
![](CC-Sarosh-059-Lab6_media/image-2757.jpg)
![](CC-Sarosh-059-Lab6_media/image-2758.jpg)
![](CC-Sarosh-059-Lab6_media/image-2759.png)
![](CC-Sarosh-059-Lab6_media/image-276.png)
![](CC-Sarosh-059-Lab6_media/image-2760.png)
![](CC-Sarosh-059-Lab6_media/image-2761.png)
![](CC-Sarosh-059-Lab6_media/image-2762.png)
![](CC-Sarosh-059-Lab6_media/image-2763.png)
![](CC-Sarosh-059-Lab6_media/image-2764.png)
![](CC-Sarosh-059-Lab6_media/image-2765.png)
![](CC-Sarosh-059-Lab6_media/image-2766.png)
![](CC-Sarosh-059-Lab6_media/image-2767.png)
![](CC-Sarosh-059-Lab6_media/image-2768.png)
![](CC-Sarosh-059-Lab6_media/image-2769.png)
![](CC-Sarosh-059-Lab6_media/image-277.png)
![](CC-Sarosh-059-Lab6_media/image-2770.png)
![](CC-Sarosh-059-Lab6_media/image-2771.jpg)
![](CC-Sarosh-059-Lab6_media/image-2772.png)
![](CC-Sarosh-059-Lab6_media/image-2773.png)
![](CC-Sarosh-059-Lab6_media/image-2774.png)
![](CC-Sarosh-059-Lab6_media/image-2775.png)
![](CC-Sarosh-059-Lab6_media/image-2776.png)
![](CC-Sarosh-059-Lab6_media/image-2777.png)
![](CC-Sarosh-059-Lab6_media/image-2778.png)
![](CC-Sarosh-059-Lab6_media/image-2779.png)
![](CC-Sarosh-059-Lab6_media/image-278.png)
![](CC-Sarosh-059-Lab6_media/image-2780.png)
![](CC-Sarosh-059-Lab6_media/image-2781.png)
![](CC-Sarosh-059-Lab6_media/image-2782.png)
![](CC-Sarosh-059-Lab6_media/image-2783.png)
![](CC-Sarosh-059-Lab6_media/image-2784.png)
![](CC-Sarosh-059-Lab6_media/image-2785.png)
![](CC-Sarosh-059-Lab6_media/image-2786.png)
![](CC-Sarosh-059-Lab6_media/image-2787.png)
![](CC-Sarosh-059-Lab6_media/image-2788.png)
![](CC-Sarosh-059-Lab6_media/image-2789.png)
![](CC-Sarosh-059-Lab6_media/image-279.png)
![](CC-Sarosh-059-Lab6_media/image-2790.png)
![](CC-Sarosh-059-Lab6_media/image-2791.png)
![](CC-Sarosh-059-Lab6_media/image-2792.png)
![](CC-Sarosh-059-Lab6_media/image-2793.png)
![](CC-Sarosh-059-Lab6_media/image-2794.png)
![](CC-Sarosh-059-Lab6_media/image-2795.png)
![](CC-Sarosh-059-Lab6_media/image-2796.jpg)
![](CC-Sarosh-059-Lab6_media/image-2797.jpg)
![](CC-Sarosh-059-Lab6_media/image-2798.png)
![](CC-Sarosh-059-Lab6_media/image-2799.png)
![](CC-Sarosh-059-Lab6_media/image-280.png)
![](CC-Sarosh-059-Lab6_media/image-2800.png)
![](CC-Sarosh-059-Lab6_media/image-2801.png)
![](CC-Sarosh-059-Lab6_media/image-2802.png)
![](CC-Sarosh-059-Lab6_media/image-2803.png)
![](CC-Sarosh-059-Lab6_media/image-2804.png)
![](CC-Sarosh-059-Lab6_media/image-2805.png)
![](CC-Sarosh-059-Lab6_media/image-2806.png)
![](CC-Sarosh-059-Lab6_media/image-2807.png)
![](CC-Sarosh-059-Lab6_media/image-2808.png)
![](CC-Sarosh-059-Lab6_media/image-2809.png)
![](CC-Sarosh-059-Lab6_media/image-281.png)
![](CC-Sarosh-059-Lab6_media/image-2810.png)
![](CC-Sarosh-059-Lab6_media/image-2811.png)
![](CC-Sarosh-059-Lab6_media/image-2812.png)
![](CC-Sarosh-059-Lab6_media/image-2813.png)
![](CC-Sarosh-059-Lab6_media/image-2814.png)
![](CC-Sarosh-059-Lab6_media/image-2815.png)
![](CC-Sarosh-059-Lab6_media/image-2816.png)
![](CC-Sarosh-059-Lab6_media/image-2817.png)
![](CC-Sarosh-059-Lab6_media/image-2818.png)
![](CC-Sarosh-059-Lab6_media/image-2819.png)
![](CC-Sarosh-059-Lab6_media/image-282.png)
![](CC-Sarosh-059-Lab6_media/image-2820.png)
![](CC-Sarosh-059-Lab6_media/image-2821.png)
![](CC-Sarosh-059-Lab6_media/image-2822.png)
![](CC-Sarosh-059-Lab6_media/image-2823.png)
![](CC-Sarosh-059-Lab6_media/image-2824.png)
![](CC-Sarosh-059-Lab6_media/image-2825.png)
![](CC-Sarosh-059-Lab6_media/image-2826.png)
![](CC-Sarosh-059-Lab6_media/image-2827.png)
![](CC-Sarosh-059-Lab6_media/image-2828.png)
![](CC-Sarosh-059-Lab6_media/image-2829.png)
![](CC-Sarosh-059-Lab6_media/image-283.png)
![](CC-Sarosh-059-Lab6_media/image-2830.jpg)
![](CC-Sarosh-059-Lab6_media/image-2831.jpg)
![](CC-Sarosh-059-Lab6_media/image-2832.png)
![](CC-Sarosh-059-Lab6_media/image-2833.png)
![](CC-Sarosh-059-Lab6_media/image-2834.png)
![](CC-Sarosh-059-Lab6_media/image-2835.png)
![](CC-Sarosh-059-Lab6_media/image-2836.png)
![](CC-Sarosh-059-Lab6_media/image-2837.png)
![](CC-Sarosh-059-Lab6_media/image-2838.png)
![](CC-Sarosh-059-Lab6_media/image-2839.png)
![](CC-Sarosh-059-Lab6_media/image-284.png)
![](CC-Sarosh-059-Lab6_media/image-2840.png)
![](CC-Sarosh-059-Lab6_media/image-2841.png)
![](CC-Sarosh-059-Lab6_media/image-2842.png)
![](CC-Sarosh-059-Lab6_media/image-2843.png)
![](CC-Sarosh-059-Lab6_media/image-2844.jpg)
![](CC-Sarosh-059-Lab6_media/image-2845.png)
![](CC-Sarosh-059-Lab6_media/image-2846.png)
![](CC-Sarosh-059-Lab6_media/image-2847.png)
![](CC-Sarosh-059-Lab6_media/image-2848.png)
![](CC-Sarosh-059-Lab6_media/image-2849.png)
![](CC-Sarosh-059-Lab6_media/image-285.png)
![](CC-Sarosh-059-Lab6_media/image-2850.png)
![](CC-Sarosh-059-Lab6_media/image-2851.png)
![](CC-Sarosh-059-Lab6_media/image-2852.png)
![](CC-Sarosh-059-Lab6_media/image-2853.png)
![](CC-Sarosh-059-Lab6_media/image-2854.png)
![](CC-Sarosh-059-Lab6_media/image-2855.png)
![](CC-Sarosh-059-Lab6_media/image-2856.png)
![](CC-Sarosh-059-Lab6_media/image-2857.png)
![](CC-Sarosh-059-Lab6_media/image-2858.png)
![](CC-Sarosh-059-Lab6_media/image-2859.png)
![](CC-Sarosh-059-Lab6_media/image-286.png)
![](CC-Sarosh-059-Lab6_media/image-2860.png)
![](CC-Sarosh-059-Lab6_media/image-2861.png)
![](CC-Sarosh-059-Lab6_media/image-2862.png)
![](CC-Sarosh-059-Lab6_media/image-2863.png)
![](CC-Sarosh-059-Lab6_media/image-2864.png)
![](CC-Sarosh-059-Lab6_media/image-2865.png)
![](CC-Sarosh-059-Lab6_media/image-2866.png)
![](CC-Sarosh-059-Lab6_media/image-2867.png)
![](CC-Sarosh-059-Lab6_media/image-2868.png)
![](CC-Sarosh-059-Lab6_media/image-2869.jpg)
![](CC-Sarosh-059-Lab6_media/image-287.png)
![](CC-Sarosh-059-Lab6_media/image-2870.jpg)
![](CC-Sarosh-059-Lab6_media/image-2871.jpg)
![](CC-Sarosh-059-Lab6_media/image-2872.jpg)
![](CC-Sarosh-059-Lab6_media/image-2873.jpg)
![](CC-Sarosh-059-Lab6_media/image-2874.png)
![](CC-Sarosh-059-Lab6_media/image-2875.png)
![](CC-Sarosh-059-Lab6_media/image-2876.png)
![](CC-Sarosh-059-Lab6_media/image-2877.png)
![](CC-Sarosh-059-Lab6_media/image-2878.png)
![](CC-Sarosh-059-Lab6_media/image-2879.png)
![](CC-Sarosh-059-Lab6_media/image-288.png)
![](CC-Sarosh-059-Lab6_media/image-2880.png)
![](CC-Sarosh-059-Lab6_media/image-2881.png)
![](CC-Sarosh-059-Lab6_media/image-2882.png)
![](CC-Sarosh-059-Lab6_media/image-2883.png)
![](CC-Sarosh-059-Lab6_media/image-2884.png)
![](CC-Sarosh-059-Lab6_media/image-2885.png)
![](CC-Sarosh-059-Lab6_media/image-2886.png)
![](CC-Sarosh-059-Lab6_media/image-2887.png)
![](CC-Sarosh-059-Lab6_media/image-2888.png)
![](CC-Sarosh-059-Lab6_media/image-2889.png)
![](CC-Sarosh-059-Lab6_media/image-289.png)
![](CC-Sarosh-059-Lab6_media/image-2890.png)
![](CC-Sarosh-059-Lab6_media/image-2891.png)
![](CC-Sarosh-059-Lab6_media/image-2892.png)
![](CC-Sarosh-059-Lab6_media/image-2893.png)
![](CC-Sarosh-059-Lab6_media/image-2894.png)
![](CC-Sarosh-059-Lab6_media/image-2895.png)
![](CC-Sarosh-059-Lab6_media/image-2896.png)
![](CC-Sarosh-059-Lab6_media/image-2897.png)
![](CC-Sarosh-059-Lab6_media/image-2898.png)
![](CC-Sarosh-059-Lab6_media/image-2899.png)
![](CC-Sarosh-059-Lab6_media/image-290.png)
![](CC-Sarosh-059-Lab6_media/image-2900.png)
![](CC-Sarosh-059-Lab6_media/image-2901.png)
![](CC-Sarosh-059-Lab6_media/image-2902.png)
![](CC-Sarosh-059-Lab6_media/image-2903.png)
![](CC-Sarosh-059-Lab6_media/image-2904.png)
![](CC-Sarosh-059-Lab6_media/image-2905.png)
![](CC-Sarosh-059-Lab6_media/image-2906.jpg)
![](CC-Sarosh-059-Lab6_media/image-2907.jpg)
![](CC-Sarosh-059-Lab6_media/image-2908.jpg)
![](CC-Sarosh-059-Lab6_media/image-2909.jpg)
![](CC-Sarosh-059-Lab6_media/image-291.png)
![](CC-Sarosh-059-Lab6_media/image-2910.jpg)
![](CC-Sarosh-059-Lab6_media/image-2911.png)
![](CC-Sarosh-059-Lab6_media/image-2912.png)
![](CC-Sarosh-059-Lab6_media/image-2913.png)
![](CC-Sarosh-059-Lab6_media/image-2914.png)
![](CC-Sarosh-059-Lab6_media/image-2915.png)
![](CC-Sarosh-059-Lab6_media/image-2916.png)
![](CC-Sarosh-059-Lab6_media/image-2917.png)
![](CC-Sarosh-059-Lab6_media/image-2918.png)
![](CC-Sarosh-059-Lab6_media/image-2919.png)
![](CC-Sarosh-059-Lab6_media/image-292.png)
![](CC-Sarosh-059-Lab6_media/image-2920.png)
![](CC-Sarosh-059-Lab6_media/image-2921.png)
![](CC-Sarosh-059-Lab6_media/image-2922.png)
![](CC-Sarosh-059-Lab6_media/image-2923.jpg)
![](CC-Sarosh-059-Lab6_media/image-2924.jpg)
![](CC-Sarosh-059-Lab6_media/image-2925.png)
![](CC-Sarosh-059-Lab6_media/image-2926.png)
![](CC-Sarosh-059-Lab6_media/image-2927.png)
![](CC-Sarosh-059-Lab6_media/image-2928.png)
![](CC-Sarosh-059-Lab6_media/image-2929.png)
![](CC-Sarosh-059-Lab6_media/image-293.png)
![](CC-Sarosh-059-Lab6_media/image-2930.png)
![](CC-Sarosh-059-Lab6_media/image-2931.png)
![](CC-Sarosh-059-Lab6_media/image-2932.png)
![](CC-Sarosh-059-Lab6_media/image-2933.png)
![](CC-Sarosh-059-Lab6_media/image-2934.png)
![](CC-Sarosh-059-Lab6_media/image-2935.png)
![](CC-Sarosh-059-Lab6_media/image-2936.png)
![](CC-Sarosh-059-Lab6_media/image-2937.png)
![](CC-Sarosh-059-Lab6_media/image-2938.png)
![](CC-Sarosh-059-Lab6_media/image-2939.png)
![](CC-Sarosh-059-Lab6_media/image-294.png)
![](CC-Sarosh-059-Lab6_media/image-2940.png)
![](CC-Sarosh-059-Lab6_media/image-2941.png)
![](CC-Sarosh-059-Lab6_media/image-2942.png)
![](CC-Sarosh-059-Lab6_media/image-2943.png)
![](CC-Sarosh-059-Lab6_media/image-2944.png)
![](CC-Sarosh-059-Lab6_media/image-2945.png)
![](CC-Sarosh-059-Lab6_media/image-2946.png)
![](CC-Sarosh-059-Lab6_media/image-2947.png)
![](CC-Sarosh-059-Lab6_media/image-2948.png)
![](CC-Sarosh-059-Lab6_media/image-2949.jpg)
![](CC-Sarosh-059-Lab6_media/image-295.png)
![](CC-Sarosh-059-Lab6_media/image-2950.png)
![](CC-Sarosh-059-Lab6_media/image-2951.png)
![](CC-Sarosh-059-Lab6_media/image-2952.png)
![](CC-Sarosh-059-Lab6_media/image-2953.png)
![](CC-Sarosh-059-Lab6_media/image-2954.png)
![](CC-Sarosh-059-Lab6_media/image-2955.png)
![](CC-Sarosh-059-Lab6_media/image-2956.png)
![](CC-Sarosh-059-Lab6_media/image-2957.png)
![](CC-Sarosh-059-Lab6_media/image-2958.png)
![](CC-Sarosh-059-Lab6_media/image-2959.png)
![](CC-Sarosh-059-Lab6_media/image-296.png)
![](CC-Sarosh-059-Lab6_media/image-2960.png)
![](CC-Sarosh-059-Lab6_media/image-2961.png)
![](CC-Sarosh-059-Lab6_media/image-2962.png)
![](CC-Sarosh-059-Lab6_media/image-2963.png)
![](CC-Sarosh-059-Lab6_media/image-2964.png)
![](CC-Sarosh-059-Lab6_media/image-2965.png)
![](CC-Sarosh-059-Lab6_media/image-2966.png)
![](CC-Sarosh-059-Lab6_media/image-2967.png)
![](CC-Sarosh-059-Lab6_media/image-2968.png)
![](CC-Sarosh-059-Lab6_media/image-2969.png)
![](CC-Sarosh-059-Lab6_media/image-297.png)
![](CC-Sarosh-059-Lab6_media/image-2970.png)
![](CC-Sarosh-059-Lab6_media/image-2971.png)
![](CC-Sarosh-059-Lab6_media/image-2972.png)
![](CC-Sarosh-059-Lab6_media/image-2973.png)
![](CC-Sarosh-059-Lab6_media/image-2974.png)
![](CC-Sarosh-059-Lab6_media/image-2975.png)
![](CC-Sarosh-059-Lab6_media/image-2976.png)
![](CC-Sarosh-059-Lab6_media/image-2977.png)
![](CC-Sarosh-059-Lab6_media/image-2978.png)
![](CC-Sarosh-059-Lab6_media/image-2979.png)
![](CC-Sarosh-059-Lab6_media/image-298.jpg)
![](CC-Sarosh-059-Lab6_media/image-2980.png)
![](CC-Sarosh-059-Lab6_media/image-2981.png)
![](CC-Sarosh-059-Lab6_media/image-2982.jpg)
![](CC-Sarosh-059-Lab6_media/image-2983.png)
![](CC-Sarosh-059-Lab6_media/image-2984.png)
![](CC-Sarosh-059-Lab6_media/image-2985.png)
![](CC-Sarosh-059-Lab6_media/image-2986.png)
![](CC-Sarosh-059-Lab6_media/image-2987.png)
![](CC-Sarosh-059-Lab6_media/image-2988.png)
![](CC-Sarosh-059-Lab6_media/image-2989.png)
![](CC-Sarosh-059-Lab6_media/image-299.jpg)
![](CC-Sarosh-059-Lab6_media/image-2990.png)
![](CC-Sarosh-059-Lab6_media/image-2991.png)
![](CC-Sarosh-059-Lab6_media/image-2992.png)
![](CC-Sarosh-059-Lab6_media/image-2993.png)
![](CC-Sarosh-059-Lab6_media/image-2994.png)
![](CC-Sarosh-059-Lab6_media/image-2995.jpg)
![](CC-Sarosh-059-Lab6_media/image-2996.png)
![](CC-Sarosh-059-Lab6_media/image-2997.png)
![](CC-Sarosh-059-Lab6_media/image-2998.png)
![](CC-Sarosh-059-Lab6_media/image-2999.png)
![](CC-Sarosh-059-Lab6_media/image-300.jpg)
![](CC-Sarosh-059-Lab6_media/image-3000.png)
![](CC-Sarosh-059-Lab6_media/image-3001.png)
![](CC-Sarosh-059-Lab6_media/image-3002.png)
![](CC-Sarosh-059-Lab6_media/image-3003.png)
![](CC-Sarosh-059-Lab6_media/image-3004.png)
![](CC-Sarosh-059-Lab6_media/image-3005.png)
![](CC-Sarosh-059-Lab6_media/image-3006.png)
![](CC-Sarosh-059-Lab6_media/image-3007.png)
![](CC-Sarosh-059-Lab6_media/image-3008.png)
![](CC-Sarosh-059-Lab6_media/image-3009.png)
![](CC-Sarosh-059-Lab6_media/image-301.jpg)
![](CC-Sarosh-059-Lab6_media/image-3010.png)
![](CC-Sarosh-059-Lab6_media/image-3011.png)
![](CC-Sarosh-059-Lab6_media/image-3012.png)
![](CC-Sarosh-059-Lab6_media/image-3013.png)
![](CC-Sarosh-059-Lab6_media/image-3014.png)
![](CC-Sarosh-059-Lab6_media/image-3015.png)
![](CC-Sarosh-059-Lab6_media/image-3016.png)
![](CC-Sarosh-059-Lab6_media/image-3017.png)
![](CC-Sarosh-059-Lab6_media/image-3018.png)
![](CC-Sarosh-059-Lab6_media/image-3019.png)
![](CC-Sarosh-059-Lab6_media/image-302.png)
![](CC-Sarosh-059-Lab6_media/image-303.png)
![](CC-Sarosh-059-Lab6_media/image-304.png)
![](CC-Sarosh-059-Lab6_media/image-305.png)
![](CC-Sarosh-059-Lab6_media/image-306.png)
![](CC-Sarosh-059-Lab6_media/image-307.png)
![](CC-Sarosh-059-Lab6_media/image-308.png)
![](CC-Sarosh-059-Lab6_media/image-309.png)
![](CC-Sarosh-059-Lab6_media/image-310.png)
![](CC-Sarosh-059-Lab6_media/image-311.png)
![](CC-Sarosh-059-Lab6_media/image-312.png)
![](CC-Sarosh-059-Lab6_media/image-313.png)
![](CC-Sarosh-059-Lab6_media/image-314.png)
![](CC-Sarosh-059-Lab6_media/image-315.png)
![](CC-Sarosh-059-Lab6_media/image-316.png)
![](CC-Sarosh-059-Lab6_media/image-317.png)
![](CC-Sarosh-059-Lab6_media/image-318.png)
![](CC-Sarosh-059-Lab6_media/image-319.png)
![](CC-Sarosh-059-Lab6_media/image-320.png)
![](CC-Sarosh-059-Lab6_media/image-321.png)
![](CC-Sarosh-059-Lab6_media/image-322.png)
![](CC-Sarosh-059-Lab6_media/image-323.png)
![](CC-Sarosh-059-Lab6_media/image-324.png)
![](CC-Sarosh-059-Lab6_media/image-325.png)
![](CC-Sarosh-059-Lab6_media/image-326.png)
![](CC-Sarosh-059-Lab6_media/image-327.png)
![](CC-Sarosh-059-Lab6_media/image-328.png)
![](CC-Sarosh-059-Lab6_media/image-329.png)
![](CC-Sarosh-059-Lab6_media/image-330.png)
![](CC-Sarosh-059-Lab6_media/image-331.png)
![](CC-Sarosh-059-Lab6_media/image-332.png)
![](CC-Sarosh-059-Lab6_media/image-333.png)
![](CC-Sarosh-059-Lab6_media/image-334.jpg)
![](CC-Sarosh-059-Lab6_media/image-335.jpg)
![](CC-Sarosh-059-Lab6_media/image-336.jpg)
![](CC-Sarosh-059-Lab6_media/image-337.jpg)
![](CC-Sarosh-059-Lab6_media/image-338.png)
![](CC-Sarosh-059-Lab6_media/image-339.png)
![](CC-Sarosh-059-Lab6_media/image-340.png)
![](CC-Sarosh-059-Lab6_media/image-341.png)
![](CC-Sarosh-059-Lab6_media/image-342.png)
![](CC-Sarosh-059-Lab6_media/image-343.png)
![](CC-Sarosh-059-Lab6_media/image-344.png)
![](CC-Sarosh-059-Lab6_media/image-345.png)
![](CC-Sarosh-059-Lab6_media/image-346.png)
![](CC-Sarosh-059-Lab6_media/image-347.png)
![](CC-Sarosh-059-Lab6_media/image-348.png)
![](CC-Sarosh-059-Lab6_media/image-349.png)
![](CC-Sarosh-059-Lab6_media/image-350.png)
![](CC-Sarosh-059-Lab6_media/image-351.png)
![](CC-Sarosh-059-Lab6_media/image-352.png)
![](CC-Sarosh-059-Lab6_media/image-353.png)
![](CC-Sarosh-059-Lab6_media/image-354.png)
![](CC-Sarosh-059-Lab6_media/image-355.png)
![](CC-Sarosh-059-Lab6_media/image-356.png)
![](CC-Sarosh-059-Lab6_media/image-357.png)
![](CC-Sarosh-059-Lab6_media/image-358.png)
![](CC-Sarosh-059-Lab6_media/image-359.png)
![](CC-Sarosh-059-Lab6_media/image-360.png)
![](CC-Sarosh-059-Lab6_media/image-361.png)
![](CC-Sarosh-059-Lab6_media/image-362.png)
![](CC-Sarosh-059-Lab6_media/image-363.png)
![](CC-Sarosh-059-Lab6_media/image-364.png)
![](CC-Sarosh-059-Lab6_media/image-365.png)
![](CC-Sarosh-059-Lab6_media/image-366.png)
![](CC-Sarosh-059-Lab6_media/image-367.png)
![](CC-Sarosh-059-Lab6_media/image-368.png)
![](CC-Sarosh-059-Lab6_media/image-369.png)
![](CC-Sarosh-059-Lab6_media/image-370.png)
![](CC-Sarosh-059-Lab6_media/image-371.png)
![](CC-Sarosh-059-Lab6_media/image-372.png)
![](CC-Sarosh-059-Lab6_media/image-373.png)
![](CC-Sarosh-059-Lab6_media/image-374.jpg)
![](CC-Sarosh-059-Lab6_media/image-375.jpg)
![](CC-Sarosh-059-Lab6_media/image-376.jpg)
![](CC-Sarosh-059-Lab6_media/image-377.png)
![](CC-Sarosh-059-Lab6_media/image-378.png)
![](CC-Sarosh-059-Lab6_media/image-379.png)
![](CC-Sarosh-059-Lab6_media/image-380.png)
![](CC-Sarosh-059-Lab6_media/image-381.png)
![](CC-Sarosh-059-Lab6_media/image-382.png)
![](CC-Sarosh-059-Lab6_media/image-383.png)
![](CC-Sarosh-059-Lab6_media/image-384.png)
![](CC-Sarosh-059-Lab6_media/image-385.png)
![](CC-Sarosh-059-Lab6_media/image-386.png)
![](CC-Sarosh-059-Lab6_media/image-387.png)
![](CC-Sarosh-059-Lab6_media/image-388.png)
![](CC-Sarosh-059-Lab6_media/image-389.png)
![](CC-Sarosh-059-Lab6_media/image-390.png)
![](CC-Sarosh-059-Lab6_media/image-391.png)
![](CC-Sarosh-059-Lab6_media/image-392.png)
![](CC-Sarosh-059-Lab6_media/image-393.png)
![](CC-Sarosh-059-Lab6_media/image-394.png)
![](CC-Sarosh-059-Lab6_media/image-395.png)
![](CC-Sarosh-059-Lab6_media/image-396.png)
![](CC-Sarosh-059-Lab6_media/image-397.png)
![](CC-Sarosh-059-Lab6_media/image-398.png)
![](CC-Sarosh-059-Lab6_media/image-399.png)
![](CC-Sarosh-059-Lab6_media/image-400.png)
![](CC-Sarosh-059-Lab6_media/image-401.png)
![](CC-Sarosh-059-Lab6_media/image-402.png)
![](CC-Sarosh-059-Lab6_media/image-403.png)
![](CC-Sarosh-059-Lab6_media/image-404.png)
![](CC-Sarosh-059-Lab6_media/image-405.png)
![](CC-Sarosh-059-Lab6_media/image-406.png)
![](CC-Sarosh-059-Lab6_media/image-407.png)
![](CC-Sarosh-059-Lab6_media/image-408.png)
![](CC-Sarosh-059-Lab6_media/image-409.jpg)
![](CC-Sarosh-059-Lab6_media/image-410.jpg)
![](CC-Sarosh-059-Lab6_media/image-411.png)
![](CC-Sarosh-059-Lab6_media/image-412.png)
![](CC-Sarosh-059-Lab6_media/image-413.png)
![](CC-Sarosh-059-Lab6_media/image-414.png)
![](CC-Sarosh-059-Lab6_media/image-415.png)
![](CC-Sarosh-059-Lab6_media/image-416.png)
![](CC-Sarosh-059-Lab6_media/image-417.png)
![](CC-Sarosh-059-Lab6_media/image-418.png)
![](CC-Sarosh-059-Lab6_media/image-419.png)
![](CC-Sarosh-059-Lab6_media/image-420.png)
![](CC-Sarosh-059-Lab6_media/image-421.png)
![](CC-Sarosh-059-Lab6_media/image-422.png)
![](CC-Sarosh-059-Lab6_media/image-423.png)
![](CC-Sarosh-059-Lab6_media/image-424.png)
![](CC-Sarosh-059-Lab6_media/image-425.png)
![](CC-Sarosh-059-Lab6_media/image-426.png)
![](CC-Sarosh-059-Lab6_media/image-427.png)
![](CC-Sarosh-059-Lab6_media/image-428.png)
![](CC-Sarosh-059-Lab6_media/image-429.png)
![](CC-Sarosh-059-Lab6_media/image-430.png)
![](CC-Sarosh-059-Lab6_media/image-431.png)
![](CC-Sarosh-059-Lab6_media/image-432.png)
![](CC-Sarosh-059-Lab6_media/image-433.png)
![](CC-Sarosh-059-Lab6_media/image-434.png)
![](CC-Sarosh-059-Lab6_media/image-435.png)
![](CC-Sarosh-059-Lab6_media/image-436.png)
![](CC-Sarosh-059-Lab6_media/image-437.png)
![](CC-Sarosh-059-Lab6_media/image-438.png)
![](CC-Sarosh-059-Lab6_media/image-439.png)
![](CC-Sarosh-059-Lab6_media/image-440.png)
![](CC-Sarosh-059-Lab6_media/image-441.png)
![](CC-Sarosh-059-Lab6_media/image-442.png)
![](CC-Sarosh-059-Lab6_media/image-443.png)
![](CC-Sarosh-059-Lab6_media/image-444.png)
![](CC-Sarosh-059-Lab6_media/image-445.png)
![](CC-Sarosh-059-Lab6_media/image-446.png)
![](CC-Sarosh-059-Lab6_media/image-447.jpg)
![](CC-Sarosh-059-Lab6_media/image-448.jpg)
![](CC-Sarosh-059-Lab6_media/image-449.png)
![](CC-Sarosh-059-Lab6_media/image-450.png)
![](CC-Sarosh-059-Lab6_media/image-451.png)
![](CC-Sarosh-059-Lab6_media/image-452.png)
![](CC-Sarosh-059-Lab6_media/image-453.png)
![](CC-Sarosh-059-Lab6_media/image-454.png)
![](CC-Sarosh-059-Lab6_media/image-455.png)
![](CC-Sarosh-059-Lab6_media/image-456.png)
![](CC-Sarosh-059-Lab6_media/image-457.png)
![](CC-Sarosh-059-Lab6_media/image-458.png)
![](CC-Sarosh-059-Lab6_media/image-459.png)
![](CC-Sarosh-059-Lab6_media/image-460.png)
![](CC-Sarosh-059-Lab6_media/image-461.png)
![](CC-Sarosh-059-Lab6_media/image-462.png)
![](CC-Sarosh-059-Lab6_media/image-463.png)
![](CC-Sarosh-059-Lab6_media/image-464.png)
![](CC-Sarosh-059-Lab6_media/image-465.png)
![](CC-Sarosh-059-Lab6_media/image-466.png)
![](CC-Sarosh-059-Lab6_media/image-467.png)
![](CC-Sarosh-059-Lab6_media/image-468.png)
![](CC-Sarosh-059-Lab6_media/image-469.png)
![](CC-Sarosh-059-Lab6_media/image-470.png)
![](CC-Sarosh-059-Lab6_media/image-471.png)
![](CC-Sarosh-059-Lab6_media/image-472.png)
![](CC-Sarosh-059-Lab6_media/image-473.png)
![](CC-Sarosh-059-Lab6_media/image-474.png)
![](CC-Sarosh-059-Lab6_media/image-475.png)
![](CC-Sarosh-059-Lab6_media/image-476.png)
![](CC-Sarosh-059-Lab6_media/image-477.png)
![](CC-Sarosh-059-Lab6_media/image-478.png)
![](CC-Sarosh-059-Lab6_media/image-479.png)
![](CC-Sarosh-059-Lab6_media/image-480.png)
![](CC-Sarosh-059-Lab6_media/image-481.jpg)
![](CC-Sarosh-059-Lab6_media/image-482.png)
![](CC-Sarosh-059-Lab6_media/image-483.png)
![](CC-Sarosh-059-Lab6_media/image-484.png)
![](CC-Sarosh-059-Lab6_media/image-485.png)
![](CC-Sarosh-059-Lab6_media/image-486.png)
![](CC-Sarosh-059-Lab6_media/image-487.png)
![](CC-Sarosh-059-Lab6_media/image-488.png)
![](CC-Sarosh-059-Lab6_media/image-489.png)
![](CC-Sarosh-059-Lab6_media/image-490.png)
![](CC-Sarosh-059-Lab6_media/image-491.png)
![](CC-Sarosh-059-Lab6_media/image-492.png)
![](CC-Sarosh-059-Lab6_media/image-493.png)
![](CC-Sarosh-059-Lab6_media/image-494.png)
![](CC-Sarosh-059-Lab6_media/image-495.png)
![](CC-Sarosh-059-Lab6_media/image-496.png)
![](CC-Sarosh-059-Lab6_media/image-497.png)
![](CC-Sarosh-059-Lab6_media/image-498.png)
![](CC-Sarosh-059-Lab6_media/image-499.png)
![](CC-Sarosh-059-Lab6_media/image-500.png)
![](CC-Sarosh-059-Lab6_media/image-501.png)
![](CC-Sarosh-059-Lab6_media/image-502.png)
![](CC-Sarosh-059-Lab6_media/image-503.png)
![](CC-Sarosh-059-Lab6_media/image-504.png)
![](CC-Sarosh-059-Lab6_media/image-505.png)
![](CC-Sarosh-059-Lab6_media/image-506.png)
![](CC-Sarosh-059-Lab6_media/image-507.png)
![](CC-Sarosh-059-Lab6_media/image-508.png)
![](CC-Sarosh-059-Lab6_media/image-509.png)
![](CC-Sarosh-059-Lab6_media/image-510.png)
![](CC-Sarosh-059-Lab6_media/image-511.png)
![](CC-Sarosh-059-Lab6_media/image-512.png)
![](CC-Sarosh-059-Lab6_media/image-513.png)
![](CC-Sarosh-059-Lab6_media/image-514.png)
![](CC-Sarosh-059-Lab6_media/image-515.png)
![](CC-Sarosh-059-Lab6_media/image-516.png)
![](CC-Sarosh-059-Lab6_media/image-517.png)
![](CC-Sarosh-059-Lab6_media/image-518.jpg)
![](CC-Sarosh-059-Lab6_media/image-519.jpg)
![](CC-Sarosh-059-Lab6_media/image-520.jpg)
![](CC-Sarosh-059-Lab6_media/image-521.jpg)
![](CC-Sarosh-059-Lab6_media/image-522.png)
![](CC-Sarosh-059-Lab6_media/image-523.png)
![](CC-Sarosh-059-Lab6_media/image-524.png)
![](CC-Sarosh-059-Lab6_media/image-525.png)
![](CC-Sarosh-059-Lab6_media/image-526.png)
![](CC-Sarosh-059-Lab6_media/image-527.png)
![](CC-Sarosh-059-Lab6_media/image-528.png)
![](CC-Sarosh-059-Lab6_media/image-529.png)
![](CC-Sarosh-059-Lab6_media/image-530.png)
![](CC-Sarosh-059-Lab6_media/image-531.png)
![](CC-Sarosh-059-Lab6_media/image-532.png)
![](CC-Sarosh-059-Lab6_media/image-533.png)
![](CC-Sarosh-059-Lab6_media/image-534.png)
![](CC-Sarosh-059-Lab6_media/image-535.png)
![](CC-Sarosh-059-Lab6_media/image-536.png)
![](CC-Sarosh-059-Lab6_media/image-537.png)
![](CC-Sarosh-059-Lab6_media/image-538.png)
![](CC-Sarosh-059-Lab6_media/image-539.png)
![](CC-Sarosh-059-Lab6_media/image-540.png)
![](CC-Sarosh-059-Lab6_media/image-541.png)
![](CC-Sarosh-059-Lab6_media/image-542.png)
![](CC-Sarosh-059-Lab6_media/image-543.png)
![](CC-Sarosh-059-Lab6_media/image-544.png)
![](CC-Sarosh-059-Lab6_media/image-545.png)
![](CC-Sarosh-059-Lab6_media/image-546.png)
![](CC-Sarosh-059-Lab6_media/image-547.png)
![](CC-Sarosh-059-Lab6_media/image-548.png)
![](CC-Sarosh-059-Lab6_media/image-549.png)
![](CC-Sarosh-059-Lab6_media/image-550.png)
![](CC-Sarosh-059-Lab6_media/image-551.png)
![](CC-Sarosh-059-Lab6_media/image-552.png)
![](CC-Sarosh-059-Lab6_media/image-553.png)
![](CC-Sarosh-059-Lab6_media/image-554.jpg)
![](CC-Sarosh-059-Lab6_media/image-555.jpg)
![](CC-Sarosh-059-Lab6_media/image-556.jpg)
![](CC-Sarosh-059-Lab6_media/image-557.jpg)
![](CC-Sarosh-059-Lab6_media/image-558.png)
![](CC-Sarosh-059-Lab6_media/image-559.png)
![](CC-Sarosh-059-Lab6_media/image-560.png)
![](CC-Sarosh-059-Lab6_media/image-561.png)
![](CC-Sarosh-059-Lab6_media/image-562.png)
![](CC-Sarosh-059-Lab6_media/image-563.png)
![](CC-Sarosh-059-Lab6_media/image-564.png)
![](CC-Sarosh-059-Lab6_media/image-565.png)
![](CC-Sarosh-059-Lab6_media/image-566.png)
![](CC-Sarosh-059-Lab6_media/image-567.png)
![](CC-Sarosh-059-Lab6_media/image-568.png)
![](CC-Sarosh-059-Lab6_media/image-569.png)
![](CC-Sarosh-059-Lab6_media/image-570.jpg)
![](CC-Sarosh-059-Lab6_media/image-571.png)
![](CC-Sarosh-059-Lab6_media/image-572.png)
![](CC-Sarosh-059-Lab6_media/image-573.png)
![](CC-Sarosh-059-Lab6_media/image-574.png)
![](CC-Sarosh-059-Lab6_media/image-575.png)
![](CC-Sarosh-059-Lab6_media/image-576.png)
![](CC-Sarosh-059-Lab6_media/image-577.png)
![](CC-Sarosh-059-Lab6_media/image-578.png)
![](CC-Sarosh-059-Lab6_media/image-579.png)
![](CC-Sarosh-059-Lab6_media/image-580.png)
![](CC-Sarosh-059-Lab6_media/image-581.png)
![](CC-Sarosh-059-Lab6_media/image-582.png)
![](CC-Sarosh-059-Lab6_media/image-583.png)
![](CC-Sarosh-059-Lab6_media/image-584.png)
![](CC-Sarosh-059-Lab6_media/image-585.png)
![](CC-Sarosh-059-Lab6_media/image-586.png)
![](CC-Sarosh-059-Lab6_media/image-587.png)
![](CC-Sarosh-059-Lab6_media/image-588.png)
![](CC-Sarosh-059-Lab6_media/image-589.png)
![](CC-Sarosh-059-Lab6_media/image-590.png)
![](CC-Sarosh-059-Lab6_media/image-591.png)
![](CC-Sarosh-059-Lab6_media/image-592.png)
![](CC-Sarosh-059-Lab6_media/image-593.png)
![](CC-Sarosh-059-Lab6_media/image-594.png)
![](CC-Sarosh-059-Lab6_media/image-595.jpg)
![](CC-Sarosh-059-Lab6_media/image-596.jpg)
![](CC-Sarosh-059-Lab6_media/image-597.jpg)
![](CC-Sarosh-059-Lab6_media/image-598.png)
![](CC-Sarosh-059-Lab6_media/image-599.png)
![](CC-Sarosh-059-Lab6_media/image-600.png)
![](CC-Sarosh-059-Lab6_media/image-601.png)
![](CC-Sarosh-059-Lab6_media/image-602.png)
![](CC-Sarosh-059-Lab6_media/image-603.png)
![](CC-Sarosh-059-Lab6_media/image-604.png)
![](CC-Sarosh-059-Lab6_media/image-605.png)
![](CC-Sarosh-059-Lab6_media/image-606.png)
![](CC-Sarosh-059-Lab6_media/image-607.png)
![](CC-Sarosh-059-Lab6_media/image-608.png)
![](CC-Sarosh-059-Lab6_media/image-609.png)
![](CC-Sarosh-059-Lab6_media/image-610.png)
![](CC-Sarosh-059-Lab6_media/image-611.png)
![](CC-Sarosh-059-Lab6_media/image-612.png)
![](CC-Sarosh-059-Lab6_media/image-613.png)
![](CC-Sarosh-059-Lab6_media/image-614.png)
![](CC-Sarosh-059-Lab6_media/image-615.png)
![](CC-Sarosh-059-Lab6_media/image-616.png)
![](CC-Sarosh-059-Lab6_media/image-617.png)
![](CC-Sarosh-059-Lab6_media/image-618.png)
![](CC-Sarosh-059-Lab6_media/image-619.png)
![](CC-Sarosh-059-Lab6_media/image-620.png)
![](CC-Sarosh-059-Lab6_media/image-621.png)
![](CC-Sarosh-059-Lab6_media/image-622.png)
![](CC-Sarosh-059-Lab6_media/image-623.png)
![](CC-Sarosh-059-Lab6_media/image-624.png)
![](CC-Sarosh-059-Lab6_media/image-625.png)
![](CC-Sarosh-059-Lab6_media/image-626.png)
![](CC-Sarosh-059-Lab6_media/image-627.png)
![](CC-Sarosh-059-Lab6_media/image-628.png)
![](CC-Sarosh-059-Lab6_media/image-629.png)
![](CC-Sarosh-059-Lab6_media/image-630.jpg)
![](CC-Sarosh-059-Lab6_media/image-631.jpg)
![](CC-Sarosh-059-Lab6_media/image-632.jpg)
![](CC-Sarosh-059-Lab6_media/image-633.png)
![](CC-Sarosh-059-Lab6_media/image-634.png)
![](CC-Sarosh-059-Lab6_media/image-635.png)
![](CC-Sarosh-059-Lab6_media/image-636.png)
![](CC-Sarosh-059-Lab6_media/image-637.png)
![](CC-Sarosh-059-Lab6_media/image-638.png)
![](CC-Sarosh-059-Lab6_media/image-639.png)
![](CC-Sarosh-059-Lab6_media/image-640.png)
![](CC-Sarosh-059-Lab6_media/image-641.png)
![](CC-Sarosh-059-Lab6_media/image-642.png)
![](CC-Sarosh-059-Lab6_media/image-643.png)
![](CC-Sarosh-059-Lab6_media/image-644.png)
![](CC-Sarosh-059-Lab6_media/image-645.png)
![](CC-Sarosh-059-Lab6_media/image-646.png)
![](CC-Sarosh-059-Lab6_media/image-647.png)
![](CC-Sarosh-059-Lab6_media/image-648.png)
![](CC-Sarosh-059-Lab6_media/image-649.png)
![](CC-Sarosh-059-Lab6_media/image-650.png)
![](CC-Sarosh-059-Lab6_media/image-651.png)
![](CC-Sarosh-059-Lab6_media/image-652.png)
![](CC-Sarosh-059-Lab6_media/image-653.png)
![](CC-Sarosh-059-Lab6_media/image-654.png)
![](CC-Sarosh-059-Lab6_media/image-655.png)
![](CC-Sarosh-059-Lab6_media/image-656.png)
![](CC-Sarosh-059-Lab6_media/image-657.png)
![](CC-Sarosh-059-Lab6_media/image-658.png)
![](CC-Sarosh-059-Lab6_media/image-659.png)
![](CC-Sarosh-059-Lab6_media/image-660.png)
![](CC-Sarosh-059-Lab6_media/image-661.png)
![](CC-Sarosh-059-Lab6_media/image-662.png)
![](CC-Sarosh-059-Lab6_media/image-663.png)
![](CC-Sarosh-059-Lab6_media/image-664.png)
![](CC-Sarosh-059-Lab6_media/image-665.png)
![](CC-Sarosh-059-Lab6_media/image-666.png)
![](CC-Sarosh-059-Lab6_media/image-667.png)
![](CC-Sarosh-059-Lab6_media/image-668.png)
![](CC-Sarosh-059-Lab6_media/image-669.jpg)
![](CC-Sarosh-059-Lab6_media/image-670.jpg)
![](CC-Sarosh-059-Lab6_media/image-671.jpg)
![](CC-Sarosh-059-Lab6_media/image-672.jpg)
![](CC-Sarosh-059-Lab6_media/image-673.jpg)
![](CC-Sarosh-059-Lab6_media/image-674.png)
![](CC-Sarosh-059-Lab6_media/image-675.png)
![](CC-Sarosh-059-Lab6_media/image-676.png)
![](CC-Sarosh-059-Lab6_media/image-677.png)
![](CC-Sarosh-059-Lab6_media/image-678.png)
![](CC-Sarosh-059-Lab6_media/image-679.png)
![](CC-Sarosh-059-Lab6_media/image-680.png)
![](CC-Sarosh-059-Lab6_media/image-681.png)
![](CC-Sarosh-059-Lab6_media/image-682.png)
![](CC-Sarosh-059-Lab6_media/image-683.png)
![](CC-Sarosh-059-Lab6_media/image-684.png)
![](CC-Sarosh-059-Lab6_media/image-685.png)
![](CC-Sarosh-059-Lab6_media/image-686.png)
![](CC-Sarosh-059-Lab6_media/image-687.png)
![](CC-Sarosh-059-Lab6_media/image-688.png)
![](CC-Sarosh-059-Lab6_media/image-689.png)
![](CC-Sarosh-059-Lab6_media/image-690.png)
![](CC-Sarosh-059-Lab6_media/image-691.png)
![](CC-Sarosh-059-Lab6_media/image-692.png)
![](CC-Sarosh-059-Lab6_media/image-693.png)
![](CC-Sarosh-059-Lab6_media/image-694.png)
![](CC-Sarosh-059-Lab6_media/image-695.png)
![](CC-Sarosh-059-Lab6_media/image-696.png)
![](CC-Sarosh-059-Lab6_media/image-697.png)
![](CC-Sarosh-059-Lab6_media/image-698.png)
![](CC-Sarosh-059-Lab6_media/image-699.png)
![](CC-Sarosh-059-Lab6_media/image-700.png)
![](CC-Sarosh-059-Lab6_media/image-701.png)
![](CC-Sarosh-059-Lab6_media/image-702.png)
![](CC-Sarosh-059-Lab6_media/image-703.png)
![](CC-Sarosh-059-Lab6_media/image-704.png)
![](CC-Sarosh-059-Lab6_media/image-705.png)
![](CC-Sarosh-059-Lab6_media/image-706.jpg)
![](CC-Sarosh-059-Lab6_media/image-707.jpg)
![](CC-Sarosh-059-Lab6_media/image-708.jpg)
![](CC-Sarosh-059-Lab6_media/image-709.jpg)
![](CC-Sarosh-059-Lab6_media/image-710.jpg)
![](CC-Sarosh-059-Lab6_media/image-711.png)
![](CC-Sarosh-059-Lab6_media/image-712.png)
![](CC-Sarosh-059-Lab6_media/image-713.png)
![](CC-Sarosh-059-Lab6_media/image-714.png)
![](CC-Sarosh-059-Lab6_media/image-715.png)
![](CC-Sarosh-059-Lab6_media/image-716.png)
![](CC-Sarosh-059-Lab6_media/image-717.png)
![](CC-Sarosh-059-Lab6_media/image-718.png)
![](CC-Sarosh-059-Lab6_media/image-719.png)
![](CC-Sarosh-059-Lab6_media/image-720.png)
![](CC-Sarosh-059-Lab6_media/image-721.png)
![](CC-Sarosh-059-Lab6_media/image-722.png)
![](CC-Sarosh-059-Lab6_media/image-723.png)
![](CC-Sarosh-059-Lab6_media/image-724.png)
![](CC-Sarosh-059-Lab6_media/image-725.png)
![](CC-Sarosh-059-Lab6_media/image-726.png)
![](CC-Sarosh-059-Lab6_media/image-727.png)
![](CC-Sarosh-059-Lab6_media/image-728.png)
![](CC-Sarosh-059-Lab6_media/image-729.png)
![](CC-Sarosh-059-Lab6_media/image-730.png)
![](CC-Sarosh-059-Lab6_media/image-731.png)
![](CC-Sarosh-059-Lab6_media/image-732.png)
![](CC-Sarosh-059-Lab6_media/image-733.png)
![](CC-Sarosh-059-Lab6_media/image-734.png)
![](CC-Sarosh-059-Lab6_media/image-735.png)
![](CC-Sarosh-059-Lab6_media/image-736.png)
![](CC-Sarosh-059-Lab6_media/image-737.png)
![](CC-Sarosh-059-Lab6_media/image-738.png)
![](CC-Sarosh-059-Lab6_media/image-739.png)
![](CC-Sarosh-059-Lab6_media/image-740.png)
![](CC-Sarosh-059-Lab6_media/image-741.png)
![](CC-Sarosh-059-Lab6_media/image-742.png)
![](CC-Sarosh-059-Lab6_media/image-743.png)
![](CC-Sarosh-059-Lab6_media/image-744.png)
![](CC-Sarosh-059-Lab6_media/image-745.png)
![](CC-Sarosh-059-Lab6_media/image-746.png)
![](CC-Sarosh-059-Lab6_media/image-747.jpg)
![](CC-Sarosh-059-Lab6_media/image-748.jpg)
![](CC-Sarosh-059-Lab6_media/image-749.jpg)
![](CC-Sarosh-059-Lab6_media/image-750.jpg)
![](CC-Sarosh-059-Lab6_media/image-751.png)
![](CC-Sarosh-059-Lab6_media/image-752.png)
![](CC-Sarosh-059-Lab6_media/image-753.png)
![](CC-Sarosh-059-Lab6_media/image-754.png)
![](CC-Sarosh-059-Lab6_media/image-755.png)
![](CC-Sarosh-059-Lab6_media/image-756.png)
![](CC-Sarosh-059-Lab6_media/image-757.png)
![](CC-Sarosh-059-Lab6_media/image-758.png)
![](CC-Sarosh-059-Lab6_media/image-759.png)
![](CC-Sarosh-059-Lab6_media/image-760.png)
![](CC-Sarosh-059-Lab6_media/image-761.png)
![](CC-Sarosh-059-Lab6_media/image-762.png)
![](CC-Sarosh-059-Lab6_media/image-763.png)
![](CC-Sarosh-059-Lab6_media/image-764.png)
![](CC-Sarosh-059-Lab6_media/image-765.png)
![](CC-Sarosh-059-Lab6_media/image-766.png)
![](CC-Sarosh-059-Lab6_media/image-767.png)
![](CC-Sarosh-059-Lab6_media/image-768.png)
![](CC-Sarosh-059-Lab6_media/image-769.png)
![](CC-Sarosh-059-Lab6_media/image-770.png)
![](CC-Sarosh-059-Lab6_media/image-771.png)
![](CC-Sarosh-059-Lab6_media/image-772.png)
![](CC-Sarosh-059-Lab6_media/image-773.png)
![](CC-Sarosh-059-Lab6_media/image-774.png)
![](CC-Sarosh-059-Lab6_media/image-775.png)
![](CC-Sarosh-059-Lab6_media/image-776.png)
![](CC-Sarosh-059-Lab6_media/image-777.png)
![](CC-Sarosh-059-Lab6_media/image-778.png)
![](CC-Sarosh-059-Lab6_media/image-779.png)
![](CC-Sarosh-059-Lab6_media/image-780.png)
![](CC-Sarosh-059-Lab6_media/image-781.png)
![](CC-Sarosh-059-Lab6_media/image-782.png)
![](CC-Sarosh-059-Lab6_media/image-783.jpg)
![](CC-Sarosh-059-Lab6_media/image-784.jpg)
![](CC-Sarosh-059-Lab6_media/image-785.jpg)
![](CC-Sarosh-059-Lab6_media/image-786.jpg)
![](CC-Sarosh-059-Lab6_media/image-787.png)
![](CC-Sarosh-059-Lab6_media/image-788.png)
![](CC-Sarosh-059-Lab6_media/image-789.png)
![](CC-Sarosh-059-Lab6_media/image-790.png)
![](CC-Sarosh-059-Lab6_media/image-791.png)
![](CC-Sarosh-059-Lab6_media/image-792.png)
![](CC-Sarosh-059-Lab6_media/image-793.png)
![](CC-Sarosh-059-Lab6_media/image-794.png)
![](CC-Sarosh-059-Lab6_media/image-795.png)
![](CC-Sarosh-059-Lab6_media/image-796.png)
![](CC-Sarosh-059-Lab6_media/image-797.png)
![](CC-Sarosh-059-Lab6_media/image-798.png)
![](CC-Sarosh-059-Lab6_media/image-799.png)
![](CC-Sarosh-059-Lab6_media/image-800.png)
![](CC-Sarosh-059-Lab6_media/image-801.png)
![](CC-Sarosh-059-Lab6_media/image-802.png)
![](CC-Sarosh-059-Lab6_media/image-803.png)
![](CC-Sarosh-059-Lab6_media/image-804.png)
![](CC-Sarosh-059-Lab6_media/image-805.png)
![](CC-Sarosh-059-Lab6_media/image-806.png)
![](CC-Sarosh-059-Lab6_media/image-807.png)
![](CC-Sarosh-059-Lab6_media/image-808.png)
![](CC-Sarosh-059-Lab6_media/image-809.png)
![](CC-Sarosh-059-Lab6_media/image-810.png)
![](CC-Sarosh-059-Lab6_media/image-811.png)
![](CC-Sarosh-059-Lab6_media/image-812.png)
![](CC-Sarosh-059-Lab6_media/image-813.png)
![](CC-Sarosh-059-Lab6_media/image-814.png)
![](CC-Sarosh-059-Lab6_media/image-815.png)
![](CC-Sarosh-059-Lab6_media/image-816.png)
![](CC-Sarosh-059-Lab6_media/image-817.png)
![](CC-Sarosh-059-Lab6_media/image-818.png)
![](CC-Sarosh-059-Lab6_media/image-819.png)
![](CC-Sarosh-059-Lab6_media/image-820.png)
![](CC-Sarosh-059-Lab6_media/image-821.png)
![](CC-Sarosh-059-Lab6_media/image-822.png)
![](CC-Sarosh-059-Lab6_media/image-823.jpg)
![](CC-Sarosh-059-Lab6_media/image-824.jpg)
![](CC-Sarosh-059-Lab6_media/image-825.jpg)
![](CC-Sarosh-059-Lab6_media/image-826.jpg)
![](CC-Sarosh-059-Lab6_media/image-827.jpg)
![](CC-Sarosh-059-Lab6_media/image-828.png)
![](CC-Sarosh-059-Lab6_media/image-829.png)
![](CC-Sarosh-059-Lab6_media/image-830.png)
![](CC-Sarosh-059-Lab6_media/image-831.png)
![](CC-Sarosh-059-Lab6_media/image-832.png)
![](CC-Sarosh-059-Lab6_media/image-833.png)
![](CC-Sarosh-059-Lab6_media/image-834.png)
![](CC-Sarosh-059-Lab6_media/image-835.png)
![](CC-Sarosh-059-Lab6_media/image-836.png)
![](CC-Sarosh-059-Lab6_media/image-837.png)
![](CC-Sarosh-059-Lab6_media/image-838.png)
![](CC-Sarosh-059-Lab6_media/image-839.png)
![](CC-Sarosh-059-Lab6_media/image-840.png)
![](CC-Sarosh-059-Lab6_media/image-841.png)
![](CC-Sarosh-059-Lab6_media/image-842.png)
![](CC-Sarosh-059-Lab6_media/image-843.png)
![](CC-Sarosh-059-Lab6_media/image-844.png)
![](CC-Sarosh-059-Lab6_media/image-845.png)
![](CC-Sarosh-059-Lab6_media/image-846.png)
![](CC-Sarosh-059-Lab6_media/image-847.png)
![](CC-Sarosh-059-Lab6_media/image-848.png)
![](CC-Sarosh-059-Lab6_media/image-849.png)
![](CC-Sarosh-059-Lab6_media/image-850.png)
![](CC-Sarosh-059-Lab6_media/image-851.png)
![](CC-Sarosh-059-Lab6_media/image-852.png)
![](CC-Sarosh-059-Lab6_media/image-853.png)
![](CC-Sarosh-059-Lab6_media/image-854.png)
![](CC-Sarosh-059-Lab6_media/image-855.png)
![](CC-Sarosh-059-Lab6_media/image-856.png)
![](CC-Sarosh-059-Lab6_media/image-857.png)
![](CC-Sarosh-059-Lab6_media/image-858.png)
![](CC-Sarosh-059-Lab6_media/image-859.png)
![](CC-Sarosh-059-Lab6_media/image-860.jpg)
![](CC-Sarosh-059-Lab6_media/image-861.jpg)
![](CC-Sarosh-059-Lab6_media/image-862.jpg)
![](CC-Sarosh-059-Lab6_media/image-863.jpg)
![](CC-Sarosh-059-Lab6_media/image-864.jpg)
![](CC-Sarosh-059-Lab6_media/image-865.png)
![](CC-Sarosh-059-Lab6_media/image-866.png)
![](CC-Sarosh-059-Lab6_media/image-867.png)
![](CC-Sarosh-059-Lab6_media/image-868.png)
![](CC-Sarosh-059-Lab6_media/image-869.png)
![](CC-Sarosh-059-Lab6_media/image-870.png)
![](CC-Sarosh-059-Lab6_media/image-871.png)
![](CC-Sarosh-059-Lab6_media/image-872.png)
![](CC-Sarosh-059-Lab6_media/image-873.png)
![](CC-Sarosh-059-Lab6_media/image-874.png)
![](CC-Sarosh-059-Lab6_media/image-875.png)
![](CC-Sarosh-059-Lab6_media/image-876.png)
![](CC-Sarosh-059-Lab6_media/image-877.png)
![](CC-Sarosh-059-Lab6_media/image-878.png)
![](CC-Sarosh-059-Lab6_media/image-879.png)
![](CC-Sarosh-059-Lab6_media/image-880.png)
![](CC-Sarosh-059-Lab6_media/image-881.png)
![](CC-Sarosh-059-Lab6_media/image-882.png)
![](CC-Sarosh-059-Lab6_media/image-883.png)
![](CC-Sarosh-059-Lab6_media/image-884.png)
![](CC-Sarosh-059-Lab6_media/image-885.png)
![](CC-Sarosh-059-Lab6_media/image-886.png)
![](CC-Sarosh-059-Lab6_media/image-887.png)
![](CC-Sarosh-059-Lab6_media/image-888.png)
![](CC-Sarosh-059-Lab6_media/image-889.png)
![](CC-Sarosh-059-Lab6_media/image-890.png)
![](CC-Sarosh-059-Lab6_media/image-891.png)
![](CC-Sarosh-059-Lab6_media/image-892.png)
![](CC-Sarosh-059-Lab6_media/image-893.png)
![](CC-Sarosh-059-Lab6_media/image-894.png)
![](CC-Sarosh-059-Lab6_media/image-895.png)
![](CC-Sarosh-059-Lab6_media/image-896.png)
![](CC-Sarosh-059-Lab6_media/image-897.png)
![](CC-Sarosh-059-Lab6_media/image-898.png)
![](CC-Sarosh-059-Lab6_media/image-899.png)
![](CC-Sarosh-059-Lab6_media/image-900.png)
![](CC-Sarosh-059-Lab6_media/image-901.jpg)
![](CC-Sarosh-059-Lab6_media/image-902.jpg)
![](CC-Sarosh-059-Lab6_media/image-903.jpg)
![](CC-Sarosh-059-Lab6_media/image-904.jpg)
![](CC-Sarosh-059-Lab6_media/image-905.png)
![](CC-Sarosh-059-Lab6_media/image-906.png)
![](CC-Sarosh-059-Lab6_media/image-907.png)
![](CC-Sarosh-059-Lab6_media/image-908.png)
![](CC-Sarosh-059-Lab6_media/image-909.png)
![](CC-Sarosh-059-Lab6_media/image-910.png)
![](CC-Sarosh-059-Lab6_media/image-911.png)
![](CC-Sarosh-059-Lab6_media/image-912.png)
![](CC-Sarosh-059-Lab6_media/image-913.png)
![](CC-Sarosh-059-Lab6_media/image-914.png)
![](CC-Sarosh-059-Lab6_media/image-915.png)
![](CC-Sarosh-059-Lab6_media/image-916.png)
![](CC-Sarosh-059-Lab6_media/image-917.png)
![](CC-Sarosh-059-Lab6_media/image-918.png)
![](CC-Sarosh-059-Lab6_media/image-919.png)
![](CC-Sarosh-059-Lab6_media/image-920.png)
![](CC-Sarosh-059-Lab6_media/image-921.png)
![](CC-Sarosh-059-Lab6_media/image-922.png)
![](CC-Sarosh-059-Lab6_media/image-923.png)
![](CC-Sarosh-059-Lab6_media/image-924.png)
![](CC-Sarosh-059-Lab6_media/image-925.png)
![](CC-Sarosh-059-Lab6_media/image-926.png)
![](CC-Sarosh-059-Lab6_media/image-927.png)
![](CC-Sarosh-059-Lab6_media/image-928.png)
![](CC-Sarosh-059-Lab6_media/image-929.png)
![](CC-Sarosh-059-Lab6_media/image-930.png)
![](CC-Sarosh-059-Lab6_media/image-931.png)
![](CC-Sarosh-059-Lab6_media/image-932.png)
![](CC-Sarosh-059-Lab6_media/image-933.png)
![](CC-Sarosh-059-Lab6_media/image-934.png)
![](CC-Sarosh-059-Lab6_media/image-935.png)
![](CC-Sarosh-059-Lab6_media/image-936.png)
![](CC-Sarosh-059-Lab6_media/image-937.jpg)
![](CC-Sarosh-059-Lab6_media/image-938.jpg)
![](CC-Sarosh-059-Lab6_media/image-939.jpg)
![](CC-Sarosh-059-Lab6_media/image-940.jpg)
![](CC-Sarosh-059-Lab6_media/image-941.png)
![](CC-Sarosh-059-Lab6_media/image-942.png)
![](CC-Sarosh-059-Lab6_media/image-943.png)
![](CC-Sarosh-059-Lab6_media/image-944.png)
![](CC-Sarosh-059-Lab6_media/image-945.png)
![](CC-Sarosh-059-Lab6_media/image-946.png)
![](CC-Sarosh-059-Lab6_media/image-947.png)
![](CC-Sarosh-059-Lab6_media/image-948.png)
![](CC-Sarosh-059-Lab6_media/image-949.png)
![](CC-Sarosh-059-Lab6_media/image-950.png)
![](CC-Sarosh-059-Lab6_media/image-951.png)
![](CC-Sarosh-059-Lab6_media/image-952.png)
![](CC-Sarosh-059-Lab6_media/image-953.png)
![](CC-Sarosh-059-Lab6_media/image-954.png)
![](CC-Sarosh-059-Lab6_media/image-955.png)
![](CC-Sarosh-059-Lab6_media/image-956.png)
![](CC-Sarosh-059-Lab6_media/image-957.png)
![](CC-Sarosh-059-Lab6_media/image-958.png)
![](CC-Sarosh-059-Lab6_media/image-959.png)
![](CC-Sarosh-059-Lab6_media/image-960.png)
![](CC-Sarosh-059-Lab6_media/image-961.png)
![](CC-Sarosh-059-Lab6_media/image-962.png)
![](CC-Sarosh-059-Lab6_media/image-963.png)
![](CC-Sarosh-059-Lab6_media/image-964.png)
![](CC-Sarosh-059-Lab6_media/image-965.png)
![](CC-Sarosh-059-Lab6_media/image-966.png)
![](CC-Sarosh-059-Lab6_media/image-967.png)
![](CC-Sarosh-059-Lab6_media/image-968.png)
![](CC-Sarosh-059-Lab6_media/image-969.png)
![](CC-Sarosh-059-Lab6_media/image-970.png)
![](CC-Sarosh-059-Lab6_media/image-971.png)
![](CC-Sarosh-059-Lab6_media/image-972.png)
![](CC-Sarosh-059-Lab6_media/image-973.png)
![](CC-Sarosh-059-Lab6_media/image-974.png)
![](CC-Sarosh-059-Lab6_media/image-975.png)
![](CC-Sarosh-059-Lab6_media/image-976.png)
![](CC-Sarosh-059-Lab6_media/image-977.jpg)
![](CC-Sarosh-059-Lab6_media/image-978.jpg)
![](CC-Sarosh-059-Lab6_media/image-979.png)
![](CC-Sarosh-059-Lab6_media/image-980.png)
![](CC-Sarosh-059-Lab6_media/image-981.png)
![](CC-Sarosh-059-Lab6_media/image-982.png)
![](CC-Sarosh-059-Lab6_media/image-983.png)
![](CC-Sarosh-059-Lab6_media/image-984.png)
![](CC-Sarosh-059-Lab6_media/image-985.png)
![](CC-Sarosh-059-Lab6_media/image-986.png)
![](CC-Sarosh-059-Lab6_media/image-987.png)
![](CC-Sarosh-059-Lab6_media/image-988.png)
![](CC-Sarosh-059-Lab6_media/image-989.png)
![](CC-Sarosh-059-Lab6_media/image-990.png)
![](CC-Sarosh-059-Lab6_media/image-991.png)
![](CC-Sarosh-059-Lab6_media/image-992.png)
![](CC-Sarosh-059-Lab6_media/image-993.png)
![](CC-Sarosh-059-Lab6_media/image-994.png)
![](CC-Sarosh-059-Lab6_media/image-995.png)
![](CC-Sarosh-059-Lab6_media/image-996.png)
![](CC-Sarosh-059-Lab6_media/image-997.png)
![](CC-Sarosh-059-Lab6_media/image-998.png)
![](CC-Sarosh-059-Lab6_media/image-999.png)
