# 41934 A1-OpenBim - Group10

### Group members
Filip Jacobi (s193840), Mikkel Grebin (s193846), Julie Vollmer (s193856)

### Describe the use case you have chosen
The chosen use case is structural analysis. In the structural analysis, the load bearing elements and their dimensions and positions in the building can be found using IFC concepts. This information can be used to create the topology of the elements to then create a structural design model. The structural model can then be analyzed using FEM after the material properties have been defined. 

### Who is the use case for?
The use case is made for the client (bygherren) but also for the structural engineers and architects. 

### What disciplinary (non-BIM) expertise did you use to solve the use case
Knowledge about programming was needed to create a script that will help solve the use case. Furthermore, knowledge about load bearing elements and their material properties is needed. 

### What IFC concepts did you use in your script (would you use in your script)
To get information about the load bearing elements, the IFC entity “IfcBuildingElement” was used to find information about “IfcFooting”, “IfcBeam” and “IfcWall”. The property sets were then found with "IfcPropertySet" by importing “ifcopenshell.util.element” and using “get_psets”. This information was found from the Revit model.

To find the positions of the load bearing elements, the code “ifcopenshell.util.placement.get_local_placement(footing.ObjectPlacement)” might be useful.  

### What disciplinary analysis does it require?
Knowledge about FEM is required to solve the use case, since this will be used to analyze the model.

### What building elements are you interested in?
The load bearing elements which include beams, columns, footing and walls.  

### What (use cases) need to be done before you can start your use case?
Before we can start our use case, the use cases Cost Estimation, Code Validation and Fire need to be done. Cost Estimation needs to be done, since this is a part of the beginning and planning of the construction. It is also necessary to take Code Validation into account when planning. Furthermore, some consideration of fire regulations must be made, as this determines the width of the corridors and where the doors should be. 

### What is the input data for your use case?
The input data for our use case is the dimensions of load bearing elements and their positions in the building. Furthermore, the element type and material are needed.

### What other use cases are waiting for your use case to complete?
The uses cases LCA, Code Validation and Cost Estimation are waiting for our use case to complete, since they need information about material properties and structural documentation. 
