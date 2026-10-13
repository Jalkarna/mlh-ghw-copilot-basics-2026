# Copilot CLI Session

> [!NOTE]
> - **Session ID:** `a693cf2e-940c-4825-9d5c-74f81fcb74de`  
> - **Started:** 10/13/2026, 9:04:26 PM  
> - **Duration:** 19s  
> - **Exported:** 10/13/2026, 9:04:46 PM  

---

<sub>3s</sub>

### User

Please briefly explain the structure of this GitHub Skills project and what I should do to run it. Then tell me the commands to create and publish a Git branch called accelerate-with-copilot. This is the Hello Copilot stage of the MLH Getting Started with Copilot challenge. Read the relevant source files, but do not edit files or run commands that change anything. Do not use subagents or contact external services.

---

<sub>8s</sub>

### `glob`

****/***

"**/*"

<details>
<summary>56 matches</summary>

```
[glob: 49 path(s) under /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026; grouped by directory]

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.github/ (37 path(s))
  images/activities-dict-highlighted.png
  images/activity-card-with-participants.png
  images/agent-mode-dropdown.png
  images/ask-mode-selection.png
  images/copilot-extension-vscode.png
  images/copilot-logo.png
  images/copilot-review-button.png
  images/copilot-sign-in-button-clicked.png
  images/copilot-sign-in-button.png
  images/copilot-signed-in.png
  images/copilot-summarize-button.png
  images/edited-files-icons.png
  images/files-added-to-context.png
  images/inline-chat-highlight.png
  images/mergington-high-school-webapp.png
  images/open-in-browser-icon.png
  images/plan-mode-dropdown.png
  images/plan-mode-start-implementation.png
  images/python-extension-vscode.png
  images/review-changes-buttons.png
  images/run-and-debug-tab.png
  images/shadow-text.gif
  images/staging-changes-icon.png
  images/toggle-chat-icon.png
  images/tools-icon.png
  steps/1-step.md
  steps/2-step.md
  steps/3-step.md
  steps/4-step.md
  steps/5-step.md
  steps/x-review.md
  workflows/0-start-exercise.yml
  workflows/1-step.yml
  workflows/2-step.yml
  workflows/3-step.yml
  workflows/4-step.yml
  workflows/5-step.yml

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/ (5 path(s))
  .gitignore
  LICENSE
  README.md
  pytest.ini
  requirements.txt

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/src/ (5 path(s))
  README.md
  app.py
  static/app.js
  static/index.html
  static/styles.css

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.devcontainer/ (1 path(s))
  devcontainer.json

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.vscode/ (1 path(s))
  launch.json

[extensions: .png=24, .md=8, .yml=6, .json=2, [no extension]=2, .ini=1, .gif=1, .txt=1]
```

</details>


---

<sub>8s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/README.md.**

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/README.md

```
# Getting Started with GitHub Copilot

_Get started using GitHub Copilot in less than an hour._

## Welcome

- **Who is this for**: Developers at any experience level looking to accelerate their code workflow.
- **What you'll learn**: The different ways to interact with Copilot to explain, write, plan, and develop code.
- **What you'll build**: You will guide Copilot to update Mergington High School's extracurricular activities website.
- **Prerequisites**:
  - Skills exercise: [Introduction to GitHub](https://github.com/skills/introduction-to-github)
  - Familiarity with [VS Code](https://code.visualstudio.com/)
  - Basic coding principles
- **How long**: This exercise takes less than one hour to complete.

In this exercise, you will:

1. Use a preconfigured Codespace to run VS Code in your browser.
1. Learn different interaction options to develop and plan with GitHub Copilot.
1. Use Copilot to summarize and review your pull request.

### How to start this exercise

Simply copy the exercise to your account, then give your favorite Octocat (Mona) **about 20 seconds** to prepare the first lesson, then **refresh the page**.

[![](https://img.shields.io/badge/Copy%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/new?template_owner=skills&template_name=getting-started-with-github-copilot&owner=%40me&name=skills-getting-started-with-github-copilot&description=Exercise:+Get+started+using+GitHub+Copilot&visibility=public)

<details>
<summary>Having trouble? 🤷</summary><br/>

When copying the exercise, we recommend the following settings:

- For owner, choose your personal account or an organization to host the repository.

- We recommend creating a public repository, since private repositories will use Actions minutes.
   
If the exercise isn't ready in 20 seconds, please check the [Actions](../../actions) tab.

- Check to see if a job is running. Sometimes it simply takes a bit longer.

- If the page shows a failed job, please submit an issue. Nice, you found a bug! 🐛

</details>

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)
```


