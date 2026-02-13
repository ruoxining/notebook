# Pythons' Code Style Guide

## Getting Started

How to use this guidance?

First, follow these steps to structure your repository and maintain consistency:

1. **Design a Class Diagram**: Plan all key classes (e.g., DataLoader, Model, Trainer, TrainingArgs).
2. **Setting up Style Management Tools**: Go to section 1 (Style Management) for instructions.
3. **Write Class Prototypes**: Begin with basic implementations for each class.
4. **Submit Incremental Pull Requests (PRs)**: Commit small, meaningful progress and review frequently.

Next, refer to the instructions in each section below when you are writing each of them.

1. Style Management
2. Commit and Pull Request (PR)
3. Prototyping
4. File Management
5. Imports
6. Comments
7. Spacing
8. Naming
9. Type Hints

---

<!---------------------------- section ---------------------------->

## 1 - Style Management

### 1.1 - Install style checking

Install the pre-commit checking by `pip install pre-commit`

and add two files at the root directory of your repository.

file `.flake8`

```
[flake8]
docstring-convention = google
extend-ignore = E501, E731
```

file `.pre-commit-config.yaml`

```yaml
# pre-commit run --all-files
repos:
-   repo: https://github.com/pycqa/flake8
    rev: 3.7.9
    hooks:
    -   id: flake8
        additional_dependencies: [
            'flake8-docstrings==1.7.0',
        ]
```

and finally, run `pre-commit install`.

---

### 1.2 - Config the Github repository

Config the branch protection rule to require review on merging each pull request.

According to this document, set up requiring at least one reviewer before merging. [Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)_{target="blank"}

---

### 1.3 - Set Up VS Code Style Helpers (Optional)

To streamline code formatting and import sorting, configure VS Code with the following extensions and settings:

1. **Install Extensions**:

   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (for Python language support).
   - [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort) (for sorting imports).


2. **Configure Settings**:

    To automatically sort the imports and format the code, open the `settings.json` and add or modify the following setting:

    ```json
    // Automatically sort the imports
    "editor.codeActionsOnSave": {
        "source.organizeImports": true,
    },
    // Trim whitespace
    "files.trimTrailingWhitespace": true,
    // Add a final new line
    "files.insertFinalNewline": true,
    ```

<!---------------------------- section ---------------------------->

## 2 - Commit and Pull Request (PR)

### 2.1 - Split Changes into Small PRs

❌ Avoid bundling multiple unrelated modifications into a single PR.

✅ Each PR should address a single, focused change that can be summarized in one sentence.

Examples:
- Pre-commit setup as a standalone PR.
- Prototyping or implementing a single class as separate PRs.

---

### 2.2 - Ensure Each PR is Complete and Meaningful

❌ Avoid submitting partially completed features.

✅ Submit only when a feature or change is complete and functional.

---

### 2.3 - Manage Committed Files

❌ Avoid using `git add .` indiscriminately.

✅ Use `git add <specific-files>` to ensure only intentional changes are included.

---

### 2.4 - Require Review Before Merging

Set up branch protection rules to require reviews before merging. Refer to the GitHub guide:
[Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)

---

### 2.5 - PR and Commit Messages

#### PR Titles:
Format titles as you would for commit messages:

**`[label] name + summary of change`**

