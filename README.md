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
