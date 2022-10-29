# The report

## 3A: Analyse use case

### 1) Goal
To support the user to calculate/find the topology of the project in order to carry out a structural analysis.

### 2)	Model Use (Bim Uses)

![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A3_UseCase/img/BIM_uses.png)

The chosen use case is structural analysis. In the structural analysis, the load bearing elements and their dimensions and positions in the building can be found using IFC concepts. This information can be used to create the topology of the elements and create a structural design model. This model can then be analysed using a FEM-program. It is assessed that the following Mapping BIM uses are needed: 01 Existing conditions modelling, 07 Design review and 08 Structural Analysis. The use case categories can be seen in the table.


## 3B: Propose a (design for a) tool / workflow

### 3) Process

BPMN for use case:
![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A3_UseCase/img/BPMN_usecase.svg)

BPMN for tool:
![alt text](https://github.com/juliev1234/OpenBim_Group10/blob/main/A3_UseCase/img/BPMN_tool.svg)

### 4) Description

The input of the tool is an IFC-file, and the output is a simplified topology of the building e.g. (x,y,z)-coordinates of the different structural elements found by the tool. 
1)	Loading the IFC-file in the tool
2)	Categorizing the different structural element e.g. beams, columns, footings, slabs and walls
3)	Extracting and manipulating coordinate data from the structural elements to a more simplified state e.g. (x,y,z)-lines that are connected together.
4)	Calculating and allocating loads to the constructed topology. This may be done by finding the dead-load of the element and thereby the building. This step will then need data from the IFC file to figure out the material of the elements and calculating a potential weight.
5)	Saving the categorized structural coordinates and load data to a standardized file for other FEM-programs to read.


## 3C: Information exchange

### 5) Information exchange
The excel template is attached. The excel file fills out the structural elements needed in the tool: Foundations, columns, beams, floor, roof, and walls. LOR, LOG and LOI are all related to the level of detailing and are based on the essential information for a structural analysis. 
As the structural analysis is an iterative process, the value of LOR is generally 200, as both the location and levels can be changed if the analyze fails.
Furthermore, it is assumed that the geometry of the structural elements isn’t fully determined either, as the choices of types can have an influence on both the loading and the CO2 emission. Therefore, the LOG is in general 200 as well. The properties are essential for the use case, which is the reason why LOI generally is 325. 

### 6) IFC and data

-	IFC data:
The IFC entities needed for the tool to function is: IfcFooting, IfcFoundation, ifcWall, IfcColumn and IfcBeam. 
The properties needed for the entities are: Dimensions, Material properties and their coordinates.
With this information the number of structural elements and coordinate data for the structural elements can be handled and sorted in the different material properties categories.

-	External sources:
A catalog with density of different materials, so the dead-load can be calculated based on the material’s properties and dimensions.

-	Assumptions:
It is assumed that all the bearing elements found from the IFC entities are geometrically connected in order to set up the topology of the building. Bearing elements are simplified throughout the cross section so a homogeneous material from a density catalog can be assigned.


## 3D: Value

### 7) Business value 
The tool will ideally save time for the company since it will be able to quickly convert the structural elements from an IFC file to a FEM-program.  In that way structural engineers can assess the bearing elements relative early in the design phase so major structural changes in the model isn’t an issue later in the design phase.

### 8) Societal value
We don’t know if it makes the world better, but it will make the modeling phase in a FEM-program for a structural engineer a lot easier.


## 3E: Delivery

### 9) Your tool/workflow
Our tool would essentially need an IFC-file which includes a structural modelled building and a data sheet with material data as input. The tool would automatically sort and calculate the data received from the IFC-file and save a file with the topology and load data. Hereafter, it is ready to be analysed using a FEM-program.

### 10) Delivery
- Step 1) (Input IFC file) Get an overview of the structural elements e.g. sort data into structural categories
- Step 2) Try out different methods to extract and sort dimensions and coordinate data.
- Step 3) Look at the different structural element independently e.g. footings, and find the coordinates and thereby the topology.
- Step 4) Calculate dead load and assign the value to the structural elements (This may be done by the already found coordinate from step 3)
- Step 5) Sort the calculated data from step 1, 2, 3 and 4 in a file that is readable for a FEM-program.

#### Our delivery
The described steps above are for the fully developed tool which is a lot of work. In our case we may simplify the tool to only look at one or more specific structural elements in order to complete all 5 steps.












