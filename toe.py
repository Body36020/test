import tkinter as tk

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(ent_temperature.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius = round(celsius, 2)
        lbl_result.config(text=f"{celsius} \N{DEGREE CELSIUS}")
    except ValueError:
        lbl_result.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create a frame to hold the Fahrenheit entry widget and label
frm_entry = tk.Frame(master=window)

# Create an entry widget for Fahrenheit
ent_temperature = tk.Entry(master=frm_entry, width=10)

# Create a label for the degree symbol and "°F"
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Use the grid() geometry manager to arrange the entry and label widgets
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create a button for conversion
btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)

# Create a label for displaying the result in Celsius
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Use the grid() geometry manager to arrange the widgets
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Start the application
window.mainloop()
