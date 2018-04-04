#!/usr/bin/env python
 
# This simple example shows how to do basic rendering and pipeline
# creation.
 
import vtk
# The colors module defines various useful colors.
from vtk.util.colors import tomato
 
# This creates a polygonal plane model.
plane = vtk.vtkPlaneSource()
 
# The mapper is responsible for pushing the geometry into the graphics
# library. It may also do color mapping, if scalars or other
# attributes are defined.
planeMapper = vtk.vtkOpenGLPolyDataMapper()
planeMapper.SetInputConnection(plane.GetOutputPort())



# METHOD #1
# Modify the shader to color based on model normal
# To do this we have to modify the vertex shader
# to pass the normal in model coordinates
# through to the fragment shader. By default the normal
# is converted to View coordinates and then passed on.
# We keep that, but add a varying for the original normal.
# Then we modify the fragment shader to set the diffuse color
# based on that normal. First lets modify the vertex
# shader
planeMapper.AddShaderReplacement(
    vtk.vtkShader.Vertex,
    "//VTK::Normal::Dec", # replace the normal block
    True, # before the standard replacements
    "//VTK::Normal::Dec\n" # we still want the default
    "  varying vec3 temp;\n"
    #"  vec4 gl_Position;\n"
    "  varying vec3 myNormalMCVSOutput;\n", #but we add this
    False # only do it once
)
planeMapper.AddShaderReplacement(
    vtk.vtkShader.Vertex,
    "//VTK::Normal::Impl", # replace the normal block
    True, # before the standard replacements
    "//VTK::Normal::Impl\n" # we still want the default
    "  myNormalMCVSOutput = vec3(gl_Position.x,gl_Position.y,0.0);\n", #but we add this
    False # only do it once
)
# now modify the fragment shader
planeMapper.AddShaderReplacement(
    vtk.vtkShader.Fragment,  # in the fragment shader
    "//VTK::Normal::Dec", # replace the normal block
    True, # before the standard replacements
    "//VTK::Normal::Dec\n" # we still want the default
    "  varying vec3 myNormalMCVSOutput;\n", #but we add this
    False # only do it once
)
planeMapper.AddShaderReplacement(
    vtk.vtkShader.Fragment,  # in the fragment shader
    "//VTK::Normal::Impl", # replace the normal block
    True, # before the standard replacements
    "//VTK::Normal::Impl\n" # we still want the default calc
    "  diffuseColor = abs(myNormalMCVSOutput);\n", #but we add this
    False # only do it once
)




 
# The actor is a grouping mechanism: besides the geometry (mapper), it
# also has a property, transformation matrix, and/or texture map.
# Here we set its color and rotate it -22.5 degrees.
planeActor = vtk.vtkActor()
planeActor.SetMapper(planeMapper)
planeActor.GetProperty().SetColor(tomato)
planeActor.RotateX(30.0)
planeActor.RotateY(-45.0)
 
# Create the graphics structure. The renderer renders into the render
# window. The render window interactor captures mouse events and will
# perform appropriate camera or actor manipulation depending on the
# nature of the events.
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
 
# Add the actors to the renderer, set the background and size
ren.AddActor(planeActor)
ren.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(200, 200)
 
# This allows the interactor to initalize itself. It has to be
# called before an event loop.
iren.Initialize()
 
# We'll zoom in a little by accessing the camera and invoking a "Zoom"
# method on it.
ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)
renWin.Render()
 
# Start the event loop.
iren.Start()