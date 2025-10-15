# A2 
## A2a – About our group 
Our group’s focus area is Sustainability and Materials. 

We are the Manager group. 

The total score for the Group’s confidence for coding in Python: 4


## A2b: Identify claim
The tool is a “GWP comparison calculator” used for comparing different materials’ global warming potentials (hereafter, referred to as GWP).

As our tool’s function   is material comparison and optimization by calculating and comparing materials’ GWP, a traditional “claim” can’t explicitly be defined. 
However, we will review the construction of the external walls  in the following building: *CES_BLD_25_16*, where the materials used for the external wall  are detailed in the report: *“25-16-D-MAT”* on page 69.


## A2c: Use case
The identified use case is the comparison of different materials’ GWP, which means that several processes are needed beforehand
First, the “claim” relies on:
-	The geometry of the BIM model
-	Materials assigned to the objects and elements
-	The lifespan of the objects and elements
-	Emission factors assigned for each material
-	The material properties
  
Further, to use this comparison tool, several subordinate tools are required. 
-	First, the material quantities must be calculated. 
-	Second, it needs to be checked that each material is linked to a valid LCA dataset. This will be done by input from the user of the tool. 
-	Last, the resulting quantities and emission factors can be aggregated to calculate the environmental impact. 
Based on the aforementioned requirements, the required BIM purposes are primarily to collect geometry data from the BIM model, relating to *gather*, *generate*, and *analyze*. 
The tool should be used in the early planning and design stages for evaluating alternative materials for the building components.

Ideally, the tool can be applied in close collaboration with the structural team in the future, as it supports the selection of the most environmentally friendly materials for the structural model, which often represents a major share of the building’s total emissions 


## A2d: Scope the use case
Within the whole use case, two steps have been identified as needing a new script/tool:. 
-	The first is _**quantify masses of materials**_, where an automated script could extract volumes and convert them into material masses based on density values. 
-	The second is _**assign layer a predefined generic material from Table 7 (BR18) by inputting the "Sorterings ID"**_, which is currently a manual process and would benefit from a function that automatically links BIM materials directly to corresponding EPD datasets.
  
**These two steps have been highlighted in red in the BPMN diagram (file .SVG).**

![Diagram of process](IMG/Group%2032.svg)

## A2e: Tool idea
Our tool idea is an OpenBIM script built with ifcOpenShell in Python that can automatically extract material quantities from the BIM model and map these elements to the corresponding EPD datasets manually by user input. 
The business value of the tool is that it reduces the time and errors associated with manual quantity take-offs, thereby making the, for now, manual EPD mapping easier and more reliable.
The societal value of this tool is that it promotes sustainable building design by simplifying the process of obtaining an early estimate of the GWP of external walls. 

## A2f: Information requirements
The data required from the BIM model include the dimensions of the building elements: volume, area, and thickness, which will be extracted via:
-	ifcElementQuantity
  
This data will be used for calculating the material masses, and afterward will be linked manually by the user to the generic GWP data in Table 7 (BR18). For the specific material masses, data will be extracted via: 
-	ifcMaterial
-	ifcMaterialLayer
-	ifcMaterialLayerSet
-	ifcMaterialProfile
-	ifcMaterialList
-	ifcMaterialConstituentSet
-	Table 7 from BR18 (outside the model)
  
Resulting in  converting the BIM-derived quantities into the appropriate units (regarding Table 7) for calculating the GWP of the different materials

## A2g: Identify appropriate software license
The tool will be published in a public repository on GitHub, as we hope that others will learn from our tool and develop it further. 
Therefore, we plan to release our tool under the GNU General Public License v3.0 (license keyword: GPL-3.0), as the Advanced BIM course beforehand has decided on this software. The GPL-3.0 is a copyleft software license, which we think is a good approach for further open development of our tool.

