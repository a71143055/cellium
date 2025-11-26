try:
    import sim_core  # built C++ module (pybind11)
except Exception:
    sim_core = None

def simulate_netlist(netlist):
    if sim_core:
        # sim_core expects list of dicts with numeric values
        return sim_core.simulate(netlist)
    else:
        return {"cells": len(netlist), "status": "fallback", "score": 0.0}
