# Dictionaries used to change sentences and calculations
temperature_conversions = { '1': { 'menu_option' : "Celsius to Fahrenheit",
                                    'original_unit' : "Celsius",
                                    'requested_unit' : "Fahrenheit",
                                    'calculation' : lambda x :(x * 9/5) + 32,
                                    'old_abbreviation' : '°C',
                                    'new_abbreviation' : '°F'
                            },
                            '2' : {'menu_option' : "Fahrenheit to Celsius",
                                    'original_unit' : "Fahrenheit",
                                    'requested_unit' : "Celsius",
                                    'calculation' : lambda x :(x - 32) * 5/9,
                                    'old_abbreviation' : '°F',
                                    'new_abbreviation' : '°C'
                            },
                            '3' : {'menu_option' : "Celsius to Kelvin",
                                    'original_unit' : "Celsius",
                                    'requested_unit' : "Kelvin",
                                    'calculation' : lambda x :(x - 273.15),
                                    'old_abbreviation' : '°C',
                                    'new_abbreviation' : 'K'
                            },
                            '4' : {'menu_option' : "Kelvin to Celsius",
                                    'original_unit' : "Kelvin",
                                    'requested_unit' : "Celsius",
                                    'calculation' : lambda x :(x + 273.15),
                                    'old_abbreviation' : 'K',
                                    'new_abbreviation' : '°C'
                            },
                            '5' : {'menu_option' : "Fahrenheit to Kelvin",
                                    'original_unit' : "Fahrenheit",
                                    'requested_unit' : "Kelvin",
                                    'calculation' : lambda x :(x - 32) * 5/9 + 273.15,
                                    'old_abbreviation' : '°F',
                                    'new_abbreviation' : 'K'
                            },
                            '6' : {'menu_option' : "Kelvin to Fahrenheit",
                                    'original_unit' : "Kelvin",
                                    'requested_unit' : "Fahrenheit",
                                    'calculation' : lambda x :(x - 273.15) * 9/5 + 32 ,
                                    'old_abbreviation' : 'K',
                                    'new_abbreviation' : '°F'
                            },
                            'M' : {'menu_option' : "Main Menu"
                            },
                            'E' : {'menu_option' : "Exit"
                            },
}


length_conversions = { '1': { 'menu_option' : "Meters to Feet",
                                    'original_unit' : "Meters",
                                    'requested_unit' : "Feet",
                                    'calculation' : lambda x :x * 3.28084,
                                    'old_abbreviation' : "m",
                                    'new_abbreviation' : "ft"
                            },
                            '2' : {'menu_option' : "Feet to Meters",
                                    'original_unit' : "Feet",
                                    'requested_unit' : "Meters",
                                    'calculation' : lambda x :x / 3.28084,
                                    'old_abbreviation' : "ft",
                                    'new_abbreviation' : "m"
                            },
                            '3' : {'menu_option' : "Inches to Centimeters",
                                    'original_unit' : "Inches",
                                    'requested_unit' : "Centimeters",
                                    'calculation' : lambda x :x * 2.54,
                                    'old_abbreviation' : "in",
                                    'new_abbreviation' : "cm"
                            },
                            '4' : {'menu_option' : "Centimeters to Inches",
                                    'original_unit' : "Centimeters",
                                    'requested_unit' : "Inches",
                                    'calculation' : lambda x :x / 2.54,
                                    'old_abbreviation' : "cm",
                                    'new_abbreviation' : "in"
                            },
                            '5' : {'menu_option' : "Millimeters to Inches",
                                    'original_unit' : "Millimeters",
                                    'requested_unit' : "Inches",
                                    'calculation' : lambda x :x / 25.4,
                                    'old_abbreviation' : "mm",
                                    'new_abbreviation' : "in"
                            },
                            '6' : {'menu_option' : "Inches to Millimeters",
                                    'original_unit' : "Inches",
                                    'requested_unit' : "Millimeters",
                                    'calculation' : lambda x :x * 25.4,
                                    'old_abbreviation' : "in",
                                    'new_abbreviation' : "mm"
                            },
                            'M' : {'menu_option' : "Main Menu"
                            },
                            'E' : {'menu_option' : "Exit"
                            },
}


