# image-displayer
[![pip install](https://img.shields.io/pypi/dm/displayer.svg?color=brightgreen)](https://pypi.org/project/displayer/)

Almost personal library.

## Install
```bash
pip install displayer
```

## Usage examples
```bash
displayer --dir path/to/target/dir/
```

```bash
displayer --dir path/to/target/dir/ --format *.png --width 256
```

```bash
displayer --dir path/to/target/dir/ --format *input.png *output.png *gt.png --width 256
```

```
from displayer.displayer import displayer


opts = {'dir': 'path/to/target/dir/',
        'format': ['*input.png', '*output.png'],
        'width': 256}
        
displayer(opts)
```
