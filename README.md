# image-displayer
![Demo](supps/intro.gif)

[![Downloads](https://pepy.tech/badge/displayer)](https://pepy.tech/project/displayer)
![license](https://img.shields.io/badge/license-MIT-red.svg)

Almost personal library.

## Install
```
pip install displayer
```

## Usage examples
```
displayer --dir path/to/target/dir/
```

```
set -f
displayer --dir path/to/target/dir/ --format *.png --width 256
set +f
```

```
set -f
displayer --dir path/to/target/dir/ --format *input.png *output.png *gt.png --width 256
set +f
```

```
from displayer.displayer import displayer


opts = {'dir': 'path/to/target/dir/',
        'format': ['*input.png', '*output.png'],
        'width': 256}
        
displayer(opts)
```