area_conversions = { '1': { 'menu_option' : "Square Meters to Square Feet",
                                    'original_unit' : "Square Meters",
                                    'requested_unit' : "Square Feet",
                                    'calculation' : lambda x :x * 10.764,
                                    'old_abbreviation' : "m²",
                                    'new_abbreviation' : "ft²"
                            },
                            '2' : {'menu_option' : "Square Feet to Square Meters",
                                    'original_unit' : "Square Feet",
                                    'requested_unit' : "Square Meters",
                                    'calculation' : lambda x :x / 10.764,
                                    'old_abbreviation' : "ft²",
                                    'new_abbreviation' : "m²"
                            },
                            '3' : {'menu_option' : "Square Inches to Square Centimeters",
                                    'original_unit' : "Square Inches",
                                    'requested_unit' : "Square Centimeters",
                                    'calculation' : lambda x :x * 6.4516,
                                    'old_abbreviation' : "in²",
                                    'new_abbreviation' : "cm²"
                            },
                            '4' : {'menu_option' : "Square Centimeters to Square Inches",
                                    'original_unit' : "Square Centimeters",
                                    'requested_unit' : "Square Inches",
                                    'calculation' : lambda x :x / 6.4516,
                                    'old_abbreviation' : "cm²",
                                    'new_abbreviation' : "in²"
                            },
                            '5' : {'menu_option' : "Square Millimeters to Square Inches",
                                    'original_unit' : "Square Millimeters",
                                    'requested_unit' : "Square Inches",
                                    'calculation' : lambda x :x / 645.2,
                                    'old_abbreviation' : "mm²",
                                    'new_abbreviation' : "in²"
                            },
                            '6' : {'menu_option' : "Square Inches to Square Millimeters",
                                    'original_unit' : "Square Inches",
                                    'requested_unit' : "Square Millimeters",
                                    'calculation' : lambda x :x * 645.2,
                                    'old_abbreviation' : "in²",
                                    'new_abbreviation' : "mm²"
                            },
                            'M' : {'menu_option' : "Main Menu"
                            },
                            'E' : {'menu_option' : "Exit"
                            },
}

# Reshape code to represent volume, not length
volume_conversions = { '1': { 'menu_option' : "Meters to Feet",
                                    'original_unit' : "Meters",
                                    'requested_unit' : "Feet",
                                    'calculation' : lambda x :x * 3.28084,
                                    'old_abbreviation' : "m",
                                    'new_abbreviation' : "ft"
                            },
                            '2' : {'menu_option' : "Feet to Meters",
                                    'original_unit' : "Feet",
                                    'requested_unit' : "Meters",
                                    'calculation' : lambda x :x / 3.28084,
                                    'old_abbreviation' : "ft",
                                    'new_abbreviation' : "m"
                            },
                            '3' : {'menu_option' : "Inches to Centimeters",
                                    'original_unit' : "Inches",
                                    'requested_unit' : "Centimeters",
                                    'calculation' : lambda x :x * 2.54,
                                    'old_abbreviation' : "in",
                                    'new_abbreviation' : "cm"
                            },
                            '4' : {'menu_option' : "Centimeters to Inches",
                                    'original_unit' : "Centimeters",
                                    'requested_unit' : "Inches",
                                    'calculation' : lambda x :x / 2.54,
                                    'old_abbreviation' : "cm",
                                    'new_abbreviation' : "in"
                            },
                            '5' : {'menu_option' : "Millimeters to Inches",
                                    'original_unit' : "Millimeters",
                                    'requested_unit' : "Inches",
                                    'calculation' : lambda x :x / 25.4,
                                    'old_abbreviation' : "mm",
                                    'new_abbreviation' : "in"
                            },
                            '6' : {'menu_option' : "Inches to Millimeters",
                                    'original_unit' : "Inches",
                                    'requested_unit' : "Millimeters",
                                    'calculation' : lambda x :x * 25.4,
                                    'old_abbreviation' : "in",
                                    'new_abbreviation' : "mm"
                            },
                            'M' : {'menu_option' : "Main Menu"
                            },
                            'E' : {'menu_option' : "Exit"
                            },
}

# Reshape code to represent weight, not area
weight_conversions = { '1': { 'menu_option' : "Square Meters to Square Feet",
                                    'original_unit' : "Square Meters",
                                    'requested_unit' : "Square Feet",
                                    'calculation' : lambda x :x * 10.764,
                                    'old_abbreviation' : "m²",
                                    'new_abbreviation' : "ft²"
                            },
                            '2' : {'menu_option' : "Square Feet to Square Meters",
                                    'original_unit' : "Square Feet",
                                    'requested_unit' : "Square Meters",
                                    'calculation' : lambda x :x / 10.764,
                                    'old_abbreviation' : "ft²",
                                    'new_abbreviation' : "m²"
                            },
                            '3' : {'menu_option' : "Square Inches to Square Centimeters",
                                    'original_unit' : "Square Inches",
                                    'requested_unit' : "Square Centimeters",
                                    'calculation' : lambda x :x * 6.4516,
                                    'old_abbreviation' : "in²",
                                    'new_abbreviation' : "cm²"
                            },
                            '4' : {'menu_option' : "Square Centimeters to Square Inches",
                                    'original_unit' : "Square Centimeters",
                                    'requested_unit' : "Square Inches",
                                    'calculation' : lambda x :x / 6.4516,
                                    'old_abbreviation' : "cm²",
                                    'new_abbreviation' : "in²"
                            },
                            '5' : {'menu_option' : "Square Millimeters to Square Inches",
                                    'original_unit' : "Square Millimeters",
                                    'requested_unit' : "Square Inches",
                                    'calculation' : lambda x :x / 645.2,
                                    'old_abbreviation' : "mm²",
                                    'new_abbreviation' : "in²"
                            },
                            '6' : {'menu_option' : "Square Inches to Square Millimeters",
                                    'original_unit' : "Square Inches",
                                    'requested_unit' : "Square Millimeters",
                                    'calculation' : lambda x :x * 645.2,
                                    'old_abbreviation' : "in²",
                                    'new_abbreviation' : "mm²"
                            },
                            'M' : {'menu_option' : "Main Menu"
                            },
                            'E' : {'menu_option' : "Exit"
                            },
}
