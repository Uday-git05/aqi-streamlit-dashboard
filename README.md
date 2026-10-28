HKBK AQI DASHBOARD — PYTHON + STREAMLIT

**Environmental Monitoring and AQI**  **
HKBK College of Engineering · Department of Civil Engineering · BCV755B — Conservation of Natural Resources

The dashboard presents a simulated 12-month 2025 air-quality dataset for an academic demonstration. Its banner reads: “Academic Research Demo: Simulated Data for HKBK College Civil Eng. Project (Course BCV755B).” The measurements and map spots are simulated; they are not official monitoring readings or real geographic locations.

## Project files

- app.py — interactive Streamlit dashboard
- data/air_quality_dummy_dataset.csv — 12 monthly sample records
- requirements.txt — Python packages used by the dashboard
- DEPLOY_TO_STREAMLIT_CLOUD.md — instructions for publishing through Streamlit Community Cloud
- .gitignore — excludes the local virtual environment and Python cache files

## Dashboard features

- Filter the sample by season and month.
- See average AQI, PM₂.₅, PM₁₀, CO, and NO₂ for the selected records.
- View AQI bands: Good, Satisfactory, Moderate, Poor, Very Poor, and Severe.
- Compare monthly PM₂.₅, PM₁₀, and NO₂ trends and view AQI by month.
- View a schematic regional map with simulated monitoring spots.
- Review seasonal observations, AQI alerts, and natural resource management recommendations.

The AQI is provided as a synthetic summary index. It is not calculated from the pollutant averages. The schematic monitoring map is for dashboard demonstration only.

## Run in VS Code on Windows

1. Install Python 3.10 or newer and Visual Studio Code.
2. Extract the project ZIP. In VS Code, choose **File → Open Folder** and open the extracted aqi_streamlit_project folder.
3. In VS Code, choose **Terminal → New Terminal**. Confirm the terminal is inside the folder containing app.py.
4. Create a virtual environment by running:

       py -m venv .venv

5. Install the packages:

       .\.venv\Scripts\python.exe -m pip install --upgrade pip
       .\.venv\Scripts\python.exe -m pip install -r requirements.txt

6. Start the dashboard:

       .\.venv\Scripts\python.exe -m streamlit run app.py

7. A browser should open. If it does not, copy the Local URL shown in the terminal—usually http://localhost:8501—into your browser.
8. To stop the dashboard, return to the VS Code terminal and press Ctrl+C.

These commands use the virtual environment’s Python directly; activating the environment is not required.

## How the dashboard works

1. pandas reads the CSV from the data folder.
2. The app assigns an AQI category to each supplied AQI value.
3. Sidebar selectors filter the records by season and month.
4. Summary cards calculate averages for the selected records.
5. Plotly charts show pollutant concentrations and AQI.
6. Alerts and recommendations describe the selected sample period.

## Edit the sample dataset

Edit data/air_quality_dummy_dataset.csv while keeping its column names and units unchanged. Save the file and refresh the app in your browser. Changing pollutant values does not recalculate AQI; AQI is a separate supplied sample value. The map markers are illustrative and are not read from the CSV.

## Common fixes

- **py is not recognized:** Install or repair Python and select **Add Python to PATH**, then reopen VS Code.
- **Streamlit is missing:** Run the package installation commands from the project folder.
- **The CSV cannot be found:** Keep it at data/air_quality_dummy_dataset.csv relative to app.py.
- **Port 8501 is busy:** Stop the other Streamlit session with Ctrl+C, or start this one with:

       .\.venv\Scripts\python.exe -m streamlit run app.py --server.port 8502

## Assignment submission

Complete the student names, USNs, class, and section on the report cover page. The assignment allows a maximum of three students per group. Print the report in Times New Roman, 12 pt, and staple it as instructed.

