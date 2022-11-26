import ifcopenshell
import ifcopenshell.util.element
import os.path
import time
import Functions as func

def modelLoader(name):

    ''' 
        load the IFC file 
    '''
    
    model_url = "model/"+name+".ifc"
    start_time = time.time()

    if (os.path.exists(model_url)):
        model = ifcopenshell.open(model_url)
        print("\n\tFile    : {}.ifc".format(name))
        print("\tLoad    : {:.2f}s".format(float(time.time() - start_time)))
        
        start_time = time.time()
        writeHTML(model,name)
        print("\tConvert : {:.4f}s".format(float(time.time() - start_time)))
        
    else:
        print("\nERROR: please check your model folder : " +model_url+" does not exist")


def writeHTML(model,name):


    material_list, allmaterials, wall_type = func.getInformation(model)
    func.printBuilding(model,name)
    func.printHighliteWall(model,name)
    
    ''' 
        write the HTML entities 
    '''
    
    # parent directory - put in setting file?
    parent_dir = "output/"
    # create an HTML file to write to
    if (os.path.exists("output/"+name))==False:
        path = os.path.join(parent_dir, name)
        os.mkdir(path)
    
    # Define walls
    walls = model.by_type('IfcWall')

    f_loc="output/"+name+"/index.html"
    f = open(f_loc, "w")

    cont=""
    
    cont+=0*"\t"+"<!DOCTYPE html>\n"
    # ---- START OF STANDARD HTML
    cont+=0*"\t"+"<html>\n"
    # ---- ADD HEAD
    cont+=1*"\t"+"<head>\n"
    # ---- ADD HTMLBUILD CSS - COULD ADD OTHERS HERE :)
    cont+=2*"\t"+"<link rel='stylesheet' href='../css/Dropdownstyle.css'></link>\n"
        # ---- ADD HEADER
    cont+=2*"\t"+"<h1> Structural element detector </h1>\n"
    # ---- ADD PARAGRAPH
    cont+=2*"\t"+"<p id='paragraph'> Welcome. This website shows the structural elements of your building and information about them. </p>\n"
    # ---- ADD TITLE
    cont+=2*"\t"+"<title> Structral element detector </title>\n"
    # ---- CLOSE HEAD
    cont+=1*"\t"+"</head>\n"

    # ---- ADD BODY
    cont+=1*"\t"+"<body>\n"  
    cont+=0*"\t"+'<div class="wrapper">\n'
    cont+=1*"\t"+'<div class="menu">\n'
    cont+=2*"\t"+'<select id="name">\n'
    cont+=3*"\t"+'<option value="start">Choose an element</option>\n'

    tal = 0
    navn = "wal"
    namelist = []
    lengthlist = []
    widthlist = []
    volumelist = []
    for wall in walls: 
        if ifcopenshell.util.element.get_psets(wall)["Pset_WallCommon"]["IsExternal"]:
            tal = tal + 1
            navn = navn+'l'
            namelist.append(navn)
            lengthlist.append(ifcopenshell.util.element.get_psets(wall)["PSet_Revit_Dimensions"]["Length"])
            widthlist.append(ifcopenshell.util.element.get_psets(wall)["PSet_Revit_Type_Construction"]["Width"])
            volumelist.append(ifcopenshell.util.element.get_psets(wall)["PSet_Revit_Dimensions"]["Volume"])
            cont+=3*"\t"+'<option value="'
            cont+= navn+'">'
            cont+= "Wall " + str(tal)+'</option>\n'
            

    cont+=2*"\t"+'</select>\n'
    cont+=1*"\t"+'</div>\n'

    # ---- Properties/content/data
    # Start
    cont+=0*"\t"+'<div class="content">\n'
    cont+=1*"\t"+'<div id="start" class="data">\n'
    cont+=2*"\t"+'<p class="image"><img src="../Images/'+str(name)+'/Main.png"></p>\n'
    cont+=1*"\t"+'</div>\n'

    # For each element
    for idx, i in enumerate(namelist):
        cont+=1*"\t"+'<div id="'
        cont+=i
        cont+='"class="data">\n'
        # Picture
        cont+=2*"\t"+'<p class="image"><img src="../Images/'+str(name)
        cont+='/Billede'+str(idx+1)+'.png'
        cont+='" alt=""></p>\n'
        # Length
        cont+=2*"\t"+'<p><b>Length</b><span>'
        cont+=str(round(lengthlist[idx],2)) + " m"
        cont+='</span></p>\n'
        # Width
        cont+=2*"\t"+'<p><b>Width</b><span>'
        cont+=str(round(widthlist[idx],2)) + " m"
        cont+='</span></p>\n'
        # Volume
        cont+=2*"\t"+'<p><b>Volume</b><span>'
        cont+=str(round(volumelist[idx],2)) + " m^3"
        cont+='</span></p>\n'
        #Density
        cont+=2*"\t"+'<p><b>Density</b><span id="dens'+str(idx+1)+'">'
        cont+="NaN"
        cont+='</span></p>\n'
        # Type
        cont+=2*"\t"+'<p><b>The name of the wall type is</b><span>'
        cont+=wall_type[idx]
        cont+='</span></p>\n'
        # Material
        cont+=2*"\t"+'<p><b>Materials in wall</b><span>'
        cont+=', '.join(material_list[idx])
        cont+='</span></p>\n'
        
        cont+=1*"\t"+'</div>\n'

    cont+=0*"\t"+'</div>\n'
    cont+=0*"\t"+'</div>\n'

    cont += '<center>'

    cont+=2*"\t"+'<div class="knap">\n'
    cont+=2*"\t"+"<p id='paragraph2'> All materials found in the building </p>\n"
    for idx, i in  enumerate(allmaterials):
        cont+=3*"\t"+'<label>'+str(i)
        cont+=3*"\t"+'<input id="inputbtn'+str(idx+1)+'" type="number" &nbsp placeholder="Density">\n'
        cont+=3*"\t"+'<button id="btn'+str(idx+1)+'" class="button">  Send Request </button>\n  </label>'
    cont+=2*"\t"+'</div>\n'
    cont +=2*"\t"+ '</center>'

    cont+=0*"\t"+'<div class="bottom">\n'
    cont+=0*"\t"+'</div>\n'


     # ---- JQUERY - IT WOULD BE CRAZY NOT TO
    cont+=0*"\t"+'<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.1/jquery.min.js" integrity="sha512-aVKKRRi/Q/YV+4mjoKBsE4x3H+BkegoM/em46NNlCqNTmUYADjBbeNefNxYV7giUp0VxICtqdrbqU7iVaeZNXA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>\n'
    
    # ---- ADD HTMLBUILD JS - COULD ADD OTHERS HERE 
    cont+=0*"\t"+"<script src='../js/Dropdown.js'></script>\n"
    cont+=0*"\t"+"<script src='../js/ButtonValue.js'></script>\n"

    # ---- CLOSE BODY AND HTML ENTITIES
    cont+=1*"\t"+"</body>\n"   
    cont+=0*"\t"+"</html>\n"

    # ---- WRITE IT OUT
    f.write(cont)
    f.close()

    # ---- TELL EVERYONE ABOUT 