---

<sub>8s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.github.**

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.github

```
images
steps
workflows
```


---

<sub>12s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/src/README.md.**

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/src/README.md

<details>
<summary>33 lines</summary>

````
# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities

## Getting Started

1. Install the dependencies:

   ```
   pip install fastapi uvicorn
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.
````

</details>


---

<sub>12s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/src/app.py.**

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/src/app.py

<details>
<summary>54 lines</summary>

```
"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
```

</details>


---

<sub>12s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/src/static/index.html.**

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/src/static/index.html

<details>
<summary>46 lines</summary>

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mergington High School Activities</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <header>
      <h1>Mergington High School</h1>
      <h2>Extracurricular Activities</h2>
    </header>

    <main>
      <section id="activities-container">
        <h3>Available Activities</h3>
        <div id="activities-list">
          <!-- Activities will be loaded here -->
          <p>Loading activities...</p>
        </div>
      </section>

      <section id="signup-container">
        <h3>Sign Up for an Activity</h3>
        <form id="signup-form">
          <div class="form-group">
            <label for="email">Student Email:</label>
            <input type="email" id="email" required placeholder="your-email@mergington.edu" />
          </div>
          <div class="form-group">
            <label for="activity">Select Activity:</label>
            <select id="activity" required>
              <option value="">-- Select an activity --</option>
              <!-- Activity options will be loaded here -->
            </select>
          </div>
          <button type="submit">Sign Up</button>
        </form>
        <div id="message" class="hidden"></div>
      </section>
    </main>

    <footer>
      <p>&copy; 2023 Mergington High School</p>
    </footer>

    <script src="app.js"></script>
  </body>
</html>
```

</details>


---

<sub>12s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/src/static/app.js.**

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/src/static/app.js

<details>
<summary>71 lines</summary>

```
document.addEventListener("DOMContentLoaded", () => {
  const activitiesList = document.getElementById("activities-list");
  const activitySelect = document.getElementById("activity");
  const signupForm = document.getElementById("signup-form");
  const messageDiv = document.getElementById("message");

  // Function to fetch activities from API
  async function fetchActivities() {
    try {
      const response = await fetch("/activities");
      const activities = await response.json();

      // Clear loading message
      activitiesList.innerHTML = "";

      // Populate activities list
      Object.entries(activities).forEach(([name, details]) => {
        const activityCard = document.createElement("div");
        activityCard.className = "activity-card";

        const spotsLeft = details.max_participants - details.participants.length;

        activityCard.innerHTML = `
          <h4>${name}</h4>
          <p>${details.description}</p>
          <p><strong>Schedule:</strong> ${details.schedule}</p>
          <p><strong>Availability:</strong> ${spotsLeft} spots left</p>
        `;

        activitiesList.appendChild(activityCard);

        // Add option to select dropdown
        const option = document.createElement("option");
        option.value = name;
        option.textContent = name;
        activitySelect.appendChild(option);
      });
    } catch (error) {
      activitiesList.innerHTML = "<p>Failed to load activities. Please try again later.</p>";
      console.error("Error fetching activities:", error);
    }
  }

  // Handle form submission
  signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const activity = document.getElementById("activity").value;

    try {
      const response = await fetch(
        `/activities/${encodeURIComponent(activity)}/signup?email=${encodeURIComponent(email)}`,
        {
          method: "POST",
        }
      );

      const result = await response.json();

      if (response.ok) {
        messageDiv.textContent = result.message;
        messageDiv.className = "success";
        signupForm.reset();
      } else {
        messageDiv.textContent = result.detail || "An error occurred";
        messageDiv.className = "error";
      }

      messageDiv.classList.remove("hidden");

      // Hide message after 5 seconds
      setTimeout(() => {
        messageDiv.classList.add("hidden");
      }, 5000);
    } catch (error) {
      messageDiv.textContent = "Failed to sign up. Please try again.";
      messageDiv.className = "error";
      messageDiv.classList.remove("hidden");
      console.error("Error signing up:", error);
    }
  });

  // Initialize app
  fetchActivities();
});
```

