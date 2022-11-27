from re import X
import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.placement
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
import os.path

#Main plot of all external walls
def printBuilding(ifcmodel, name):

    #Creating dirc under Images
    parent_dir = "output/Images"
    if (os.path.exists("output/Images/"+name))==False:
        path = os.path.join(parent_dir, name)
        os.mkdir(path)

    #model_url = "model/"+name+".ifc"
    ifc_file = ifcmodel
    element = ifc_file.by_type('IfcWall')
    
    #3d plot stuff      
    fig = plt.figure()
    settings = ifcopenshell.geom.settings()
    ax = fig.add_subplot(projection="3d",adjustable='box')

    #Allocating all x y and z coordinates
    vallx = []
    vally = []
    vallz = []

    #Plotting loop
    for wall in element:

        #Only External walls
        if ifcopenshell.util.element.get_psets(wall)["Pset_WallCommon"]["IsExternal"]:
            matrix = ifcopenshell.util.placement.get_local_placement(wall.ObjectPlacement)
            
            #Transformations matrixes
            trans_matrix = matrix[0:3,0:3]
            addCoord = matrix[0:3,3]
            shape = ifcopenshell.geom.create_shape(settings, wall)

            verts = shape.geometry.verts
            faces = shape.geometry.faces
            edges = shape.geometry.edges

            grouped_verts = [np.dot(trans_matrix,[verts[i], verts[i + 1], verts[i + 2]])+addCoord for i in range(0, len(verts), 3)]
            grouped_edges = [[edges[i], edges[i + 1]] for i in range(0, len(edges), 2)]
            grouped_faces = [[faces[i], faces[i + 1], faces[i + 2]] for i in range(0, len(faces), 3)]

        

            v = np.array(grouped_verts)
            f = np.array(grouped_faces)

            vallx = np.append(vallx,v[:,0])
            vally = np.append(vally,v[:,1])
            vallz = np.append(vallz,v[:,2])
                    
            pc = art3d.Poly3DCollection(v[f],facecolor = "lightblue" ,edgecolor="black",alpha=1)
            ax.add_collection3d(pc)
                
    #Constraint for xyz-axis
    ax.set_xlim3d([np.amin(vallx)-2, np.amax(vallx)+2])
    ax.set_ylim3d([np.amin(vally)-2, np.amax(vally)+2])
    ax.set_zlim3d([np.amin(vallz)-2, np.amax(vallz)+2])        
    ax.set_box_aspect([ub - lb for lb, ub in (getattr(ax, f'get_{a}lim')() for a in 'xyz')])

    #Save figure in dirc
    plotName = "Main.png"
    plotDirc = "output/Images/"+name+"/"+plotName
    plt.savefig(plotDirc)
    plt.close()

#Generating plots of highligted walls 
def printHighliteWall(ifcmodel, name):

     #Creating dirc under Images
    parent_dir = "output/Images"
    if (os.path.exists("output/Images/"+name))==False:
        path = os.path.join(parent_dir, name)
        os.mkdir(path)
    

    ifc_file = ifcmodel
    element = ifc_file.by_type('IfcWall')
    
    plotIndex = 0
    #Plotting loop 1
    for plot in element:
        if ifcopenshell.util.element.get_psets(plot)["Pset_WallCommon"]["IsExternal"]: 
            
            plotIndex += 1 
            wall_show = plotIndex-1
            
            #3d plot stuff
            fig = plt.figure()
            settings = ifcopenshell.geom.settings()
            ax = fig.add_subplot(projection="3d",adjustable='box')

            #Allocating all x y and z coordinates
            vallx = []
            vally = []
            vallz = []
            index = 0
            
            #Plotting loop 2
            for wall in element:

                #Only external walls
                if ifcopenshell.util.element.get_psets(wall)["Pset_WallCommon"]["IsExternal"]:
                    
                    #Transformations matrixes
                    matrix = ifcopenshell.util.placement.get_local_placement(wall.ObjectPlacement)
                    trans_matrix = matrix[0:3,0:3]
        
                    addCoord = matrix[0:3,3]
                    shape = ifcopenshell.geom.create_shape(settings, wall)

                    #Coordinates 
                    verts = shape.geometry.verts
                    #Index
                    faces = shape.geometry.faces
                    edges = shape.geometry.edges

                    grouped_verts = [np.dot(trans_matrix,[verts[i], verts[i + 1], verts[i + 2]])+addCoord for i in range(0, len(verts), 3)]
                    grouped_edges = [[edges[i], edges[i + 1]] for i in range(0, len(edges), 2)]
                    grouped_faces = [[faces[i], faces[i + 1], faces[i + 2]] for i in range(0, len(faces), 3)]

        

                    v = np.array(grouped_verts)
                    f = np.array(grouped_faces)

                    vallx = np.append(vallx,v[:,0])
                    vally = np.append(vally,v[:,1])
                    vallz = np.append(vallz,v[:,2])
                    if index == wall_show:
                        pc = art3d.Poly3DCollection(v[f],facecolor = "red" ,edgecolor="grey",alpha=1)
                    else:
                        pc = art3d.Poly3DCollection(v[f],alpha=0.2)#edgecolor="black"
            
                    index = index + 1
                    ax.add_collection3d(pc)
                
            #Constraint for xyz-axis
            ax.set_xlim3d([np.amin(vallx)-2, np.amax(vallx)+2])
            ax.set_ylim3d([np.amin(vally)-2, np.amax(vally)+2])
            ax.set_zlim3d([np.amin(vallz)-2, np.amax(vallz)+2])
            ax.set_box_aspect([ub - lb for lb, ub in (getattr(ax, f'get_{a}lim')() for a in 'xyz')])

            #Save figure in  dirc
            plotName = "Billede"+str(plotIndex)+".png"
            plotDirc = "output/Images/"+str(name)+"/"+plotName
            plt.savefig(plotDirc)
            plt.close()

#Finding materials in walls             
def getInformation(ifcmodel):

    ifc_file = ifcmodel
    walls = ifc_file.by_type('IfcWall')
    
    # Materials and wall type
    wall_type = []
    material_list = []
    material_list2 = []
    allmaterials = []    
    for wall in walls:  
        material = []
        #Only external walls
        if ifcopenshell.util.element.get_psets(wall)["Pset_WallCommon"]["IsExternal"]:        
            if wall.HasAssociations:
                for i in wall.HasAssociations:
                    if i.is_a('IfcRelAssociatesMaterial'):
                        wall_type.append(i.RelatingMaterial.ForLayerSet.LayerSetName)

                        if i.RelatingMaterial.is_a('IfcMaterial'):
                            material.append(i.RelatingMaterial.Name)

                        if i.RelatingMaterial.is_a('IfcMaterialList'):
                            for materials in i.RelatingMaterial.Materials:
                                material.append(materials.Name)

                        if i.RelatingMaterial.is_a('IfcMaterialLayerSetUsage'):
                            for materials in i.RelatingMaterial.ForLayerSet.MaterialLayers:
                                material.append(materials.Material.Name) 

            #List of all material in each external wall
            material_list.append(material)

            #List of all materials
            material_list2 += material
            for i in material_list2:
                if i not in allmaterials:
                    allmaterials.append(i)

    return material_list,allmaterials,wall_type



