# Deploy the HKBK AQI dashboard

This guide publishes the Streamlit app from GitHub to Streamlit Community Cloud.

## What you need

- A GitHub account
- Git installed on your computer
- VS Code
- The HKBK AQI project ZIP

The project uses simulated classroom data. Do not add passwords, API keys, or personal information to the repository.

## 1. Extract and open the project

1. Extract aqi_streamlit_project.zip into a new folder you can find easily, such as Documents\aqi_streamlit_project.
2. In VS Code, choose File → Open Folder and open the extracted aqi_streamlit_project folder.
3. In the VS Code Explorer, check that these files are at the top level:
   - app.py
   - requirements.txt
   - README.md
   - .gitignore
   - data\air_quality_dummy_dataset.csv
4. Do not upload the .venv folder. The supplied .gitignore excludes it from Git.

## 2. Run it locally first

Open Terminal → New Terminal in VS Code. The terminal should be inside the folder containing app.py.

Run these commands one by one:

    py -m venv .venv
    .\.venv\Scripts\python.exe -m pip install --upgrade pip
    .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    .\.venv\Scripts\python.exe -m streamlit run app.py

A browser should open at http://localhost:8501. To stop the app, click the terminal and press Ctrl+C.

## 3. Create an empty GitHub repository

1. Sign into github.com and choose New repository.
2. Enter a repository name, for example aqi-streamlit-dashboard.
3. Choose Public if you are comfortable making the source code and dummy CSV visible to everyone. Choose Private if you want the code private; connect Streamlit Community Cloud to GitHub and grant access to that repository.
4. Leave Add a README, Add .gitignore, and Choose a license unchecked. The local project already contains its files.
5. Create the repository and copy its HTTPS URL. It will look like:
   https://github.com/YOUR-USERNAME/aqi-streamlit-dashboard.git

## 4. Upload the project from VS Code

In the VS Code terminal, run the commands below. Replace YOUR-USERNAME with your GitHub username and use your actual repository name.

    git init
    git add app.py requirements.txt README.md .gitignore DEPLOY_TO_STREAMLIT_CLOUD.md data/air_quality_dummy_dataset.csv
    git commit -m "Add HKBK AQI Streamlit dashboard"
    git branch -M main
    git remote add origin https://github.com/YOUR-USERNAME/aqi-streamlit-dashboard.git
    git push -u origin main

If Git asks you to sign in, complete the browser sign-in opened by VS Code or Git Credential Manager. Do not paste a password or token into this guide or into app.py.

If Git reports that origin already exists, use this command instead of the remote-add command:

    git remote set-url origin https://github.com/YOUR-USERNAME/aqi-streamlit-dashboard.git

Then run git push -u origin main.

## 5. Deploy on Streamlit Community Cloud

1. Open https://share.streamlit.io and sign in with GitHub.
2. Choose Create app, then select the repository you just uploaded.
3. Select branch main.
4. Set the app file path to app.py. It is in the repository root.
5. Optionally choose an app URL, then choose Deploy.
6. Wait for the app to build. The first installation may take a few minutes.
7. Open the generated streamlit.app URL and check the filters, charts, AQI alert, and map.

The app reads its CSV using a path relative to app.py, and requirements.txt is next to app.py, which matches the deployment layout.

## 6. Publish later changes

After editing app.py or the CSV in VS Code, save the files and run:

    git add app.py data/air_quality_dummy_dataset.csv
    git commit -m "Update AQI dashboard"
    git push

Streamlit Community Cloud detects changes pushed to the connected branch and updates the app. If you change requirements.txt, include it in git add so the cloud environment can install the updated packages.

## Troubleshooting

- Build failed: open the app menu in Streamlit Community Cloud and check the app logs. Confirm requirements.txt is in the repository root.
- CSV missing: confirm the file is at data/air_quality_dummy_dataset.csv and that its capitalization matches.
- Module missing: add that package to requirements.txt, then commit and push.
- Git asks for identity: configure your name and email in Git, then retry the commit. Use the name and email associated with your GitHub account if appropriate.
- App loads the old version: confirm your changes were pushed to the same repository and branch selected by the deployed app.
