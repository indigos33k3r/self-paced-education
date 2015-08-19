# Version Control

**Udacity: UD 775**

---

### Setting up a Git workspace

Before you move on to the next lesson, you should take the time to customize your command line to make using Git nicer. Here's what mine looks like:

![my-terminal](../img/terminal.png)

Below is a nice setup for your terminal and Git environment:

**Restart Git Bash or your terminal**

Once you’ve completed the following instructions, you'll need to close and re-open Git Bash (if you are using Windows) or your terminal (if you are using Mac or Linux). Many of the configurations listed here will not take place until you have done this, so if you don’t see your changes taking place right away, this is probably why.

**Downloading necessary files**

Later in these instructions, you'll need the two files `git-completion.bash` and `git-prompt.sh`. To download them:

1. Visit [this page](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash), where you can find git-completion.bash.
2. Right click anywhere on the page and select "Save As..."
3. Save the file to your home directory
4. Rename the file to git-completion.bash using the command line. (Some browsers will name the file git-completion.bash.txt.)
5. Repeat the above steps to save [this page](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh) as git-prompt.sh in your home directory.

**Creating a .bash_profile**

Some of the following configurations will require you to add to a file called .bash_profile, which is used to configure Git Bash if you’re using Windows, or the terminal if you’re using Mac or Linux. (If your terminal is using a different shell than bash, than many of the following instructions will not work. However, bash is the default on both Mac and Ubuntu.) Note: Since this file has a period at the beginning of its name, it is called a hidden file and will not appear in most file system navigators. To create this file:

1. Navigate to your home directory
2. Create a new file named `.bash_profile`
3. Use `ls -a`, which shows hidden files, to confirm your file has been created.

Alternatively, if you're interested, you can use the `.bash_profile` we used when filming this course. To do so:

1. Download [bash_profile_course](https://www.udacity.com/api/nodes/2955818665/supplemental_media/bash-profile-course/download).
2. Move the file to your home directory.
3. Rename the file to `.bash_profile`, including the period at the beginning.

If you already have a `.bash_profile`, you don’t need to create a new one.

**Setting up tab completion**

Setting up tab completion allows you to type the first few characters of a Git command, press tab, and have the rest of the command filled in. In Lesson 2, you’ll also be giving names to some of your commits, and tab completion will allow you to auto complete these names in the same way. Having tab completion set up can make working with Git much more efficient.

To set up tab completion:

1. Follow the instructions above in the section "Downloading necessary files" to make sure your home directory contains the file git-completion.bash.
2. Add the line source git-completion.bash to your .bash_profile.

**Modifying your prompt**

Every time you type a command, the symbol that appears before you type is called the prompt. Many people who use Git like to modify their prompt to show what commit they’re currently on, and whether they have any uncommitted changes.

The example `.bash_profile` already contains a customized prompt. If you’re not using this profile and you don’t already have a custom prompt, we recommend including the name of the directory you’re in, followed by the commit you have checked out with a * if you have uncommitted changes. We also recommend using a bright color, such as blue, so that your prompt will stand out from the commands that you run. To get a prompt like this:

1. Follow the instructions above in the section "Downloading necessary files" to make sure your home directory contains the file `git-prompt.sh`
2. Add the following lines to your `.bash_profile`:

        source git-prompt.sh
        export PS1="[\033[01;34m]\W\$(__git_ps1)$[\033[00m] "

It's not necessary to understand how these magic-looking lines work. Even experienced Unix programmers usually copy and paste bash prompt strings rather than writing them from scratch. If you're curious though, [here](http://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html) is an explanation of what kinds of things a bash prompt can contain and how to configure it.

**Configuring your name and email**

When you used git log earlier, you saw that Git listed the author of each commit. In order to do this, Git needs to know your name and email address. In fact, Git will not allow you to commit before you’ve given it this information. To do so:

1. Run `git config --global user.name "Your name"`
2. Run `git config --global user.email "youremail@domain.com"`

Fill in your own name and email address where indicated.

**Set up a default editor**

Sometimes Git will automatically open a text editor. For example, if you make a commit without specifying a commit message, Git will open a text editor and allow you to use it to write the commit message. You’ll want this editor to be one you like. To configure which editor Git will open:

1. Make sure you can open your editor from the command line
2. Run the command `git config --global core.editor`, followed by the command you run to start your editor.

For example, if you use Sublime, you would run git config --global core.editor "subl -n -w". (The -n flag will open Sublime in a new window, and the -w flag will cause Git to wait for you to close the file before continuing.) As a reminder, if you haven’t installed the subl command, which launches Sublime from the command line, you should do so. As another example, since the command emacs will launch the Emacs editor, you would run `git config --global core.editor emacs` if you use Emacs.

Note that on some systems, you'll need to give a full path to the editor you use. For example, if you want to use Sublime on Windows, you'll probably need to use `git config --global core.editor "'C:/Program Files/Sublime Text 2/sublime_text.exe' -n -w"` rather than the simpler `git config --global core.editor "subl -n -w"`.

**Additional Git configurations**

There are a couple of additional Git configurations that will be helpful for you in future lessons. We’re including them here so that all our configuration suggestions will be in one place. It will become clear in later lessons why these are useful. For now, add the following configurations:

* Run `git config --global push.default upstream`
* Run `git config --global merge.conflictstyle diff3`
* Restart Git Bash or your terminal

Don’t forget to do this, or some of your changes won't take effect.

If you made it through all of that, you should have a pretty snazzy Git environment now!