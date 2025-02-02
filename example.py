from evci_tool.analysis import *

ui_inputs = { 
    "planning_scenario": "Public places",
    "years_of_analysis": [1,2,3],
    "Ai": 50,
    "Li": 1500,
    "Bipc": .25,
    "Birate": 3.5,
    "Eg": 5.5,
    "backoff_factor":1,
    "cabling_cost": 500000,
    "capex_2W": 2500,
    "capex_3WS": 112000,
    "capex_4WS": 250000,
    "capex_4WF": 1500000,
    "hoarding cost": 900000,
    "kiosk_cost": 180000,
    "year1_conversion": 0.02,
    "year2_conversion": 0.05,
    "year3_conversion": 0.1,
    "holiday_percentage": 0.3,
    "fast_charging": 0.3,
    "slow_charging": 0.15,
    "cluster": True,
    "cluster_th": 0.02,
    "plot_dendrogram": True
}

analysis = analyze_sites('abc124','panaji',ui_inputs)
