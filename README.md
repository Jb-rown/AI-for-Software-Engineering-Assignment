# AI for Software Engineering Assignment

This repository contains the implementation and documentation for the **Week 4 Assignment: AI in Software Engineering**, themed *"Building Intelligent Software Solutions"*. The project demonstrates the application of AI in software development through theoretical analysis, practical tasks, and ethical considerations. It includes code, a report, and supporting materials as per the assignment requirements.

## Table of Contents
- [AI for Software Engineering Assignment](#ai-for-software-engineering-assignment)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Part 1: Theoretical Analysis](#part-1-theoretical-analysis)
    - [Part 2: Practical Implementation](#part-2-practical-implementation)
      - [Task 1: AI-Powered Code Completion](#task-1-ai-powered-code-completion)
      - [Task 2: Automated Testing with AI](#task-2-automated-testing-with-ai)
      - [Task 3: Predictive Analytics for Resource Allocation](#task-3-predictive-analytics-for-resource-allocation)
    - [Part 3: Ethical Reflection](#part-3-ethical-reflection)
    - [Bonus Task: Innovation Challenge](#bonus-task-innovation-challenge)
  - [Deliverables](#deliverables)
  - [Tools and Resources](#tools-and-resources)
  - [Contributing](#contributing)

## Overview
This project fulfills the Week 4 Assignment objectives by:
- Analyzing AI's role in software engineering (e.g., code generation, bug detection, bias mitigation).
- Implementing practical tasks using AI tools like GitHub Copilot, Selenium IDE, and Scikit-learn.
- Reflecting on ethical implications of AI in software development.
- Proposing an innovative AI tool for automated documentation generation.

The deliverables include well-commented code, a Jupyter notebook, test results, and a proposal, all shared via GitHub, a PDF report on the Community platform, and a 3-minute video demo in Groups.

## Project Structure
```
AI-Software-Engineering-Assignment/
├── code/
│   ├── task1_code_completion/
│   │   ├── manual_sort.py
│   │   ├── ai_sort.py
│   │   └── analysis.md
│   ├── task2_automated_testing/
│   │   ├── login_test.py
│   │   └── results_screenshot.png
│   ├── task3_predictive_analytics/
│   │   └── breast_cancer_prediction.ipynb
├── report/
│   └── assignment_report.pdf
├── bonus/
│   └── docgenai_proposal.md
├── README.md
```

- **code/**: Contains scripts and notebooks for the practical tasks.
- **report/**: PDF report with answers, screenshots, and reflections.
- **bonus/**: Proposal for the innovation challenge.
- **README.md**: This file, providing an overview and instructions.


## Installation
To run the code in this repository, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/AI-Software-Engineering-Assignment.git
   cd AI-Software-Engineering-Assignment
   ```

2. **Set Up Python Environment**:
   - Ensure Python 3.8+ is installed.
   - Install dependencies:
     ```bash
     pip install pandas scikit-learn selenium jupyter
     ```

3. **Install Selenium WebDriver**:
   - Download and configure [Chrome WebDriver](https://chromedriver.chromium.org/downloads) for Task 2.
   - Ensure Chrome browser is installed.

4. **Run Jupyter Notebook** (for Task 3):
   ```bash
   jupyter notebook code/task3_predictive_analytics/breast_cancer_prediction.ipynb
   ```

5. **Optional**: Use GitHub Copilot or Tabnine in your IDE for Task 1 code completion.

## Usage
Each task can be executed independently. Below are instructions for each:

### Part 1: Theoretical Analysis
- **Location**: `report/assignment_report.pdf`
- Contains answers to short-answer questions and case study analysis on AIOps in DevOps.
- Read the PDF for detailed theoretical insights.

### Part 2: Practical Implementation

#### Task 1: AI-Powered Code Completion
- **Location**: `code/task1_code_completion/`
- **Files**:
  - `manual_sort.py`: Manual implementation of a dictionary list sorting function.
  - `ai_sort.py`: AI-generated (GitHub Copilot) implementation with error handling.
  - `analysis.md`: 200-word comparison of efficiency and robustness.
- **Run**:
  ```bash
  python code/task1_code_completion/manual_sort.py
  python code/task1_code_completion/ai_sort.py
  ```
- **Input Example**:
  ```python
  data = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
  sorted_data = sort_dict_list_manual(data, "age")
  ```
- **Output**: Sorted list of dictionaries by the specified key.

#### Task 2: Automated Testing with AI
- **Location**: `code/task2_automated_testing/`
- **Files**:
  - `login_test.py`: Selenium script to test a login page.
  - `results_screenshot.png`: Screenshot of test results (assumed).
- **Run**:
  - Update `login_test.py` with the actual login page URL.
  - Execute:
    ```bash
    python code/task2_automated_testing/login_test.py
    ```
- **Output**: Console output showing test results (e.g., pass/fail for valid/invalid credentials).
- **Summary**: See `report/assignment_report.pdf` for a 150-word analysis on AI’s role in test coverage.

#### Task 3: Predictive Analytics for Resource Allocation
- **Location**: `code/task3_predictive_analytics/`
- **File**: `breast_cancer_prediction.ipynb`
- **Run**:
  - Open the notebook in Jupyter:
    ```bash
    jupyter notebook code/task3_predictive_analytics/breast_cancer_prediction.ipynb
    ```
  - Execute cells to preprocess the Kaggle Breast Cancer Dataset, train a Random Forest model, and evaluate performance.
- **Output**:
  - Accuracy: ~0.9649
  - F1-Score: ~0.9647
- **Dataset**: Automatically downloaded from UCI ML Repository in the notebook.

### Part 3: Ethical Reflection
- **Location**: `report/assignment_report.pdf`
- Discusses potential biases in the Breast Cancer Dataset (e.g., demographic underrepresentation) and mitigation using IBM AI Fairness 360 tools like reweighing and adversarial debiasing.

### Bonus Task: Innovation Challenge
- **Location**: `bonus/docgenai_proposal.md`
- Proposes "DocGenAI," an AI tool for automated documentation generation using NLP and transformer models.
- Read the proposal for details on purpose, workflow, and impact.

## Deliverables
1. **Code**: All scripts and notebooks in the `code/` directory, hosted on GitHub.
2. **Report**: `report/assignment_report.pdf`, shared on the Community platform as an article.
3. **Presentation**: A 3-minute video demo (not included in the repository; shared in Groups for peer review).
4. **Bonus**: `bonus/docgenai_proposal.md`, outlining the innovative AI tool.

## Tools and Resources
- **AI Tools**:
  - GitHub Copilot (Task 1)
  - Selenium IDE (Task 2)
  - Google Colab/Jupyter (Task 3)
- **Datasets**:
  - [Kaggle Breast Cancer Wisconsin Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29) (Task 3)
- **Libraries**:
  - Scikit-learn, Pandas (Task 3)
  - Selenium (Task 2)
- **Documentation**:
  - [GitHub Copilot](https://docs.github.com/en/copilot)
  - [Selenium](https://www.selenium.dev/documentation/)
  - [IBM AI Fairness 360](https://aif360.mybluemix.net/)

## Contributing
This is an academic assignment repository, so contributions are not expected. For feedback or collaboration, join the Community discussion at `#AISoftwareAssignment`.

