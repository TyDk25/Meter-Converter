import PySimpleGUI as gi
from functions import meter_converter

##ENTERS FEET
feet_label = gi.Text("Enter feet: ")
#GETS THE RESPONSE FROM THE USER & RECEIVES KEY FROM
feet_input = gi.Input(key="feet")

inches_label = gi.Text("Enter inches: ")
inches_input = gi.Input(key="inches")

button = gi.Button("Convert")
output_label = gi.Text("", key="output")

window = gi.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output_label]])

print(inches_input)

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = meter_converter(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()