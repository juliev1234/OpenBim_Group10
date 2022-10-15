# Idea
We want to make the HTML-Build_IFC-Converter to a tool that pulls information about the structural elements in an IFC file and displays it in a nice and organized way. This requires a cooperation between python and Java script to generate the information. I would be nice to subcategorize the structural elements in each level, so it becomes easier to understand the model.

# Changes made

## Overall changes
We have changed the colors of the website to different kinds of pink to give it a nice aesthetic look. This has been done in the css-file.
## Header
We have added a header at the top of the page called “Structural element detector”. This is written in a pink box. The code to make these changes can be seen here:

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/headerhtml.png)
![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/headercss.png)

## Paragraph
We have added a paragraph underneath the header which describes the purpose of the website.

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/paragraphhtml.png)
![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/paragraphcss.png)

## Title
We have added a title so that the website is called “Structural element detector”. 

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/title.png)

## Number of structural elements
We have added descriptions about how many columns and beams there are in the building. This has been done by finding the number of ‘IfcBeam’ and ‘IfcWall’ by scripting and inserting these numbers in the properties box. 

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/structuralhtml.png)
![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A2_FutureBIM/Pictures/structuraljs.png)

# Trials 
The plan was also to include the dimensions of structural elements to get a nice overview of the properties of the elements.  But it caused errors using the Ifcopenshell.util.element.get_psets for a costum entity in the HTMLBUILD.py and thereafter implementing it as data in the property box in the html-build.js. 




