import tkinter
import tkinter.ttk as ttk


def _temp_calcs() -> None:
    """
    Converts a given temperature value from `initial_value` entry widget according
        to the selections made in the two option menus. Celsius, Fahrenheit or Kelvin.
    Note that the round() function is being used for calculations because
        decimal precision is not the goal here.
    Also note that the calculation includes multiplying and dividing by 10000.0 to
        deal with rounding errors.
    """
    try:
        first_string = user_selected_unit.get()  # selected temp unit of first option menu
        second_string = user_selected_unit_2.get()  # selected temp unit of second option menu
        if first_string == 'Celsius':  # if user selects Celsius in first option menu
            if second_string == 'Fahrenheit':  # if user selects Fahrenheit in second option menu
                value = float(initial_value.get())  # convert initial string from entry widget to float
                result_value.set(round((int(value * 9 / 5 * 10000.0) / 10000.0 + 32), 3))
            else:
                value = float(initial_value.get())
                result_value.set(round((int(value * 10000.0) / 10000.0 + 273.15), 3))
        elif first_string == 'Fahrenheit':
            if second_string == 'Celsius':
                value = float(initial_value.get())
                result_value.set(round(int((value - 32) * 10000.0) / 10000.0 * 5 / 9, 3))
            else:
                value = float(initial_value.get())
                result_value.set(round((int((value - 32) * 10000.0) / 10000.0 * (5 / 9) + 273.15), 3))
        else:  # first_string will be kelvin
            if second_string == 'Celsius':
                value = float(initial_value.get())
                result_value.set(round((int(value * 10000.0) / 10000.0 - 273.15), 3))
            else:  # second string will be fahrenheit
                value = float(initial_value.get())
                result_value.set(round((int((value - 273.15) * 10000.0) / 10000.0 * 1.8000 + 32), 3))
    except (TypeError, ValueError):
        pass


if __name__ == '__main__':
    # main window
    main_window = tkinter.Tk()
    main_window.title("Temperature Conversion")
    main_window.minsize(300, 115)  # setting min size of main window
    main_window.maxsize(300, 150)  # setting max size of main window

    # column configure
    main_window.columnconfigure(0, weight=1)
    main_window.columnconfigure(1, weight=1)
    main_window.columnconfigure(2, weight=1)

    # row configure
    main_window.rowconfigure(0, weight=1)
    main_window.rowconfigure(1, weight=1)
    main_window.rowconfigure(2, weight=1)
    main_window.rowconfigure(3, weight=1)

    # text at top of window
    ttk.Label(main_window, text="Enter a value to convert:").grid(column=0, row=0)

    # initial entry and converted entry
    initial_value = tkinter.StringVar()
    initial_entry = ttk.Entry(main_window, textvariable=initial_value).grid(column=0, row=1, sticky='w', padx=5)

    result_value = tkinter.StringVar()
    result_entry = ttk.Entry(main_window, textvariable=result_value).grid(column=1, row=1, sticky='w', padx=5)

    # list of options for option menus
    option_list = ['Celsius', 'Fahrenheit', 'Kelvin']

    # string variables for user selection
    user_selected_unit = tkinter.StringVar()
    user_selected_unit_2 = tkinter.StringVar()

    # master window, variable (stringvar), default option value (option_list[0]), all the options with * in front
    temp_menu_1 = ttk.OptionMenu(main_window, user_selected_unit, option_list[0], *option_list)
    temp_menu_1.grid(column=0, row=2, sticky='w', padx=5, pady=2)

    # second option menu for temp unit selection
    temp_menu_2 = ttk.OptionMenu(main_window, user_selected_unit_2, option_list[1], *option_list)
    temp_menu_2.grid(column=1, row=2, sticky='w', padx=5, pady=2)

    # calculate button
    calc_button = ttk.Button(main_window, text="Convert", command=_temp_calcs)
    calc_button.grid(column=0, row=3, sticky='w', padx=5)

    # # Style
    # # use ttk.(whatever widget).winfo_class() to get the style name to use for Style
    # widget_style = ttk.Style(main_window)
    # widget_style.configure('TButton', font=('Blackadder ITC', 10, 'underline', 'bold'),
    #                        foreground='red', background='blue')
    # widget_style.configure('TMenubutton', font=('Calibri', 10, 'bold'), foreground='black', background='light grey')

    tkinter.mainloop()
