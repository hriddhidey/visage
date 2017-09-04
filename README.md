# Visage
Add virtual makeup to a picture of a face.

<table>
<tr>
<td> <img height='300' text='Before' alt="Plain human face." src="https://user-images.githubusercontent.com/11678594/30020825-ef9a1d74-9182-11e7-93f3-90a218de516b.png"> </td>
<td> <img height='300' text='After' alt="Human face with makeup." src="https://user-images.githubusercontent.com/11678594/30020826-efe4d6ca-9182-11e7-9b59-0324abdf7219.png"> </td>
</tr>
<tr>
<td>Image without makeup.</td>
<td>Image with lipstick and eyeliner.</td>
</tr>
</table>

## Installation _(MacOS)_

* You need **>=Python2.7** and `pip` to get this working. MacOS comes with Python2.7 installed by default. If you don't have `pip`, follow these steps to get it - 	
	* `curl -O https://bootstrap.pypa.io/get-pip.py`
	* `sudo python get-pip.py`
	* `pip install --upgrade pip`

* If you don't have [Homebrew](https://brew.sh/), copy paste the following in your terminal to get it - 
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

* Install **Cmake** - `brew install cmake`

* Install **Boost** and **Boost-Python** - 
	* `brew install boost`
	* `brew install boost-python`

* Kindly consider using a **virtual environment** for development. Check out [**this link**](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to get an idea about how to do that. 

* Install the python module requirements by running - `pip install pyvisage`

## Usage

The module consists of two classes - `Detect Features` and `ApplyMakeup`. You can import both of them from `pyvisage`, and use access their functions to either selectively detect face only, or apply lipstick directly.

Example - 
```
from pyvisage import ApplyMakeup as am

output_file = am.apply_lipstick('input.jpg',170,10,30) // (R,G,B) - (170,10,30)
```
For detailed usage, refer to [Wiki](https://github.com/hriddhidey/visage/wiki).
