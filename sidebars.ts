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
      items: ['codex', 'claude-desktop', 'cursor'],
    },
    'examples',
    'contributing',
    'security',
  ],
};

export default sidebars;
