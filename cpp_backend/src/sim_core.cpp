#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <string>
#include <map>

namespace py = pybind11;

py::dict simulate(const std::vector<std::map<std::string, double>>& netlist) {
    py::dict out;
    int n = static_cast<int>(netlist.size());
    out["cells"] = n;
    double score = 0.0;
    for (const auto &nmap : netlist) {
        auto it = nmap.find("x");
        if (it != nmap.end()) score += it->second;
    }
    out["score"] = score / (n + 1.0);
    out["status"] = "ok";
    return out;
}

PYBIND11_MODULE(sim_core, m) {
    m.doc() = "Cellium simulation core (sample)";
    m.def("simulate", &simulate, "Simulate a netlist and return summary");
}
