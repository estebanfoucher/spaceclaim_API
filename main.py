#########################################################################################
############## script for creating Named Selection based on location ####################
#########################################################################################

# center point of inlet is located at -10mm,5mm,-7.5mm
# center point of outlet is located at 15mm,20mm,-7.5mm

from spaceclaim_API import GetRootPart
from spaceclaim_API import NamedSelection
from spaceclaim_API import Selection

part = GetRootPart()
bodies = part.GetAllBodies()

#########################################################################################
######## Approach 2 - using midpoint functionality

##### define list for inlet and outlet center coordinates
inletCoord = [-0.01, 0.005, -0.0075]
outletCoord = [0.015, 0.02, -0.0075]

remFaces = []

##### loop for bodies and its faces to identify face midpoint, compare it with inlet and outlet center coordinates
for body in bodies:
	for face in body.Faces:
		mdPoint = face.MidPoint().Point		
		if inletCoord[0] == mdPoint[0] and inletCoord[1] == mdPoint[1] and inletCoord[2] == mdPoint[2]:
			inletFace = face			
		elif outletCoord[0] == mdPoint[0] and outletCoord[1] == mdPoint[1] and outletCoord[2] == mdPoint[2]:
			outletFace = face
		else:
			remFaces.append(face)

##### Create Named Selections and rename it
##### inlet		
result = NamedSelection.Create(Selection.Create(inletFace), Selection())
result = NamedSelection.Rename("Group1", "inlet")

##### outlet
result = NamedSelection.Create(Selection.Create(outletFace), Selection())
result = NamedSelection.Rename("Group1", "outlet")

##### wall
result = NamedSelection.Create(Selection.Create(remFaces), Selection())
result = NamedSelection.Rename("Group1", "wall")

##### fluid
result = NamedSelection.Create(Selection.Create(bodies[0]), Selection())
result = NamedSelection.Rename("Group1", "fluid")

#########################################################################################