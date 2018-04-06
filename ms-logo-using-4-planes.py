#!/usr/bin/env python
 
# This simple example shows how to do basic rendering and pipeline
# creation.

'''
This example creates a Microsoft logo but with four different planes seaparated by a small distance.
Working.


'''

import vtk
# The colors module defines various useful colors.
from vtk.util.colors import tomato
 
# This creates a polygonal cube model.

cube = vtk.vtkPlaneSource()
cubeMapper = vtk.vtkOpenGLPolyDataMapper()
cubeMapper.SetInputConnection(cube.GetOutputPort())
firstactor = vtk.vtkActor()
firstactor.SetMapper(cubeMapper)
firstactor.GetProperty().SetColor(tomato)
firstactor.SetPosition(1.05, 0, 0)


plane = vtk.vtkPlaneSource()
planeMapper = vtk.vtkOpenGLPolyDataMapper()
planeMapper.SetInputConnection(plane.GetOutputPort())
secondactor = vtk.vtkActor()
secondactor.SetMapper(planeMapper)
secondactor.GetProperty().SetColor(tomato)
secondactor.SetPosition(0,0,0)


plane2 = vtk.vtkPlaneSource()
planeMapper2 = vtk.vtkOpenGLPolyDataMapper()
planeMapper2.SetInputConnection(plane.GetOutputPort())
thirdactor = vtk.vtkActor()
thirdactor.SetMapper(planeMapper2)
thirdactor.GetProperty().SetColor(tomato)
thirdactor.SetPosition(0,1.05,0)

plane3 = vtk.vtkPlaneSource()
planeMapper3 = vtk.vtkOpenGLPolyDataMapper()
planeMapper3.SetInputConnection(plane.GetOutputPort())
fourthactor = vtk.vtkActor()
fourthactor.SetMapper(planeMapper3)
fourthactor.GetProperty().SetColor(tomato)
fourthactor.SetPosition(1.05,1.05,0)

#vec3(0.486, 0.733, 0.0) Green
#vec3(0.0, 0.631, 0.945) Blue
#vec3(0.964, 0.325, 0.078) Red
#vec3(1.0, 0.733, 0.0) Yellow


cubeMapper.AddShaderReplacement(
    vtk.vtkShader.Fragment,  # in the fragment shader
    "//VTK::Normal::Impl", # replace the normal block
    True, # before the standard replacements
    "//VTK::Normal::Impl\n" # we still want the default calc
    "  diffuseColor = vec3(1.0, 0.733, 0.0);\n", #but we add this
    False # only do it once
)



planeMapper.AddShaderReplacement(
    vtk.vtkShader.Fragment,  # in the fragment shader
    "//VTK::Normal::Impl", # replace the normal block
    True, # before the standard replacements
    "//VTK::Normal::Impl\n" # we still want the default calc
    "  diffuseColor = vec3(0.0, 0.631, 0.945);\n", #but we add this
    False # only do it once
)


planeMapper2.AddShaderReplacement(
    vtk.vtkShader.Fragment,  # in the fragment shader
    "//VTK::Normal::Impl", # replace the normal block
    True, # before the standard replacements
    "//VTK::Normal::Impl\n" # we still want the default calc
    "  diffuseColor = vec3(0.964, 0.325, 0.078);\n", #but we add this
    False # only do it once
)


# now modify the fragment shader
planeMapper3.AddShaderReplacement(
    vtk.vtkShader.Fragment,  # in the fragment shader
    "//VTK::Normal::Impl", # replace the normal block
    True, # before the standard replacements
    "//VTK::Normal::Impl\n" # we still want the default calc
    "  diffuseColor = vec3(0.486, 0.733, 0.0);\n", #but we add this
    False # only do it once
)

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
vtkRenderWindowInteractor = vtk.vtkRenderWindowInteractor()
vtkRenderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(firstactor)
renderer.AddActor(secondactor)
renderer.AddActor(thirdactor)
renderer.AddActor(fourthactor)

renderer.SetBackground(1,1,1)
renderWindow.SetSize(600, 600)
renderWindow.Render()
vtkRenderWindowInteractor.Start()
