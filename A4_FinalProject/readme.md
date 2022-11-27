# Use case

The chosen use case is structural analysis. In the structural analysis, the load bearing elements and their dimensions and positions in the building is found using IFC concepts. This information is used to create the topology of the elements and create a plot of the model. Furthermore, information about length, width, volume etc. are found. This is presented on a website to give a good overview of the structural elements and to make it possible for the user to enter the density of the materials. This way the self-weight of the elements can be calculated. 

The video that shows the use case can be found [here](https://www.youtube.com/watch?v=UIK1KJLiRRM).

## BPMN for tool

On the figure below, the flow chart illustrates our tool, and what we have achieved with the python/html translation code. The starting point is to get the model included on the website to estimate the elements and thereby extract information about the dimensions and positions. Furthermore, we were able to identify the material related to the elements and illustrating these properties together with a geometrical illustration of the structural model including coordinates.
![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/ae0d3e214ebe4d16f4a9d5249284aafb8c11b819/A4_FinalProject/img/BPMN_tool.svg)

## BPMN for use case (large scale)

The BPMN below shows the ideal chart for the original use case we had in mind. The green box is indicating what we have achieved with our tool. The rest of the chart shows our previous ideas and in which direction the tool can be developed.
![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/547489e9e8e25725c3c06d1f32349d2e3451a1c7/A4_FinalProject/img/BPMN_usecase.png)


# Future work

For future work the script should also include all the other structural elements like beams and floors instead of only walls. It would be great if it was possible to move around in the plot, instead of using a picture of it. Instead of the drop-down menu, it could be cool if it was possible to click directly on the structural elements to get the information. Furthermore, the script should be changed so that it is possible to enter the density and thereby calculate the self-weight of the structural elements. At last, it would also be great if the script could export the information so that it could be imported to a FEM-program.
