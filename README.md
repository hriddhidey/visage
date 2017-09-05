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

* Install **Cmake, Boost, and Boost-Python** - `brew install cmake boost boost-python`

* Kindly consider using a **virtual environment** for development. Check out [**this link**](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for detailed explanations on how to do that. Follow these steps to get up and running quickly -
```
pip install virtualenv
virtualenv my_project
cd my_project && source bin/activate
```
* Install the python module requirements by running - `pip install pyvisage`
>_Note_: If you are not using `virtualenv`, you might need `sudo` to make this work.

## Usage

The module is named `visage`, and consists of two classes - `Detect Features` and `ApplyMakeup`. You can import, and access their functions to either selectively detect face only, or apply lipstick directly. Kindly read the [Wiki](https://github.com/hriddhidey/visage/wiki) for detailed usage.

Example - 
>_Note_: You will need a working internet connection the first time you run this, as it will download a predictor file to your project folder the first time.
```
from visage import ApplyMakeup
AM = ApplyMakeup()
output_file = AM.apply_lipstick('input.jpg',170,10,30) // (R,G,B) - (170,10,30)
```
