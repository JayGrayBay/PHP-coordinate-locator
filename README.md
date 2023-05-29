# PHP-coordinate-locator
locates and writes php &amp; css code to add content to your website

**PyQt Website Designer**

This project is a Python application that uses PyQt5 to create a graphical user interface. When the user clicks on a spot within the window, the program generates a PHP file and a CSS file that, when displayed in a web browser, will show the text "Here" at the clicked coordinates.

**Installation**

This project requires Python 3 and PyQt5. To install PyQt5, you can use pip:

pip install PyQt5

**Usage**

To use the program, simply run the 

python main.py


A window will appear. Click anywhere within the window to generate the PHP and CSS files.

The generated files will be saved in the output directory. The filenames will include a timestamp based on the date and time of the click. This timestamp is formatted as "Year-Month-Day_Hour-Minute-Second".

To view the output, host the PHP file on a web server and open it in a web browser. You will see the text "Here" at the spot you clicked. The corresponding CSS file will contain the styling to place the text at the clicked coordinates.

Highlight Animation
The program includes a feature where a yellow highlight will appear at the clicked location within the window. This highlight will last for 3 seconds.
