# This is a sample Python script.

#######################
# Overlap Calculator
#######################
#
# Stephen Uruqhart, April 19, 2026
#
# Copyright? Who am I kidding - this is mostly CoPilot
#
######################

import streamlit as st
import math

def circle_overlap_percent(spacing, diameter):
    r = diameter / 2
    D = abs(spacing)  # distance between centers

    if D >= 2 * r:
        return 0.0

    if D == 0:
        return 100.0

    part1 = 2 * r**2 * math.acos(D / (2 * r))
    part2 = 0.5 * D * math.sqrt(4 * r**2 - D**2
    overlap_area = part1 - part2

    circle_area = math.pi * r ** 2
    percent = (overlap_area / circle_area) * 100

    return percent


st.title("Ptychography  Overlap Calculator")
st.write("Compute the percent overlap between adjacent focus spots.")

spacing = st.number_input("Step size", value=0.5)
diameter = st.number_input("Focus Diameter", value=2.5, min_value=0.0)

if st.button("Calculate Overlap"):
    percent = circle_overlap_percent(spacing, diameter)
    st.subheader(f"Overlap: {percent:.2f}%")





