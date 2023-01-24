# Frontend

## Setup

Install dependencies using `yarn install`.

## Developing

You can run the frontend locally using `yarn dev`. This will show a link that you can `Cmd+click` / `Ctrl+click` to open. 

As a shortcut, you can also use `yarn dev --open`.

## Building

You can build a production version of the site using `yarn build`. This will build static files and place them in the `/build` directory.

You can easily serve the built version using `yarn preview`, or `yarn preview --open`.

## Folder Structure

 - `.svelte-kit` is used internally by SvelteKit, you shouldn't need to touch it
 - `build` contains the static files output by `yarn build`
 - `node_modules` contains all the dependencies installed by `yarn install`
 - `src` contains most of the source code for a project
   - `components` contains re-usable UI components that are used in multiple routes. It can be referenced in imports by `$components`
   - `lib` contains re-usable TypeScript functions / data. It can be referenced by `$lib`
   - `routes` contains code for each page of our site. A "route" is like a folder - for example, in `https://domain.com/about/contact`, the route is `/about/contact/`. In SvelteKit, the code for this page would be found in `src/routes/about/contact/+page.svelte`. For each route, we can have:
     - `+layout.svelte` defines a "wrapper" that surrounds all pages in the directory and any subdirectories. You can have up to one per route, but often only need one per app. They are useful for things like navbars, which should be the same (or very similar) on every page in the hierarchy.
     - `+page.svelte` contains the code for a particular route.
     - `[component-name-here].svelte` contains a component that is only used within that particular route. This saves such one-off components from polluting `$components`.
     - `+layout.ts` is mostly used when doing SSR. In this case, it simply tells SvelteKit to statically render all pages in the hierarchy.
   - `app.d.ts` allows us to customise the types of some in-built SvelteKit features
   - `app.html` is a basic template that SvelteKit inserts itself into.
   - `app.scss` defines the SCSS files that should be included in the project.
   - `variables.scss` allows us to customise SCSS variables that can be used throughout the project. Notably, it allows us to customise Bulma theming (see [here](https://bulma.io/documentation/customize/variables/)).
 - `/static` contains files that should be copied into the build directory
 - `.eslintignore` tells ESLint which files it should ignore
 - `.eslintrc.cjs` configures ESLint
 - `.gitignore` says which files should be excluded from `git`. In general, these are any files that are generated programmatically. `yarn.lock` is a notable exception to this.
 - `package.json` contains a list of project dependencies, as well as configuration for shorcut commands (e.g. `yarn run check` is a shortcut for `npx svelte-kit sync && svelte-check --tsconfig ./tsconfig.json`)
 - `svelte.config.js` configures SvelteKit (including telling it that the output should be a static site, as well as configuring shortened paths such as `$components`)
 - `tsconfig.json` configures the TypeScript compiler
 - `vite.config.js` configures Vite, which powers the dev server and build commands
 - `yarn.lock` contains a list of exactly which version we are using for every dependency. It is generated whenever yarn does an `install`, and is useful to ensure that builds are reproducible (for example, if they are done on a build server or in a Docker container). 