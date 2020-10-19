# static_analysis_example

Simple taint analysis example based on official online documentaion, that can be found here: [https://pyre-check.org/docs/pysa-running/#example](https://pyre-check.org/docs/pysa-running/#example)

## installation steps (ubuntu)

```shell
python3 -m venv /temp/static_analysis_example
source /tempstatic_analysis_example/bin/activate
pip3 install pyre-check
```

## how to run

```shell
pyre analyze
```

## how to save the results

```shell
pyre analyze --save-results-to ./pysa-results
```