Refer to the [Git Commit Style Guide](https://gist.github.com/ericavonb/3c79e5035567c8ef3267){target="_blank"} for approved labels.

#### PR Messages:

The PR description should match the commit message format, providing clear and concise context for the changes.

---


<!---------------------------- section ---------------------------->

## 3 - Prototyping

### 3.1 - Define Class Prototypes

A prototype is the skeleton of a class, including:

- The class definition.
- Function declarations with proper docstrings.

Example:

```python
class Bar(foo):
    def __init__(self, arg: bool) -> None:
        """Comment.

        Args:
            arg      : arg.
        """
        pass

    def bar(self) -> bool:
        """Comment.

        Returns:
            arg     : arg.
        """
        return True
```

---

### 3.2 - Include a Main Function

It’s encouraged to add a main function to demonstrate the general workflow:

- How classes will be instantiated.
- How functions will be called.

Example:

```python
int main():
    """Comment."""
    bar = Bar(True)
    return

if __name__ == "__main__":
    main()
```

---

<!---------------------------- section ---------------------------->

## 4 - File Management

### 4.1 - OOP

Encapsulate each function (except `main`) into a related class.

---

### 4.2 - Write Prototypes First

Ensure prototypes are written before detailed implementations.

---

### 4.3 - Avoid Hyphen or Underscore in File Naming

Use folders to organize files instead of naming files with hyphens or underscores.

✅ Do: `models/models.py`

❌ Don't: `models_main.py`

---

<!---------------------------- section ---------------------------->

## Imports

### 5.1 - Order

1. Import all Python standard libraries, in alphabetical order (based on the package name instead of the folder name), and add an empty line.
2. Import all 3rd-party libraries, in alphabetical order, and add an empty line.
3. Import all libraries defined within the project.

Example:

```python
import os

import torch
import transformers

from myfile import MyClass
```

If you have set up the automatical sorting tool in VSCode, it can avoid you from singing an alphabet song every time you add an import.

---

### 5.2 - Importing Names

❌ Don't use `from x import y`.

✅ The only examptions are those well-established ones, e.g., `from typing import Dict, List, Optional, Sequence, Union`.

✅ Do use `import x` and `x.y` to avoid namespace conflicts, for example:

```python
import torch
import transformers

torch.nn.Module
transformers.Trainer
```

---

<!---------------------------- section ---------------------------->

## Comments

### 6.1 - Where Should Comments Appear?

- File docstring
- Class docstring
- Function docstring
- Other (full-line comment, inline comment)

---

### 6.2 - Formats

- **Required**:
  - File docstring (at the top of the file)
  - Class docstring (immediately after the class name)
  - Function docstring (immediately after the function name)

- Docstrings can be either a sentence or multiple paragraphs.

    Example for a single sentence:

    ```python
    """A sentence describing the file content."""
    ```

    Example for multiple paragraphs:

    ```python
    """A sentence describing the file content.

    Declarations.
    """
    ```

- **Function docstring format**:

    ```python
    """A sentence describing the function's content.

    Args:
        arg1    : explanation

    Returns:
        return1 : explanation
    """
    ```

---

### 6.3 - File Docstring

Ensure there is no space between the docstring and the imports.

---

### 6.4 - Be Sure to Make Every Doc a 'Sentence'


✅ Do `# a comment`.

❌ Don't `# a comment.`.

---

### 6.5 - Keep Consistency in Omitting 'The'

✅ Do

```python
# comment 1.
# comment 2.
# comment 3.
```

❌ Don't

```python
# comment 1.
# the comment 2.
# comment 3.
```

---

<!---------------------------- section ---------------------------->

## Spacing

- In every comment: Add 1 empty line between each section.
- Except at the top of the file, do not use more than 2 empty lines.

If you have configured the styling tool in VSCode, it will automatically manage the spacing for you.

---

<!---------------------------- section ---------------------------->

## Naming

### 8.1 - Avoid Abbreviations and Use Full Spellings

✅ Do `path_checkpoint`.

❌ Don't `path_ckpt`.

---

### 8.2 - Naming Conventions (My Own Habit)

- Class Names: Use a noun-adjective format.
- Function Names: Use a verb-noun format.
- Functions and files that perform similar tasks or operate on the same objects should begin with the same substring.

---

### 8.3 - Private Members

Class private members should start with an underscore _ to distinguish them from input parameters.


e.g., the correct private number name should be

```python
def __init__(self, foo):
    self._foo = foo     # recommended
```

instead of

```python
def __init__(self, foo):
    self.foo = foo      # not recommended
```

---

### 8.4 - Accessing Private Members

Avoid directly accessing private members outside the class.

```python
class Foo:
    def __init__(self, bar):
        self._bar = bar

    def get_bar(self):
        return self._bar


foo = Foo()
foo._bar                # not recommended, since the members should be 'considered as private'.
foo.get_bar()           # not recommended, since the function name looks messy.
```

Instead, using a `@property` decorator is recommonded.

```python
class Foo:
    def __init__(self, bar):
        self._bar = bar

    @property
    def bar(self):
        return self._bar

foo = Foo()
foo.bar                 # recommended
```

---

<!---------------------------- section ---------------------------->

## Type Hints

### 9.1 - Write Type Hints

✅ Do: write type hints in function declarations.

```python
def foo(bar: int) -> str:
    """
    Args:
        bar:
    Returns:
        str:
    """
    pass
```

❌ Don't: write types in the comment.

```python
def foo(bar: int) -> str:
    """
    Args:
        bar (int):
    Returns:
        str (str):
    """
    pass
```

---

### 9.2 - Use the typing Library

Use the typing library when you need to indicate the element type of a `Dict`, `List`, etc.

```python
from typing import Dict

typing.Dict[str, Union[int, float]]
```

Commonly used examples:

- `Dict[x, y]` — for dictionaries with keys of type `x` and values of type `y`.
- `Union[x, y, ...]` — for a type that can be one of several types (e.g., `Union[int, float]`).
- `List[x]` — for a list where each element is of type `x`.
- `Tuple[x, y, ...]` — for a tuple with fixed types and length.
- `Optional[x]` — equivalent to `Union[x, None]`, meaning a value could be of type `x` or `None` (e.g., `Optional[str]`).
- `Callable[[x, y], z]` — for a function type that takes arguments of types `x` and `y`, and returns a value of type `z`.
- `Any` — for any type (used when you don't want to specify a type).


More examples in [typing — Support for type hints](https://docs.python.org/3/library/typing.html){_target="blank"}

---

## References and Credits

This code style guide is based on the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html){:target="_blank"}.

Written with the help of GPT-4o.
