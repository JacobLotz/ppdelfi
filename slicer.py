import numpy as np
from visit_utils import *
from visit import *
import os

def slicer(variables_, n_slice_, zoom_, solution_, autolegend = False, dirname = "zoom"):

    # Clear visit
    DeleteAllPlots()

    # Copy input
    variables = variables_
    zoom = zoom_
    n_slice = n_slice_
    lastsolution = solution_

    first = 1;

    for var in variables:

        OpenDatabase(lastsolution, 0)

        if (var == "mesh"):
            AddPlot("Mesh", "main", 1, 1)


        #Select correct data
        if (var == "u"):
            AddPlot("Pseudocolor", "u", 1, 1)
            PseudocolorAtts = PseudocolorAttributes()
            PseudocolorAtts.min = -1.5
            PseudocolorAtts.max = 1.5
            PseudocolorAtts.minFlag = 1
            PseudocolorAtts.maxFlag = 1
            PseudocolorAtts.colorTableName = "RdBu"
            PseudocolorAtts.invertColorTable = 1
            SetPlotOptions(PseudocolorAtts)

        if (var == "v"):
            AddPlot("Pseudocolor", "v", 1, 1)
            PseudocolorAtts = PseudocolorAttributes()
            PseudocolorAtts.min = -1.2
            PseudocolorAtts.max = 1.2
            PseudocolorAtts.minFlag = 1
            PseudocolorAtts.maxFlag = 1
            PseudocolorAtts.colorTableName = "RdBu"
            PseudocolorAtts.invertColorTable = 1
            SetPlotOptions(PseudocolorAtts)
        
        if (var == "w"):
            AddPlot("Pseudocolor", "w", 1, 1)
            PseudocolorAtts = PseudocolorAttributes()
            #PseudocolorAtts.min = -0.1
            #PseudocolorAtts.max = -0.1
            #PseudocolorAtts.minFlag = 1
            #PseudocolorAtts.maxFlag = 1
            PseudocolorAtts.colorTableName = "viridis_light"
            PseudocolorAtts.invertColorTable = 1
            SetPlotOptions(PseudocolorAtts)

        if (var == "p"):
            AddPlot("Pseudocolor", "p", 1, 1)
            PseudocolorAtts = PseudocolorAttributes()
            #PseudocolorAtts.min = -1.7
            #PseudocolorAtts.max = 1.7
            PseudocolorAtts.minFlag = 1
            PseudocolorAtts.maxFlag = 1
            PseudocolorAtts.colorTableName = "RdBu"
            PseudocolorAtts.invertColorTable = 1
            SetPlotOptions(PseudocolorAtts)

        if (var == "vorticity"):
            AddPlot("Pseudocolor", "vorticity", 1, 1)
            PseudocolorAtts = PseudocolorAttributes()
            PseudocolorAtts.min = -2
            PseudocolorAtts.max = 2
            PseudocolorAtts.minFlag = 1
            PseudocolorAtts.maxFlag = 1
            PseudocolorAtts.colorTableName = "RdBu"
            PseudocolorAtts.invertColorTable = 1
            SetPlotOptions(PseudocolorAtts)

        # 3D plot layout
        AnnotationAtts = AnnotationAttributes()
        AnnotationAtts.axes3D.visible = 0
        AnnotationAtts.axes2D.visible = 0
        AnnotationAtts.userInfoFlag = 0
        AnnotationAtts.databaseInfoFlag = 0
        AnnotationAtts.legendInfoFlag = 1
        AnnotationAtts.backgroundColor = (160, 160, 160, 255)
        AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
        SetAnnotationAttributes(AnnotationAtts)

        # Create window object
        SaveWindowAtts = SaveWindowAttributes()
        SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
        SaveWindowAtts.width = 1920 #720
        SaveWindowAtts.height = 1080#720
        SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint;#720
        SaveWindowAtts.progressive = 1
        SetSaveWindowAttributes(SaveWindowAtts)

        # Draw 3D plot to extract data and slice through
        DrawPlots()

        # Find min and max of plot
        if autolegend:
            Query("Max")
            val1 = GetQueryOutputValue()

            Query("Min")
            val2 = GetQueryOutputValue()

            if abs(val1)>abs(val2):
                val = abs(val1)
            else:
                val = abs(val2)

            PseudocolorAtts.min = -val
            PseudocolorAtts.max = val
            SetPlotOptions(PseudocolorAtts)

        

        #Get range of data such that visit knows over which range it has to loop
        SpatialExtends = Query("SpatialExtents", use_actual_data=0)
        # Convert string to floats
        SpatialExtends = SpatialExtends.split("(")[1].split(")")[0].split(", ")
        SpatialExtends = [i.replace(",", ".") for i in SpatialExtends]
        SpatialExtends = [float(i) for i in SpatialExtends]
        zmin = SpatialExtends[-2]
        zmax = SpatialExtends[-1]-0.0001

        if zoom:
            # 2D view layout for slices
            View2DAtts = View2DAttributes()
            #View2DAtts.windowCoords = (-1, 3, -2.0, 2)
            View2DAtts.windowCoords = (-1.6, 8, -2.7, 2.7)
            View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
            View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
            View2DAtts.windowValid = 1
            SetView2D(View2DAtts)

        # Create slicer operator object
        AddOperator("Slice", 1)
        SliceAtts = SliceAttributes()
        SliceAtts.originType = SliceAtts.Point  # Point, Intercept, Percent, Zone, Node
        #SliceAtts.originPoint = (0, 0, zs[0])
        SliceAtts.axisType = SliceAtts.ZAxis  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
        #SliceAtts.project2d = 1
        SliceAtts.meshName = "main"
        SetOperatorOptions(SliceAtts, -1, 1)

        if(first == 1):
            #first = 0

            # Annotation object to show zcoordinate
            zcoor = CreateAnnotationObject("Text2D")
            zcoor.position = (0.05, 0.95)
            zcoor.height = 0.02
            zcoor.fontBold = 0

    
    
        # Create array of coordinates to slice over
        zs = np.linspace(zmin, zmax, n_slice)
        zs = zs[:-1]
    
    
        # Create directory to save slices in
        savedir = "slices-"+dirname+"-" + var
        if not os.path.exists(savedir):
            os.makedirs(savedir)
    
    

        # Actual slicing for all slicing points
        for z in zs:
        
            #Update slice location
            SliceAtts.originPoint = (0, 0, z)
            SetOperatorOptions(SliceAtts, -1, 1)

            #Update z coordinate text in plot
            zcoor.text = "t = " + "{:.3f}".format(z)

            # Draw and save plot
            DrawPlots()
            SaveWindowAtts.fileName = savedir + "/"
            SetSaveWindowAttributes(SaveWindowAtts)
            name = SaveWindow()
            print("name = %s" % name)
    
        zcoor.text = ""

        # Delete everything
        ClearAllWindows()
    
        RemoveAllOperators()
        DeleteAllPlots()
        #ResetView()