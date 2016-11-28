# Import methods from header
### Sublime Text plugin for C++ files
This is a simple plugin which reads a header file and imports all 
of class's methods in a source file, ready for implementation.  
##### Here's how to use it:
 - Write your header file
 - Save it as *foo.hpp*
 - Create a source file
 - Save it as *foo.cpp*
 - Hit **Ctrl + Shift + P** to open the command palette
 - Type in *Import methods from header*
 - When the command shows up, select it and validate
 - Enjoy the results

Example header file:
![Example header file](http://i.imgur.com/7OyxyQb.png "Example header file")

New source file (*same name*) and Command Palette:
![Example header file](http://i.imgur.com/rGhnDQq.png "New source file and Command Palette")

Source file filled in by the command:
![Source file filled in by the command](http://i.imgur.com/5V79NOp.png "Source file after")

##### Here's what the command does for that:
 - Looks up your source file name and replaces *.cpp* with *.hpp*
 - Opens your header file
 - Extract the class's name
 - Finds the lines where methods are declared
 - Insert every one of them in your source file with appropriate formatting (namespace, return type, braces and tabs, etc)  
   
 And that's it.  

 ##### How to install:
 - Download the three files
 - Put them in <ST dir>/Packages/User/

**\*\*Note: if you already have a user-defined** *.sublime-commands* **file, 
you can paste the contents of this one in yours.**  
(be sure to insert the entry properly into the JSON object)

##### Warning
I wrote that small utility for myself in the first place, and as a result, 
the "parsing algorithm" fits my coding style very tightly.  
__It may not fit yours.__  
I actually mean that this plugin might show *unexpected behavior* when presented your 
coding style, which implies that it *may* very well __wreck havock__ in your code.  
You should then adapt the Python script for it to work properly. It is (I think) easy 
to understand and well documented.