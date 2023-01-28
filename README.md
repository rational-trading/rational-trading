# rational-trading

## Setup

### 1. Install NodeJS + NPM

Install the current or LTS version for your relevant platform.

https://nodejs.org/en/download/

Verify they are working with `node --version` and `npm --version`.

### 2. Install Yarn

Run `npm install --global yarn` in this directory (although you can probably run it anywhere).

Verify it is working with `yarn --version`.

### 3. Install VSCode

https://code.visualstudio.com/Download

### 4. Open workspace

`VSCode > File > Open workspace from file`, and select the `projects.code-workspace` file. This should give you a view with "backend", "common", and "frontend" views. An alternative to this approach is to simply open three different windows for the three subfolders, but that's a bit clunky. 

### 5. Install extensions

Once you have opened the workspace, select the extensions tab on the right and search `@recommended`. This will bring a list of extensions I recommend you install.

Once you have done this, use `Cmd+shift+p` on MacOS or `Ctrl+shift+p` on other platforms to open the command pallet. Type "Reload" and select the "Developer: Reload Window" option. It's worth remembering this shortcut, as it's incredibly useful when the editor gets confusde (which will be a lot).

### 6. Follow the individual READMEs

Follow the individual readme's for each of the projects, remembering to `cd` to their respective directories before running any commands.

## Contribution Guidelines

When making a change, you should use the following workflow.

### 1. Creating a branch

On the relevant issue page, you can use the sidebar on the right to automatically create a branch for the issue.

### 2. Switch Branches

On your local machine, switch to the branch you have just created. You can either do this with the commands provided by GitHub in the step above, or via VSCode by:
 - clicking the "sync" button in the bottom left of the screen
 - clicking the branch button next to the left of it (probably says "main")
 - searching + selecting the branch you want to switch to (might be prefixed with `origin/`)

### 3. Make Changes

Make some changes to the code, ensuring you have saved as you go along. You don't have to do the whole feature at once - it's better to break it into smaller stages.

### 4. Stage Your Changes

VSCode should have a handy "Source Control" pane integrated into it, which should show in the sidebar whenever you open the workspace. When you want to make a commit, you should click the "+" icon next to the files you want to commit, which should move them into "staged changes". Once you are happy with the changes, enter a short description of the change into the "message" box, and click commit.

### 5. Ensure Your Changes Have Synced

Make sure that your changes have synced with the server by clicking the "sync" icon in the bottom left of VSCode. 

### 6. Repeat Until Feature Complete

Repeat steps 3-5 until you have completed the feature, and are ready to merge it into the main branch. 

### 7. Merge Main Into Feature Branch (NOT THE OTHER WAY ROUND)

This step should be done periodically, to ensure that any conflicts are caught early, before they become a hassle to fix.

First, ensure that all local changes have been committed (e.g. there are no staged or unstaged files).

You should now ensure that your feature branch is up-to-date with any changes that have been made on `main`. Assuming you have the "gitlens" extension installed, you can do this by:
 - Clicking the "sync" icon in the bottom left of VSCode to ensure all changes are synced
 - Opening the VSCode Source Control pane
 - Expanding the "branches" section near the bottom of the Source Control pane
 - Clicking the "fetch" button on the main branch, if there are unsynced changes
 - Right clicking main (NOT YOUR BRANCH), and then selecting "Merge Branch Into Current Branch"

If the operation succeeds, click the "sync" button and continue to the next step. If you get a merge conflict, then carefully resolve the conflicts (making sure you don't break your code or anyone else's), stage the files, and commit the changes. Once you've done this, click the "sync" button and continue to the next step.

### 8. Make a Pull Request

Go to the repo page on GH, and open the "Pull requests" tab. Click "new pull request", and ensure that the branches are `base: main <- compare: [issue-branch]`. Click "Create pull request", give it a name and a description referencing the issue (e.g. "Resolves #12"), and then click "Create Pull Request" again.

Next, post a link to the PR in the `code-review` Discord channel with the format:
`@everyone [PR TITLE] [PR LINK]`
Anyone that wants to review the change should react with 👀, and then remove that and react with 👍 when they are happy with the changes.

If a reviewer has a question or qualm with the code, they can either leave a comment on the main PR itself, add a one-off comment to a portion of the code, or start a review. Any discussion in the Discord should be within a message thread, and not in the main `code-review` channel.

You can merge the PR once:
 - all tests pass
 - all 👀 reactions have been removed
 - all discussions have been resolved
 - and once you have received at least two 👍 reactions

Once you have merged the change to main, react to your message with ✅. 

### How often should I commit?

Whilst coding, you should commit often. A good guideline is to commit whenever you have a working version of the code with a describable change - the feature doesn't have to be complete, but it must compile and shouldn't break anyone else's code.

### What if multiple people are working on the same issue?

If there are multiple members of the team collaborating on a single issue, you should all create spin-off branches from the issue branch. For example, I might create the branch `1-create-template-for-frontend-miles` as a spin-off of `1-create-template-for-frontend-miles`. Any changes you make should be done on your personal branch, and then synced with the feature branch in the manner described above (replacing any occurences of `main` with the feature branch). Once all team members are happy that the feature branch is finished, you can then sync it with `main` in the manner described above. 





