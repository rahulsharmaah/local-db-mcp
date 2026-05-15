import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    'installation',
    'configuration',
    'tools',
    {
      type: 'category',
      label: 'Client Setup',
      items: ['codex', 'codex-cloud', 'cursor', 'claude-desktop', 'client-templates'],
    },
    'examples',
    'contributing',
    'security',
    'privacy',
    'terms',
  ],
};

export default sidebars;
