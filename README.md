# Data Entry Application

This is a modern and interactive data entry application built using Python and Tkinter. The application allows users to input their first name, last name, select their age using a calendar, enter comments, and select their gender. The data can then be submitted to an Excel sheet. The application features a clear and exit button, as well as responsive UI elements.

## Features

- First and Last Name Entry Fields
- Calendar to Select Age (with default to current date and toggle functionality)
- Comment Box
- Gender Radio Buttons (Male, Female, Other)
- Submit Button (saves data to an Excel sheet)
- Clear Button (resets all fields)
- Exit Button (closes the application)
- Modern and responsive UI with logos for each input field

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- `tkcalendar` package
- `ttkthemes` package
- `openpyxl` package
- `Pillow` package

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/data-entry-app.git
   cd data-entry-app

## Usage

1. Run the application:
    python app.py

2. Input Data:
- Enter your first name and last name.
- Select your age using the calendar widget.
- Enter any comments.
- Select your gender.

3. Submit Data:
- Click the Submit button to save the data to the Excel sheet.
- Click the Clear button to reset all input fields.
- Click the Exit button to close the application.

## Application Layout

- First and Last Name: Text entry fields for entering first and last names.
- Age: Calendar widget for selecting the date of birth (toggles on button click).
- Comment: A text box for entering any additional comments.
- Gender: Radio buttons for selecting gender (Male, Female, Other).
- Buttons: Submit, Clear, and Exit buttons to handle respective operations.

## File Structure

data-entry-app/
├── app.py
├── data.xlsx
├── images/
│   ├── name.png
│   ├── name_family.png
│   ├── date.png
│   ├── comment.png
│   └── gender-equality.png
└── README.md

## Contributing

1. Fork the repository:
Click the "Fork" button on the upper right corner of the repository page.

2. Clone your fork:
git clone https://github.com/your-username/data-entry-app.git
cd data-entry-app

3. Create a branch:
git checkout -b feature-branch

4. Make your changes and commit them:
git commit -m "Describe your changes"

5. Push to your fork:
git push origin feature-branch

6. Create a pull request:
Go to the original repository and click "New Pull Request".

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's de-facto standard GUI package.
* [tkcalendar](https://pypi.org/project/tkcalendar/) - Calendar widget for Tkinter.
* [ttkthemes](https://github.com/TkinterEP/ttkthemes) - Themed Tkinter widgets.
* [openpyxl](https://openpyxl.readthedocs.io/en/stable/) - Library for Excel file manipulation.
* [Pillow](https://python-pillow.org/) - Python Imaging Library.

Feel free to open issues or submit pull requests for any improvements or bugs you encounter. Happy coding!
You can save this content into a file named `README.md` in your project directory.
