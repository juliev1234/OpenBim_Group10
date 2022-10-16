# Idea
We want to make the HTML-Build_IFC-Converter to a tool that pulls information about the structural elements in an IFC file and displays it in a nice and organized way. This requires a cooperation between python and Java script to generate the information. I would be nice to subcategorize the structural elements in each level, so it becomes easier to understand the model.

# Changes made

### Overall changes
We have changed the colors of the website to different kinds of pink to give it a nice aesthetic look. This has been done in the css-file.

### Header
We have added a header at the top of the page called “Structural element detector”. This is written in a pink box. The code to make these changes can be seen here:

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/headerhtml.png)
![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/headercss.png)

### Paragraph
We have added a paragraph underneath the header which describes the purpose of the website.

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/paragraphhtml.png)
![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/paragraphcss.png)

### Title
We have added a title so that the website is called “Structural element detector”. 

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/title.png)

### Number of structural elements
We have added descriptions about how many columns and beams there are in the building. This has been done by finding the number of ‘IfcBeam’ and ‘IfcWall’ by scripting and inserting these numbers in the properties box. 

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/structuralhtml1.png)
![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/structuralhtml2.png)

In the JavaScript the following code has been written to insert the total number of beams and walls:

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/structuraljs.png)

### Level specific data 
The goal is also to display the number of walls, beams etc. pr. level, this has been done and illustrated for the “walls-elements” by the following modification of the given code.

#### Python:
The following generates a dictionary containing the number of walls of each level.

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/levelhtml1.png)

A for-loop made for each floor in the IFC file generates the following HTML code for the Java-script to handle.

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/levelhtml2.png)

#### Java:
In the JavaScript line 42 has been added to the code to output the level specific wall amount when pressing the level button. 

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/leveljs.png)


# Future work 
The plan was also to include the dimensions together with other properties of the structural elements to get a nice overview of the structure and to easily get access to its information.  But it caused errors using the Ifcopenshell.util.element.get_psets for a custom entity in the HTMLBUILD.py and thereafter implementing it as data in the property box in the html-build.js. 

Furthermore, it would be interesting to investigate the plan view in the future work. It could be nice to have a plan view of the structural elements when pressing the different plan views on the webpage, to have an indication of the location of the elements. In this context, the topology of the element would be relevant to illustrate as well. 




