# dictf
An extended Python dict implementation that supports multiple key selection with a pretty syntax.

## How to use it
First you install the package with pip
```bash
pip install dictf
```
Then you can use it like this:
```python
from dictf import dictf


example_dictf = dictf(name="Led Zepellin", singer="Robert Plant", guitarist="Jimmy Page")

print(example_dictf["name"])
>>> 'Led Zepellin'

print(example_dictf[["name"]])
>>> {'name': 'Led Zepellin'}

# The pandas inspired syntax makes it easy to understand how the lib works
print(example_dictf[["name", "singer"]])
>>> {'name': 'Led Zepellin', 'singer': 'Robert Plant'}

# The return type is a dictf whenever you use a list, tuple or set as key
print(type(example_dictf[["name", "singer"]]))
>>> dictf

# If one key doesn't exist, a KeyError is raised
print(example_dictf[["name", "singer", "drummer"]])
>>> KeyError
```
Currently you can not make multiple assignments at the same time, and I'm not sure we need to add this functionality. I'm open to suggestions, though!

## Contributing
Contributions are welcome and appreciated. Make sure to read our [guide for contributing](https://github.com/Eric-Mendes/dictf/blob/main/CONTRIBUTING.md) and don't forget to check out our [code of conduct](https://github.com/Eric-Mendes/dictf/blob/main/CODE_OF_CONDUCT.md).

Also, please do check out our other libs as well such as https://github.com/Eric-Mendes/unexpected-isaves.