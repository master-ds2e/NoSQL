#  Infrastructures de données: NoSQL

- [Instructor](#Instructor)
- [Syllabus](#Syllabus)
- [Program](#Program)
- [Prerequisites](#Prerequisites)
- [Preparation Before the First Session](#Preparation)
- [Grading](#Grading)
- [Resources](#Resources)

<a name="Instructor"></a>
## Instructor
Contact:
 - Wirtz Kevin
 - University of Strasbourg, BETA
 - kevin.wirtz@unistra.fr
 - On discord (Send me a mail if you need a new link for another account)

About me:
 - University degree at Strasbourg (Statistics and Econometrics).
 - Third PHD student in Economics.  (Bibliometrics, novelty, ...)
 - R since 2016 and Python 2018.
 - Working with SQL and noSQL databases.


<a name="Syllabus"></a>
## Syllabus 

The aim of this course is to teach students a way to store and process non-relational data. Depending on the size but also the problem at hand you will not use the same storage system. You will learn to choose the right format for the non-relational data you have.
During the whole course we are going to use Python as our programming language. We start off with basic unstructured formats like json, xml, dictionnaries. Next we study the most currently used noSQL databases: [MongoDB](https://www.mongodb.com/), [Neo4j](https://neo4j.com/download-neo4j-now). We finish with a short presentation of other DBs. 

The goal of the course is not to be exhaustive. Programming is a vast space of knowledge, sometimes you will do something I have never done before. In the end you will learn what I know and I will learn from your questions. This also means that I can't have the answers to all of your problems, basic behavior in programming is to first do research on your side. Websites like stackoverflow/stackexchange/Quora/Youtube/Github/... all of them are your best friends when it comes to solving issues. If after your own research you are still lost then you can send me a message about your problem. Either I will have the solution because I encountered it previously, or I don't but I can guide you to the solution. In no way you should ask me to code things for you, it's your job !

<a name="Program"></a>
## Program 

20H face to face lecture

- Introduction
- Chapter 1:  Basic data format that are non-relational
- Chapter 2:  MongoDB
- Chapter 3:  Neo4j
- Chapter 4:  Other alternatives.

    <img src="img/edt.png">

<a name="Prerequisites"></a>
## Prerequisites

- Prior knowledge in Python is required and familiarity with programming concepts.
- A laptop connected to the internet and running Windows, Linux, MacOS
- Anaconda installed, see below. Choose one of the IDE (I'll be using Spyder and Jupyter-Notebook)
- One text editor ([Sublime](https://www.sublimetext.com/), [Atom](https://atom.io/), [Vim](https://www.vim.org/), ...)


If you have little experience with Python or shell programming, the following tutorials may be helpful:

- https://www.w3schools.com/python/python_intro.asp
- https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/230659-decouvrez-python
- https://pythonprogramming.net/introduction-learn-python-3-tutorials/
- https://www.anotherbookondatascience.com/chapter1.html
- https://tutorial.djangogirls.org/en/intro_to_command_line/
- https://swcarpentry.github.io/shell-novice


<a name="Preparation"></a>
## Preparation before the First Session

- Install [Anaconda](https://www.anaconda.com/products/individual) if it's not already done. If you have no previous installation of python make sure to add Anaconda to your path. If you want to work with environments please read https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
    
    <img src="img/conda.png">

- Install [Sublime](https://www.sublimetext.com/3)

## Preparation before Chapter II

- Install MongoDB:
    * Windows
        Install it using the msi found in https://www.mongodb.com/try/download/community. During install just click next. Chances are your install will be found in C:\Program Files. MongoDB poorly handles the space in the path. I recommend moving C:\Program Files\MongoDB to C:\MongoDB (Make sure that the mongo server is shutdown in the task manager before). Last thing to do is to modify C:\MongoDB\Server\4.4\bin\mongod.cfg lines 8 and 19 to the appropriate path.
        You can now start your Mongo Server, open the cmd prompt at this location C:\MongoDB\Server\4.4 and run:
    ```bash
    mongod.exe --dbpath data --config bin\mongod.cfg
   ```
   * macOS
   https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
   
   * Linux
   https://docs.mongodb.com/manual/administration/install-on-linux/

- Install MongoDB compass https://www.mongodb.com/try/download/compass

## Preparation before Chapter III

### Method 1
First you need to install [java](https://www.oracle.com/java/technologies/javase-jdk16-downloads.html)

Then install [neo4j desktop](https://neo4j.com/download-thanks-desktop/?edition=desktop&flavour=windows&release=1.4.3&offline=true)

When everything is done you can launch Neo4j Desktop and you should be able to connect to the default db (Movie)

### Method 2
First you need to install java. Seems like there's a lot of compatibility issue so I recommend you use the same version as me. 
https://www.oracle.com/java/technologies/javase-jdk11-downloads.html

- Install Neo4j following these tutorials(n.b: you can stop the tutorials if you are able to have the same output as the image below):
    https://neo4j.com/download-thanks/?edition=community \
    https://riptutorial.com/neo4j/example/13244/installation---starting-a-neo4j-server \
    https://www.youtube.com/watch?v=3JMhX1sT98U 

<img src="img/Neo4j_setup.png">


<a name="Evaluation system"></a>

## Grading

You will have two grades at the end of the semester for this module. 

### Final exam

Date: tba.
Content: Questions mixed with the differents module inside of the UE. For my side of the exam you'll have a study case with a Python code to interpret and comment. Details tbd

### Dossier

Date: tba.
It's not a "dossier" per say:

- In each chapter there's a couple of "todo", At the end of each Chapter you'll send me these todos. This is mainly to see your participation since most of them will be worked and discussed during the course. That is one side of your grade.

- I recommend using Jupyter-Notebook (more on that later).

<a name="Resources"></a>
## Resources

- https://www.w3schools.com/python/python_mongodb_getstarted.asp
- https://www.youtube.com/watch?v=E-1xI85Zog8&t