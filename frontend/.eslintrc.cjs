module.exports = {
    root: true,
    parser: "@typescript-eslint/parser",
    extends: ["airbnb-base", "plugin:@typescript-eslint/recommended"],
    plugins: ["svelte3", "@typescript-eslint"],
    overrides: [{ files: ["*.svelte"], processor: "svelte3/svelte3" }],
    rules: {
        indent: ["error", 4],
        "import/no-extraneous-dependencies": "off",
        "import/no-mutable-exports": "off",
        "import/prefer-default-export": "off",
        "import/extensions": ["error", { ts: "never", svelte: "always" }],
        "import/no-unresolved": "off",
        quotes: ["error", "double"],
        "no-return-assign": ["error", "except-parens"],
        "class-methods-use-this": "off",
        "operator-linebreak": ["error", "after"],
        "no-shadow": "off",
        "@typescript-eslint/no-shadow": ["error"],
        "import/first": "off",
        "no-multiple-empty-lines": ["error", { "max": 2, "maxBOF": 0, "maxEOF": 0 }],
        "@typescript-eslint/no-explicit-any": ["off"],
    },
    settings: {
        // eslint-disable-next-line global-require
        "svelte3/typescript": () => require("typescript"),
        "import/resolver": {
            "eslint-import-resolver-custom-alias": {
                alias: {
                    $lib: "./src/lib",
                    $components: "./src/components",
                    $app: "./.svelte-kit/runtime/app"
                },
                extensions: [".ts", ".svelte"],
                packages: [
                    "packages/*",
                ],
            },
        },
    },
    parserOptions: {
        sourceType: "module",
        ecmaVersion: 2020,
    },
    env: {
        browser: true,
        es2017: true,
        node: true,
    },
};
