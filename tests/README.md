AquaPredict AI — Test Documentation

Purpose

This directory contains automated tests for the prototype's water-deficit assessment API.

Prerequisites

- Python 3.10 or later
- Dependencies listed in the root "requirements.txt"

Running the Tests

From the repository root:

pip install -r requirements.txt
python -m pytest -v

Test Coverage

Test| Expected Behaviour
Home endpoint| Returns API status and project name
Water shortage| Identifies positive demand-supply deficit
Supply exceeds demand| Returns a negative deficit
Equal supply and demand| Returns zero deficit
Negative supply| Rejects invalid input
Negative demand| Rejects invalid input
Empty region| Rejects invalid region identifier

Interpretation

Passing tests indicates that the tested API behaves as expected for these inputs. It does not establish the accuracy of scarcity forecasts, the suitability of water sources, or the reliability of external datasets.
