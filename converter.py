import PySimpleGUI as gi
from functions import meter_converter

gi.theme("Black")
##ENTERS FEET
feet_label = gi.Text("Enter feet: ")
#GETS THE RESPONSE FROM THE USER & RECEIVES KEY FROM
feet_input = gi.Input(key="feet")

inches_label = gi.Text("Enter inches: ")
inches_input = gi.Input(key="inches")

button = gi.Button("Convert")
output_label = gi.Text("", key="output")
exit_button = gi.Button("Exit")


window = gi.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output_label,exit_button]])

print(inches_input)

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
    try:
            feet = float(values["feet"])
            inches = float(values["inches"])
            result = meter_converter(feet, inches)
            window["output"].update(value=f"{result} m", text_color="white")
    except ValueError:
        gi.popup("Please enter two numbers", font=("Helvetica",15))
  

  


window.close()