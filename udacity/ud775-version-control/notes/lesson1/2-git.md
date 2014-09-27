# Version Control

**Udacity: UD 775**

---

### Where do versions come from?

One way of saving different versions of a file is to manually create new files every now and then with the content from the file you're working in. This is really tedious, and not exactly feasible for a project with thousands of files, like [Linux](https://github.com/torvalds/linux).

How else could we get versions of our files? You've probably already seen version control before:

* Google Drive
    * Google Drive will let you see all revisions that have been made to a file
* Wikipedia
    * You can click the "view history" button on any Wikipedia article to see changes that have been made.
    * Try it out [here](http://en.wikipedia.org/w/index.php?title=Scotland&action=history)!
    
### Version Control for Code

If you had to design a version control system specifically for code, what would it look like? Something like Google Drive wouldn't be great, because you have to use their editor, and versions get saved every single time an edit is made. You also have to be connected to the internet for things to work properly. A good VCS for programming would look like this:

* You can use any editor you want to
* Versions are saved only when you save them
* You can save versions while offline, and then upload the changes to a server later

Luckily for us, there's a version control system that meets all of these requirements!

### Introducing Git

Here is a short history of Git, taken from the first chapter of the official Git book:

> As with many great things in life, Git began with a bit of creative destruction and fiery controversy. The Linux kernel is an open source software project of fairly large scope. For most of the lifetime of the Linux kernel maintenance (1991–2002), changes to the software were passed around as patches and archived files. In 2002, the Linux kernel project began using a proprietary DVCS system called BitKeeper.

In 2005, the relationship between the community that developed the Linux kernel and the commercial company that developed BitKeeper broke down, and the tool’s free-of-charge status was revoked. This prompted the Linux development community (and in particular Linus Torvalds, the creator of Linux) to develop their own tool based on some of the lessons they learned while using BitKeeper. Some of the goals of the new system were as follows:

* Speed
* Simple design
* Strong support for non-linear development (thousands of parallel branches)
* Fully distributed
* Able to handle large projects like the Linux kernel efficiently (speed and data size)
* Since its birth in 2005, Git has evolved and matured to be easy to use and yet retain these initial qualities. It’s incredibly fast, it’s very efficient with large projects, and it has an incredible branching system for non-linear development (See Chapter 3).