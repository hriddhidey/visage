# Visage
Add virtual makeup to a picture of a face.

<table>
<tr>
<td> <img width='300' text='Before' alt="Plain human face." src="https://user-images.githubusercontent.com/11678594/30020825-ef9a1d74-9182-11e7-93f3-90a218de516b.png"> </td>
<td> <img width='300' text='After' alt="Human face with makeup." src="https://user-images.githubusercontent.com/11678594/30020826-efe4d6ca-9182-11e7-9b59-0324abdf7219.png"> </td>
</tr>
<tr>
<td>Image without makeup.</td>
<td>Image with lipstick and eyeliner.</td>
</tr>
</table>

<br />


## Installation 

### _MacOS_

1. You need **>=Python2.7** and `pip` to get this working. MacOS comes with Python2.7 installed by default. If you don't have `pip`, follow these steps to get it - 	
	* `curl -O https://bootstrap.pypa.io/get-pip.py`
	* `sudo python get-pip.py`
	* `pip install --upgrade pip`


2. Install **Cmake, Boost, and Boost-Python** - `brew install cmake boost boost-python`
> If you don't have [Homebrew](https://brew.sh/), copy paste the following in your terminal to get it - 
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

3. See Step 4 - Generic.

<br />

### _Linux_

1. You will need **>=Python2.7** and `pip` to get this working.
Kindly figure out how to get the same for your distribution.

2. You need Cmake, and Boost-Python. To get the same, use `yum` or `apt-get` as you please.
```
sudo yum install cmake boost boost-devel 
```
>*Note:* You will need C++11 compiler for Cmake. CentOS does not come with the same out of the box. Follow [**this link's instructions**](https://hiltmon.com/blog/2015/08/09/c-plus-plus-11-on-centos-6-dot-6/) to get it.

>*Note:* Kindly raise issues if you face setup problems on your Linux distributions. I will ammend the instructions to resolve the same.

3. See Step 4 - Generic.

<br />

### _Generic_

4. Kindly consider using a **virtual environment** for development. Check out [**this link**](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for detailed explanations on how to do that. Follow these steps to get up and running quickly -
```
pip install virtualenv
virtualenv my_project
cd my_project && source bin/activate
```
Now you can install your python modules and run your code in an isolated chamber. Once you're done, run `deactivate` to close the virtual environment.

5. Install the python module requirements by running - `pip install pyvisage`
>_Note_: If you are not using `virtualenv`, you might need `sudo` to make this work.

<br />

## Usage

The module is named `visage`, and consists of two classes - `Detect Features` and `ApplyMakeup`. You can import, and access their functions to either selectively detect face only, or apply lipstick directly. Kindly read the [Wiki](https://github.com/hriddhidey/visage/wiki) for detailed usage.

Example - 
>_Note_: You will need a working internet connection the first time you run this, as it will download a predictor file to your project folder the first time.
```
from visage import ApplyMakeup
AM = ApplyMakeup()
output_file = AM.apply_lipstick('input.jpg',170,10,30) # (R,G,B) - (170,10,30)
```
This assumes you have a front-facing image of a human face saved in your current directory as `input.jpg`.

<br />

## Guidelines for Image

Certain best practices to be followed to ensure optimal detection and application -
* Positioning: Face the camera directly and position yourself so that your face fills the about 50-70% of the frame. Avoid extreme angles and poses.
* Expressions: Preferably maintain a neutral expression. Smiles will be detected comfortably, as long as the shape of the mouth and lips aren't too contorted. Remove any dark glasses or tinted lenses, and keep both eyes open for proper application of eyeliner.
* Lighting: For increased visibility, avoid bright backlighting ( such as the sun, or other bright light sources ), and glare, by taking your photographs under an even light. 
* Orientation: Kindly ensure an upright orientation in portrait mode.
<img width="300" alt="screen shot 2017-08-08 at 12 51 54 pm" src="https://user-images.githubusercontent.com/11678594/30049806-9e7d90bc-9239-11e7-9db0-57825c1c4928.png">

* Focus & Movement: Image focus and blur can have similar effects on performance as low resolution. Thus, make sure your captured image is not blurry. If the camera is having difficulty focusing, you might be too close or too far from the device.

<br />

## Attributions
I would like to thank [Davis E. King](https://github.com/davisking) who built [dlib](http://dlib.net/), for the documentation and sample codes provided, which were a great help in building this.

<br />
