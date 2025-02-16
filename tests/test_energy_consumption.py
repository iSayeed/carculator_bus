from carculator_bus import *
import numpy as np

def test_acceleration():
    ecm = EnergyConsumptionModel("Long haul")
    # Sum of acceleration should be close to zero
    assert np.isclose(ecm.acceleration.sum(),0) == True
    # Average speed of Long haul driving cycle should be above 60 and below 80
    assert (ecm.velocity[..., 0]/1000*3600).mean() > 60
    assert (ecm.velocity[..., 0]/1000*3600).mean() < 80


def test_motive_energy():
    # 40t diesel and gas trucks must have a fuel consumption comprised between
    # 15 L/100km and 35 L/km

    tip = BusInputParameters()
    tip.static()
    _, array = fill_xarray_from_input_parameters(tip)
    tm = BusModel(array, country="CH")
    tm.set_all()

    assert (tm.array.sel(powertrain=["ICEV-d", "ICEV-g"], parameter="TtW energy", size="13m-city")/1000*100/42.4).min() > 14
    assert (tm.array.sel(powertrain=["ICEV-d", "ICEV-g"], parameter="TtW energy", size="13m-city")/1000*100/42.4).max() < 45
