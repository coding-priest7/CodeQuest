# CodeQuest

CodeQuest is a powerful open-source project that leverages the TF-IDF (Term Frequency-Inverse Document Frequency) algorithm to curate and present a list of coding questions based on specific keywords. The repository is designed to help programmers and coding enthusiasts find relevant coding challenges tailored to their interests and areas of expertise.

Using TF-IDF, CodeQuest analyzes a vast collection of coding questions, taking into account the frequency of keywords within each question and their significance across the entire question set. This algorithm allows CodeQuest to identify and prioritize questions that are most closely related to the provided keywords, ensuring that users receive a curated list of highly relevant challenges.

The curated questions cover various domains of programming, including algorithms, data structures, dynamic programming, and more. Each question is accompanied by a detailed problem statement, which provides clear instructions and requirements for solving the challenge. By focusing on the keywords specified, CodeQuest ensures that users can find questions that align with their learning objectives and areas of interest.

Whether you are a beginner looking for introductory challenges or an experienced programmer seeking advanced problems, CodeQuest's TF-IDF-powered question curation provides an efficient and tailored experience.

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Navigate to the project directory:

```bash
  cd project_name
```

Install dependencies

```bash
  pip3 install flask
  pip3 install flask-wtf
  pip3 install selenium
  pip3 install webdriver_manager
  pip3 install beautifulsoup4
```

Start the server

```bash
  flask --app app run
```

start a development server that gets updated with changes

```bash
  flask --app app.py --debug run
```
