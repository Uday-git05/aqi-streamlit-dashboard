HKBK AQI DASHBOARD — PYTHON + STREAMLIT

This classroom project uses a synthetic 12-month 2025 dataset. It is not official air-quality data.

PROJECT FILES
app.py: interactive Streamlit dashboard
data/air_quality_dummy_dataset.csv: input data
requirements.txt: packages to install

RUN IN VS CODE ON WINDOWS
1. Install Python 3.10 or newer and Visual Studio Code.
2. In VS Code select File, Open Folder and choose this aqi_streamlit_project folder.
3. Select Terminal, New Terminal. Confirm the terminal is in the project folder.
4. Create a private Python environment by running:
   py -m venv .venv
5. Install packages using the Python inside that environment:
   .\.venv\Scripts\python.exe -m pip install --upgrade pip
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
6. Start the app:
   .\.venv\Scripts\python.exe -m streamlit run app.py
7. If a browser does not open automatically, copy the Local URL shown in the terminal, usually http://localhost:8501, into a browser.
8. Stop the app by returning to the VS Code terminal and pressing Ctrl+C.

HOW IT WORKS
1. pandas reads the CSV from the data folder.
2. A Python function assigns each AQI value to one of six bands.
3. Sidebar filters select a season and month.
4. Summary metrics recalculate for the selected rows.
5. Plotly charts show pollutant concentrations and AQI.
6. Alerts and recommendations explain the sample pattern.

EDIT THE DATA
Edit the CSV while keeping the column names and units unchanged. Save and refresh the browser. AQI is a separate dummy index; changing pollutant values will not recalculate it.

COMMON FIXES
If py is not recognized, reinstall Python and select Add Python to PATH, then reopen VS Code.
If Streamlit is missing, run the package installation command from this project folder.
If the CSV cannot be found, keep it at data/air_quality_dummy_dataset.csv.
These commands call the environment's Python directly, so PowerShell activation is not required.
If port 8501 is busy, stop another app with Ctrl+C or add --server.port 8502 to the run command.

SUBMISSION
Complete the student names, USNs, class and section in the report cover page. The assignment allows groups of up to three students.
