import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://kit.svelte.dev/docs/integrations#preprocessors
  // for more information about preprocessors
  preprocess: [
    vitePreprocess(),
    preprocess({
      scss: {
        prependData: '@use "src/variables.scss" as *;',
      },
    }),
  ],
  kit: {
    adapter: adapter({
      pages: '../backend/static',
      assets: '../backend/static'
    }),
    alias: {
      $lib: 'src/lib/',
      $components: 'src/components/'
    },
  },
};

export default config;
