# Common

## Setup

Install dependencies using `yarn install`.

## Building

You can check the library library builds using `yarn build`. When developing, you can continually build whenever there's a change using `yarn watch:build` (this can be useful for seeing an up-to-date list of errors).

## Linting

You can manually run the linter using `yarn lint`. To automatically fix some of the errors, you can use `yarn lint --fix`.

## Folder Structure

Most of the folder structure is similar to the frontend.

 - `src` contains most of the source code you need.
   - `index.ts` defines which types, functions, and variables should be exported from the module. If you want to add something new to the library, you will need to re-export it here.
   - `[generic-file-name].ts` files contain code for the library

