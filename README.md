# Moving Symbols

Description of Moving Symbols.

## Environment

This code was tested on Python 2.7 on Ubuntu 16.04. It might not work for Python 3.X; support might
be added in the future, or perhaps someone can make a pull request to make it support both 2.X and
3.X... :)

## Dependencies

* PIL==5.0.0
* pygame==1.9.3
* pymunk==5.3.2
* numpy==1.14.0
* opencv-python==3.4.0.12
* scipy==1.0.0

The packages listed above need to be installed. This can be done via `pip`.

**One important note:** There is a visualization script, `view_moving_symbols.py`, that seems to
fail when using the `pip` version of `opencv-python`. If you really want to run that script, I
recommend installing OpenCV from source instead of through `pip`.

## How To Use (ICLR 2018 Workshop Submission)

This section describes how to generate the datasets used in our ICLR 2018 Workshop submission.

### Generate the images

Run our scripts to automatically download and organize object images in the format Moving Symbols
expects.

```bash
cd data
./generate_mnist_images.sh
./generate_icons8_images.sh
# The line below prints a lot of messages about skipping images. This is normal.
./generate_omniglot_images.sh
```

### Generate the videos

To generate the actual videos, run the `generate_moving_symbols.py` script:

```bash
cd iclr2018_workshop
python generate_moving_symbols.py
```

## How To Use (external projects)

The core Moving Symbols code is contained in a friendly Python package. That means as long as this
project directory is in your PYTHONPATH, you can import the required classes.

Including the project directory in your PYTHONPATH can be done in one of two ways. First, you can
modify the environment variable in the terminal:

```bash
export PYTHONPATH=/path/to/project/root:$PYTHONPATH
```

Or you can augment the system path in your Python script directly:

```python
import sys
sys.path.append('/path/to/project/root')
from moving_symbols import MovingSymbolsEnvironment
```

## User Guide

I'll fill this in later. For now, look through the `generate_moving_symbols.py` script for examples
on how to use the Moving Symbols package.