</details>


---

<sub>12s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/requirements.txt.**

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/requirements.txt

```
fastapi
uvicorn
httpx
watchfiles
```


---

<sub>12s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.devcontainer/devcontainer.json.**

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.devcontainer/devcontainer.json

<details>
<summary>16 lines</summary>

```
{
  "name": "Python 3",
  "image": "mcr.microsoft.com/devcontainers/python:3.13",
  "forwardPorts": [8000],
  "postCreateCommand": "pip install -r requirements.txt",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.debugpy",
        "GitHub.copilot-chat",
        "GitHub.copilot"
      ]
    }
  }
}
```

</details>


---

<sub>12s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.vscode/launch.json.**

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.vscode/launch.json

<details>
<summary>21 lines</summary>

```
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Launch Mergington WebApp",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "src.app:app",
        "--reload",
        "--reload-include",
        "src/static/*"
      ],
      "jinja": true
    }
  ]
}
```

</details>


---

<sub>12s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.github/workflows/0-start-exercise.yml.**

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.github/workflows/0-start-exercise.yml

<details>
<summary>58 lines</summary>

```
name: Step 0 # Start Exercise

on:
  push:
    branches:
      - main

permissions:
  contents: write
  actions: write
  issues: write

env:
  STEP_1_FILE: ".github/steps/1-step.md"

jobs:
  start_exercise:
    if: |
      !github.event.repository.is_template
    name: Start Exercise
    uses: skills/exercise-toolkit/.github/workflows/start-exercise.yml@v0.8.1
    with:
      exercise-title: "Getting Started with GitHub Copilot"
      intro-message: "Welcome to the exciting world of GitHub Copilot! 🚀 In this exercise, you'll unlock the potential of this AI-powered coding assistant to accelerate your development process. Let's dive in and have some fun exploring the future of coding together! 💻✨"

  post_next_step_content:
    name: Post next step content
    runs-on: ubuntu-latest
    needs: [start_exercise]
    env:
      ISSUE_NUMBER: ${{ needs.start_exercise.outputs.issue-number }}
      ISSUE_REPOSITORY: ${{ github.repository }}

    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          ref: main

      - name: Get response templates
        uses: actions/checkout@v6
        with:
          repository: skills/exercise-toolkit
          path: exercise-toolkit
          ref: v0.8.1

      - name: Create comment - add step content
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: ${{ env.STEP_1_FILE }}
          vars: |
            login: ${{ github.actor }}
            full_repo_name: ${{ github.repository }}

      - name: Create comment - watching for progress
        uses: GrantBirki/comment@v2.1.1
        with:
          repository: ${{ env.ISSUE_REPOSITORY }}
          issue-number: ${{ env.ISSUE_NUMBER }}
          file: exercise-toolkit/markdown-templates/step-feedback/watching-for-progress.md

      - name: Enable next step workflow
        run: |
          gh workflow enable "Step 1"
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

</details>


---

<sub>12s</sub>

### `view`

**view the file at /home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.github/steps/1-step.md.**

/home/ubuntu/mlh-hacktoberfest-work/mlh-ghw-copilot-basics-2026/.github/steps/1-step.md

````
## Step 1: Hello Copilot

Welcome to your **"Getting Started with GitHub Copilot"** exercise! :robot:

In this exercise, you will be using different GitHub Copilot features to work on a website that allows students of Mergington High School to sign up for extracurricular activities. 🎻 ⚽️ ♟️

<img width="600" alt="screenshot of Mergington High School WebApp" src="../images/mergington-high-school-webapp.png" />

### 📖 Theory: Getting to know GitHub Copilot

<img width="150" align="right" alt="copilot logo" src="../images/copilot-logo.png" />

GitHub Copilot is an AI coding assistant that helps you write code faster and with less effort, allowing you to focus more energy on problem solving and collaboration.

GitHub Copilot has been proven to increase developer productivity and accelerate the pace of software development. For more information, see [Research: quantifying GitHub Copilot’s impact on developer productivity and happiness in the GitHub blog.](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)

As you work in your IDE, you'll most often interact with GitHub Copilot in the following ways:

| Interaction Mode          | 📝 Description                                                                                                                 | 🎯 Best For                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **⚡ Inline suggestions** | AI-powered code suggestions that appear as you type, offering context-aware completions from single lines to entire functions. | Completion of the current line, sometimes a whole new block of code                                             |
| **💭 Inline Chat**        | Interactive chat scoped to your current file or selection. Ask questions about specific code blocks.                           | Code explanations, debugging specific functions, targeted improvements                                          |
| **💬 Ask Mode**           | Optimized for answering questions about your codebase, coding, and general technology concepts.                                | Understanding how code works, brainstorming ideas, asking questions                                             |
| **🤖 Agent Mode**         | Recommended default mode for most coding tasks: autonomous edits, tool use, and follow-through until the task is done.         | Daily coding tasks, from scoped fixes to larger multi-file implementation work                                   |
| **🧭 Plan Agent**         | Optimized for drafting a plan and asking clarifying questions before any code changes are made.                                | When you want a reviewed plan first, then hand off to implementation                                            |

As you work, you'll find GitHub Copilot can help out in several places across the `github.com` website and in your favorite coding environments such as VS Code, Jet Brains, and Xcode!

For today's coding though, we will practice with VS Code in a pre-configured development environment known as a [GitHub Codespace](https://github.com/features/codespaces).

> [!TIP]
> You can learn more about current and upcoming features in the [GitHub Copilot Features](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features) documentation.

### :keyboard: Activity: Get a project intro from Copilot Chat

Let's start up our development environment, use copilot to learn a bit about the project, and then give it a test run.

1. Use the below button to open the **Create Codespace** page in a new tab. Use the default configuration.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Confirm the **Repository** field is your copy of the exercise, not the original, then click the green **Create Codespace** button.
   - ✅ Your copy: `/{{full_repo_name}}`
   - ❌ Original: `/skills/getting-started-with-github-copilot`

1. Wait a moment for Visual Studio Code to load in your browser.
1. In the left sidebar, click the extensions tab and verify that the `GitHub Copilot Chat` and `Python` extensions are installed and enabled.

   <img width="350" alt="copilot extension for VS Code" src="../images/copilot-extension-vscode.png" />

   <img width="350" alt="python extension for VS Code" src="../images/python-extension-vscode.png" />

   <details>
   <summary>🔎 GitHub Copilot Chat extension missing ❓</summary>

   If the GitHub Copilot Chat extension is missing for you, ensure you are signed in to GitHub Copilot. Find the **GitHub Copilot** icon on the bottom right of the VS Code window.

   | Status bar icon                                                                                                         | Sign in required                                                                                         | Copilot active                                                                                                  |
   | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
   | <img width="300" alt="Copilot menu prompting the user to use AI features" src="../images/copilot-sign-in-button.png" /> | <img width="300" alt="Copilot chat sign in button" src="../images/copilot-sign-in-button-clicked.png" /> | <img width="300" alt="Copilot menu showing inline suggestions enabled" src="../images/copilot-signed-in.png" /> |

   You should be good to go at this point, even if the extension is still not visible in the extensions tab.

   </details>

1. At the top of VS Code, locate and click the **Toggle Chat icon** to open a Copilot Chat side panel.

   <img width="150" alt="image" src="../images/toggle-chat-icon.png" />

   > 🪧 **Note:** If this is your first time using GitHub Copilot, you may need to accept the usage terms to continue.


1. Make sure you are in **Ask Mode** for our first interaction

   <img width="350" alt="screenshot showing Ask Mode selection in Copilot Chat" src="../images/ask-mode-selection.png" />

1. Enter the below prompt to ask Copilot to introduce you to the project.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Please briefly explain the structure of this project.
   > What should I do to run it?
   > ```

   > 🪧 **Note:** It is not necessary to follow Copilot's recommended instructions. We have already prepared the environment for you.

