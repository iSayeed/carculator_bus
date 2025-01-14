from pathlib import Path
import carculator_bus.bus_input_parameters as tip
import json
import pytest


DEFAULT = Path(__file__, "..").resolve() / "fixtures" / "default_test.json"
EXTRA = Path(__file__, "..").resolve() / "fixtures" / "extra_test.json"


def test_retrieve_list_powertrains():
    assert isinstance(tip.BusInputParameters().powertrains, list)
    assert len(tip.BusInputParameters().powertrains) > 5


def test_can_pass_directly():
    d, e = json.load(open(DEFAULT)), set(json.load(open(EXTRA)))
    e.remove("foobazzle")
    assert len(tip.BusInputParameters(d, e).powertrains) == 5
    assert len(tip.BusInputParameters(d, e).parameters) == 12


def test_alternate_filepath():
    assert len(tip.BusInputParameters(DEFAULT, EXTRA).powertrains) == 5
    assert len(tip.BusInputParameters(DEFAULT, EXTRA).parameters) == 13
