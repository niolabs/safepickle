# safepickle

A safe alternative to Python's pickle module.

## Installation

```
pip install safepickle
```

## Usage

Safepickle is designed to be used as a drop-in replacement wherever you currently use the `pickle` module. So in your code you can just import `safepickle` instead.

```python
import safepickle as pickle

obj = {'loves pickles': true}
obj_str = pickle.dumps(obj)
obj_again = pickle.loads(obj_str)

assert obj_again == obj
```
