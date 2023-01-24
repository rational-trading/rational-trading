import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-auto';
// eslint-disable-next-line import/no-unresolved
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
    adapter: adapter(),
    alias: {
      $lib: 'src/lib/',
      $components: 'src/components/',
      $common: 'src/../../common/',
    },
  },
};

export default config;
