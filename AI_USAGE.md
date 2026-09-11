# AI Usage

## Interaction 1: Understanding the Lab Setup

**AI model used:** ChatGPT

I used ChatGPT to help me understand how to begin Lab 1 because I was confused about the required GitHub repository structure and which files I needed to create.

My question to ChatGPT was:

```text
I'm so confused. I don't even have anything downloaded to do this assignment.
```

I first asked ChatGPT what the assignment requirements meant before asking how to complete the setup. ChatGPT explained that the project needed files such as `environment.yml`, `.gitignore`, `README.md`, `AI_USAGE.md`, a `src/` directory, and a `data/` directory.

I verified this guidance by comparing the suggested files with the Lab 1 rubric.

## Interaction 2: Conda Environment Error

While trying to create the environment, I received this error:

```text
EnvironmentSpecPluginNotDetected: Environment at environment.yml is not able to be detected by any installed environment specifier plugins.
```

I first asked ChatGPT what the error meant before asking how to fix it. ChatGPT explained that the error could mean that `environment.yml` was empty or not formatted correctly. I checked the file and found that it was empty.

I then asked how to fix it and added the required environment information, including Python 3.12 and pandas 2.2.

I verified the fix by successfully creating the Conda environment and activating the `lab1` environment.

## Interaction 3: Python File Path Error

When I tried to run my analysis, I received this error:

```text
python: can't open file '/Users/mariumkalhoro/Desktop/lab1-reproducible-setup/src/analysis.py': [Errno 2] No such file or directory
```

I first asked ChatGPT what the error meant before asking how to fix it. ChatGPT helped me check the `src` directory, where I discovered that I had accidentally created nested `src` folders.

After understanding the problem, I corrected the folder structure so that the script was located at `src/analysis.py`.

I verified the fix by running:

```text
python src/analysis.py
```

The actual output was:

```text
Lab 1 analysis ran successfully.
Rows: 5
Mean value: 30.00
```

This confirmed that the Python script could read the data and run successfully.

## How I Used AI Critically

I used ChatGPT for explanations and step-by-step troubleshooting rather than assuming every suggestion was correct. When errors occurred, I first asked what they meant before asking for a fix. I verified the suggestions myself by checking my files, rebuilding the Conda environment, and running the analysis script successfully.
