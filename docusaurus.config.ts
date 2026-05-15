import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Local DB MCP',
  tagline: 'Safe local database inspection for MCP clients',
  favicon: 'img/favicon.svg',

  url: 'https://rahulsharmaah.github.io',
  baseUrl: '/local-db-mcp/',
  organizationName: 'rahulsharmaah',
  projectName: 'local-db-mcp',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'throw',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/rahulsharmaah/local-db-mcp/edit/main/',
          showLastUpdateAuthor: true,
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/favicon.svg',
    navbar: {
      title: 'Local DB MCP',
      items: [
        {type: 'docSidebar', sidebarId: 'tutorialSidebar', position: 'left', label: 'Docs'},
        {
          href: 'https://github.com/rahulsharmaah/local-db-mcp',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {label: 'Introduction', to: '/'},
            {label: 'Configuration', to: '/configuration'},
            {label: 'Clients', to: '/codex'},
          ],
        },
        {
          title: 'Project',
          items: [
            {label: 'GitHub', href: 'https://github.com/rahulsharmaah/local-db-mcp'},
            {label: 'Security', to: '/security'},
            {label: 'Contributing', to: '/contributing'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Local DB MCP contributors.`,
    },
    prism: {
      additionalLanguages: ['bash', 'powershell', 'json', 'yaml', 'sql'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