1. Now that we know a bit more about the project, let's actually try running it! In the left sidebar, select the `Run and Debug` tab and then press the **Start Debugging** icon.

   <img width="300" alt="image" src="../images/run-and-debug-tab.png" />

1. We want to see our webpage running in a browser, so let's find the url and port. If it isn't visible, expand the lower panel and select the **Ports** tab.

1. In the list, find port `8000` and the related link. Hover over the link and select the **Open in browser** icon.

   ![image](../images/open-in-browser-icon.png)

### :keyboard: Activity: Use Copilot to help remember a terminal command 🙋

Great work! Now that we are familiar with the app and we know it works, let's ask copilot for help starting a branch so we can do some customizing.

1. In VS Code's bottom panel, select the **Terminal** tab and on the right side click the plus `+` sign to create a new terminal window.

   > 🪧 **Note:** This will avoid stopping the existing debug session that is hosting our web application service.

1. Within the new terminal window use the keyboard shortcut `Ctrl + I` (windows) or `Cmd + I` (mac) to bring up **Copilot's Terminal Inline Chat**.

1. Let's ask Copilot to help us remember a command we have forgotten: creating a branch and publishing it.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey copilot, how can I create and publish a new Git branch called "accelerate-with-copilot"?
   > ```

   > 💡 **Tip:** If Copilot doesn't give you quite what you want, you can always continue explaining what you need. Copilot will remember the conversation history for follow-up responses.

1. Press the `Run` button to let Copilot insert the terminal command for us. No need to copy and paste!

1. After a moment, look in the VS Code lower status bar, on the left, to see the active branch. It should now say `accelerate-with-copilot`. If so, you are all done with this step!

1. Now that your branch is pushed to GitHub, Mona should already be busy checking your work. Give her a moment and keep watch in the comments. You will see her respond with progress info and the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:

- Make sure your created the branch with the exact name `accelerate-with-copilot`. No prefixes or suffixes.
- Make sure the branch was indeed published to your repository.

</details>

````


---

<sub>19s</sub>

### Copilot

**Project structure:** This is a FastAPI exercise for the Mergington High School activities website.

- `src/app.py` contains the API, in-memory activities data, and signup endpoints.
- `src/static/` contains the browser UI: `index.html`, `app.js`, and `styles.css`.
- `.devcontainer/devcontainer.json` defines the Python Codespace and installs `requirements.txt`.
- `.vscode/launch.json` contains the VS Code debug configuration for Uvicorn.
- `.github/steps/` and `.github/workflows/` manage the staged GitHub Skills lessons and progress checks.

**Run it:** From the repository root, install dependencies and start the development server:

```bash
pip install -r requirements.txt
python -m uvicorn src.app:app --reload --reload-include 'src/static/*'
```

Then open `http://localhost:8000`; the API documentation is available at `http://localhost:8000/docs`. In the prepared Codespace, dependencies are installed automatically and you can instead use **Run and Debug → Launch Mergington WebApp**, which forwards port 8000.

**Create and publish the branch:**

```bash
git switch -c accelerate-with-copilot
git push --set-upstream origin accelerate-with-copilot
```

The second command publishes the branch and sets `origin/accelerate-with-copilot` as its upstream.

---

<sub>Generated by [GitHub Copilot CLI](https://github.com/features/copilot/cli)</sub>
