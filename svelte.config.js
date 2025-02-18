import 'dotenv/config'
import adapterBun from 'svelte-adapter-bun';
import adapterNode from '@sveltejs/adapter-node';
import adapterAuto from '@sveltejs/adapter-auto';
import adapterNetlify from '@sveltejs/adapter-netlify'
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		// adapter-auto only supports some environments, see https://svelte.dev/docs/kit/adapter-auto for a list.
		// If your environment is not supported, or you settled on a specific environment, switch out the adapter.
		// See https://svelte.dev/docs/kit/adapters for more information about adapters.
		adapter: (() => {
			switch (process.env.ENVIRONMENT) {
				case 'bun':
					return adapterBun();
				case 'node':
					return adapterNode();
				case 'netlify':
					return adapterNetlify();
				default:
					return adapterAuto();
			}
		})()
	}
};

export default config;