# Byte pair encoding (BPE)

The original version of this algorithem focuses on compression. It replaces the highest-frequency pair of bytes with a new byte that was not contained in the initial dataset. A lookup table of the replacement is required to rebuild the initial dataset. The modified version builds tokens that match varying amount of source text from single characters to whole words.

Example

Suppose the sentence to be 

```
aaabbaaabac
```

Since the byte pair (each alphabet as a byte) 'aa' occurs the most often, it is replaced by a byte 'Z' (first match).

```
ZabbZabac
```

Then 'ab' with 'Y'

```
ZYbZYac
```

Then 'ZY' with X

```
XbXac
```

Then this sequence can not be further compressed since there are no byte pair appearing more than once.



This algorithm is effective for tokenization because it has low computational overhead and remains consistent and reliable.


References

[Wikipedia - Byte Pair Encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding)
