# textformatting_vsct

This is a python package designed to allow for color usage in the VSCode terminal. textformatting_vsct is intended to be relatively simple and easy to use. Its main audience is Python learners who would like to experiment with packages or changing their console output for various projects. Of course all other users are welcome, too!

(textformatting_vsct is a Python package developed by a single person as a learning experience.)

### Features:
- Rich Color Support: Colorize text and backgrounds with RGB and hex color codes.
- Text Styles: Text can be emboldened, italicized, underlined, and more.
- Predefined Colors: Numerous predefined color codes to increase ease of use.
- Specific Color Support: Utilize functions to create specific colors for more precise colorizing.
- Utility Functions: Remove formatting from text, convert between color codes, and more.
- Gradient Text: Create gradient effects for text.

### Installation:
Install textformatting_vsct via pip:
  ```bash
  pip install textformatting_vsct
  ```

Or clone this repository:
  ```bash
  git clone https://github.com/Zentiph/textformatting_vsct
  ```

### Quick Start:
Importing the package:
  ```python
  import textformatting_vsct as tf
  ```

Applying text color, background color, and text styles:
  ```python
  # make sure to use tf.RESET to stop the formatting from bleeding into the next lines
  green_txt = tf.TextColors.GREEN + "This text is green" + tf.RESET
  red_bg_txt = tf.BGColors.RED + "This text has a red bg" + tf.RESET
  bold_txt = tf.Styles.BOLD + "This text is bold" + tf.RESET
  ```

Utilizing functions for specific color outputs:
  ```python
  red_orange_txt = tf.rgb_text(255, 200, 0) + "This text is red-orange" + tf.RESET
  brown_bg_txt = tf.rgb_bg(150, 75, 0) + "This text has a brown bg" + tf.RESET
  ```

Converting between color codes:
  ```python
  >>> hex_color = "ffff00"
  >>> rgb_color = tf.hex_to_rgb(hex_color)
  >>> print(rgb_color)
  [255, 255, 0]
  ```

Applying text gradient:
  ```python
  txt = "A colorful message"
  start_color = [255, 0, 0]
  end_color = [0, 0, 255]
  
  red_to_blue = tf.gradient(txt, start_color, end_color)
  ```

### Usage:
For more information on this module's features, visit the [documentation](TODO:).

### Contributing:
Contributions are currently not welcome. Please be aware that this was made as a learning project by one person, so contributions would take a while to be added. There is a chance contributions will be welcomed in the future.

### License:
textformatting_vsct is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for more details.