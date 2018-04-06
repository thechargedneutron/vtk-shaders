#!/usr/bin/env python
 
# This simple example shows how to do basic rendering and pipeline
# creation.

'''
Testing more than one actos in a single renderer.
Working

'''
 
import vtk
# The colors module defines various useful colors.
from vtk.util.colors import tomato
 
# This creates a polygonal cube model.

cube = vtk.vtkCubeSource()
cubeMapper = vtk.vtkOpenGLPolyDataMapper()
cubeMapper.SetInputConnection(cube.GetOutputPort())
firstactor = vtk.vtkActor()
firstactor.SetMapper(cubeMapper)
firstactor.GetProperty().SetColor(tomato)
firstactor.SetPosition(1.2, 0, 0)


plane = vtk.vtkCubeSource()
planeMapper = vtk.vtkOpenGLPolyDataMapper()
planeMapper.SetInputConnection(plane.GetOutputPort())
secondactor = vtk.vtkActor()
secondactor.SetMapper(planeMapper)
secondactor.GetProperty().SetColor(tomato)
secondactor.SetPosition(0,0,0)


renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
vtkRenderWindowInteractor = vtk.vtkRenderWindowInteractor()
vtkRenderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(firstactor)
renderer.AddActor(secondactor)

renderer.SetBackground(1,1,1)
renderWindow.SetSize(600, 600)
renderWindow.Render()
vtkRenderWindowInteractor.Start()

'''


 
# The actor is a grouping mechanism: besides the geometry (mapper), it
# also has a property, transformation matrix, and/or texture map.
# Here we set its color and rotate it -22.5 degrees.
cubeActor = vtk.vtkActor()
cubeActor.SetMapper(cubeMapper)
cubeActor.GetProperty().SetColor(tomato)
cubeActor.RotateX(30.0)
cubeActor.RotateY(-45.0)
 
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
ren.AddActor(cubeActor)
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
'''