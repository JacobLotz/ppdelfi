import numpy as np
from visit_utils import *
from visit import *
import os

from math import log10, floor
def round_sig(x, sig=2):
  return round(x, sig-int(floor(log10(abs(x))))-1)


def slicer(variables_, frame_rate_, zoom_, solution_, autolegend = False, dirname = "zoom"):

    # Clear visit
    DeleteAllPlots()

    # Copy input
    variables = variables_
    zoom = zoom_
    frame_rate = frame_rate_
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
            PseudocolorAtts.min = -0.00052
            PseudocolorAtts.max = 0.00052
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
            autolegend = True;
            AddPlot("Pseudocolor", "p", 1, 1)
            PseudocolorAtts = PseudocolorAttributes()
            #PseudocolorAtts.min = -1.7
            #PseudocolorAtts.max = 1.7
            PseudocolorAtts.minFlag = 1
            PseudocolorAtts.maxFlag = 1
            PseudocolorAtts.colorTableName = "RdBu"
            PseudocolorAtts.invertColorTable = 1
            SetPlotOptions(PseudocolorAtts)

        if (var == "vmag"):
            AddPlot("Pseudocolor", "vmag", 1, 1)
            PseudocolorAtts = PseudocolorAttributes()
            PseudocolorAtts.min = 0
            PseudocolorAtts.max = 2.6
            PseudocolorAtts.minFlag = 1
            PseudocolorAtts.maxFlag = 1
            PseudocolorAtts.colorTableName = "viridis_light"
            PseudocolorAtts.invertColorTable = 0
            SetPlotOptions(PseudocolorAtts)
            autolegend = True;

        if (var == "vmagvec"):
            autolegend = True;
            AddPlot("Vector", "vvec", 1, 1)
            VectorAtts = VectorAttributes()
            VectorAtts.nVectors = 25000/(9)
            VectorAtts.colorByMagnitude = 0
            VectorAtts.scale = 0.02*(3)
            VectorAtts.glyphLocation = 1
            SetPlotOptions(VectorAtts)

            AddPlot("Pseudocolor", "vmag", 1, 1)
            PseudocolorAtts = PseudocolorAttributes()
            PseudocolorAtts.min = 0
            PseudocolorAtts.max = 2.5
            PseudocolorAtts.minFlag = 1
            PseudocolorAtts.maxFlag = 1
            PseudocolorAtts.colorTableName = "viridis_light"
            PseudocolorAtts.invertColorTable = 0
            SetPlotOptions(PseudocolorAtts)

        if (var == "vorticity"):
            #autolegend = False;
            AddPlot("Pseudocolor", "vorticity", 1, 1)
            PseudocolorAtts = PseudocolorAttributes()
            PseudocolorAtts.min = -20
            PseudocolorAtts.max = 20
            PseudocolorAtts.minFlag = 1
            PseudocolorAtts.maxFlag = 1
            PseudocolorAtts.colorTableName = "RdBu"
            PseudocolorAtts.invertColorTable = 1
            SetPlotOptions(PseudocolorAtts)


        if (var == "vorticityvec"):
            autolegend = False;
            AddPlot("Vector", "vvec2", 1, 1)
            VectorAtts = VectorAttributes()
            VectorAtts.nVectors = 25000/(4)
            VectorAtts.colorByMagnitude = 0
            #VectorAtts.scaleByMagnitude = 1;
            VectorAtts.scale = 0.02*(2*2);
            #VectorAtts.autoScale = 1;
            VectorAtts.scaleByMagnitude = 1;
            VectorAtts.glyphLocation = 1
            SetPlotOptions(VectorAtts)

            AddPlot("Pseudocolor", "vorticity", 1, 1)
            PseudocolorAtts = PseudocolorAttributes()
            PseudocolorAtts.min = -75
            PseudocolorAtts.max = 75
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

            if (var == "vorticityvec"):
                val = val/(4*3)

            val = round_sig(val, 2)

            PseudocolorAtts.min = -val
            PseudocolorAtts.max = val

            if (var == "vmag" or var == "vmagvec"):
                PseudocolorAtts.min = 0;
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
            View2DAtts.windowCoords = (-0.5, 1.5, -0.75, 1.25)
            #View2DAtts.windowCoords = (-1.6, 8, -2.7, 2.7)
            #View2DAtts.windowCoords = (-1.2, 3.0, -0.8625, 1.5)
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
        n_slice = int(frame_rate*zmax)
        n_slice = 41
        zs = np.linspace(zmin, zmax, n_slice)
        zs = zs[:-1]

        print(zs)

        #zs = [0.0, 0.15, 0.26, 0.30, 0.50, 0.58, 0.69, 0.88]*zmax
        zs = [0, 0.6, 1.04, 1.2, 2, 2.32, 2.76, 3.52]


        zs = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]



    
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
            zcoor.text = "t/T = " + "{:.3f}".format(z/zmax)

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