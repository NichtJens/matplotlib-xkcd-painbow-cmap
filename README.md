# Painbow colormap for Matplotlib
 (from xkcd [#2537](https://xkcd.com/2537))

## Usage

Importing the package registers the colormap to matplotlib, thus this works:

```python
import painbow

plt.imshow(image, cmap="painbow")
```

(The registration (i.e., the import line) can happen in a different/central part of your code, if that's desirable. Also, it is only needed once.)

Alternatively, you can simply import the colormap object and use it directly:

```python
from painbow import cmap

plt.imshow(image, cmap=cmap)
```

(The object must be imported wherever it is used.)

## Example

![result](result.png)

See [example.py](example.py) for how this was produced.

## Note
Color values and 2D example data taken from the [R implementation by Steve Haroz](https://github.com/steveharoz/painbow). Make sure to check out the [analysis](https://github.com/steveharoz/painbow#examples) of the colormap's qualities in the repo.



