#9/2/2015:
    project ideas:
    -aggregation of resources from the web, like what can you do with deep dream API
    -rasberry pi and image processing seem interestingly interconneced, what kind of data 
    from the RP could a GPU do something with. process written notes from class with google?
    get more info to define any interesting words written in notes?
    -A game that uses OpenGL to simulate something intersting, like cutting down a tree, or blacksmithing, or destruction


#first day:
    I have not infrequently manually "pattern matched" files, never again. #grep
    git stuff
        clone, pull, push, commit, add, branch
        Git is all about allowing many people to work on the same code at the same time.
        Users duplicate the project, contribute to it, and merge their contributions with the
        master project stored on github
    linux stuff
        apt-get, cd, ls, mkdir, tree
        Using linux as a platform gives access to a metric boat-load of tools required for "a stack"
    regular expressions stuff
        \d,\w,[],{},.,?
        Regular expressions help with the constant need to interpret strings, for example pairing through
        user input looking for useful info
    
#9/15/2015
    more Github tutorial
    
#9/18/2015

    https://github.com/IanHuntress/OpenSourceLabs/blob/master/Lab3/README.md
    Link to lab 3 stuff
    
#9/25/2015
    Documentation stuff
    
    https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=203505
    
        I fixed a spelling error here https://www.freebsd.org/doc/handbook/dialup.html in this file (that I eventually found)
    http://svn.freebsd.org/doc/head/en_US.ISO8859-1/books/handbook/serialcomms/chapter.xml 
    "Configuration" was written as "confiuration." This error is a powerful demonstration of the need for good documentation.
    In the words of Sevi, "The people deserve to know" how to set up their dialup connection.
    This is the link to the bugzilla https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=203505
    
        This was an excercise in huberous. When I found that the file was not exactly where I expected it to be, I thought that it
    was more likely that someone mistakenly stored it far far away from where it belonged than my simply missing it.
    
    The debate was slightly one sided under the double-think that all proprietary software is evil, but that sometimes it can
    contribute to good works. The reasons for open source software are all offshoots and consequences of the core idea that
    the crowd has wisdom, moreover, the crowd has passion. The place of open source software is where people are passionate about
    a need or problem, rather than passionate about making as much money as possible. In contrast, the place of proprietary
    software is in reaching the widest possible audiance of users regardless of their interest in the problem. 
        An individual or company should decide what type of software they will create based on the interest of the audiance
    and the nature of their problem. Moorthey's google books patent happened to fit into the format of a patent based on 
    the wide, mildly interested audiance. Other projects like FreeBSD are not wrong in using open source, they simply met with
    a different audiance. 
    
        If I was personally creating a "side project" which I could fit into either opensource or proprietary models, I would
    most likely ignore the needs of my problem and audiance and seek only to maximize profits. This is mostly likely a bias
    associated with being young; I hope eventaully to outgrow it.
    
        I also watched that TED talk about open source drug manufactoring; it was well worth the subsequent 5 hours of being absorbed
    in TED talks.
    
#10/2/2015
    CMake and build systems: a program whose job is to handle all of the compiling and linking and pulling together of resources
    for another program. It allows partial builds, continuous tests, generation of test data, and continuous test cases.
    
    
#10/9/2015 - 10/23/2015
        I am unable to complete Lab7. Even though I have had all the time in the world to learn about Continuous Integration, I did not
    and I do not understand in the context of Observatory3. I fixed a typo bug, submitted a pull request, watched some automated
    tests run, but my understanding from the TA's is that my fix needed to involve an automated test.
        Moorthey once said partial credit for labs could be given if the lab is treated like a "hackathon."
        I was check off for this lab.
        
#10/23/2015

![alt text](https://github.com/IanHuntress/OpenSourceLabs/blob/master/Lab7/lab7pic.bmp "Lab7")

SurviveCommons:
- Number of contributors:3, but two of them have the same name, they might be the same person
- Lines of code:18766 (18759 reported by git ls-files -z | xargs -0 wc -l) 
- First contribution: June 2015
- Last contribution: October 2015

YAPS:
- Number of contributors:3
- Lines of code:2363  
- First contribution: February 2015
- Last contribution: October 2015

Lapsus:
- Number of contributors:7
- Lines of code:32242
- First contribution: January 2015
- Last contribution: October 2015

EveOnlineMarketAnalysisTool:
- Number of contributors:8
- Lines of code:345129 
- First contribution: August 2015
- Last contribution: October 2015

#11/6/2015

![alt text](https://github.com/IanHuntress/OpenSourceLabs/blob/master/Lab9/graph.bmp "Lab7")
![alt text](https://github.com/IanHuntress/OpenSourceLabs/blob/master/Lab9/plotgroup.bmp "Lab7")
![alt text](https://github.com/IanHuntress/OpenSourceLabs/blob/master/Lab9/linegraph.bmp "Lab7")
![alt text](https://github.com/IanHuntress/OpenSourceLabs/blob/master/Lab9/datarulesplot.bmp "Lab7")

Why does the book graph the not-pruned Titanic rules?

Our project currently consists of a github with a bunch of npm/openGL/JS tools crammed together.
Recently, I found a github project called Draw.js that implements most of the Whiteboard stuff
that we began our project for. This means we will have to slightly reorient our goals, not to start from
scratch, reimplimenting something, but improving on what already exists. This might result in 
superfluous additions to the original goal, but that is exactly the kind of nonsense I most enjoy






