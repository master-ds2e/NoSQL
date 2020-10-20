#  Infrastructures de données: NoSQL

- [Instructor](#Instructor)
- [Syllabus](#Syllabus)
- [Program](#Program)
- [Prerequisites](#Prerequisites)
- [Preparation Before the First Session](#Preparation)
- [Project Work](#Project)
- [Resources](#Resources)

<a name="Instructor"></a>
## Instructor
Contact:
 - Wirtz Kevin
 - University of Strasbourg, BETA
 - kevin.wirtz@unistra.fr

About me:
 - University degree at Strasbourg (Statistics and Econometrics).
 - Second year PHD student in Economics.  (Bibliometrics, novelty, ...)
 - R since 2016 and Python 2018.
 - Working with SQL and noSQL databases.


<a name="Syllabus"></a>
## Syllabus 

The aim of this course is to teach students a way to store and process non-relational data. Depending on the size but also the problem at hand you will not use the same storage system. You will learn to choose the right format for the non-relational data you have.
During the whole course we are going to use Python as our programming language. We start off with basic unstructured formats like json, xml, dictionnaries. Next we study the most currently used noSQL database: [MongoDB](https://www.mongodb.com/). We finish with alternatives to MongoDB. 


<a name="Program"></a>
## Program 

20H face-to-face lecture

- Chapter 1:  Basic data format that are non-relational (2h)
- Chapter 2:  Non-relational DB (MongoDB)
- Chapter 3:  Other alternatives.

<a name="Prerequisites"></a>
## Prerequisites

- Prior knowledge in Python is required and familiarity with programming concepts.
- A laptop connected to the internet and running Windows, Linux, MacOS
- Anaconda installed, see below. Choose one of the IDE (I'll be using Spyder)
- One text editor ([Sublime](https://www.sublimetext.com/), [atom](https://atom.io/), [Vim](https://www.vim.org/), ...)


If you have little experience with Python or shell programming, the following tutorials may be helpful:

- https://www.w3schools.com/python/python_intro.asp
- https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/230659-decouvrez-python
- https://pythonprogramming.net/introduction-learn-python-3-tutorials/
- https://www.anotherbookondatascience.com/chapter1.html
- https://tutorial.djangogirls.org/en/intro_to_command_line/
- https://swcarpentry.github.io/shell-novice


<a name="Preparation"></a>
## Preparation Before the First Session

- Install [Anaconda](https://www.anaconda.com/products/individual) if it's not already done. If you have no previous installation of python make sure to add Anaconda to your path. If you want to work with environments please read https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
    
    <img src="img/conda.png">

- Install [Sublime](https://www.sublimetext.com/3)
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



<a name="Project"></a>
## Project Work

Group project to store and retrieve data

<a name="Resources"></a>
## Resources

- https://www.w3schools.com/python/python_mongodb_getstarted.asp
- https://www.youtube.com/watch?v=E-1xI85Zog8&t