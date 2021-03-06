import adsk.core
import adsk.fusion
import adsk.cam

# Import the entire apper package
import apper

# Alternatively you can import a specific function or class
from apper import AppObjects

import math


# Class for a Fusion 360 Command
# Place your program logic here
# Delete the line that says 'pass' for any method you want to use
class PointsToJointOrigins(apper.Fusion360CommandBase):

    # Run whenever a user makes any change to a value or selection in the addin UI
    # Commands in here will be run through the Fusion processor and changes will be reflected in  Fusion graphics area
    def on_preview(self, command: adsk.core.Command, inputs: adsk.core.CommandInputs, args, input_values):
        pass

    # Run after the command is finished.
    # Can be used to launch another command automatically or do other clean up.
    def on_destroy(self, command: adsk.core.Command, inputs: adsk.core.CommandInputs, reason, input_values):
        pass

    # Run when any input is changed.
    # Can be used to check a value and then update the add-in UI accordingly
    def on_input_changed(self, command: adsk.core.Command, inputs: adsk.core.CommandInputs, changed_input, input_values):
        pass

    # Run when the user presses OK
    # This is typically where your main program logic would go
    def on_execute(self, command: adsk.core.Command, inputs: adsk.core.CommandInputs, args, input_values):
        app = adsk.core.Application.get()
        ui = app.userInterface
 
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        vi = adsk.core.ValueInput
        
        SelectionInput = input_values['selection_input_id']
        for point in SelectionInput:
            comp = point.parentSketch.parentComponent
            geo = adsk.fusion.JointGeometry.createByPoint(point)
            jointOrigin = comp.jointOrigins.createInput(geo)
            comp.jointOrigins.add(jointOrigin)
        

    # Run when the user selects your command icon from the Fusion 360 UI
    # Typically used to create and display a command dialog box
    def on_create(self, command: adsk.core.Command, inputs: adsk.core.CommandInputs):

        SelectionInput = inputs.addSelectionInput('selection_input_id', 'Points', 'Select sketch points to place the Joint Origins')
        SelectionInput.setSelectionLimits(1, 0)
        SelectionInput.addSelectionFilter('SketchPoints')

