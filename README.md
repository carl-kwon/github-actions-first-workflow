# github-actions-first-workflow


[PyTest](https://docs.github.com/ko/actions/automating-builds-and-tests/building-and-testing-python)

```
name: PyTest

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Test with pytest
      run: |
        pip install pytest pytest-cov
        pytest tests.py --doctest-modules --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report=html
```
