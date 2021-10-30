# ASCII Table Maker

## Instructions:

***

The function has only one parameter:

`data` - a `list` of all the data the table will contain in this format:

```py
[
    ['C1R1', 'C1R2', 'C1R3'],
    ['C2R1', 'C2R2', 'C2R3'],
    ['C3R1', 'C3R2', 'C3R3']
]
```

>### `C` signifies the *column* and `R` signifies the *row*.

The resulting table should look something like this:

```plaintext
+------+------+------+
| C1R1 | C1R2 | C1R3 |
+------+------+------+
| C2R1 | C2R2 | C2R3 |
+------+------+------+
| C3R1 | C3R2 | C3R3 |
+------+------+------+
```

It will convert any kind of data to a string using `Python`'s `str()` method.

It *should* be able to handle varying lengths as well since it decides the width of each **column** individually.

So the `input`:

```py
[
    ['**C1R1**', 'C1R2', 'C1R3'],
    ['C2R1', 'C2R2', '*C2R3*'],
    ['*C3R1*', 'C3R2', 'C3R3']
]
```

Should `output` as:

```plaintext
+----------+------+--------+
| **C1R1** | C1R2 |  C1R3  |
+----------+------+--------+
|   C2R1   | C2R2 | *C2R3* |
+----------+------+--------+
|  *C3R1*  | C3R2 |  C3R3  |
+----------+------+--------+
```
